from abc import ABCMeta, abstractmethod

from fastapi_pagination import Params
from fastapi_pagination.ext.tortoise import paginate

from ._base import BaseService


class PaginationService(BaseService, metaclass=ABCMeta):
    def __init__(self, params: Params):
        self._params = params

    @abstractmethod
    def _get_query(self): ...

    async def do(self):
        query = self._get_query()
        return await paginate(query, self._params)
