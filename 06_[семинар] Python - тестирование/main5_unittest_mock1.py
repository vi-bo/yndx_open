import unittest

from unittest.mock import Mock
class AliveChecker:
    def __init__(self, http_session, target):
        self.http_session = http_session
        self.target = target
    
    def do_check(self):
        try:
            resp = self.http_session.get(
                f'https://{self.target}/ping')
        except Exception:
            return False
        else:
            return resp == 200

def test_with_raising_mock():
    get_mock = Mock(side_effect=Exception('EEEEE'))
    pseudo_client = Mock()
    pseudo_client.get = get_mock
    alive_checker = AliveChecker(pseudo_client, 'test.com')
    assert not alive_checker.do_check()
    pseudo_client.get.assert_called_once_with('https://test.com/ping')