from base_crud import BaseCrud


class Autoinspection(BaseCrud):
    def __init__(self, data_sources_credits=None, data_sources_classes=None):
        self.__data_sources_credits = data_sources_credits
        self.__data_sources_classes = data_sources_classes
        self.__data_sources = self.__initialize_data_sources()

    def __initialize_data_sources(self) -> list:
        data_sources = []
        for i in range(len(self.__data_sources_credits)):
            data_sources.append(
                self.__data_sources_classes[i](self.__data_sources_credits[i]))
        return data_sources

    def __create_sources(self):
        for data_source in self.__data_sources:
            data_source.create_source()

    def add_item(self, item: dict):
        for data_source in self.__data_sources:
            data_source.add_item(item)

    def update_item(self, item: dict):
        for data_source in self.__data_sources:
            data_source.update_item(item)

    def remove_item(self, item: dict):
        for data_source in self.__data_sources:
            data_source.remove_item(item)

    def get_item(self, id_: int) -> dict:
        answers = []
        for data_source in self.__data_sources:
            answers.append(data_source.get_item(id_))
        return answers[0] if self.__check_dicts_are_equal(answers) else None

    def get_items(self) -> tuple:
        answers = []
        for data_source in self.__data_sources:
            answers.append(data_source.get_items())
        return answers[0] if self.__check_dicts_collections_are_equal(answers) else None

    @staticmethod
    def __check_equal_results(answers):
        for i in range(len(answers)):
            for j in range(i + 1, len(answers)):
                if answers[i] != answers[j]:
                    return False
        return True

    @staticmethod
    def __check_dicts_collections_are_equal(answers):
        if not answers or not len(answers):
            return False
        dict_collection_length = len(answers[0])
        for i in range(len(answers)):
            for j in range(len(answers)):
                for k in range(dict_collection_length):
                    if not Autoinspection.__check_dicts_are_equal([answers[i][k], answers[j][k]]):
                        return False
        return True

    @staticmethod
    def __check_dicts_are_equal(answers):
        for dict_item_ind in range(len(answers)):
            for another_item_ind in range(dict_item_ind + 1, len(answers)):
                for key in answers[dict_item_ind].keys():
                    if type(answers[dict_item_ind][key]) == float or type(answers[dict_item_ind][key]) == int:
                        if float(answers[dict_item_ind][key]) != float(answers[another_item_ind][key]):
                            return False
                    else:
                        if answers[dict_item_ind][key] != answers[another_item_ind][key]:
                            return False
        return True
