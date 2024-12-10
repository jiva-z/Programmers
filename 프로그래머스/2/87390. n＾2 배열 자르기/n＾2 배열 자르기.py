def solution(n, left, right):
    result = []
    for index in range(left, right + 1):
        row = index // n
        col = index % n
        result.append(max(row, col) + 1)
    return result