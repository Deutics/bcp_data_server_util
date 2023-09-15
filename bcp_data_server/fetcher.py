from json import JSONDecodeError

import requests
from dateutil import parser
from pytz import timezone

from . import Base
from .config import Server, DataFetcherConfig


class DataFetcherMain:
    class Helpers:
        @staticmethod
        def call_api(endpoint, params: dict = {}):
            response = requests.get(endpoint, params=params, headers=Server.Auth.request_header())
            response.raise_for_status()
            try:
                return response.json()
            except JSONDecodeError:
                return {}

    @classmethod
    @Base.Decorators.format_endpoint
    def detail(cls, endpoint, identifier=None, params: dict = {}):
        if identifier is None:
            endpoint += f"{identifier}/"
        return cls.Helpers.call_api(endpoint, params=params)

    @classmethod
    @Base.Decorators.format_endpoint
    def _list(cls, endpoint, params: dict = {}, single=False, count=None):
        if single:
            params['limit'] = 1
        elif count and count < DataFetcherConfig.list_size:
            if count == -1:
                params['limit'] = DataFetcherConfig.list_size
            else:
                params['limit'] = count
        else:
            params['limit'] = DataFetcherConfig.list_size
        data = cls.Helpers.call_api(endpoint, params=params)
        if single:
            if data.get("results"):
                cls.clean_dates(data["results"][0])
                yield data["results"][0]
            return
        if data.get("results"):
            if data.get("next"):
                _count = 0
                for item in data['results']:
                    _count += 1
                    cls.clean_dates(item)
                    yield item
                if count and _count >= count:
                    if count != -1:
                        return
                for item in cls.list(data["next"], params={}, single=False,
                                     count=count and ((count - _count) if count != -1 else -1)):
                    yield item
            else:
                for item in data['results']:
                    cls.clean_dates(item)
                    yield item
        return []

    @classmethod
    def list(cls, endpoint=None, *args, **kwargs):
        response = cls._list(endpoint, *args, **kwargs)
        if kwargs.get("single"):
            response = list(response)
            return response and response[0]
        return response

    @classmethod
    def clean_dates(cls, result):
        for _date in cls._dates:
            if result.get(_date):
                result[_date] = timezone('Asia/Karachi').localize(parser.parse(result[_date]))
        return result
