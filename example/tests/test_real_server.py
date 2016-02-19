# Third-party imports...
from nose.tools import assert_dict_contains_subset, assert_is_instance, assert_true

# Local imports...
from example.services import get_users


def test_request_response():
    response = get_users()

    assert_dict_contains_subset({'Content-Type': 'application/json; charset=utf-8'}, response.headers)
    assert_true(response.ok)
    assert_is_instance(response.json(), list)
