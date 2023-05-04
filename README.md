# temperature-conversion

Celsius to Fahrenheit Converter API
This Flask API converts Celsius temperature to Fahrenheit temperature.

Installation:

Clone this repository to your local machine.
Create and activate a virtual environment:

$ python3 -m venv venv
$ source venv/bin/activate

Install the required packages:


$ pip install -r requirements.txt
Run the Flask application:


Use your preferred HTTP client to interact with the API at http://localhost:5000/convert.


Request:
Send a GET request to http://localhost:5000/convert with the Celsius temperature to be converted as a query parameter:

Body:
{
    "celsius": 0
}


Response:
The response will be a JSON object containing the Fahrenheit temperature:


Output:

{   
    "fahrenheit": 32.0
}

