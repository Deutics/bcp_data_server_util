from json import JSONDecodeError

import requests
from .config import Server
from . import Base


class DataWriterMain:
    class Definition:
        class Method:
            POST = "post"
            PATCH = "patch"

    class Caller:
        __slots__ = ['endpoint', 'payload', 'params', 'method']

        class Helpers:
            @staticmethod
            def call_api(endpoint, payload, method, params=None):
                response = getattr(requests, method)(endpoint, data=payload, params=params,
                                                     headers=Server.Auth.request_header())
                response.raise_for_status()
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text

        def __init__(self, endpoint, payload, method, params: dict = {}):
            self.endpoint = endpoint
            self.payload = payload
            self.params = params
            self.method = method

        def execute(self):
            return self.Helpers.call_api(self.endpoint, method=self.method, payload=self.payload, params=self.params)

        def detail(self, identifier):
            self.endpoint += f"{identifier}/"
            return self

    @classmethod
    @Base.Decorators.format_endpoint
    def create(cls, endpoint, payload, params: dict = {}) -> Caller:
        return cls.Caller(endpoint=endpoint,
                          payload=payload,
                          method=cls.Definition.Method.POST,
                          params=params
                          )

    @classmethod
    @Base.Decorators.format_endpoint
    def update(cls, endpoint, payload, params: dict = {}) -> Caller:
        return cls.Caller(endpoint=endpoint,
                          payload=payload,
                          method=cls.Definition.Method.PATCH,
                          params=params
                          )
