provider "aws" {
  region = var.aws_region
}

# IAM User for GitHub Actions
resource "aws_iam_user" "github_actions" {
  name = "${var.cluster_name}-github-actions"
  path = "/"

  tags = {
    Name = "${var.cluster_name}-github-actions"
  }
}

# Attach AWS managed AdministratorAccess
resource "aws_iam_user_policy_attachment" "github_actions_admin" {
  user       = aws_iam_user.github_actions.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# Create access keys for GitHub Actions
resource "aws_iam_access_key" "github_actions" {
  user = aws_iam_user.github_actions.name
}
