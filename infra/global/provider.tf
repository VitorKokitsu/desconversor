terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket  = "ctf-terraform-states"
    key     = "global/desconversor/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region

  assume_role {
    role_arn     = var.terraform_role
    session_name = "${var.projeto}-${var.env}-infra"
  }

  default_tags {
    tags = {
      Ambiente = var.env
      Custo    = var.custo
      Squad    = var.squad
      Projeto  = var.projeto
      Name     = var.projeto
    }
  }
}
