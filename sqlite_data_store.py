import sqlite3

from base_data_store import BaseDataStore


class SqliteDataStore(BaseDataStore):
    def __init__(self, data_store_credits=None):
        super().__init__(data_store_credits)
        self.__conn = None

    @property
    def conn(self):
        return self.__conn

    def _connect(self) -> bool:
        if self.__conn:
            return False
        try:
            self.__conn = sqlite3.connect(self._data_store_credits['path'])
            return True
        except Exception:
            return False

    def _close(self) -> bool:
        if self.conn:
            self.__conn.close()
            self.__conn = None
            return True
        return False

    def __get_max_element_id(self):
        elements = self.get_items()
        return max([element["id"] for element in elements]) if elements else 0

    def add_item(self, item: dict):
        new_item = self.__dict_to_tuple(item)
        if self._connect():
            cur = self.conn.cursor()
            print(new_item)
            execute_str = "INSERT INTO automobiles VALUES(?, ?, ?, ?, ?, ?);"
            cur.execute(execute_str, new_item)
            self.conn.commit()
            self._close()

    @staticmethod
    def __tuple_to_dict(value):
        if len(value) == 6:
            new_item = {
                "id": value[0],
                "brand": value[1],
                "number": value[2],
                "color": value[3],
                "year_of_manufacture": value[4],
                "vehicle": value[5],
            }
            return new_item
        return None

    def __dict_to_tuple(self, item):
        new_item = (
            self.__get_max_element_id() + 1,
            item["brand"],
            item["number"],
            item["color"],
            item["year_of_manufacture"],
            item["vehicle"],
        )
        return new_item

    def update_item(self, item: dict):
        list_item = list(self.__dict_to_tuple(item))[1:]
        list_item.append(item['id'])
        if self._connect():
            cur = self.conn.cursor()
            execute_str = "UPDATE automobiles SET brand=?, number=?, color=?, year_of_manufacture=?, vehicle=? WHERE id=?;"
            cur.execute(execute_str, tuple(list_item))
            self.conn.commit()
            self._close()

    def remove_item(self, item: dict):
        if self._connect():
            cur = self.conn.cursor()
            execute_str = "DELETE FROM automobiles WHERE id=?"
            cur.execute(execute_str, (item['id'],))
            self.conn.commit()
            self._close()

    def get_items(self) -> tuple:
        if self._connect():
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM automobiles;")
            all_results = cur.fetchall()
            for i in range(len(all_results)):
                all_results[i] = self.__tuple_to_dict(all_results[i])
            self._close()
            return tuple(all_results)

    def get_item(self, id_: int) -> dict:
        if self._connect():
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM automobiles WHERE id=?;", (id_,))
            all_results = cur.fetchall()
            self._close()
            if len(all_results) == 1:
                return self.__tuple_to_dict(all_results[0])
