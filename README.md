# Cloura
### Cloud Infrastructure & CI/CD Automation

Cloura is a DevOps project that demonstrates how to provision cloud infrastructure, deploy a containerized full-stack application, and automate the software delivery process using Azure, Terraform, Docker, and GitLab CI/CD.

The project was developed as part of a DevOps bootcamp to gain hands-on experience with infrastructure automation, containerization, CI/CD pipelines, and security scanning.

---

## 1. Project Overview

Cloura combines cloud infrastructure and application deployment into one automated environment.

The project consists of three main components:

- **Cloud Infrastructure:** Azure resources provisioned using Terraform.
- **DevOps Environment:** Self-hosted GitLab and GitLab Runner for CI/CD automation.
- **Full-Stack Application:** An IT Support Ticket System developed using Streamlit, FastAPI, and PostgreSQL.

The goal is to demonstrate an automated workflow from source code changes to application deployment and verification.

## 2. Solution Architecture

The solution is hosted on an Azure Ubuntu virtual machine.

Terraform provisions the required cloud resources, including the Virtual Network, Subnet, Network Security Group, and Virtual Machine.

Docker runs GitLab and the application services, while GitLab Runner executes the CI/CD pipeline using the Shell Executor.

```text
                  Developers
                      |
                      v
               GitLab Repository
                      |
                      v
                 GitLab CI/CD
                      |
                      v
              GitLab Runner
              (Shell Executor)
                      |
                      v
        Test → Build → Security
                      |
                      v
               Deploy → Verify
                      |
                      v
                Docker Compose
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Streamlit    FastAPI    PostgreSQL
       Frontend     Backend     Database
```

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Cloud Platform | Microsoft Azure |
| Infrastructure as Code | Terraform |
| Operating System | Ubuntu Linux |
| Containerization | Docker, Docker Compose |
| Version Control | GitHub, GitLab |
| CI/CD | GitLab CI/CD, GitLab Runner |
| Security Scanning | Trivy |
| Automation | Bash |
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | PostgreSQL |

## 4. Repository Structure

```text
Cloura-fullstack-infr-project/
│
├── app/
│   ├── backend/
│   └── streamlit/
│
├── gitlab/
│
├── terraform/
│
├── scripts/
│   ├── setup-docker.sh
│   ├── deploy-gitlab.sh
│   ├── app-health-check.sh
│   ├── health-check.sh
│   ├── backup.sh
│   └── redeploy.sh
│
├── docker-compose.yml
├── .gitlab-ci.yml
└── README.md
```

## 5. Infrastructure Provisioning

Terraform automates the creation of the Azure infrastructure.

**Provisioned resources:**

- Resource Group
- Virtual Network (VNet)
- Subnet
- Network Security Group (NSG)
- Public IP Address
- Ubuntu Virtual Machine

### Terraform Commands

Navigate to the Terraform directory:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Preview infrastructure changes:

```bash
terraform plan
```

Provision the infrastructure:

```bash
terraform apply
```

Azure authentication, required variables, and permissions must be configured before deployment.

## 6. Docker & GitLab Setup

Docker is used to run the application's containerized services and the self-hosted GitLab instance.

### Docker Installation

The project includes a Bash script that automates Docker Engine and Docker Compose installation on Ubuntu.

```bash
sudo bash scripts/setup-docker.sh
```

Verify the installation:

```bash
docker --version
docker compose version
```

### GitLab & Runner

GitLab is hosted on the Azure virtual machine using Docker.

GitLab Runner is installed directly on the VM and configured with the **Shell Executor** to execute CI/CD jobs.

## 7. CI/CD Pipeline

The GitLab CI/CD pipeline automates the application delivery process through five stages.

| Stage | Description |
|---|---|
| **Test** | Checks backend and frontend Python files for compilation errors |
| **Build** | Validates Docker Compose configuration and builds Docker images |
| **Security** | Scans Docker images using Trivy |
| **Deploy** | Deploys application containers using Docker Compose |
| **Verify** | Runs application health checks after deployment |

### Security Scanning with Trivy

Trivy scans Docker images for **HIGH** and **CRITICAL** vulnerabilities.

The scan is configured with:

```bash
--scanners vuln
--severity HIGH,CRITICAL
--exit-code 0
```

The configuration reports detected vulnerabilities without automatically failing the pipeline because of those findings.

### Deployment

The Deploy stage runs on the `main` branch and starts the application containers:

```bash
docker compose up -d --remove-orphans
```

### Verification

After deployment, the Verify stage runs:

```bash
./scripts/app-health-check.sh
```

This checks the application's health after deployment.

## 8. IT Support Ticket Application

Cloura includes a full-stack IT Support Ticket System that allows users to submit technical support requests.

### Frontend — Streamlit

Provides an interactive interface for entering user information, selecting an issue category, and submitting ticket details.

### Backend — FastAPI

Processes support ticket requests and handles communication with the database.

### Database — PostgreSQL

Stores submitted support tickets.

### Application Workflow

```text
User
  |
  v
Streamlit Frontend
  |
  v
FastAPI Backend
  |
  v
PostgreSQL Database
  |
  v
Ticket Submission Confirmation
```

## 9. Running the Application

Ensure Docker Engine and Docker Compose are installed and the required environment configuration is available.

From the project root:

**Build and start the containers:**

```bash
docker compose up -d --build
```

**Check container status:**

```bash
docker compose ps
```

**View logs:**

```bash
docker compose logs -f
```

**Stop the containers:**

```bash
docker compose down
```

## 10. Security Considerations

The project incorporates several security practices:

- Network access controls through Azure NSG.
- Docker image vulnerability scanning with Trivy.
- Automated application checks through GitLab CI/CD.
- Containerized application components.

This project is an educational prototype rather than a production-ready deployment. Security scanning is informational, and additional hardening would be required for a production environment.

## 11. Project Outcomes

The project provided hands-on experience with:

- Azure infrastructure provisioning using Terraform.
- Linux VM configuration and administration.
- Docker and Docker Compose.
- Self-hosted GitLab and GitLab Runner.
- CI/CD pipeline implementation.
- Automated application deployment.
- Trivy security scanning.
- Bash scripting and operational automation.
- Full-stack application deployment and verification.

## 12. Team Members

- Sara
- Wessal
- Fai
- Ghadeer

---

**Project Status:** Functional DevOps prototype developed for educational and demonstration purposes.
