class Server:
    base_url: str = None
    secret_key: str = None

    class Auth:
        @classmethod
        def request_header(cls):
            return {
                "secret-key": Server.secret_key
            }

    @classmethod
    def setup(cls, base_url: str = None, secret_key: str = None):
        cls.base_url = base_url
        cls.secret_key = secret_key


class DataFetcherConfig:
    list_size = 10

    @classmethod
    def setup(cls, list_size: int = None):
        cls.list_size = list_size
