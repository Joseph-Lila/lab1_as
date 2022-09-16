class Automobile:
    def __init__(self, id_, brand, number, color, year_of_manufacture, vehicle):
        self.id = id_
        self.brand = brand
        self.number = number
        self.color = color
        self.year_of_manufacture = year_of_manufacture
        self.vehicle = vehicle

    def __str__(self):
        return f"<+++=< {self.brand} - {self.number} >=+++>"
