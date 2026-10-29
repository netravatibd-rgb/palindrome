def check_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

string = input("Enter a string: ")
check_palindrome(string)