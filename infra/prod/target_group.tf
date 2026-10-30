resource "aws_lb_target_group" "app" {
  name        = "tg-${data.terraform_remote_state.global.outputs.projeto}-${var.env}"
  vpc_id      = data.terraform_remote_state.infra.outputs.vpc_id
  target_type = "ip"
  port        = 8000
  protocol    = "HTTP"

  health_check {
    enabled  = true
    protocol = "HTTP"
    path     = "/healthcheck"
    matcher  = "204"
    interval = 30

    healthy_threshold   = 5
    unhealthy_threshold = 2
  }
}
