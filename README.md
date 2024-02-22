# EC530---APIs, Databases & Containers
Trying out sample APIs to use in a Remote Health Monitoring System

**API for reading data from the sensors
A basic outline of the API:**
1. Endpoint - '/sensor-data'
2. Method - POST
3. This API allows users to send readings from sensors on the patient to the system
4. API need authorization through access tokens, which must be given in the request headers
5. Only authorized users will be granted access the endpoint
6. The request body must contain the data structured in proper JSON format, for example,
   {
  "sensor_id": "ABCD",
  "timestamp": "2024-02-12T08:00:00",
  "data": {
    "temperature": 36.5,
    "pulse": 75,
    "bp": {
      "systolic": 120,
      "diastolic": 80
        }
      }
    }
7. The API if successful would respond with a success code (200) or return error messages with error codes
8. Data sent should be encrypted in HTTPS for security

**API for device interface
A basic outline of the API:**
1. Endpoint - '/devices'
2. Methods - GET (retrieve), POST (register), PUT (update), DELETE (delete)
3. This API lets users manage the devices in the system
4. API need authorization through access tokens, which must be given in the request headers
5. Only authorized users will be granted access the endpoint
6. GET - Retrives the list of all devices in the system
7. POST - Registes devices in the system when data is given in JSON form, for example,
   {
  "device_id": "A1B2C3",
  "name": "BP Monitor",
  "status": "Active"
    }
8. PUT - Updates information about a device when request is given in JSON format, for example,
   {
  "name": "Updated BP Monitor",
  "status": "Inactive"
    }
10. DELETE - Deletes a device from the system
11. The API if successful would respond with a success code (200) or return error messages with error codes
12. Data sent should be encrypted in HTTPS for security
