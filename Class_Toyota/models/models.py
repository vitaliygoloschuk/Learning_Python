import json


class Toyota:
    file = "cars.json"

    def __init__(self, car, shift_gear, change_color):
        self.car = car
        self.shift_gear = shift_gear
        self.change_color = change_color

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_cars(cls):
        data = cls.get_data()
        for auto in data:
            print(auto["car_model"])
            print(auto["amount_gear"])
            print(auto["color"])
            print()

    @classmethod
    def get_by_id(cls, id):
        autos = cls.get_data()
        counter = 0
        for auto in autos:
            if id == auto["id"]:
                print(auto["car_model"])
                print(auto["amount_gear"])
                print(auto["color"])
                print()
                break
            counter += 1
            if counter == len(autos):
                print("Not found with this id\n")

    def save(self):
        data = self.get_data()
        new_car = {"car_model": self.car, "amount_gear": self.shift_gear, "color": self.change_color}
        if len(data) > 0:
            new_car["id"] = data[-1]["id"] + 1
        else:
            new_car["id"] = 1
        data.append(new_car)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def update_by_id(cls, id):
        autos = cls.get_data()
        counter = 0
        for auto in autos:
            if id == auto["id"]:
                new_gir = input("Please set new value for gear:\n ")
                new_color = input("Please set new value for color:\n ")
                auto["amount_gear"] = new_gir
                auto["color"] = new_color
                print()
                print(auto["car_model"])
                print(auto["amount_gear"])
                print(auto["color"])
                print()
                break
            counter += 1
            if counter == len(autos):
                print("Not found with this id\n")
            file = open("database/" + cls.file, "w")
            data_in_json = json.dumps(autos)
            file.write(data_in_json)