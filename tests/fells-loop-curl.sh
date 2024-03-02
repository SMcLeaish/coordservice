#!/bin/bash
curl -X 'POST' 'http://127.0.0.1:8000/process-gpx/'  -H 'accept: application/json'  -H 'Content-Type: multipart/form-data'  -F 'file=@data/fells_loop.gpx;type=application/gpx+xml'
