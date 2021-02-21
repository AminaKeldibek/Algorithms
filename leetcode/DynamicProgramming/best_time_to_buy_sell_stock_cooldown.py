import math

class LongSolution:
    def find_max_profit(self, profit, day, last_action, prices):
        if last_action in ('cooldown', 'sell'):
            if day == len(prices) - 1:
                return profit
            cooldown_profit = self.find_max_profit(profit, day + 1, 'cooldown', prices)

        if last_action == 'sell':
            return cooldown_profit

        if last_action == 'cooldown':
            return max(cooldown_profit, self.find_max_profit(profit - prices[day], day + 1, 'buy', prices))

        if last_action in ('buy', 'skip'):
            if day == len(prices) - 1:
                return profit + prices[day]
            return max(
              self.find_max_profit(profit, day + 1, 'skip', prices),
              self.find_max_profit(profit + prices[day], day + 1, 'sell', prices)
            )


    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        return self.find_max_profit(0, 0, 'cooldown', prices)
