#!/bin/bash

set -e

GITLAB_DIR="/home/azureuser/gitlab"

echo "======================================"
echo " GitLab Deployment"
echo "======================================"

# -------------------------------------------------------
# 1. Check Docker service
# -------------------------------------------------------

echo ""
echo "1. Checking Docker..."

if sudo systemctl is-active --quiet docker; then
    echo "Docker: RUNNING"
else
    echo "Docker is not running. Starting Docker..."
    sudo systemctl start docker
fi

# -------------------------------------------------------
# 2. Check Docker Compose
# -------------------------------------------------------

echo ""
echo "2. Checking Docker Compose..."

sudo docker compose version

# -------------------------------------------------------
# 3. Validate GitLab Compose configuration
# -------------------------------------------------------

echo ""
echo "3. Validating GitLab configuration..."

cd "$GITLAB_DIR"

sudo docker compose config --quiet

echo "GitLab configuration: VALID"

# -------------------------------------------------------
# 4. Start GitLab
# -------------------------------------------------------

echo ""
echo "4. Starting GitLab..."

sudo docker compose up -d

# -------------------------------------------------------
# 5. Show status
# -------------------------------------------------------

echo ""
echo "5. GitLab container status..."

sudo docker compose ps

echo ""
echo "======================================"
echo " GitLab deployment completed"
echo "======================================"