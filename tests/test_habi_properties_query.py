import pytest
import threading
from app.habi_properties_query import server
import requests
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("SERVICE_HOST", "localhost")
PORT = os.getenv("SERVICE_PORT", "8000")


@pytest.fixture(scope='module')
def fixture_server():
    """
    This fixture server will be used for generate and isolated environment for 'deploy and run' our API service.
    Doing this will garantee an execution of the API service until it reaches the expected results in the tests.
    """
    fake_server = threading.Thread(target=server)
    fake_server.daemon = True
    fake_server.start()


def test_endpoint_empty_response(fixture_server):
    """
    This test checks if passing a request body that can't find any Habi properties with the specified filters, it
    needs to return an empty response with a success status code (200).

    :param fixture_server: The fixture server method for mocking the server and execute this test.
    """

    # This filters will no return any data from bbdd, so we're gonna pass it to get an empty response.
    data = {
        "year": 2021,
        "city": "bogota",
        "status": "en_venta"
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(f'http://{HOST}:{PORT}/get_properties', json=data, headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_endpoint_normal_response(fixture_server):
    """
    This test checks if passing a request body with filters that could satisfy the Habi properties data, the endpoint
    might return a normal response with data and a success status code (200).

    :param fixture_server: The fixture server method for mocking the server and execute this test.
    """

    data = {
        "city": "bogota",
        "status": "en_venta"
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(f'http://{HOST}:{PORT}/get_properties', json=data, headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_endpoint_bad_request_body(fixture_server):
    """
    This test checks if the request body has and invalid format or data (like wrong filter fields), the endpoint will
    return an status code 400 and an error message.

    :param fixture_server: The fixture server method for mocking the server and execute this test.
    """

    data = {
        "city": "bogota",
        "status": "en_venta",
        "test": "will fail"
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(f'http://{HOST}:{PORT}/get_properties', json=data, headers=headers)
    assert response.status_code == 400
    assert 'Error en la solicitud realizada' in response.text
