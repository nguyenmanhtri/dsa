We are give an array A consisting of N distinct integers. We would like to sort array A in ascending order. First, we divide it into one or more slices. Then we sort each slice. After that, we join the sorted slices in the same order. Write a function `solution` that returns the maximum number of slices for which the algorithm will return a correctly sorted array.

Input: A = [2, 4, 1, 6, 5, 9, 7]
Output: 3. They array can be splitted into 3 slices: [2, 4, 1], [6, 5], [9, 7]. Then, after sorting each slice and joining them together, the whole array will be sorted into ascending order.
