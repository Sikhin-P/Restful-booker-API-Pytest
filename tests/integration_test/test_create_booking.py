import pytest
from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import create_booking_url
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_json_key_is_present, verify_https_status_code


class TestCreateBooking:

    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response = post_request(url=create_booking_url(), auth=None,
                                headers=common_headers_json(),payload=payload_create_booking(), in_json=False)
        verify_json_key_is_present(response.json()['bookingid'])
        verify_https_status_code(response, 200)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_request(url=create_booking_url(), auth=None,
                                headers=common_headers_json(), payload={}, in_json=False)
        verify_https_status_code(response, 500)


