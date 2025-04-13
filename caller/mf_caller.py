from http import HTTPStatus

from fastapi import Depends
from httpx import AsyncClient
from config_loader import ConfigLoader
from exception.generic_exception import GenericException
from http_client_configuration.http_client_mf import MfHttpClientConfig

class MfCaller:

    def __init__(self, http_client: AsyncClient=Depends(MfHttpClientConfig.get_httpx_client)):
        self.http_client = http_client

    async def get_active_plan(self, product_code, include_hierarchy, internal_identifier):
        config = ConfigLoader.get_config()
        url = config['esewaUrl']['esewaMF'] + '/api/mf/subscription/package'
        params = {
            "productCode": product_code,
            "includeHierarchy": str(include_hierarchy).lower(),
            "internalIdentifier": internal_identifier,
        }
        response = await self.http_client.get(url, params=params)
        if response.status_code != 200:
            raise GenericException(HTTPStatus.SERVICE_UNAVAILABLE, response.text, "Service is currently not available")
        # response.raise_for_status()
        return response.json()