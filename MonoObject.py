import json


class MonoObject:

    def bind(self, data: dict, skip_fields=[]):

        for key, val in data.items():
            if key in skip_fields:
                continue
            if hasattr(self, key) is False:
                continue

            setattr(self, key, val)

    def to_dict(self) -> dict:

        return self.__dict__

    def to_json(self):
        data = self.to_dict()

        json_data = json.dumps(data)

        return json_data

    def to_json_pretty(self):
        data = self.to_dict()

        json_data = json.dumps(data, default=lambda o: o.__dict__, sort_keys=False, indent=4)

        return json_data

    def __str__(self):
        return str(self.to_dict())
