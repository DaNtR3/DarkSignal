variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Prefix for resources"
  type        = string
  default     = "sre-project-cluster"
}