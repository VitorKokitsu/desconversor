output "task_definition_arn" {
  value = aws_ecs_task_definition.server.arn
}

output "ecs_service_id" {
  value = aws_ecs_service.web.id
}

output "security_group_id" {
  value = aws_security_group.app.id
}

output "target_group_arn" {
  value = aws_lb_target_group.app.arn
}
