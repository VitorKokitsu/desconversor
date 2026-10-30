terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket  = "ctf-terraform-states"
    key     = "prod/desconversor/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region

  assume_role {
    role_arn     = data.terraform_remote_state.global.outputs.terraform_role
    session_name = "${data.terraform_remote_state.global.outputs.projeto}-${var.env}-infra"
  }

  default_tags {
    tags = {
      Ambiente = var.env
      Custo    = data.terraform_remote_state.global.outputs.custo
      Squad    = data.terraform_remote_state.global.outputs.squad
      Projeto  = data.terraform_remote_state.global.outputs.projeto
      Name     = data.terraform_remote_state.global.outputs.projeto
    }
  }
}
