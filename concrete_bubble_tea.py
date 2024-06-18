from bubble_tea import BubbleTea

class ConcreteBubbleTea(BubbleTea):
    def __init__(self, name, size, ice_level, sugar_level, tea_type):
        super().__init__(name, size, ice_level, sugar_level, tea_type)

    def calculate_price(self):
        price = self.base_price
        for topping in self.toppings:
            price += topping.price
        return price
