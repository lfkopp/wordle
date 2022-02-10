#%%
import numpy as np
from random import shuffle
#%%
with open('wordlist.txt') as f:
    wordlist = [x.strip() for x in f.readlines()]


# %%
def guessing(guess,result,wordlist):
    for i in range(5):
        g, r = guess[i], result[i]
        if r == 'x':
            wordlist = [x for x in wordlist if g not in x]
        if r == 'y':
            wordlist = [x for x in wordlist if x[i] != g]
            wordlist = [x for x in wordlist if g in x]
        if r == 'g':
            wordlist = [x for x in wordlist if x[i] == g]
    return wordlist

def compara(x,word):
    result = ['x','x','x','x','x']
    for i in range(5):
        if x[i] in word:
            result[i] = 'y'
            if x[i] == word[i]:
                result[i] = 'g'
    result = ''.join(result)
    return result
#%%

guess = input('guess the word') 
result = input('x,y,g')
wordlist = guessing(guess,result,wordlist)


# %%
wordlist
# %%
len(wordlist)
# %%


words = []
shuffle(wordlist)
for word in wordlist:
    scorelist = []
    shuffle(wordlist)
    for x in wordlist[:100]:
        result = compara(x,word)
        w = guessing(x, result, wordlist)
        scorelist.append(-np.log2(len(w)/len(wordlist)))
    words.append(tuple((word,np.median(scorelist))))

# %%
words.sort(key=lambda tup: tup[1], reverse=True)
words
# %%

# %%
