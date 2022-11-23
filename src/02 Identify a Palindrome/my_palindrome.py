def is_palindrome(string: str) -> bool:
    rev = string[::-1]
    return rev == string

print(is_palindrome("racecar"))