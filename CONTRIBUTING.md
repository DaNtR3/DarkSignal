# Contributing to DarkSignal

Thank you for your interest in contributing to DarkSignal! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Commit Message Standards](#commit-message-standards)
- [Code Style Guides](#code-style-guides)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Documentation Standards](#documentation-standards)
- [Reporting Issues](#reporting-issues)
- [Security Disclosure](#security-disclosure)

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:

- Be respectful and constructive in discussions
- Treat all community members with dignity
- Report unacceptable behavior to the maintainers
- Focus on the code, not the person

---

## Getting Started

### Prerequisites

- **Git**: Version control system
- **Python 3.11+**: Programming language
- **Docker**: Container runtime
- **Kubernetes kubectl**: Cluster management (optional, for testing)
- **Terraform 1.0+**: Infrastructure provisioning
- **AWS CLI**: Cloud provider credentials (optional)

### Fork & Clone

1. **Fork the repository** on GitHub
   - Click the "Fork" button on https://github.com/DaNtR3/DarkSignal

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/DarkSignal.git
   cd DarkSignal
   git remote add upstream https://github.com/DaNtR3/DarkSignal.git
   ```

3. **Keep your fork updated**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

---

## Development Setup

### Local Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Install development dependencies
pip install pytest pytest-cov black flake8
```

### Docker Development

```bash
# Build Docker image
docker build -t darksignal:dev -f dockerfile .

# Run container
docker run -p 5090:5090 darksignal:dev

# Access app at http://localhost:5090
```

### Running the Application

```bash
# Development mode
FLASK_ENV=development python app.py

# Production mode
FLASK_ENV=production python app.py
```

### Kubernetes Testing (Optional)

```bash
# Apply Kubernetes manifests locally
cd infra/namespaces
kubectl apply -f .

cd ../web_app
kubectl apply -f .

# Check deployment status
kubectl get pods -n app-namespace
```

---

## Branch Naming Conventions

Follow these naming conventions for your feature branches:

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/description` | `feature/sql-injection-detection` |
| Bug Fix | `bugfix/description` | `bugfix/login-validation-error` |
| Hotfix | `hotfix/description` | `hotfix/critical-security-patch` |
| Documentation | `docs/description` | `docs/api-documentation` |
| Refactor | `refactor/description` | `refactor/auth-service` |
| Test | `test/description` | `test/add-unit-tests` |
| Chore | `chore/description` | `chore/update-dependencies` |

**Examples**:
```bash
git checkout -b feature/phishing-simulation
git checkout -b bugfix/prometheus-metrics
git checkout -b docs/kubernetes-deployment
```

---

## Commit Message Standards

Write clear, descriptive commit messages following conventional commits:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without feature/fix
- **perf**: Performance improvements
- **test**: Adding/updating tests
- **chore**: Build process, dependencies, etc.
- **ci**: CI/CD pipeline changes
- **infra**: Infrastructure changes (Kubernetes, Terraform)

### Scope

The area of code affected:
- `auth` - Authentication module
- `api` - API routes
- `db` - Database operations
- `k8s` - Kubernetes manifests
- `terraform` - Terraform configuration
- `prometheus` - Monitoring/metrics
- `docker` - Container configuration
- `ci` - GitHub Actions workflows

### Examples

```
feat(auth): add multi-factor authentication support

- Implement TOTP-based MFA
- Add user enrollment flow
- Update authentication routes

Closes #123
```

```
fix(api): correct password validation endpoint

The /pwned/check-password endpoint was not properly validating
input parameters. This fix adds proper input sanitization.

Fixes #456
```

```
docs(k8s): add deployment troubleshooting guide

Added comprehensive troubleshooting section for Kubernetes
deployments, including common issues and solutions.
```

```
ci: update GitHub Actions Terraform version

Bump Terraform version from 1.13.0 to 1.14.0 in CI pipeline.
```

---

## Code Style Guides

### Python Code Style

**Follow PEP 8** with these additional guidelines:

```bash
# Format code with Black
pip install black
black .

# Check style with Flake8
pip install flake8
flake8 .

# Check imports
pip install isort
isort .
```

**Python Standards**:
- **Line length**: Maximum 100 characters
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Docstrings**: Use triple quotes for all functions/classes
- **Type hints**: Use type annotations where possible
- **Imports**: Group stdlib, third-party, local (alphabetically)

**Example**:
```python
"""Module for authentication services."""

from typing import Optional, Dict
from flask import Flask, request

class AuthService:
    """Handles user authentication and authorization."""

    def __init__(self, db_connection: str) -> None:
        """Initialize the authentication service.
        
        Args:
            db_connection: Database connection string.
        """
        self.db_connection = db_connection

    def validate_password(self, password: str) -> bool:
        """Validate password strength.
        
        Args:
            password: Password to validate.
            
        Returns:
            True if password meets strength requirements.
        """
        return len(password) >= 12
```

### JavaScript Code Style

**Follow ESLint conventions**:
- **Quotes**: Single quotes (`'`)
- **Semicolons**: Required at end of statements
- **Indentation**: 2 spaces
- **Naming**: camelCase for variables, PascalCase for classes
- **Comments**: JSDoc for functions

**Example**:
```javascript
/**
 * Validates password strength on client side
 * @param {string} password - The password to validate
 * @returns {boolean} True if password is strong enough
 */
function validatePassword(password) {
  const minLength = 12;
  const hasUppercase = /[A-Z]/.test(password);
  const hasNumbers = /[0-9]/.test(password);
  
  return password.length >= minLength && hasUppercase && hasNumbers;
}
```

### CSS Code Style

**Follow CSS best practices**:
- **BEM naming**: Block__Element--Modifier
- **Indentation**: 2 spaces
- **Organization**: Properties in logical order (layout, display, spacing, colors)

**Example**:
```css
/* Base component */
.button {
  display: inline-block;
  padding: 12px 24px;
  font-size: 14px;
  color: #ffffff;
  background-color: #007bff;
}

/* Button modifier */
.button--primary {
  background-color: #0056b3;
  font-weight: bold;
}

.button--danger {
  background-color: #dc3545;
}

/* Button element state */
.button:hover {
  opacity: 0.9;
}

.button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
```

### HTML Standards

**Follow semantic HTML**:
- Use semantic elements (`<header>`, `<nav>`, `<main>`, `<footer>`)
- Proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`)
- Accessible attributes (alt text, aria-labels)
- Valid HTML5 structure

**Example**:
```html
<header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main>
  <section>
    <h1>Welcome to DarkSignal</h1>
    <img src="image.png" alt="DarkSignal Dashboard">
  </section>
</main>
```

### Terraform Code Style

**Follow Terraform best practices**:
- **Formatting**: Use `terraform fmt`
- **Naming**: snake_case for all resources/variables
- **Organization**: Group related resources
- **Comments**: Explain non-obvious configurations
- **Variables**: Always include descriptions

**Example**:
```terraform
# VPC Configuration
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "main-vpc"
  }
}

# Format with:
terraform fmt -recursive
```

---

## Testing Requirements

### Python Tests

All Python code changes should include tests:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run specific test function
pytest tests/test_auth.py::test_validate_password
```

**Test file structure**:
```
tests/
├── test_auth.py
├── test_api.py
├── test_handlers.py
└── __init__.py
```

**Example test**:
```python
import pytest
from services.auth_service import AuthService

class TestAuthService:
    """Test suite for authentication service."""

    def setup_method(self):
        """Set up test fixtures."""
        self.auth_service = AuthService()

    def test_validate_password_weak(self):
        """Test validation of weak passwords."""
        assert not self.auth_service.validate_password("123456")

    def test_validate_password_strong(self):
        """Test validation of strong passwords."""
        assert self.auth_service.validate_password("SecurePass123!")

    def test_validate_password_none(self):
        """Test validation with None input."""
        with pytest.raises(TypeError):
            self.auth_service.validate_password(None)
```

### Test Coverage

- **Minimum coverage**: 70% for new code
- **Critical paths**: 100% coverage required
- **Run coverage**: `pytest --cov=src --cov-report=term-missing`

---

## Pull Request Process

### Before Submitting

1. **Update your branch**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests locally**:
   ```bash
   pytest
   pytest --cov=src
   ```

3. **Format code**:
   ```bash
   black .
   flake8 .
   isort .
   ```

4. **Build Docker image** (if applicable):
   ```bash
   docker build -t darksignal:test -f dockerfile .
   ```

5. **Test Kubernetes deployment** (if applicable):
   ```bash
   kubectl apply -f infra/namespaces/
   kubectl apply -f infra/web_app/
   ```

### Submitting PR

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature
   ```

2. **Create Pull Request** on GitHub with the following template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Related Issues
Closes #(issue number)

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Performed
- [ ] Unit tests added/updated
- [ ] Integration tests passed
- [ ] Manual testing completed

## Checklist
- [ ] My code follows the code style guidelines
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing unit tests passed locally
- [ ] CI/CD pipeline passes

## Screenshots (if applicable)
Include screenshots for UI changes
```

### PR Review Process

1. **Automated checks** must pass:
   - CI/CD pipeline (tests, linting, building)
   - Code coverage maintained or improved
   - No merge conflicts

2. **Code review** by maintainers:
   - At least 1 approval required
   - Address review comments
   - Push updates to same branch

3. **Merge**:
   - Squash commits if requested
   - Delete feature branch after merge

---

## Documentation Standards

### Code Documentation

- **Docstrings**: All functions, classes, and modules
- **Inline comments**: Explain "why", not "what"
- **Type hints**: Use Python type annotations
- **Examples**: Include usage examples for complex code

### README Updates

Update `README.md` if:
- Adding new features
- Changing setup instructions
- Adding new dependencies
- Modifying API endpoints
- Changing configuration

### Changelog

Create or update `CHANGELOG.md` entry for:
- New features
- Bug fixes
- Breaking changes
- Deprecations

Format:
```markdown
## [Version] - YYYY-MM-DD

### Added
- New feature description

### Fixed
- Bug fix description

### Changed
- Change description

### Removed
- Removed feature description
```

---

## Reporting Issues

### Bug Reports

When reporting bugs, include:

1. **Description**: Clear summary of the issue
2. **Steps to reproduce**: Exact steps to trigger the bug
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**:
   - OS and Python version
   - Docker/Kubernetes version (if applicable)
   - DarkSignal version
6. **Screenshots/logs**: Relevant output or error messages
7. **Possible solution**: Optional suggestion for fix

### Feature Requests

When requesting features:

1. **Title**: Clear feature name
2. **Description**: Detailed feature description
3. **Use case**: Why this feature is needed
4. **Proposed implementation**: Optional approach
5. **Alternative solutions**: Other possible approaches

### Issue Labels

Use these labels when creating issues:
- `bug` - Bug report
- `enhancement` - Feature request
- `documentation` - Documentation improvement
- `good first issue` - Good for new contributors
- `help wanted` - Need community assistance

---

## Security Disclosure

### Reporting Security Issues

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead:

1. **Email the maintainer**:
   - Subject: `[SECURITY] DarkSignal Vulnerability Report`
   - Include: Vulnerability description, steps to reproduce, impact
   - Send to: See SECURITY.md or contact maintainers

2. **Include**:
   - Detailed vulnerability description
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (optional)
   - Your contact information

3. **Timeline**:
   - Expect acknowledgment within 48 hours
   - Security patches will be prioritized
   - Coordinated disclosure timeline

### Security Testing Guidelines

When testing security features:
- Only test on your own infrastructure
- Never test without explicit authorization
- Report findings responsibly
- Do not attempt to access unauthorized systems
- Respect privacy and data protection laws

---

## License

By contributing to DarkSignal, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE) file for details.

---

## Questions or Need Help?

- **GitHub Issues**: For bugs and features
- **GitHub Discussions**: For questions and ideas
- **Email**: Contact maintainers for sensitive matters

Thank you for contributing to DarkSignal! 🎉
