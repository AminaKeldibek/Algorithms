class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def find_min_cost(price, special, needs):
            min_price = sum([p * n for p, n  in zip(price, needs)])
            for promo in special:
                if not any(n1 > n2 for n1, n2 in zip(promo[:len(promo) - 1], needs)):
                    price_with_promo = promo[len(promo) - 1]
                    price_with_promo += find_min_cost(
                        price,
                        special,
                        [n - p for p, n  in zip(promo[:len(promo) - 1], needs)]
                    )
                    min_price = min(min_price, price_with_promo)

            return min_price

        return find_min_cost(price, special, needs)
