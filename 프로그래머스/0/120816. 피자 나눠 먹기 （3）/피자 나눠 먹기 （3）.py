def solution(slice, n):
    piece = n // slice

    if (n % slice == 0):
        return piece
    else:
        return piece + 1
        