resource "aws_security_group" "app" {
  name        = "${data.terraform_remote_state.global.outputs.projeto}-${var.env}"
  vpc_id      = data.terraform_remote_state.infra.outputs.vpc_id
  description = "Permite acesso do Load Balancer ao Desconversor"

  egress = [
    {
      description = "Internet"
      cidr_blocks = [
        "0.0.0.0/0"
      ]
      ipv6_cidr_blocks = [
        "::/0"
      ]
      prefix_list_ids = []
      security_groups = []
      self            = false
      protocol        = "-1"
      from_port       = 0
      to_port         = 0
    }
  ]

  ingress = [
    {
      description      = "HTTP"
      cidr_blocks      = []
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = [data.aws_security_group.http.id]
      self             = false
      protocol         = "TCP"
      from_port        = 8000
      to_port          = 8000
    }
  ]
}
