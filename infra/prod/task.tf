variable "task_cpu" {
  type    = number
  default = 256
}

variable "task_memory" {
  type    = number
  default = 512
}

variable "task_cpu_architecture" {
  type    = string
  default = "ARM64"
}

resource "aws_ecs_task_definition" "server" {
  family                   = "${data.terraform_remote_state.global.outputs.projeto}-${var.env}"
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  task_role_arn            = var.task_definition_role
  execution_role_arn       = var.task_definition_role
  runtime_platform {
    cpu_architecture        = var.task_cpu_architecture
    operating_system_family = "LINUX"
  }
  container_definitions = jsonencode([
    {
      name      = data.terraform_remote_state.global.outputs.projeto
      image     = "${data.terraform_remote_state.global.outputs.ecr_repository_url}:${var.env}"
      cpu       = var.task_cpu
      memory    = var.task_memory
      essential = true
      environment = [
        {
          name  = "ENV"
          value = var.env
        },
        {
          name  = "AWS_DEFAULT_REGION"
          value = var.aws_region
        },
      ]
      secrets = [
        {
          name      = "API_KEY"
          valueFrom = "${data.aws_secretsmanager_secret.app.arn}:api_key::"
        },
        {
          name      = "MIDDLEWARE_API_URL"
          valueFrom = "${data.aws_secretsmanager_secret.app.arn}:middleware_api_url::"
        },
        {
          name      = "TRANSACTION_BUCKET"
          valueFrom = "${data.aws_secretsmanager_secret.app.arn}:transaction_bucket::"
        },
        {
          name      = "TRANSACTION_BUCKET_DEMO"
          valueFrom = "${data.aws_secretsmanager_secret.app.arn}:transaction_bucket_demo::"
        },
      ]
      portMappings = [
        {
          containerPort : 8000
          hostPort : 8000
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = data.terraform_remote_state.global.outputs.cloudwatch_log_group_name
          awslogs-region        = var.aws_region
          awslogs-stream-prefix = "${data.terraform_remote_state.global.outputs.projeto}-${var.env}"
        }
      }
    }
  ])
}
