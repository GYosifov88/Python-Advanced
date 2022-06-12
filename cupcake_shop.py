from collections import deque


def stock_availability(list, command, *args):
    invertory = list
    action = command
    items = []
    if action == 'delivery':
        for item in args:
            invertory.append(item)
    elif action == 'sell':
        for thing in args:
            items.append(str(thing))

        if len(items) <= 0:
            invertory.pop(0)
        else:
            for el in items:
                if el.isdigit():
                    num = int(el)
                    invertory = invertory[num:]
                else:
                    for el in items:
                        if el in invertory:
                            invertory = [x for x in invertory if x != el]

    return invertory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



