def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for value in range(2, num//2+1):
        if num % value == 0:
            return False
    return True

def get_factors(num: int) -> list[int]:
    div = 2
    ret = []
    while div <= num:
        if is_prime(div) and num % div == 0:
            ret.append(div)
            num = num//div
        else:
            div += 1
    return ret

print(get_factors(630))
