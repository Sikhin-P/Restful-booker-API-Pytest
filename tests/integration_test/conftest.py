from pytest import fixture


@fixture(scope='session')
def namespace():
    return {'auth_token': None,
            'booking_id': None}
