class items:
    def __init__(self, item_name, item_type, item_price):
        self.name = item_name
        self.type = item_type
        self.price = item_price


shopping_cart = []
shopping_cart.append(items('dior', "clothing", 2000))
shopping_cart.append(items('avocdao', "wic", 2))
shopping_cart.append(items('bmw', "other", 40000))


# //sales taxes
# https://worldpopulationreview.com/state-rankings/alcohol-tax-by-state
# https://www.avalara.com/blog/en/north-america/2020/02/how-to-handle-sales-tax-on-clothing-a--state-by-state-guide.html

def cashout_cart(state, items):
    sum = 0
    sumAfterTaxes = 0
    for x in items:
        if state == "MA":
            if x.type == "clothing":
                if x.price > 175:
                    y = (x.price * 0.0625) + x.price
                else:
                    y = x.price
            elif x.type == "wic":
                y = x.price
            else:
                y = (x.price * 0.0625) + x.price
        elif state == "NH":
            y = x.price
        elif state == "ME":
            if x.type == "clothing":
                y = (x.price * 0.055) + x.price
            elif x.type == "wic":
                y = x.price
            else:
                print("This state does not matter, pick a state that does matter")
                exit()
            sum = y
            sumAfterTaxes = sumAfterTaxes + sum
    print(sumAfterTaxes)
    return sumAfterTaxes
