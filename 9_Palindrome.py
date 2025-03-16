def check_palindrome(num):
    if num == num[::-1]:
        print(f"{num} is an palindrome")
    else:
        print(f"{num} Not palindrome")
user_input = input("Enter the number to check :")
check_palindrome(user_input)
