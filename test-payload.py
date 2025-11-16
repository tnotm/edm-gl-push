ETJO_ENVIRONMENTS = [
    "ETJO-TEST",
    "ETJO-DEV12",
    "ETJO-DEV3"
]

DIMENSIONS = [
    "Account AG COA",
    "Account AG COA FR",
    "BSV AG COA"
]

for env in ETJO_ENVIRONMENTS:
    for dim in DIMENSIONS:
        payload = {
            "applicationName": "Fusion GL",
            "dimensionName": dim,
            "fileName": f"{dim}.csv",
            "connection": env
        }
        print(f"Payload for {dim} → {env}: {payload}")