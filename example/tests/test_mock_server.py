# Third-party imports...
from mock import patch
from nose.tools import assert_dict_contains_subset, assert_list_equal, assert_true

# Local imports...
from example.services import get_users
from example.tests.mocks import get_free_port, start_mock_server


class TestMockServer(object):
    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_request_response(self):
        mock_users_url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('example.services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        assert_dict_contains_subset({'Content-Type': 'application/json; charset=utf-8'}, response.headers)
        assert_true(response.ok)
        assert_list_equal(response.json(), [])
