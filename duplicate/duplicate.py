def is_duplicate(s):
    n = len(s)
    if n == 0:
        return False
    if n == 1:
        return True        

    if n % 2 != 0:
        return False

    mid = n // 2
    left = s[:mid]
    right = s[mid:]

    if left != right:
        return False

    return is_duplicate(left)
