from store import Store
from fruit_tea import FruitTea
from topping import Topping

def main():
    store = Store()

    teas = [
        FruitTea("Mango Bubble Tea", "Medium", "Normal", "Less", "Fruity", "Mango"),
        FruitTea("Lychee Bubble Tea", "Large", "More", "Normal", "Fruity", "Lychee"),
        FruitTea("Apple Bubble Tea", "Small", "Less", "More", "Fruity", "Apple"),
        FruitTea("Grape Bubble Tea", "Medium", "Normal", "Less", "Fruity", "Grape"),
        FruitTea("Melon Bubble Tea", "Large", "More", "Normal", "Fruity", "Melon"),
        FruitTea("Grapefruit Bubble Tea", "Small", "Less", "More", "Fruity", "Grapefruit"),
        FruitTea("Lemon Bubble Tea", "Medium", "Normal", "Less", "Fruity", "Lemon"),
        FruitTea("Guava Bubble Tea", "Large", "More", "Normal", "Fruity", "Guava"),
        FruitTea("Passionfruit Bubble Tea", "Small", "Less", "More", "Fruity", "Passionfruit"),
        FruitTea("Strawberry Bubble Tea", "Medium", "Normal", "Less", "Fruity", "Strawberry")
    ]

    for tea in teas:
        topping = Topping("Pearls", 1.2)
        tea.add_topping(topping)
        store.order_tea(tea)

    store.display_order_history()

if __name__ == "__main__":
    main()
