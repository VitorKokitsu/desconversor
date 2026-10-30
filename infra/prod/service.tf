resource "aws_ecs_service" "web" {
  name            = "${data.terraform_remote_state.global.outputs.projeto}-${var.env}"
  cluster         = data.aws_ecs_cluster.cluster.arn
  task_definition = aws_ecs_task_definition.server.arn
  desired_count   = 1
  propagate_tags  = "TASK_DEFINITION"

  availability_zone_rebalancing     = "ENABLED"
  health_check_grace_period_seconds = 30

  capacity_provider_strategy {
    capacity_provider = "FARGATE"
    base              = 1
    weight            = 1
  }

  network_configuration {
    subnets          = data.terraform_remote_state.infra.outputs.private_subnets_ids
    security_groups  = [aws_security_group.app.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = data.terraform_remote_state.global.outputs.projeto
    container_port   = 8000
  }
}
