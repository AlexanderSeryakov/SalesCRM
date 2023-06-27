def get_total(retail_price, quantity, discount):
    """ Calculate total profit for sale with discount """
    if discount == '0':
        return retail_price * quantity
    if '%' in discount:
        discount = int(discount.replace('%', '')) / 100
        return retail_price * quantity * (1 - discount)

    return retail_price * quantity - float(discount)


def get_total_cleaned(retail_price, quantity, discount, purchase_price):
    """ Calculate total cleaned profit for sale.
        Cleaned profit = total profit - total purchase price - tax.
        In this case tax = 6%.
     """
    total = get_total(retail_price, quantity, discount)
    return total * 0.94 - purchase_price * quantity

