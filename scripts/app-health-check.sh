#!/bin/bash

set -e

echo "======================================"
echo " CloudAura Application Health Check"
echo "======================================"

# -------------------------------------------------------
# 1. Check PostgreSQL
# -------------------------------------------------------

echo ""
echo "1. Checking PostgreSQL..."

if docker compose exec -T db pg_isready \
    -U "${POSTGRES_USER}" \
    -d "${POSTGRES_DB}" > /dev/null 2>&1; then

    echo "PostgreSQL: OK"

else

    echo "PostgreSQL: FAILED"
    exit 1

fi

# -------------------------------------------------------
# 2. Check FastAPI
# -------------------------------------------------------

echo ""
echo "2. Checking FastAPI..."

fastapi_ok=false

for i in $(seq 1 10); do

    if curl -fsS "http://localhost:8000/health" > /dev/null 2>&1; then
        fastapi_ok=true
        break
    fi

    echo "Waiting for FastAPI... (attempt $i/10)"
    sleep 2

done

if [ "$fastapi_ok" = true ]; then
    echo "FastAPI: OK"
else
    echo "FastAPI: FAILED"
    exit 1
fi

# -------------------------------------------------------
# 3. Check Streamlit
# -------------------------------------------------------

echo ""
echo "3. Checking Streamlit..."

streamlit_ok=false

for i in $(seq 1 10); do

    if curl -fsS "http://localhost:8501" > /dev/null 2>&1; then
        streamlit_ok=true
        break
    fi

    echo "Waiting for Streamlit... (attempt $i/10)"
    sleep 2

done

if [ "$streamlit_ok" = true ]; then
    echo "Streamlit: OK"
else
    echo "Streamlit: FAILED"
    exit 1
fi

echo ""
echo "======================================"
echo " Application health check passed"
echo "======================================"