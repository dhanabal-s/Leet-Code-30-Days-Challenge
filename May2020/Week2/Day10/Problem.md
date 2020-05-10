# Problem

__Find the Town Judge__

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:</br>
The town judge trusts nobody.</br>
Everybody (except for the town judge) trusts the town judge.</br>
There is exactly one person that satisfies properties 1 and 2.</br>
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.</br>

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.</br>

Example 1:</br>
Input: N = 2, trust = [[1,2]]</br>
Output: 2</br>

Example 2:</br>
Input: N = 3, trust = [[1,3],[2,3]]</br>
Output: 3</br>

Example 3</br>
Input: N = 3, trust = [[1,3],[2,3],[3,1]]</br>
Output: -1</br>

Example 4:</br>
Input: N = 3, trust = [[1,2],[2,3]]</br>
Output: -1</br>

Example 5:</br>
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]</br>
Output: 3</br>
 
Note:

1 <= N <= 1000</br>
trust.length <= 10000</br>
trust[i] are all different</br>
trust[i][0] != trust[i][1]</br>
1 <= trust[i][0], trust[i][1] <= N

[LeetCode Problem link](https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325)

[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/May2020/Week2/Day10/Solution.py)
