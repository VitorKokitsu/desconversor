resource "aws_ecs_cluster" "cluster" {
  name = var.projeto

  service_connect_defaults {
    namespace = var.service_connect_arn
  }

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}
