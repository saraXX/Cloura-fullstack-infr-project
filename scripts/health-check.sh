#!/bin/bash

set -e

GITLAB_DIR="/home/azureuser/gitlab"

echo "======================================"
echo " GitLab Health Check"
echo "======================================"

# -------------------------------------------------------
# 1. Check Docker service
# -------------------------------------------------------

echo ""
echo "1. Checking Docker service..."

if sudo systemctl is-active --quiet docker; then
    echo "Docker: OK"
else
    echo "Docker: FAILED"
    exit 1
fi

# -------------------------------------------------------
# 2. Check GitLab container
# -------------------------------------------------------

echo ""
echo "2. Checking GitLab container..."

cd "$GITLAB_DIR"

if sudo docker ps \
    --format '{{.Names}}' \
    | grep -q "^gitlab$"; then

    echo "GitLab container: RUNNING"

else

    echo "GitLab container: NOT RUNNING"
    exit 1

fi

# -------------------------------------------------------
# 3. Check GitLab internal health
# -------------------------------------------------------

echo ""
echo "3. Checking GitLab internal health..."

sudo docker exec gitlab \
    gitlab-rake gitlab:check SANITIZE=true

echo ""
echo "======================================"
echo " GitLab health check passed"
echo "======================================"