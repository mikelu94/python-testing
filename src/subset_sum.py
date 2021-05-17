def subset_sum(array: list[int], target: int) -> bool:
    """Calculate whether there exists a subarray that sums to a given target."""
    array_length = len(array)
    if not target:
        return True
    subset_sum_exists = [[j == 0 for j in range(target+1)] for _ in range(array_length)]
    for i in range(array_length):
        if i == 0:
            subset_sum_exists[i][array[i]] = True
        else:
            for j in range(target+1):
                if j < array[i]:
                    subset_sum_exists[i][j] = subset_sum_exists[i-1][j]
                else:
                    subset_sum_exists[i][j] = subset_sum_exists[i-1][j] or subset_sum_exists[i-1][j-array[i]]
    return subset_sum_exists[array_length-1][target]
