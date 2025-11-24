# DarkSignal

A lightweight security simulation platform designed to emulate real-world identity-based attacks, monitor critical behaviors, and generate actionable alerts.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Kubernetes Deployment](#kubernetes-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Monitoring & Observability](#monitoring--observability)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

DarkSignal provides a comprehensive security simulation environment for:
- **Attack Emulation**: Simulate identity-based and behavioral attacks
- **Real-time Monitoring**: Track and log critical security events
- **Alerting**: Generate actionable alerts based on threat patterns
- **Observability**: Full observability stack with Prometheus and Grafana

### Tech Stack

- **Backend**: Python 3.11+ with Flask
- **Container**: Docker
- **Orchestration**: Kubernetes
- **Monitoring**: Prometheus + Grafana + AlertManager
- **Observability**: OpenTelemetry (OTEL)

---

## Features

- ✅ Lightweight Flask-based web application
- ✅ Containerized deployment with Docker
- ✅ Full Kubernetes infrastructure (namespaces, deployments, services, configmaps)
- ✅ Integrated monitoring stack (Prometheus, Grafana, AlertManager)
- ✅ OpenTelemetry instrumentation for distributed tracing
- ✅ Automated CI/CD pipeline with GitHub Actions
- ✅ Identity-based attack simulation
- ✅ Real-time behavioral monitoring

---

## Architecture

```
┌─────────────────────────────────────────────┐
│         GitHub Actions CI/CD Pipeline        │
│  (Trigger: push/PR to src/ or infra/)       │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   Build Docker Image         │
        │ (ghcr.io/DaNtR3/DarkSignal)  │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │  Deploy to Kubernetes        │
        │  (kubectl apply)             │
        └──────────────┬───────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
   ┌─────────────┐         ┌──────────────────┐
   │  Web App    │         │  Monitoring      │
   │  Namespace  │         │  Stack           │
   │  - Flask    │         │  - Prometheus    │
   │  - App      │         │  - Grafana       │
   │  - Services │         │  - AlertManager  │
   └─────────────┘         └──────────────────┘
```

---

## Prerequisites

- **Python 3.11+**
- **Docker** (for containerization)
- **kubectl** (for Kubernetes management)
- **Kubernetes cluster** (local or cloud-based)
- **Git** (for version control)

### Optional

- **Helm** (for advanced deployments)
- **kind** or **minikube** (for local Kubernetes cluster)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DaNtR3/DarkSignal.git
cd DarkSignal
```

### 2. Create Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
FLASK_ENV=development
FLASK_APP=app.py
DEBUG=True
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

---

## Configuration

### Flask Configuration

The application runs on port `5090` by default. Modify in `app.py` if needed.

### Kubernetes Configuration

Update Kubernetes manifests in `infra/` directories:

- `infra/namespaces/`: Define Kubernetes namespaces
- `infra/web_app/`: Flask app deployment, service, and configmap
- `infra/prometheus/`: Monitoring configuration
- `infra/grafana/`: Dashboard configuration
- `infra/alertmanager/`: Alert routing and notifications
- `infra/script/`: Additional Kubernetes jobs/scripts

---

## Running the Application

### Local Development

```bash
python app.py
```

The application will be available at `http://localhost:5090`

### Docker

```bash
docker build -t darksignal:latest -f dockerfile .
docker run -p 5090:5090 darksignal:latest
```

---

## Kubernetes Deployment

### Prerequisites

1. **Configure kubectl**:
   ```bash
   kubectl config use-context <your-cluster>
   ```

2. **Create namespaces**:
   ```bash
   kubectl apply -f infra/namespaces/
   ```

### Deploy All Services

```bash
# Deploy in order: namespaces → alertmanager → prometheus → grafana → web_app
kubectl apply -f infra/namespaces/
kubectl apply -f infra/alertmanager/
kubectl apply -f infra/prometheus/
kubectl apply -f infra/grafana/
kubectl apply -f infra/web_app/
kubectl apply -f infra/script/
```

### Verify Deployment

```bash
# Check all pods
kubectl get pods -A

# Check services
kubectl get svc -A

# View logs
kubectl logs -f deployment/web-app -n app-namespace
```

### Port Forwarding (for local access)

```bash
# Flask App
kubectl port-forward svc/web-app 5090:5090 -n app-namespace

# Prometheus
kubectl port-forward svc/prometheus 9090:9090 -n prometheus-namespace

# Grafana
kubectl port-forward svc/grafana 3000:3000 -n grafana-namespace

# AlertManager
kubectl port-forward svc/alertmanager 9093:9093 -n alertmanager-namespace
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

The project includes an automated CI/CD pipeline (`.github/workflows/build-and-deploy.yml`) that:

1. **Triggers** on:
   - Push to `main` branch with changes in `src/`, `dockerfile`, or `requirements.txt`
   - Pull requests to `main` with the same paths

2. **Actions**:
   - Builds Docker image and pushes to GitHub Container Registry (ghcr.io)
   - Updates Kubernetes manifests with new image tags
   - Applies all Kubernetes manifests
   - Verifies deployment rollout

### Setup Instructions

1. **Create GitHub Secret** for Kubernetes access:
   ```bash
   cat ~/.kube/config | base64 -w 0 > kubeconfig.b64
   ```

2. **Add secret to GitHub**:
   - Go to: Settings → Secrets and variables → Actions
   - Add secret: `KUBE_CONFIG` with your base64-encoded kubeconfig

3. **Trigger Pipeline**:
   ```bash
   git push origin main
   ```

### Environment Variables

The workflow uses:
- `REGISTRY`: GitHub Container Registry (ghcr.io)
- `IMAGE_NAME`: `${{ github.repository }}` (DaNtR3/DarkSignal)

---

## Project Structure

```
DarkSignal/
├── app.py                 # Flask application entry point
├── dockerfile             # Docker image build configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── LICENSE                # Project license
├── VERSION                # Version file
├── .env                   # Environment variables (not in git)
├── .gitignore             # Git ignore rules
│
├── src/                   # Source code
│   └── handlers/
│       └── year_handler.py
│
├── routes/                # Flask route blueprints
│   └── auth_routes.py
│
├── services/              # Business logic services
│   └── auth_service.py
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── home_page.html
│   ├── 404.html
│   └── partials/
│       ├── header.html
│       ├── navbar.html
│       └── footer.html
│
├── static/                # Static assets
│   ├── css/
│   │   ├── background_body.css
│   │   ├── generals.css
│   │   ├── styles_404.css
│   │   ├── styles_login.css
│   │   └── styles_main.css
│   └── images/
│
├── infra/                 # Kubernetes infrastructure
│   ├── namespaces/        # Kubernetes namespaces
│   ├── web_app/           # Flask app K8s manifests
│   ├── prometheus/        # Prometheus monitoring
│   ├── grafana/           # Grafana dashboards
│   ├── alertmanager/      # AlertManager configuration
│   └── script/            # Kubernetes jobs/scripts
│
├── .github/
│   └── workflows/
│       └── build-and-deploy.yml  # CI/CD pipeline
│
└── scripts/               # Utility scripts
```

---

## API Documentation

### Authentication Routes

Base URL: `/auth`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/auth/user` | Get current user |
| POST | `/auth/users` | Create new user |

### Error Handling

| Status | Response |
|--------|----------|
| 404 | Custom 404.html page |

*For detailed API documentation, see route blueprints in `routes/auth_routes.py`*

---

## Monitoring & Observability

### OpenTelemetry Instrumentation

The application includes OTEL instrumentation for:
- **Flask request tracing**
- **Distributed logging**
- **Metrics export** (via Prometheus exporter)

Configuration in `dockerfile`:
```dockerfile
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

### Prometheus Metrics

Access Prometheus at: `http://localhost:9090` (via port-forward)

### Grafana Dashboards

Access Grafana at: `http://localhost:3000` (via port-forward)

Default credentials (update in production):
- Username: `admin`
- Password: (check `infra/grafana/grafana-config.yaml`)

### AlertManager

Configure alerts in: `infra/alertmanager/alertmanager-config.yaml`

---

## Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Commit changes**: `git commit -m "Add your feature"`
4. **Push to branch**: `git push origin feature/your-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Add unit tests for new features
- Update documentation for API changes
- Ensure CI/CD pipeline passes before merging

---

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.

---

## Support

For issues, questions, or contributions, please open an issue on [GitHub](https://github.com/DaNtR3/DarkSignal/issues).

---

**Last Updated**: November 2025  
**Maintainer**: DaNtR3
