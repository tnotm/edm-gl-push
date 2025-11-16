## Export a Dimension by Name

 * Type: Post
 * API Call: /epm/rest/v1/dimensions/byName/export

## Example cURL Command

``` bash
curl --user epm_cloud_user -X POST -H 'Content-Type: application/json' -d @example_request_payload.json https://servername.fa.us2.oraclecloud.com/epm/rest/v1/dimensions/byName/export
```

## Example of call:

```json
{
    "applicationName": "Corporate Planning",
    "dimensionName": "Account"
    "fileName": "Account.csv",
    "connection": "Production"
}
```
    
## Example Response(initial):
```json
{
  "links": [
    {
      "rel": "results",
      "href": "http://servername.fa.us2.oraclecloud.com/epm/rest/v1/jobRuns/81ecd091-f969-4053-85ef-3718d1ad63b0"
    }
  ]
}
```

## Example of Job Run Result
```json
{
    "id": "0105ee75-3f15-4efd-b725-a1769001fbfa",
    "description": "Exporting dimension Account (cdefe5d3-0f9b-4b11-8c2d-91af7f1b3ec5) to connection Production (d35589c5-e69d-48e9-9354-0485d69c06a5)",
    "origin": "EXPORT_DIMENSION",
    "status": "COMPLETED",
    "result": {
        "success": false,
        "dimensionName": "Account",
        "failedViewpoints": [],
        "links": [],
        "startTime": "2023-05-04T07:59:35.317Z",
        "endTime": "2023-05-04T07:59:38.429Z",
        "connectionName": "Production",
        "recordCount": 0,
        "runByUser": "epm_default_cloud_admin",
        "tasks": [
            {
                "syncId": "4cae87ac-735f-4c00-acd0-b23e01a80d44",
                "taskName": "Transfer file to Financials Cloud",
                "taskKey": "export.fincloud.export.transfer.file.task.name",
                "status": "ERROR",
                "startTime": "2023-05-04T07:59:38.029Z",
                "endTime": "2023-05-04T07:59:38.433Z",
                "duration": "00:00:00.404",
                "messages": [
                    "Transfer file to Financials Cloud failed because of the following reason: Unknown host 'https://fuscdrmsmc76-fa-ext.us.oracle.com/'.  Check and modify the connection details and ensure the connected system is online"
                ]
            }
        ],
        "messages": "Exported 418 records for viewpoint 'Account Vision Chile'.\nExported 418 records for viewpoint 'Account Vision Chile | Account Vision Chile Base'.\nExported 418 records for viewpoint 'Account Vision Chile | Account Vision Chile Current'.\n"
    },
    "created": "2023-05-04T07:59:35.331Z",
    "createdBy": "8bc5dbf7-fcd4-462e-a1c7-e72d0b92fbfb",
    "lastModified": "2023-05-04T07:59:38.497Z",
    "lastModifiedBy": "8bc5dbf7-fcd4-462e-a1c7-e72d0b92fbfb",
    "links": [
        {
            "rel": "self",
            "href": "http://servername.fa.us2.oraclecloud.com/epm/rest/v1/jobRuns/81ecd091-f969-4053-85ef-3718d1ad63b0/result"
        },
        {
            "rel": "jobRun",
            "href": "http://servername.fa.us2.oraclecloud.com/epm/rest/v1/jobRuns/81ecd091-f969-4053-85ef-3718d1ad63b0"
        }
    ]
}
```