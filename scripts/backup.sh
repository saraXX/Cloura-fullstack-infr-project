#!/bin/bash

set -e

BACKUP_DIR="/srv/gitlab-backups"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

echo "======================================"
echo " GitLab Backup"
echo "======================================"

# -------------------------------------------------------
# 1. Create backup directory
# -------------------------------------------------------

echo ""
echo "1. Preparing backup directory..."

sudo mkdir -p "$BACKUP_DIR"

# -------------------------------------------------------
# 2. Create GitLab application backup
# -------------------------------------------------------

echo ""
echo "2. Creating GitLab application backup..."

sudo docker exec gitlab \
    gitlab-backup create

# -------------------------------------------------------
# 3. Back up GitLab configuration
# -------------------------------------------------------

echo ""
echo "3. Backing up GitLab configuration..."

sudo tar -czf \
    "$BACKUP_DIR/gitlab-config-$TIMESTAMP.tar.gz" \
    /srv/gitlab/config

# -------------------------------------------------------
# 4. Show backup files
# -------------------------------------------------------

echo ""
echo "4. GitLab application backups:"

sudo ls -lh /srv/gitlab/data/backups

echo ""
echo "5. GitLab configuration backups:"

sudo ls -lh "$BACKUP_DIR"

echo ""
echo "======================================"
echo " Backup completed successfully"
echo "======================================"