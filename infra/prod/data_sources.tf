data "terraform_remote_state" "infra" {
  backend = "s3"
  config = {
    bucket = var.ctf_states_bucket
    key    = "prod/cotefacil-infraestrutura/terraform.tfstate"
    region = var.aws_region
  }
}

data "terraform_remote_state" "global" {
  backend = "s3"
  config = {
    bucket = var.ctf_states_bucket
    key    = "global/desconversor/terraform.tfstate"
    region = var.aws_region
  }
}

data "aws_secretsmanager_secret" "app" {
  name = "${var.env}/${data.terraform_remote_state.global.outputs.projeto}"
}

data "aws_ecs_cluster" "cluster" {
  cluster_name = data.terraform_remote_state.global.outputs.ecs_cluster_name
}

data "aws_lb_listener" "https" {
  arn = data.terraform_remote_state.infra.outputs.private_lb_listener_arn
}

data "aws_security_group" "http" {
  id = data.terraform_remote_state.infra.outputs.http_sg_id
}
