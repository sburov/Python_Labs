class Radiator:
    radiators_class = 'Heating'

    def __init__(self, thremal_power, color, manufacturer, wheelbase):
        self.thremal_power = thremal_power
        self.color = color
        self.manufacturer = manufacturer
        self.wheelbase = wheelbase 

    def __del__(self): 
        return 

    def __str__(self):
        return "\tthremal_power: {}\n \tcolor: {}\n \tmanufacturer: {}\n \twheelbase: {}".format(self.thremal_power, self.color, self.manufacturer, self.wheelbase)

    @staticmethod
    def RadiatorsClass():
        return Radiator.radiators_class


if __name__ == "__main__":
    radiator1 = Radiator("158 Watt", "White", "China", "80 Millimeters")
    print("The first radiator:\n", radiator1.__str__()) 

    radiator2 = Radiator("186 Watt", "Brown", "USA", "96 Millimeters")
    print("The second radiator:\n", radiator2.__str__())   

    radiator3 = Radiator("198 Watt", "Silver", "Canada", "80 Millimeters")
    print("The third radiator:\n", radiator3.__str__()) 

    print("Class of radiators: ", radiator1.RadiatorsClass())

