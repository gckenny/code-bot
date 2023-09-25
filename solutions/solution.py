def solution(a: list[int]) -> int:
    a.sort()
    n = len(a)
    return max(a[n-1] * a[n-2] * a[n-3], a[0] * a[1] * a[n-1])
