sti=input("Enter any word ")
listo=[]
dico={}
for index,letter in enumerate (sti):
    dico[index]=letter
print(dico)
for i in sti:
    listo.append(i)
print(listo)

# Input string
input_string = "hello world"

# Initialize an empty dictionary
frequency_dict = {}

# Count the frequency of each character
for char in input_string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

# Print the result
print("Character frequencies:", frequency_dict)
print("********************")
word=list(sti)
print(word)
