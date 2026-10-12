#!/bin/bash

set -e

GITLAB_DIR="/home/azureuser/gitlab"

echo "======================================"
echo " GitLab Redeployment"
echo "======================================"

# -------------------------------------------------------
# 1. Go to GitLab directory
# -------------------------------------------------------

echo ""
echo "1. Opening GitLab deployment directory..."

cd "$GITLAB_DIR"

# -------------------------------------------------------
# 2. Validate Docker Compose configuration
# -------------------------------------------------------

echo ""
echo "2. Validating GitLab configuration..."

sudo docker compose config --quiet

echo "GitLab configuration: VALID"

# -------------------------------------------------------
# 3. Recreate GitLab container
# -------------------------------------------------------

echo ""
echo "3. Recreating GitLab container..."

sudo docker compose up -d --force-recreate

# -------------------------------------------------------
# 4. Show current status
# -------------------------------------------------------

echo ""
echo "4. Checking GitLab status..."

sudo docker compose ps

echo ""
echo "======================================"
echo " GitLab redeployment completed"
echo "======================================"