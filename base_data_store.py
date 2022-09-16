from base_crud import BaseCrud


class BaseDataStore(BaseCrud):
    def __init__(self, data_store_credits=None):
        self._data_store_credits = data_store_credits

    def _connect(self) -> bool:
        pass

    def _close(self) -> bool:
        pass
