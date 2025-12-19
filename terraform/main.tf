provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "single_ec2" {
  ami           = "ami-0f5ee92e2d63afc18" # Ubuntu 22.04 (ap-south-1)
  instance_type = "t2.micro"
  key_name      = var.key_name

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  user_data = file("user_data.sh")

  tags = {
    Name = "flask-express-single-ec2"
  }
}
