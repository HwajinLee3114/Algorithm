def solution(num_list):
    sum_tot = 0
    prod_tot = 1
    
    for num in num_list:
        sum_tot += num
        prod_tot *= num
    return 1 if prod_tot < sum_tot ** 2 else 0