# Problem
__Possible Bipartition__

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:<br>
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]<br>
Output: true<br>
Explanation: group1 [1,4], group2 [2,3]<br>

Example 2:<br>
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]<br>
Output: false<br>

Example 3:<br>
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]<br>
Output: false<br>
 
Constraints:<br>
* 1 <= N <= 2000
* 0 <= dislikes.length <= 10000
* dislikes[i].length == 2
* 1 <= dislikes[i][j] <= N
* dislikes[i][0] < dislikes[i][1]
* There does not exist i != j for which dislikes[i] == dislikes[j].


[Leetcode Problem link]()

[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/May2020/Week4/Day_27/Solution.py)

