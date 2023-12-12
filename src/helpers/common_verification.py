# HTTP Status Verification

def verify_https_status_code(response, expected_status):
    assert response.status_code == expected_status, \
        f"Expected HTTPS Status is : {expected_status}, current status is {response.status_code}"


def verify_json_key_is_present(key):
    assert key is not None, f"The key {key} is empty"
    