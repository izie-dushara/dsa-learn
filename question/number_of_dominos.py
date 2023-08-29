def max_number_of_dominos(M, N):
    return (M * N) // 2


# Input
M, N = map(int, input().split())

# Calculate and output the mx. number of dominoes
result = max_number_of_dominos(M, N)
print(result)
