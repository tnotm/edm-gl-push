# edm-gl-push-nonprd.ps1
# Requires: Yaml module (Install-Module Yaml) and PowerShell 5.1+
# Usage: .\edm-gl-push-nonprd.ps1

# Load configuration
$config = ConvertFrom-Yaml -InputString (Get-Content -Path config.yaml -Raw)

# Configure logging
$logFile = "dimension_export.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

function Log {
    param($message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] $message"
    Add-Content -Path $logFile -Value $logEntry
}

try {
    # Loop through all dimension/environment combinations
    foreach ($dimension in $config.dimensions) {
        foreach ($environment in $config.environments) {
            try {
                # Build payload
                $payload = @{
                    dimension = $dimension
                    environment = $environment
                }

                # API call with error handling
                $response = Invoke-RestMethod -Uri $config.api_url `
                    -Method Post `
                    -Body (ConvertTo-Json $payload) `
                    -Headers @{ 'Content-Type' = 'application/json' } `
                    -Credential (New-Object System.Management.Automation.PSCredential ($config.api_user, (ConvertTo-SecureString $config.api_password -AsPlainText -Force)))

                # Log success
                Log "✅ Success: $dimension → $environment (Status: $($response.status))"
                
            } catch {
                $errorDetails = $_.Exception.Message
                Log "⚠️ API call failed for $dimension → $environment: $errorDetails"
                continue  # Continue with next dimension
            }
        }
    }
} catch {
    # Critical error handling
    Log "❌ CRITICAL ERROR: $($_.Exception.Message)"
    exit 1
}