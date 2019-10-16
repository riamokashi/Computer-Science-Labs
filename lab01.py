A.lower() = input("please enter a word ")

while A != "quit":
    if A.lower()[0] == 'a' or A.lower()[0] == 'e' or A.lower()[0] == 'i' or A.lower()[0] == 'o' or A.lower()[0] == 'u':
        print(A.lower() + "way")
    else:
        print(A.lower()[1:] + A.lower()[0] + "ay")
    A.lower() = input("please enter a word ")
