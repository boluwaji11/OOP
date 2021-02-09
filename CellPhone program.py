import CellPhoneClass as cp


def main():

    manufacturer = input("Enter the phone's manufacturer: ")
    model = input("Enter the model: ")
    price = float(input("Enter the retail price: "))

    cell = cp.Cellphone(manufacturer, model, price)

    cell.set_manufact(manufacturer)
    cell.set_model(model)
    cell.set_retail_price(price)

    print()
    print("The Manufacturer is", cell.get_manufact())
    print("The Model is", cell.get_model())
    print("The Retail Price is", cell.get_retail_price())


main()
