#!/bin/bash
# run_export.sh
# Requires: yq (YAML processor) and curl
# Usage: chmod +x run_export.sh && ./run_export.sh

# Load configuration
API_URL=$(yq e '.api_url' config.yaml)
API_USER=$(yq e '.api_user' config.yaml)
API_PASSWORD=$(yq e '.api_password' config.yaml)
DIMENSIONS=$(yq e '.dimensions[]' config.yaml)
ENVIRONMENTS=$(yq e '.environments[]' config.yaml)

LOG_FILE="dimension_export.log"

# Create log file with timestamp
echo "[$(date +'%Y-%m-%d %H:%M:%S')] STARTING DIMENSION EXPORT PROCESS" >> $LOG_FILE

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Process all combinations
for dimension in $DIMENSIONS; do
    for environment in $ENVIRONMENTS; do
        # API call with error handling
        response=$(curl -s -X POST -H "Content-Type: application/json" \
            -u "$API_USER:$API_PASSWORD" \
            -d "{\"dimension\": \"$dimension\", \"environment\": \"$environment\"}" \
            "$API_URL" 2>/dev/null)

        if [ $? -eq 0 ]; then
            status=$(echo "$response" | jq -r '.status')
            log "✅ Success: $dimension → $environment (Status: $status)"
        else
            log "⚠️ API call failed for $dimension → $environment"
            # Optional: Add retry logic here
            # sleep 2
        fi
    done
done

log "[$(date +'%Y-%m-%d %H:%M:%S')] PROCESS COMPLETED"