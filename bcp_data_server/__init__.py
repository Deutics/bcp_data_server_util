from .config import Server


class Base:
    class Decorators:
        @staticmethod
        def format_endpoint(function):
            def function_to_execute(cls, endpoint=None, *args, **kwargs):
                endpoint = endpoint or cls._endpoint
                formatted_endpoint = '/'.join(
                    (Server.base_url.strip("/"),
                     endpoint.strip("/"))) + "/" if (not endpoint.startswith(Server.base_url)) else endpoint
                return function(cls, formatted_endpoint, *args, **kwargs)

            function_to_execute.__name__ = function.__name__
            return function_to_execute
