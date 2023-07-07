def marking(cc):
    return cc if len(cc) < 4 else '#' * (len(cc) - 4) + cc[-4:]


def sum_two_smallest_numbers(numbers):
    return min(numbers) + sorted(numbers)[1]


if __name__ == '__main__':
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
    ls = [x for x in range(-4, 5)]
    print(sum(ls))


