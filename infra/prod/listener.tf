resource "aws_lb_listener_rule" "host" {
  listener_arn = data.aws_lb_listener.https.arn

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app.arn
  }

  condition {
    host_header {
      values = ["desconversor.cotefacil.net"]
    }
  }

  tags = {
    Name = "desconversor"
  }
}
