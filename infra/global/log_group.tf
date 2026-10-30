resource "aws_cloudwatch_log_group" "task-log-group" {
  name              = var.projeto
  retention_in_days = 1
}
