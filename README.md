# CloudAura – Internal Git & CI/CD Platform

## Overview

CloudAura is a self-hosted GitLab platform deployed on Microsoft Azure to provide a centralized environment for source code management, team collaboration, and automated software delivery.

The project uses **Terraform** for infrastructure provisioning, **Docker Compose** for containerized deployment, **GitLab CI/CD** for automation, and **Bash scripts** for operational management.

A full-stack IT Support Ticket System was developed as a sample application to demonstrate the CI/CD workflow.

## Tech Stack

| Technology | Purpose |
|---|---|
| Microsoft Azure | Cloud infrastructure |
| Terraform | Infrastructure as Code |
| Docker & Docker Compose | Containerization and deployment |
| GitLab CE | Source control and CI/CD platform |
| GitLab Runner | Pipeline execution |
| Bash | Operational automation |
| Streamlit | Application frontend |
| FastAPI | Application backend |
| PostgreSQL | Database |

## Architecture

The platform runs on an Azure Ubuntu VM within a Virtual Network, protected by a Network Security Group.

GitLab is deployed using Docker Compose, while GitLab Runner uses the Shell executor to build and deploy the sample application.

```text
Developer
    |
    v
GitLab Repository
    |
    v
GitLab CI/CD Pipeline
    |
    v
GitLab Runner
    |
    +-- Test
    +-- Build
    +-- Deploy
    +-- Verify
    |
    v
CloudAura IT Support Application
    |
    +-- Streamlit (Frontend)
    +-- FastAPI (Backend)
    +-- PostgreSQL (Database)
```

## Project Structure

```text
Cloura-fullstack-infr-project/
├── terraform/          # Azure infrastructure
├── gitlab/             # GitLab Docker Compose configuration
├── app/
│   ├── backend/        # FastAPI
│   └── streamlit/      # Frontend
├── scripts/            # Bash automation
├── docker-compose.yml  # Application services
├── .gitlab-ci.yml      # CI/CD pipeline
├── .env.example        # Environment template
└── README.md
```

## Infrastructure & Deployment

Terraform provisions the Azure Resource Group, Virtual Network, Subnet, Network Security Group, Virtual Machine, and Public IP.

To provision the infrastructure:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

After provisioning, Docker and Docker Compose are installed on the VM, and GitLab is deployed using its Compose configuration.

GitLab Runner is configured to execute CI/CD jobs and deploy the sample application.

## CI/CD Workflow

The pipeline contains four stages:

| Stage | Description |
|---|---|
| **Test** | Validate backend and frontend Python files |
| **Build** | Validate Docker Compose and build application images |
| **Deploy** | Deploy containers using Docker Compose |
| **Verify** | Check PostgreSQL, FastAPI, and Streamlit availability |

**Result:** The GitLab pipeline was successfully executed with **5/5 jobs passed**.

## Bash Automation

The project includes operational scripts:

| Script | Purpose |
|---|---|
| `deploy-gitlab.sh` | Start and validate GitLab deployment |
| `redeploy.sh` | Recreate the GitLab container |
| `health-check.sh` | Validate Docker and GitLab health |
| `app-health-check.sh` | Verify application services |
| `backup.sh` | Back up GitLab data and configuration |

GitLab health checks, application verification, and backup creation were successfully tested.

## Security & Operations

The platform includes:

- Azure NSG rules for network access control.
- SSH key-based authentication.
- GitLab CI/CD variables for database credentials.
- Git-ignored `.env` files to protect local secrets.
- Persistent Docker storage for GitLab and PostgreSQL.
- Bash scripts for health checks and backups.

**Note:** This is a single-node demonstration environment. Production deployment would require additional hardening, HTTPS, and off-VM backups.

## Troubleshooting

| Issue | Recommended Check |
|---|---|
| GitLab unavailable | VM status and GitLab container health |
| Pipeline pending | GitLab Runner service |
| Build failure | Docker Compose configuration and job logs |
| Application unavailable | Container logs and application health check |
| Database connection error | PostgreSQL status and environment variables |

## Project Results

The project successfully demonstrates:

- Azure infrastructure provisioning using Terraform.
- Self-hosted GitLab deployment using Docker Compose.
- GitLab Runner configuration.
- Automated CI/CD pipeline execution.
- Deployment of a full-stack IT Support application.
- Operational health checks and GitLab backups.

## Conclusion

CloudAura demonstrates a practical internal DevOps platform that integrates **Infrastructure as Code, Git-based collaboration, containerization, CI/CD automation, and operational scripting** in a single Azure environment.
