# EDM to GL Push - non-PRD
_Create script to push EDM dimensions to Oracle Fusion ERP_

## Requirements
 * Load all non-prod environments not currently connected via Autosys
 * Load all dimensions to each envionment
 * Monitor each dimension load for completion.

## Steps required to load a dimension
 * Export a dimension by name
 * Poll the result until Status = COMPLETED or ERROR

## Basic design

* For each environment
    * For each dimension
        * run Exprot API
            * poll completion with Result API until complete

## Environment List
ETJO-TEST, ETJO-DEV12, ETJO-DEV3, ETJO-DEV5, ETJO-DEV13, ETJO-DEV14, ETJO-DEV1, ETJO-DEV10

## Dimension List
Account AG COA
Account AG COA FR
BSV AG COA
Deparment AG COA
Future1 AG COA
Future2 AG COA
Intercompany AG COA
Offering AG COA
Office AG COA
Reporting Segment AG COA

## Documents
_Reference documents for API_

 * [edm-swagger.json](docs/edm-swagger.json] - Complete download of all EDM API endpoints with arguments.
 * [export-api.md](docs/export-api.md)
 * [result-api.md](docs/result-api.md)