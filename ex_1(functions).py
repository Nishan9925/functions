# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
    return s == s[::-1]


s = str(input("Enter a word right here to check if it is a palindrome word  "))
a = palindrome(s)
if a:
    print("yes")
else:
    print("no")
