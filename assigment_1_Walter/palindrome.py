#Q2
def isPalindrome(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])
    
inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")
