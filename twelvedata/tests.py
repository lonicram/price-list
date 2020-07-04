import json
from unittest import TestCase
from unittest.mock import patch

from twelvedata.api import Api, BASE_URL


class MockResponse:
    pass


class ApiTestCase(TestCase):
    """Sample Api Test Case"""
    def setUp(self) -> None:
        self.test_api_key = 'test_api_key'

    def test_api_initialization(self):
        api_key = self.test_api_key
        api = Api(api_key)

    @patch('requests.get')
    def test_getting_data(self, get_mock):
        api = Api(api_key=self.test_api_key)
        expected_body = '{}'
        expected_body_data = {}
        mock_response = MockResponse()
        mock_response.status_code = 200
        mock_response.body = '{}'

        def mock_json():
            return json.loads(mock_response.body)
        mock_response.json = mock_json

        get_mock.return_value = mock_response

        response = api.get('time_series', 'AAPL')
        get_mock.assert_called_with(
            f"{BASE_URL}/time_series",
            params={'symbol': 'AAPL'},
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.body, expected_body)
        self.assertEqual(response.json(), expected_body_data)
