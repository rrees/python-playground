import reverse as rev

def reverse(s):
    def reverse_word(chrs, start, end):
        c = chrs[start]
        p = start
        q = end
        while p < q:
            c = chrs[p]
            chrs[p] = chrs[q]
            chrs[q] = c
            p = p + 1
            q = q - 1
        return chrs

    reversed_chrs = list(rev.a_string(s))

    last_start = 0
    for i in range(len(reversed_chrs)):
        if not reversed_chrs[i] in ' ':
            continue

        reversed_chrs = reverse_word(reversed_chrs, last_start, i - 1)

        last_start = i

    reversed_chrs = reverse_word(reversed_chrs, last_start + 1, len(reversed_chrs) - 1)

    return "".join(reversed_chrs)
