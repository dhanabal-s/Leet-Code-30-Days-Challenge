# Problem

__Flood Fill__

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:</br>
Input: </br>
image = [[1,1,1],[1,1,0],[1,0,1]]</br>
sr = 1, sc = 1, newColor = 2</br>
Output: [[2,2,2],[2,2,0],[2,0,1]]</br>

Explanation:</br> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:

The length of image and image[0] will be in the range [1, 50].</br>
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.</br>
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].</br>

[LeetCode Problem link](https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/)

[Solution](https://github.com/DhanabalShanmugam/Leet-Code-30-Days-Challenge/blob/master/May2020/Week2/Day_11/Solution.py)
