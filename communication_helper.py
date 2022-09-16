import json


class CommunicationHelper:
    @staticmethod
    def append_data_to_command(command: str):
        f = open("data.json")
        data = json.load(f)
        f.close()
        data = json.dumps(data)
        return f"{command} {data}"

    @staticmethod
    def get_data_dict(data):
        return json.loads(data)

    @staticmethod
    def get_str_from_dict(data_dict):
        return json.dumps(data_dict)
