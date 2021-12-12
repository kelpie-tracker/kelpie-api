# kelpie-api
API to control locations and mobile entities for Kelpie Tracker

Resources available for API access:
* [**Fence**](https://github.com/kelpie-tracker/kelpie-api#fence-fences)
* [**Positions**](https://github.com/kelpie-tracker/kelpie-api#position-positions)

## Methods
Requests for the API must follow the standards:
| Method | Description |
|---|---|
| `GET` | Returns information from one or more records. |
| `POST` | Used to create a new record. |

## Response Code

| Code | Description |
|---|---|
| `200` | Request executed successfully (success).|
| `400` | Validation errors or the fields entered do not exist in the system.|
| `401` | Invalid access data.|
| `404` | Searched record not found (Not found).|
| `405` | Method not implemented.|
| `410` | Searched record has been deleted from the system and is no longer available.|
| `422` | Data reported is outside the scope defined for the field.|
| `429` | Maximum number of requests reached. (*wait a few seconds and try again*)|

# Group Resources


# Fence [/fences]

Geographical barriers to delimit the space of a region.

### List [GET]

+ Request (application/json)

+ Response 200 (application/json)

    + Body

          [
            {
                "bottom": -22.9463,
                "id": 1,
                "left": -43.1963,
                "registered_on": "2021-12-12T11:03:55",
                "right": -43.1777,
                "up": -22.9273
            }
        ]

### New (Create) [POST]

+ Attributes (object)

    + up (float, optional)
    + right (float, optional)
    + bottom (float, optional)
    + left (float, optional)

+ Request (application/json)

    + Body

            {
                "up": -22.927271836395280,
                "right": -43.17771782650461,
                "bottom": -22.946273929306827,
                "left": -43.19634344082100
            }

+ Response 200 (application/json)

    + Headers

            X-RateLimit-Limit: 60
            X-RateLimit-Remaining: 59

    + Body

            {
                "message": "new fence added"
            }


# Position [/positions]

Positions of mobile entities being monitored.

### List [GET]

+ Request (application/json)

+ Response 200 (application/json)

    + Body

            [
                {
                    "date": "2021-11-04",
                    "id": "1111",
                    "latitude": -43.4684,
                    "longitude": -23.0208
                }
            ]

### New (Create) [POST]

+ Attributes (object)

    + id: contact name (string, required) - 255 characters limit
    + longitude (float, optional)
    + latitude (float, optional)

+ Request (application/json)

    + Body

            {
                "id": "1111",
                "longitude": -23.0208077,
                "latitude": -43.4683931
            }

+ Response 200 (application/json)

    + Headers

            X-RateLimit-Limit: 60
            X-RateLimit-Remaining: 59

    + Body

            {
                "message": "new position added"
            }
