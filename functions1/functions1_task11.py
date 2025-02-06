def is_palindrome(word):
    word = word.lower()  
    return word == word[::-1]  

word = input("Enter a word: ")
if is_palindrome(word):
    print("palindrome!")
else:
    print("not a palindrome.")