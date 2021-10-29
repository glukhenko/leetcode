BIG = 1
MEDIUM = 2
SMALL = 3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {BIG: big, MEDIUM: medium, SMALL: small}

    def addCar(self, carType: int) -> bool:
        slot_exist = bool(self.slots.get(carType))
        if slot_exist:
            self.slots[carType] -= 1
        return slot_exist

if __name__ == '__main__':

    parking_slots = [1, 1, 0]
    parking = ParkingSystem(*parking_slots)
    result = [None]
    cars = (1, 2, 3, 1)
    for car in cars:
        result.append(parking.addCar(car))
    print(f'result: {result}')
    expected = [None, True, True, False, False]