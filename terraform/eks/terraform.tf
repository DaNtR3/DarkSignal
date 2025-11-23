terraform {
  required_version = ">= 1.0"

  backend "s3" {
      bucket         = "sre-project-s3-dantr3-bucket"
      key            = "sre-project/eks/terraform.tfstate"
      region         = "us-east-1"
      dynamodb_table = "terraform-locks"
      encrypt        = true
    }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}