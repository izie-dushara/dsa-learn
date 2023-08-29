def divisible_melon(n):
    """
     if you divide it equally then there's only one for each which is not even
    """
    if n == 2:
        return "NO"
    else:
        return "YES" if n % 2 == 0 else "NO"
    # if n % 2 == 0:
    #     return "YES"
    # else:
    #     return "NO"


n = int(input(""))
result = divisible_melon(n)
print(result)
