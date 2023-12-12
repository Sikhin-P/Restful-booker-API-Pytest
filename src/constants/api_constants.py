# Add the constants here...

def base_url():
    return 'https://restful-booker.herokuapp.com'


def create_booking_url():
    return 'https://restful-booker.herokuapp.com/booking'


def create_token_url():
    return 'https://restful-booker.herokuapp.com/auth'


def patch_put_delete_booking_url(booking_id):
    return 'https://restful-booker.herokuapp.com/booking/' + booking_id


