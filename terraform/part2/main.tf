resource "aws_instance" "flask" {
  ami           = var.ami
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.flask_sg.name]
  user_data = file("flask_user_data.sh")
}

resource "aws_instance" "express" {
  ami           = var.ami
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.express_sg.name]
  user_data = file("express_user_data.sh")
}
