1. Service Name
QRGen Microservice - QR Code Generator API

2. Description
QRGen is a lightweight REST-based microservice developed using Flask. It generates QR codes from user-provided text or URLs through HTTP API requests.

The service is independent of any particular business application and can be reused by applications such as event registration systems, attendance systems, payment applications, certificate verification systems, and portfolio applications.

3. Technology Stack
Python
Flask
qrcode
Pillow
REST API
Postman for API testing

4. Features
Generate QR codes from text or URLs
Support custom QR code size
Return JSON response containing generation details
Return the generated QR image directly
Validate input parameters
Handle invalid requests using appropriate HTTP status codes
Lightweight and database-independent
Provides a health-check endpoint

5. API Endpoints
5.1 Health Check

Method: GET

URL:

http://127.0.0.1:5000/

Purpose:

Checks whether the microservice is running.

Response:

{
    "service": "QRGen Microservice",
    "status": "running",
    "message": "QR Code Generator API is running"
}

Status Code: 200 OK

5.2 Generate QR Code

Method: GET

URL:

http://127.0.0.1:5000/api/qr

Query Parameters:

Parameter	Required	Description
text	Yes	Text or URL to encode
size	No	QR image size between 100 and 1000 pixels

Sample Request:

GET http://127.0.0.1:5000/api/qr?text=https://example.com&size=300

Successful Response:

Status Code: 200 OK

{
    "success": true,
    "message": "QR code generated successfully",
    "text": "https://example.com",
    "size": 300,
    "image_url": "/api/qr/image?text=https://example.com&size=300"
}
5.3 QR Image Endpoint

Method: GET

URL:

http://127.0.0.1:5000/api/qr/image

Query Parameters:

Parameter	Required	Description
text	Yes	Text or URL to encode
size	No	QR image size between 100 and 1000 pixels

Sample Request:

GET http://127.0.0.1:5000/api/qr/image?text=https://example.com&size=300

Response:

The endpoint returns a PNG image containing the generated QR code.

Status Code: 200 OK

Content-Type:

image/png

6. Input Validation
The service performs the following validations:

The text parameter must be provided.
The text parameter cannot be empty.
The size parameter must be an integer.
The QR size must be between 100 and 1000 pixels.
Unsupported endpoints return HTTP 404.
Unsupported HTTP methods return HTTP 405.

7. Error Responses
7.1 Missing Text

Request:

GET /api/qr

Status: 400 Bad Request

{
    "success": false,
    "error": "Missing required parameter: text"
}
7.2 Invalid Size

Request:

GET /api/qr?text=Hello&size=abc

Status: 400 Bad Request

{
    "success": false,
    "error": "Size must be a valid integer"
}
7.3 Size Out of Range

Request:

GET /api/qr?text=Hello&size=50

Status: 400 Bad Request

{
    "success": false,
    "error": "Size must be between 100 and 1000"
}
7.4 Invalid Endpoint

Request:

GET /api/invalid

Status: 404 Not Found

{
    "success": false,
    "error": "Endpoint not found"
}

8. Installation
Clone or download the project.

Open a terminal inside the project directory.

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Activate it on macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

9. Running the Service
Run:

python app.py

The service starts on:

http://127.0.0.1:5000

You should see output similar to:

* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000

10. Testing in Browser
Health check:

http://127.0.0.1:5000/

Generate QR code:

http://127.0.0.1:5000/api/qr?text=https://example.com&size=300

View the generated QR image:

http://127.0.0.1:5000/api/qr/image?text=https://example.com&size=300

11. Postman Testing
Test 1 - Valid Request

Method:

GET

URL:

http://127.0.0.1:5000/api/qr?text=https://example.com&size=300

Expected status:

200 OK

Expected response:

{
    "success": true,
    "message": "QR code generated successfully",
    "text": "https://example.com",
    "size": 300,
    "image_url": "/api/qr/image?text=https://example.com&size=300"
}
Test 2 - Invalid Request

Method:

GET

URL:

http://127.0.0.1:5000/api/qr

Expected status:

400 Bad Request

Expected response:

{
    "success": false,
    "error": "Missing required parameter: text"
}

12. Microservice Architecture
Client / Student Application
            |
            | HTTP GET
            v
     QRGen Microservice
            |
            v
      Flask REST API
            |
      Input Validation
            |
            v
      QR Code Generator
            |
       +----+----+
       |         |
       v         v
    JSON      PNG Image
   Response    Response

13. Advantages
Simple and reusable
Independent of business logic
No database dependency
Easy integration through REST API
Lightweight deployment
Supports both text and URL-based QR generation
Provides proper HTTP error handling

14. Conclusion
QRGen Microservice demonstrates how a small, reusable functionality can be implemented as an independent REST microservice.

Other applications can communicate with the service using HTTP requests without implementing QR code generation themselves.