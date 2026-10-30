output "custo" {
  value = var.custo
}

output "squad" {
  value = var.squad
}

output "projeto" {
  value = var.projeto
}

output "terraform_role" {
  value = var.terraform_role
}

output "access_logs_bucket_id" {
  value = "cotefacil-elb-logs"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.repository.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.cluster.name
}

output "cloudwatch_log_group_name" {
  value = aws_cloudwatch_log_group.task-log-group.name
}
