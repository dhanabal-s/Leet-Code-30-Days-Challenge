# Problem
__Online Stock Span__

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:</br>
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]</br>
Output: [null,1,1,1,2,1,4,6]</br>
Explanation: </br>
First, S = StockSpanner() is initialized.  Then:</br>
S.next(100) is called and returns 1,</br>
S.next(80) is called and returns 1,</br>
S.next(60) is called and returns 1,</br>
S.next(70) is called and returns 2,</br>
S.next(60) is called and returns 1,</br>
S.next(75) is called and returns 4,</br>
S.next(85) is called and returns 6.</br>

Note that (for example) S.next(75) returned 4, because the last 4 prices</br>
(including today's price of 75) were less than or equal to today's price.</br>
 

Note:</br>
Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.</br>
There will be at most 10000 calls to StockSpanner.next per test case.</br>
There will be at most 150000 calls to StockSpanner.next across all test cases.</br>
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.


[LeetCode Problem link](https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/)

[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/May2020/Week3/Day_19/Solution.py)

