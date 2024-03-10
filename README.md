# coordservice

## Description:
This FastAPI service utilizes the coordextract library to process GPX 
files, extract coordinates, convert them to MGRS, and return the data 
as serialized JSON. 

## Requirements:
- FastAPI
- Uvicorn (for serving the application)
- coordextract 
- pydantic (for data validation and serialization)

## Installation:
This was developed using Poetry. Fore easy installation install Poetry 
by following the instructions at 
https://python-poetry.org/docs/#installation.

1. Clone the coordservice repository to your local machine.
2. Navigate to the coordservice directory.
3. Run `poetry install` to install the project dependencies.

## Usage:
1. Start the FastAPI server:
   uvicorn main:app --reload

2. Endpoint Usage:
   The service provides a single endpoint `/process-gpx` that accepts 
   POST requests with a GPX file. The file should be included in the 
   request body as form-data.

3. cURL Example:
   curl -X 'POST' \
     'http://127.0.0.1:8000/process-gpx' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@path_to_your_gpx_file.gpx;type=application/gpx+xml'

   Replace `path_to_your_gpx_file.gpx` with the actual path to your 
   GPX file.

4. Response:
   The response will be JSON serialized data of the processed GPX file, 
   including coordinates and their MGRS conversion.

## License:
This project is licensed under the MIT License - see the LICENSE file 
for details.

