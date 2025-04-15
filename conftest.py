#To reuse the create token and create booking fn in all the testcases

import allure
import pytest
from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *


@pytest.fixture(scope="session")
def create_token():
    response = post_request(url=APIConstants().url_create_token(),
                            auth=None,
                            headers=Utils().common_headers_json(),
                            payload=payload_create_token(),
                            in_json=False)
    verify_http_status_code(response_data=response.status_code,expected_data=200)
    verify_json_key_not_none(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            auth=None,
                            headers=Utils().common_headers_json(),
                            payload=payload_create_booking(),
                            in_json=False)
    booking_id=response.json()["bookingid"]
    verify_http_status_code(response_data=response.status_code,expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id

