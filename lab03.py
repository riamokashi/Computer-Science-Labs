
A = input("Enter a word ('quit' to quit): ").lower()
VOWELS = 'aeiou' 

while A != "quit":
#    if A[0] == 'a' or A[0] == 'e' or A[0] == 'i' or A[0] == 'o' or A[0] == 'u':
    if A[0] in VOWELS:    
        print(A + "way")
    else:
        for i, ch in enumerate(A):
            if ch in VOWELS:    
                print(A[i:] + A[:i] + "ay")
                break
        if A == 'b':
            print('bay')
    A = input("Enter a word ('quit' to quit): ").lower()
    

#hello
#i ch
#0 h
#1 e
#2 l
#3 l
#

    