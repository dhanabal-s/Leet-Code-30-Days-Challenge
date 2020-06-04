# Problem
__Two City Scheduling__

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:<br>
Input: [[10,20],[30,200],[400,50],[30,20]]<br>
Output: 110<br>
Explanation: <br>
The first person goes to city A for a cost of 10.<br>
The second person goes to city A for a cost of 30.<br>
The third person goes to city B for a cost of 50.<br>
The fourth person goes to city B for a cost of 20.<br>

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 
Note:<br>
* 1 <= costs.length <= 100
* It is guaranteed that costs.length is even.
* 1 <= costs[i][0], costs[i][1] <= 1000

[Leetcode Problem link](https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/)

[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/Jun2020/Week1/Day3/Solution.py)


