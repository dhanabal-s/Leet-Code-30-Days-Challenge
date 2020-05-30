# Problem
__Uncrossed Lines__

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];<br>
The line we draw does not intersect any other connecting (non-horizontal) line.<br>
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.<br>

Return the maximum number of connecting lines we can draw in this way.<br>

Example 1:<br>
Input: A = [1,4,2], B = [1,2,4]<br>
Output: 2<br>
Explanation: We can draw 2 uncrossed lines as in the diagram.<br>
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.<br>

Example 2:<br>
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]<br>
Output: 3<br>

Example 3:<br>
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]<br>
Output: 2<br>
 
Note:<br>
* 1 <= A.length <= 500
* 1 <= B.length <= 500
* 1 <= A[i], B[i] <= 2000


[LeetCode Problem link](https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/)


[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/new/master/May2020/Week4/Day_25/Solution.py)

