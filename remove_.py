def remove(n, digit):
    n_str = str(n)
    while n_str.count(str(digit)):
        n_str = n_str.replace(str(digit), '', 1)
    return int(n_str)
