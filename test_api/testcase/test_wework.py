from test_api.api.wework import WeWork


class TestWeWork:
    def test_get_work(self):
        secret='GUKKxigux3vmCdYeiV9hQiSYoDRguvcD4nNX9rsbpbk'
        print(WeWork().get_token(secret))




