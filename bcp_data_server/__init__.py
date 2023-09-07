from .config import Server


class Base:
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
