from automobile import Automobile


class BaseCrud:
    def add_item(self, item: dict):
        pass

    def update_item(self, item: dict):
        pass

    def remove_item(self, item: dict):
        pass

    def get_item(self, id_: int) -> dict:
        pass

    def get_items(self) -> tuple:
        pass
