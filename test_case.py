
Test_Case = "Checking an API for Outdoor Temperature and Response Time"

Purpose = "To verify the availability and functionality of an API for obtaining outdoor temperature using an API key"

Prerequisites = "You have access to an API key that allows you to retrieve weather-related data"

Steps = [
    "Obtain an API key for accessing weather information.",
    "Create a GET request to the API, including the API key in the request header.",
    "Specify the necessary parameters, such as location coordinates or city name.",
    "Execute the request."
]

Expected_Result = [
    "The response should have a status code of 200 (Successful request).",
    "The response should contain data about the outdoor temperature."
]

Postconditions = [
    "Verify that the response contains data about the temperature.",
    "Check the response time - the time taken to receive a response from the API should not exceed a certain threshold (e.g., 1 second)"
]

