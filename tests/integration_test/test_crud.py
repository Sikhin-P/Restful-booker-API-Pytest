import pytest
from src.helpers.api_request_wrapper import post_request, put_request, delete_request
from src.constants.api_constants import create_booking_url, create_token_url, patch_put_delete_booking_url
from src.helpers.payload_manager import payload_create_booking, payload_update_booking
from src.helpers.utils import common_headers_json
from src.helpers import payload_manager
from src.helpers.common_verification import verify_json_key_is_present, verify_https_status_code


class TestCRUD:

    def test_create_token(self):
        response = post_request(url=create_token_url(), auth=None, headers=common_headers_json(),
                                payload=payload_manager.payload_create_token(), in_json=False)
        verify_json_key_is_present(response.json()['token'])
        verify_https_status_code(response, 200)
        pytest.auth_token = response.json()['token']
        return response.json()['token']

    def test_create_booking(self):
        response = post_request(url=create_booking_url(), auth=None,
                                headers=common_headers_json(), payload=payload_create_booking(), in_json=False)
        verify_json_key_is_present(response.json()['bookingid'])
        verify_https_status_code(response, 200)
        pytest.booking_id = str(response.json()['bookingid'])
        return response.json()['bookingid']

    def test_update_booking(self):
        url = patch_put_delete_booking_url(pytest.booking_id)
        header = common_headers_json()
        header['Cookie'] = 'token=' + pytest.auth_token
        response = put_request(url=url, auth=None, headers=header,
                               payload=payload_update_booking(), in_json=False)
        verify_https_status_code(response, 200)

    def test_delete_booking(self):
        url = patch_put_delete_booking_url(pytest.booking_id)
        header = common_headers_json()
        header['Cookie'] = 'token=' + pytest.auth_token
        response = delete_request(url=url, auth=None, headers=header,
                                  in_json=False)
        verify_https_status_code(response, 201)
