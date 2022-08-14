from unittest import mock, TestCase
from src import util


class TestApp(TestCase):
    @mock.patch("src.util.get_url_200_info", return_value=(600, 1))
    def test_url_200_query_success(self, mock_resp):
        resp_time, status = util.get_url_200_info()
        expected_resp_time, expected_status = 600, 1
        self.assertEqual(resp_time, expected_resp_time)
        self.assertEqual(status, expected_status)

    @mock.patch("src.util.get_url_503_info", return_value=(650, 0))
    def test_url_503_query_success(self, mock_resp):
        resp_time, status = util.get_url_503_info()
        expected_resp_time_max_limit, expected_status = 999, 0
        self.assertLess(resp_time, expected_resp_time_max_limit)
        self.assertEqual(status, expected_status)
