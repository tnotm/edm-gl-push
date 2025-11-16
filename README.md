# Dimension Export Automation

This project contains production-ready scripts for pushing dimension exports to your API with robust error handling and comprehensive logging.

## Features
- Production-grade error handling
- Comprehensive logging with timestamps
- Configurable through YAML
- Cross-platform compatibility (PowerShell, Bash, Python)
- Automatic log file generation
- Clear error reporting

## Prerequisites

### For PowerShell
- PowerShell 5.1+
- [Yaml module](https://www.powershellgallery.com/packages/Yaml/)

### For Bash
- [yq](https://github.com/mikefarah/yq) (YAML processor)
- curl

### For Python
- Python 3.7+
- `pip install requests` (for API calls)
- `pip install pyyaml` (for YAML parsing)

## Installation

1. Create a `config.yaml` file with your configuration:
```yaml
api_url: "https://your-api-url.com/epm/rest/v1"
api_user: "your_api_username"
api_password: "your_api_password"
dimensions:
  - "Account AG COA"
  - "Account AG COA FR"
environments:
  - "ETJO-TEST"
  - "ETJO-PROD"
```

2. Save the scripts to your project root:
- PowerShell: `edm-gl-push-nonprd.ps1`
- Bash: `run_export.sh`
- Python: `run_export.py`

## How to Use

### PowerShell Script
1. Install the Yaml module: `Install-Module -Name Yaml`
2. Run the script: `.\\edm-gl-push-nonprd.ps1`

### Bash Script
1. Install yq: `brew install yq` (macOS) or `sudo apt-get install yq` (Ubuntu)
2. Make the script executable: `chmod +x run_export.sh`
3. Run the script: `./run_export.sh`

### Python Script
1. Ensure Python 3.7+ is installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python run_export.py`

## Logging

All logs are written to `dimension_export.log` in the **current working directory** (where you run the script) with this format:
```
[2023-10-05 14:30:22] ✅ Success: Account AG COA → ETJO-TEST (Status: 200)
[2023-10-05 14:30:25] ⚠️ API call failed for Account AG COA FR → ETJO-PROD
```

## Error Handling

| Error Type | Behavior |
|------------|----------|
| API failure | Logs warning with context |
| Critical error | Exits with status 1 |
| Configuration issue | Logs detailed error |

## Security Note

> 🔒 **Critical Security Consideration**:
> - Never commit credentials to version control
> - Use environment variables or secret managers for sensitive data
> - The example config shows credentials in plaintext - this is for demonstration only

## Version Information

> 💡 **Version 1.0** (2023-10-05):
> - Initial production-ready implementation
> - Supports PowerShell, Bash, and Python
> - Comprehensive logging and error handling

## Troubleshooting

- **Missing log entries?** Check permissions on the log file
- **API failures?** Verify your API credentials and URL in `config.yaml`
- **Script not running?** Ensure dependencies are installed
- **Log file issues?** Check for permission errors or file corruption
- **Python errors?** Run `pip install -r requirements.txt` first

## Example Workflow

1. Create `config.yaml` with your credentials
2. Save scripts to project root
3. Run the appropriate script:
   - PowerShell: `.\\edm-gl-push-nonprd.ps1`
   - Bash: `./run_export.sh`
   - Python: `python run_export.py`
4. Check `dimension_export.log` for results

> 💡 Pro Tip: Add `--verbose` flag to PowerShell script for more detailed logs

## MIT License 2025
_The MIT License is one of the most simple and permissive free software licenses, allowing anyone to use, copy, modify, distribute, and even sell the software for free. It grants these permissions with almost no restrictions, giving developers maximum flexibility for their own projects. The only requirement is that the original copyright notice and the license text itself must be included with all copies or substantial portions of the software._