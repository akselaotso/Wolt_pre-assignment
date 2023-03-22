from math import ceil 

class cost_calculator:
    feePer500m = 100
    feePerItemOverFour = 50
    bulkCharge = 120

    def __init__(self, value, distance, items, time) -> None:
        self.value = value
        self.distance = distance
        self.items = items
        self.time = time

    def __surcharge(self) -> int:
        if self.value < 1000:
            return 1000 - self.value
        return 0

    def __item_charge(self) -> int:
        if self.items < 5:
            return 0
        
        charge = (self.items - 4) * self.feePerItemOverFour

        if self.items < 13:
            return charge

        return charge + self.bulkCharge

    def __distance_charge(self) -> int: 
        if self.distance < 1000:
            return 200
        
        distanceBill = ceil(self.distance / 500.0) * self.feePer500m

        return distanceBill

    def __is_rush_hour(self) -> bool:
        #2021-10-12T13:00:00Z

        if self.time[10] == "F" and 15 <= int(self.time[11:13]) <= 19:
            return True

        return False

    def final_price(self) -> int:
        if self.value > 9999:
            return 0
        
        price = self.__item_charge() + self.__distance_charge() + self.__surcharge()

        if self.__is_rush_hour():
            price = int(price * 1.2)
        
        if price > 1500:
            return 1500
        
        return price

