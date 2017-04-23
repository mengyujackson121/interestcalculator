from collections import defaultdict


class Stock:
    def __init__(self, name, expected_monthly_growth, current_month, starting_value):
        self.name = name
        self.expected_monthly_growth = expected_monthly_growth

        self.current_month = current_month
        self.value = {current_month: starting_value}

        self.purchase_history = defaultdict(int)
        self.selling_history = defaultdict(int)

    def get_total_money_spent(self):
        total_amount_bought = 0
        for month, amount in self.purchase_history:
            total_amount_bought += amount * self.value[month]
        return total_amount_bought

    def get_total_money_made(self):
        total_amount_sold = 0
        for month, amount in self.selling_history:
            total_amount_sold += amount * self.value[month]
        return total_amount_sold

    def get_current_shares(self):
        shares = 0
        for month, amount in self.purchase_history:
            shares += amount

        for month, amount in self.selling_history:
            shares -= amount

        return shares

    def put_money_in(self, money_to_put_in):
        amount_can_buy = money_to_put_in / self.value[self.current_month]
        self.purchase_history[self.current_month] += amount_can_buy

    def get_money_out(self, money_to_get_out):
        amount_must_get_out = money_to_get_out / self.value[self.current_month]
        self.selling_history[self.current_month] += amount_must_get_out

    def go_to_next_month(self):
        self.value[self.current_month + 1] = self.value[self.current_month] * self.expected_monthly_growth
        self.current_month += 1

    def __str__(self):
        return "Stock ($%f Bought, $%f Sold, %d Current Shares, %d Current Value)" % (
        self.get_total_money_spent(), self.get_total_money_made(), self.get_current_shares(),
        self.get_current_shares() * self.value[self.current_month])
