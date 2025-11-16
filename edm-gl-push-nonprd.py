# src/main.py
import logging
import requests
from datetime import datetime
import os
from pathlib import Path

# Load configuration from your existing config.yaml
config_path = Path("config.yaml")
if not config_path.exists():
    raise FileNotFoundError(f"Config file not found at {config_path}")

try:
    with open(config_path, 'r') as f:
        config = {
            "environments": [env.strip() for env in f.read().splitlines() if env.strip()],
            "dimensions": [dim.strip() for dim in f.read().splitlines() if dim.strip()],
            "api_url": os.getenv("API_URL", "https://your-api-url.com/epm/rest/v1")
        }
except Exception as e:
    raise RuntimeError(f"Failed to load config: {str(e)}")

# Configure environments and dimensions from config
ETJO_ENVIRONMENTS = config["environments"]
DIMENSIONS = config["dimensions"]
API_BASE_URL = config["api_url"]

# Get auth from environment variables (more secure than hardcoded)
API_USER = os.getenv("API_USER", "your_username")
API_PASSWORD = os.getenv("API_PASSWORD", "your_password")
AUTH = (API_USER, API_PASSWORD)

# Configure logging (production-ready)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f'dimension_export_{datetime.now().strftime("%Y%m%d")}.log', mode='a')
    ]
)
logger = logging.getLogger("dimension_export")

def generate_payload(dim: str, env: str) -> dict:
    """Generate payload with proper error handling and validation"""
    try:
        return {
            "applicationName": "Fusion GL",
            "dimensionName": dim,
            "fileName": f"{dim}.csv",
            "connection": env
        }
    except Exception as e:
        logger.error(f"Failed to generate payload for dim={dim}, env={env}: {str(e)}")
        raise

def process_payload(dim: str, env: str):
    """Process payload with comprehensive error handling"""
    try:
        # Generate payload
        payload = generate_payload(dim, env)
        
        # Log payload for verification
        logger.info(f"Generating payload for {dim} → {env}: {payload}")
        
        # Make API call
        response = requests.post(
            f"{API_BASE_URL}/dimensions/byName/export",
            json=payload,
            auth=AUTH,
            timeout=30  # Prevent hanging requests
        )
        
        # Handle API response
        if response.status_code >= 400:
            error_msg = f"API error ({response.status_code}): {response.text}"
            logger.error(f"Failed to process {dim} → {env}: {error_msg}")
            raise Exception(error_msg)
        
        logger.info(f"✅ Success! {dim} → {env} (Status: {response.status_code})")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.exception(f"Network error processing {dim} → {env}: {str(e)}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error processing {dim} → {env}: {str(e)}")
        raise

# 🔥 Execute the full export process
logger.info(f"{'='*50}")
logger.info(f"STARTING DIMENSION EXPORT PROCESS")
logger.info(f"{'='*50}")

try:
    for env in ETJO_ENVIRONMENTS:
        for dim in DIMENSIONS:
            try:
                process_payload(dim, env)
            except Exception as e:
                logger.exception(f"Critical failure in {dim} → {env}: {str(e)}")
                continue
    logger.info(f"{'='*50}")
    logger.info(f"EXPORT PROCESS COMPLETE")
    logger.info(f"{'='*50}")
    
except Exception as e:
    logger.critical(f"SEVERE SYSTEM FAILURE: {str(e)}")
    raise