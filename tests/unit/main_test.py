"""
This file contains the tests for the main module.
"""
from unittest.mock import patch, MagicMock
import pytest
from httpx import AsyncClient
from coordextract_service.main import app  #

@pytest.mark.asyncio
async def test_process_gpx_endpoint()-> None:
    """
    Test the /process-gpx/ endpoint.
    """
    with patch('pathlib.Path.open') as mock_open, \
         patch('shutil.copyfileobj') as mock_copyfileobj, \
         patch('coordextract_service.main.process_coords', return_value\
               ={"status": "success"}) as mock_process_coords, \
         patch('pathlib.Path.unlink') as mock_unlink:
        mock_open.return_value = MagicMock()
        file_content = b'GPX data here'
        files = {'file': ('test.gpx', file_content)}

        async with AsyncClient(app=app, base_url="http://testserver") as ac:
            response = await ac.post("/process-gpx/", files=files)

        assert response.status_code == 200
        assert response.json() == {"status": "success"}

        mock_open.assert_called_once()
        mock_copyfileobj.assert_called_once()
        mock_process_coords.assert_called_once()
        mock_unlink.assert_called_once()
