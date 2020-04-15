import unittest
from unittest.mock import patch

import requests

from market_csgo_adapter import MarketCSGOAdapter
from exceptions import ApiCallError


class MarketCSGOAdapterTestCase(unittest.TestCase):

    def setUp(self):
        requests_get_patcher = patch(
            "market_csgo_adapter.requests.get"
        )
        self.requests_get_mock = requests_get_patcher.start()
        self.addCleanup(requests_get_patcher.stop)
        self.adapter = MarketCSGOAdapter("1234")

    def test_raises_error(self):
        self.requests_get_mock.return_value.status_code = 500

        with self.assertRaises(ApiCallError):
            self.adapter._api_call("")

    def test_raises_request_error(self):
        self.requests_get_mock.side_effect = requests.RequestException

        with self.assertRaises(ApiCallError):
            self.adapter._api_call("")

    def test_call_ok(self):
        test_dict = {"key": "value"}
        self.requests_get_mock.return_value.status_code = 200
        self.requests_get_mock.return_value.json.return_value = test_dict

        result = self.adapter._api_call("")

        self.assertEqual(test_dict, result)














