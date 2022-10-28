#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] Stock Price Fluctuation 
#
# https://leetcode.cn/problems/stock-price-fluctuation/description/
#
# algorithms
# Medium (46.11%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 48.9K
# Testcase Example:  '["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]\n' +
#

question_content="""You are given a stream of records about a particular stock. Each record
contains a timestamp and the corresponding price of the stock at that
timestamp.

Unfortunately due to the volatile nature of the stock market, the records do
not come in order. Even worse, some records may be incorrect. Another record
with the same timestamp may appear later in the stream correcting the price
of the previous wrong record.

Design an algorithm that:


Updates the price of the stock at a particular timestamp, correcting the
price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest
price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.


Implement the StockPrice class:


StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the
given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.



Example 1:


Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum",
"update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices
[10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices
[10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the
price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp
1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so
it is updated to 3.
⁠                         // Timestamps are [1,2] with corresponding prices
[3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the
correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices
[3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp
4.



Constraints:


1 <= timestamp, price <= 10^9
At most 10^5 calls will be made in total to update, current, maximum, and
minimum.
current, maximum, and minimum will be called only after update has been
called at least once.


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class StockPrice:

    def __init__(self):
        self.data = {}
        self.max = {'price': float('-inf'), 'time': None}
        self.min = {'price': float('inf'), 'time': None}
        self.current = None

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.data and price == self.max['price'] \
            or price == self.min['price'] : # 如果更新的值对最大,最小值有影响
            # max_data = (timestamp, price)
            # min_data = (timestamp, price)
            
            self.data[timestamp] = price
            self.max = {'price': price, 'time': timestamp}
            for timestamp, price in self.data.items():  # 遍历查找最值, 更优化的方法是边插入边排序查找起来快
                if price > self.max['price']:
                    self.max = {'price': price, 'time': timestamp}
                if price < self.min['price']:
                    self.min = {'price': price, 'time': timestamp}
                if timestamp > self.current:
                    self.current = timestamp
        self.data[timestamp] = price
        if price > self.max['price']:
            self.max = {'price': price, 'time': timestamp}
        if price < self.min['price']:
            self.min = {'price': price, 'time': timestamp}
        if self.current is None or timestamp > self.current:
            self.current = timestamp

    def current(self) -> int:
        return self.data[self.current]

    def maximum(self) -> int:
        return self.max['price']

    def minimum(self) -> int:
        return self.min['price']





# @lc code=end




if __name__ == "__main__":
    # Your StockPrice object will be instantiated and called as such:
  obj = StockPrice()
  obj.update(10, 1)
  param_2 = obj.current()
  param_3 = obj.maximum()
  param_4 = obj.minimum()

