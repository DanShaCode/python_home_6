
def A_Progression (a1, d, n, arithmetic_progressive):
    if n == 1:
        arithmetic_progressive.append(a1)
        arithmetic_progressive.sort()
        return arithmetic_progressive
    arithmetic_progressive.append(a1 + ((n - 1) * d))
    return A_Progression(a1, d, n - 1,arithmetic_progressive)