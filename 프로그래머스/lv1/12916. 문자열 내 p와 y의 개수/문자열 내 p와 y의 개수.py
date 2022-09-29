def solution(s):
    p_sum = 0
    y_sum = 0
    result = True
    
    for i in s:
        if 'p' is i or 'P' is i:
            p_sum += 1
        elif 'y' is i or 'Y' is i:
            y_sum += 1
            
    if y_sum != p_sum:
        result = False
    return result