from httpx import Timeout, Limits, AsyncClient

class MfHttpClientConfig:
    _client = None

    @staticmethod
    async def get_httpx_client() -> AsyncClient:
        if MfHttpClientConfig._client is None:
            timeout = Timeout(connect=30.0, read=30.0, write=30.0, pool=30.0)
            limits = Limits(max_connections=100, max_keepalive_connections=25)
            MfHttpClientConfig._client = AsyncClient(timeout=timeout, limits=limits)
        return MfHttpClientConfig._client
