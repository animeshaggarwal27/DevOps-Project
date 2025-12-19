terraform {
  backend "s3" {
    bucket = "terraform-state-bucket"
    key    = "ecs/terraform.tfstate"
    region = "ap-south-1"
  }
}
