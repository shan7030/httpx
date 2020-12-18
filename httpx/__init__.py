from .__version__ import __description__, __title__, __version__
from ._api import delete, get, head, options, patch, post, put, request, stream
from ._auth import Auth, BasicAuth, DigestAuth
from ._client import AsyncClient, Client
from ._config import Limits, Proxy, Timeout, create_ssl_context
from ._exceptions import (
    CloseError,
    ConnectError,
    ConnectTimeout,
    CookieConflict,
    DecodingError,
    HTTPError,
    HTTPStatusError,
    InvalidURL,
    LocalProtocolError,
    NetworkError,
    PoolTimeout,
    ProtocolError,
    ProxyError,
    ReadError,
    ReadTimeout,
    RemoteProtocolError,
    RequestError,
    RequestNotRead,
    ResponseClosed,
    ResponseNotRead,
    StreamConsumed,
    StreamError,
    TimeoutException,
    TooManyRedirects,
    TransportError,
    UnsupportedProtocol,
    WriteError,
    WriteTimeout,
)
from ._models import URL, Cookies, Headers, QueryParams, Request, Response
from ._status_codes import StatusCode, codes
from ._transports.asgi import ASGITransport
from ._transports.default import (
    create_default_transport,
    create_default_async_transport,
)
from ._transports.wsgi import WSGITransport

__all__ = [
    "__description__",
    "__title__",
    "__version__",
    "ASGITransport",
    "AsyncClient",
    "Auth",
    "BasicAuth",
    "Client",
    "CloseError",
    "codes",
    "ConnectError",
    "ConnectTimeout",
    "CookieConflict",
    "Cookies",
    "create_ssl_context",
    "create_default_transport",
    "create_default_async_transport",
    "DecodingError",
    "delete",
    "DigestAuth",
    "get",
    "head",
    "Headers",
    "HTTPError",
    "HTTPStatusError",
    "InvalidURL",
    "Limits",
    "LocalProtocolError",
    "NetworkError",
    "options",
    "patch",
    "PoolTimeout",
    "post",
    "ProtocolError",
    "Proxy",
    "ProxyError",
    "put",
    "QueryParams",
    "ReadError",
    "ReadTimeout",
    "RemoteProtocolError",
    "request",
    "Request",
    "RequestError",
    "RequestNotRead",
    "Response",
    "ResponseClosed",
    "ResponseNotRead",
    "StatusCode",
    "stream",
    "StreamConsumed",
    "StreamError",
    "Timeout",
    "TimeoutException",
    "TooManyRedirects",
    "TransportError",
    "UnsupportedProtocol",
    "URL",
    "WriteError",
    "WriteTimeout",
    "WSGITransport",
]


__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        setattr(__locals[__name], "__module__", "httpx")  # noqa
