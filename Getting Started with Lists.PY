empty__list = []
print()

number = [1,2,3,4,5]
print(number) 

triples = [1,2,3]*3
print(triples)

alist = [100,200,300,400,500]
alist = alist [::-1]
print(alist)

def match__word(word):
    ctr = 0
    lst = []
    for word in word:
        if len (word) > 1 and word[0] == word [-1]:
            ctr += 1
            lst.append(word)

    print("list of word with first and last character same/n",lst)
    return ctr 


count = match__word(['abc','cfc','xyz','aba','1221'])
print("Number of words having first and last character same:",count)    