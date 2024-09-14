def solution(num_list):
    odd_tot = ''
    even_tot = ''
    for num in num_list:
        if num % 2:
            odd_tot += str(num)
        else:
            even_tot += str(num)
    return int(odd_tot) + int(even_tot)