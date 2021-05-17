def subset_sum(array: list[int], target: int) -> bool:
    n = len(array)
    if not target:
        return True
    SS = [[j == 0 for j in range(target+1)] for _ in range(n)]
    for i in range(n):
        if i == 0:
            SS[i][array[i]] = True
        else:
            for j in range(target+1):
                if j < array[i]:
                    SS[i][j] = SS[i-1][j]
                else:
                    SS[i][j] = SS[i-1][j] or SS[i-1][j-array[i]]
    return SS[n-1][target]
