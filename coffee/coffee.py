class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 3 <= len(value) <= 15:
            raise ValueError("Name must be between 3 and 15 characters")
        self._name = value

    def customers(self):
        from order import Order
        return list(set(order.customer for order in Order._all_orders if order.coffee == self))

    def num_orders(self):
        from order import Order
        return len([order for order in Order._all_orders if order.coffee == self])

    def average_price(self):
        from order import Order
        prices = [order.price for order in Order._all_orders if order.coffee == self]
        return sum(prices) / len(prices) if prices else 0
