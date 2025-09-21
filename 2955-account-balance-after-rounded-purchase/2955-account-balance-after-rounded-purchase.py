class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        return 100 - (purchaseAmount + 5) // 10 * 10