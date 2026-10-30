variable "custo" {
  type    = string
  default = "ti"
}

variable "squad" {
  type    = string
  default = "integracao"
}

variable "projeto" {
  type    = string
  default = "desconversor"
}

variable "env" {
  default = "global"
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "terraform_role" {
  type    = string
  default = "arn:aws:iam::110365709862:role/terraform-rule"
}

variable "service_connect_arn" {
  type    = string
  default = "arn:aws:servicediscovery:us-east-1:110365709862:namespace/ns-7uzaxgucf7nvkd2h"
}
