def reversesentence(sentence):
    words = sentence.split()  
    reversed_words = words[::-1] 
    return " ".join(reversed_words)  

user_input = input("Enter a sentence: ")
print(reversesentence(user_input))
