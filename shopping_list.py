def shopping_list(budget, **kwargs):
    dictionary = {}
    basket = {}
    for key, value in kwargs.items():
        dictionary[key] = value[0] * value[1]
    if budget >= 100:
        for key, value in dictionary.items():
            if len(basket) != 5:
                if value <= budget:
                    basket[key] = value
                    budget -= value
        result =[]
        for key, value in basket.items():
            result.append(f"You bought {key} for {value:.2f} leva.")
        return "\n".join(result)
    else:
        return "You do not have enough budget."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))



