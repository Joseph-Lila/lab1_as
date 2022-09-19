import json
from typing import Union

from base_data_store import BaseDataStore


class JsonDataStore(BaseDataStore):
    def __init__(self, data_store_credits=None):
        super().__init__(data_store_credits)
        self.__connected = False
        self.__file = None

    def _connect(self) -> bool:
        if self.__connected:
            return False
        try:
            self.__file = open(self._data_store_credits['path'], mode="r+")
            self.__connected = True
            return True
        except Exception:
            return False

    def __get_data_dict(self) -> Union[dict, None]:
        if self._connect():
            data = json.load(self.__file)
            self._close()
            return data
        return None

    def __put_data_dict(self, data_dict):
        if self._connect():
            json.dump(data_dict, self.__file, indent=4)
            self._close()

    def _close(self) -> bool:
        if self.__connected:
            self.__file.close()
            self.__connected = False
            return True
        return False

    def add_item(self, item: dict):
        data_dict = self.__get_data_dict()
        if data_dict is not None:
            item["id"] = self.__get_max_element_id() + 1
            data_dict["elements"].append(item)
            self.__put_data_dict(data_dict)

    def __get_max_element_id(self):
        elements = self.get_items()
        return max([element["id"] for element in elements]) if elements else 0

    def update_item(self, item: dict):
        data_dict = self.__get_data_dict()
        if data_dict is not None:
            for element in data_dict["elements"]:
                if element["id"] == item["id"]:
                    element["number"] = item["number"]
                    element["brand"] = item["brand"]
                    element["color"] = item["color"]
                    element["year_of_manufacture"] = item["year_of_manufacture"]
                    element["vehicle"] = item["vehicle"]
            self.__put_data_dict(data_dict)

    def remove_item(self, item: dict):
        data_dict = self.__get_data_dict()
        if data_dict is not None:
            elements: list = data_dict["elements"]
            cnt = 0
            for i in range(len(elements)):
                if elements[i]['id'] == item['id']:
                    break
                else:
                    cnt += 1
            if cnt == len(elements):
                return
            else:
                data_dict['elements'].pop(cnt)
            self.__clear_file()
            self.__put_data_dict(data_dict)

    def get_item(self, id_: int) -> dict:
        data_dict = self.__get_data_dict()
        if data_dict is not None:
            for element in data_dict["elements"]:
                if element["id"] == id_:
                    return element

    def get_items(self) -> tuple:
        data_dict = self.__get_data_dict()
        if data_dict is not None:
            return tuple(data_dict["elements"])

    def __clear_file(self):
        f = open(self._data_store_credits['path'], mode='w')
        f.close()
