import allure
import pytest
import logging #To print the message/logs

from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify the create booking status and booking id should not be null")
    @allure.description("Creating a booking from the payload and verify that booking id is not null")
    def test_create_booking_positive(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the Testcase of TestCreateBoooking")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        logger.info("Post request done")
        logger.info("Now verifying")
        verify_http_status_code(response_data=response.status_code, expected_data=200)
        logger.info(f"Response I got : {response.json()}")
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])
        logger.info(f"Booking id : {response.json()["bookingid"]}")

    @pytest.mark.negative
    @allure.title("verify the create booking status when booking id is null")
    @allure.description("Creating a booking from the payload when booking id is null")
    def test_create_booking_negative(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the Testcase of TestCreateBooking")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        logger.info("Post request done")
        logger.info("Now verifying")
        verify_http_status_code(response_data=response.status_code, expected_data=500)

    @pytest.mark.negative2
    @allure.title("verify the create booking status when firstname is null")
    @allure.description("Creating a booking from the payload when firstname is null")
    def test_create_booking_negative2(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the Testcase of TestCreateBoooking")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={"name" : "Waquar"},
            in_json=False
        )
        logger.info("Post request done")
        logger.info("Now verifying")
        verify_http_status_code(response_data=response.status_code, expected_data=500)





