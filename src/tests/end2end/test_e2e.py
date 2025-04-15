import allure
import pytest
from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *
class TestE2E(object):
    @allure.title("E2E - create booking -> update booking -> delete booking")
    @allure.description("verify the create booking id, when we update we are able to update and delete it also | Full "
                        "CRUD")
    def test_update_booking_with_id_token(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_put_patch_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response.status_code,expected_data=200)
        verify_response_key(response.json()["firstname"],expected_data="Tim")
        verify_response_key(response.json()["lastname"],expected_data="Brown")


    @allure.title("Test CRUD operation, delete")
    @allure.description("verify booking gets deleted with booking id and token")
    def test_delete_booking_id(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_put_patch_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            in_json=False
        )
        verify_http_status_code(response_data=response.status_code,expected_data=201)
        verify_response_delete(response=response.text)





