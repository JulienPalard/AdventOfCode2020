from itertools import count


def A181391(starting):
    """Van Eck's sequence.

    For n >= 1, if there exists an m < n such that a(m) = a(n), take
    the largest such m and set a(n+1) = n-m; otherwise a(n+1) =
    0. Start with a(1)=0.
    """
    last_pos = {value: pos for pos, value in enumerate(starting)}
    for i in starting:
        yield i
    cur_value = starting[-1]
    for i in count(start=len(starting) - 1):
        next_value = i - last_pos.get(cur_value, i)
        last_pos[cur_value] = i
        yield next_value
        cur_value = next_value


for i, value in enumerate(A181391([19, 20, 14, 0, 9, 1])):
    if i == 2020 - 1:
        print("Part 1:", value)
    if i == 30000000 - 1:
        print("Part 2:", value)
        break
