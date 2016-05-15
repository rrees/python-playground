
def ints_left_zero(ints):
    end = len(ints) - 1

    while ints[end] == 0 and end > -1:
        end = end - 1

    if end == 0:
        return ints

    i = 0
    while i < end:
        if not ints[i] == 0:
            i = i + 1
            continue

        j = i
        while j < end:
            ints[j] = ints[j+1]
            j = j + 1

        ints[end] = 0
        end = end - 1

    return ints
