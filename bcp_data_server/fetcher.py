import requests
from .config import Server, DataFetcherConfig


class DataFetcherMain:
    class Decorators:
        @staticmethod
        def format_endpoint(function):
            def function_to_execute(cls, endpoint=None, *args, **kwargs):
                formatted_endpoint = '/'.join(
                    (Server.base_url.strip("/"),
                     cls._endpoint.strip("/"))) + "/" if not endpoint else endpoint
                return function(cls, formatted_endpoint, *args, **kwargs)

            function_to_execute.__name__ = function.__name__
            return function_to_execute

    class Helpers:
        @staticmethod
        def call_api(endpoint, params: dict = {}):
            response = requests.get(endpoint, params=params, headers=Server.Auth.request_header())
            response.raise_for_status()
            obj = response.json()
            return obj

    @classmethod
    @Decorators.format_endpoint
    def detail(cls, endpoint, identifier, params: dict = {}):
        endpoint += f"{identifier}/"
        return cls.Helpers.call_api(endpoint, params=params)

    @classmethod
    @Decorators.format_endpoint
    def _list(cls, endpoint, params: dict = {}, single=False, count=None):
        if single:
            params['limit'] = 1
        elif count and count < DataFetcherConfig.list_size:
            params['limit'] = count
        else:
            params['limit'] = DataFetcherConfig.list_size
        data = cls.Helpers.call_api(endpoint, params=params)
        if single:
            if data.get("results"):
                yield data["results"][0]
            return
        if data.get("results"):
            if data.get("next"):
                _count = 0
                for item in data['results']:
                    _count += 1
                    yield item
                if count and _count >= count:
                    return
                for item in cls.list(data["next"], params={}, single=False, count=count and (count - _count)):
                    yield item
            else:
                for item in data['results']:
                    yield item
        return []

    @classmethod
    def list(cls, endpoint=None, *args, **kwargs):
        response = cls._list(endpoint, *args, **kwargs)
        if kwargs.get("single"):
            response = list(response)
            return response and response[0]
        return response
