from typing import List


def sum_binary_greater_than_zero(a: int, b: int) -> bool:
    res = bin_sum(a, b)
    return int(res, 2) > 0


def bin_sum(a: int, b: int) -> str:
    bin_a = bin(a)
    bin_b = bin(b)
    return bin(int(bin_a, 2) & int(bin_b, 2))


def solution(A: List[int]) -> int:
    res = 1
    cur_sum = A[0]
    for ele in A[1:]:
        if sum_binary_greater_than_zero(cur_sum, ele):
            res += 1
            cur_sum = int(bin_sum(cur_sum, ele), 2)

    return res


A = [7, 13, 8, 2, 3]
print(f"your output: {solution(A)}")
print("expected output: 3")
