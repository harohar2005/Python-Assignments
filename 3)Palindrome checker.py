


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]



text = input("Enter a string: ")
print(is_palindrome(text))