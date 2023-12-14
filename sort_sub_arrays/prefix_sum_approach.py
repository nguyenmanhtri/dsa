from typing import List


def solution(A: List[int]) -> int:
    """
    Input: A = [2, 4, 1, 6, 5, 9, 7]
    Output: 3
    """
    n = len(A)
    max_left = [0] * n
    min_right = [0] * n

    max_left[0] = A[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], A[i])

    min_right[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], A[i])

    res = 1
    for i in range(n - 1):
        if max_left[i] <= min_right[i + 1]:
            res += 1

    return res


def solution_b(A):
    res = 0
    curr_max = A[0]
    for i in range(len(A)):
        curr_max = max(curr_max, A[i])

        if i == len(A) - 1 or curr_max <= A[i + 1]:
            res += 1

    return res


A = [2, 4, 1, 6, 5, 9, 7]
# print(f"your output: {solution(A)}")
print(f"your output: {solution_b(A)}")
print("expected output: 3\n")

A = [1, 2, 0, 3]
# print(f"your output: {solution(A)}")
print(f"your output: {solution_b(A)}")
print("expected output: 2")
