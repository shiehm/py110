# Solution 1 - Solving by examining a pattern
def cum_sum(num):
    cum_sum = 0
    for n in range(num, 0, -1):
        cum_sum += n
    return cum_sum

def sum_evens(row):
    total = [num * 2 for num in range(1, cum_sum(row) + 1)]
    prior = [num * 2 for num in range(1, cum_sum(row - 1) + 1)]
    return  sum(total) - sum(prior)
    
# Solution 2 - Building the actual list of lists in its entirety
def build_rows(rows):
    all_rows = []
    current_num = 2
    for row in range(1, rows + 1):
        current_row = []
        for _ in range(row):
            current_row.append(current_num)
            current_num += 2
        all_rows.append(current_row)
    return all_rows

def sum_last_row(rows):
    return sum(build_rows(rows)[-1])    