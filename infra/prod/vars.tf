variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "ctf_states_bucket" {
  default = "ctf-terraform-states"
  type    = string
}

variable "env" {
  default = "prod"
}

variable "task_definition_role" {
  type    = string
  default = "arn:aws:iam::110365709862:role/middlewareRole"
}
