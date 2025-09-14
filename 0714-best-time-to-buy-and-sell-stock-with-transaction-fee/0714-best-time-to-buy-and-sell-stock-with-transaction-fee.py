class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 初始化两个状态变量：
        # cash: 当前不持有股票的时间的最大利润(只有现金)
        # hold: 当前持有股票是的最大利润
        cash, hold  = 0, -prices[0]
        # cash = 0: 初始的时候没有股票，利润为0
        # hold = -prices[0]: 如果第一天买入股票， 利润为负的股票价格（因为支出了现金， 还没售出，利润为负的现金支出）

        for i in range(1, len(prices)):
            # 保存前一天的cash值，因为后面计算hold 时需要用到更新当前的cash
            prev_cash = cash

            # 更新cash的状态：今天不持有股票的最大利润
            # 有两种选择：
            # 1， 昨天就不持有股票，今天继续不持有股票（什么都不做）：cash
            # 2,  昨天持有， 今天卖出：hold + prices[i] - fee
            # 选择利润最大的方案
            cash = max(cash, hold + prices[i] - fee)

            # 更新hold的状态：今天持有股票的最大利润
            # 有两种选择：
            # 1， 昨天就持有股票，今天继续持有： hold
            # 2,  昨天不持有， 今天买入： prev_case - prices[i]
            # 选择利润最大的方案
            hold = max(hold, cash - prices[i])
        # 最终返回cash, 因为最终状态应该是卖出股票，持有现金
        return cash
        