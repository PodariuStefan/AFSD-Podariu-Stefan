import random
import json

def random_product(arr):
    chosen_product = random.choice(arr)
    return chosen_product

def state(new_cash_state, customer_id):
    total_cash = 0
    if customer_id == 0:
        with open("availableProducts.json", 'r+') as products, open("availableCash.json", "r+") as cash:
            # we take both json files and make dictionaries
            initial_products = json.load(products)
            initial_cash_amount = json.load(cash)

    else:
        with open("availableProducts.json", 'r+') as products, open(new_cash_state, "r+") as cash:
            # we take both json files and make dictionaries
            initial_products = json.load(products)
            initial_cash_amount = json.load(cash)
            #takes a dictionary and chooses a random product from the available products

    all_products = []
    value_per_product = 0
    total_price = 0

    for product in initial_products['products']:
        all_products.append(product["name"])

    choice = random_product(all_products)

    for product in initial_products['products']:
        if product['name'] == choice:
            value_per_product = product['price']

    for money in initial_cash_amount["cash"]:
        total_cash += money["value"] * money["amount"]

    variation = round(random.uniform(1, 20), 2)

    while True:
        quantity = random.choice(range(1, 13))
        if total_cash < (value_per_product * quantity) + variation:
            continue
        else:
            total_price = round((value_per_product * quantity) + variation, 2)
            break

    iteration_price = round(total_price - variation, 2)

    print(f"Client number {customer_id} buys {choice} for {iteration_price} RON ({quantity} pieces), but pays {variation} RON extra that need to be given back to the customer.")

    valid_values = []

    for coin in initial_cash_amount["cash"]:
        if coin["value"] <= variation and coin["amount"] > 0:
            valid_values.append(coin["value"])

    # print(f"All valid values: {valid_values}")

    change = 0.0

    for i in range(len(valid_values) - 1, -1, -1):
        # print(f"valid_values[{i}] = {valid_values[i]}")
        while True:
            if round(change + valid_values[i], 2) <= variation:
                change += valid_values[i]
                # print(round(change, 2))
                for money in initial_cash_amount["cash"]:
                    if money["value"] == valid_values[i] and money["amount"] > 0:
                        money["amount"] -= 1
                        # print(money["amount"])
            else:
                break

        # print(round(change, 2))

    if round(change, 2) != variation:
        print(f"The cash register has {round(change, 2)} RON, it cannot pay the change because it is {round(variation - change, 2)} short.")
        return 0
    else:
        print(f"The change of {round(change, 2)} RON has been paid successfully.")

    print(initial_cash_amount)
    products.close()
    cash.close()

    new_cash_amount = initial_cash_amount

    with open("state.json", 'w') as current_state:
        json.dump(new_cash_amount, current_state, indent= 2)

        return new_cash_amount

def main():
    customer_id = 0

    while state("state.json",customer_id):
        customer_id += 1

    return 0