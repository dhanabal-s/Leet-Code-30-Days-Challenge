# Problem
__Edit Distance__

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character

Example 1:<br>
Input: word1 = "horse", word2 = "ros"<br>
Output: 3<br>
Explanation: <br>
horse -> rorse (replace 'h' with 'r')<br>
rorse -> rose (remove 'r')<br>
rose -> ros (remove 'e')<br>

Example 2:<br>
Input: word1 = "intention", word2 = "execution"<br>
Output: 5<br>
Explanation: <br>
intention -> inention (remove 't')<br>
inention -> enention (replace 'i' with 'e')<br>
enention -> exention (replace 'n' with 'x')<br>
exention -> exection (replace 'n' with 'c')<br>
exection -> execution (insert 'u')<br>


[LeetCode Problem link](https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/)


[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/May2020/Week5/Day_31/Solution.py)


