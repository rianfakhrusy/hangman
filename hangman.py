words = ["awkward", "hazard", "memento", "gazebo", "cordon", "festival", "zombie", "chandelier"]
import random
word = words[random.randint(0,len(words)-1)].lower()
limit = (len(word)+1)//3+2
                 
ans = ['_'] * len(word)
c = ''
count = 0
failed = {}
inputted = {}
print(' '.join(ans), "failed:", list(k for k in failed.keys()))
while count < len(word) and len(failed) < limit:
    c = input().lower()
    if len(c) != 1:
        print("You must use only one character")
        continue
    
    if c in inputted:
        print("You have already inputted the character")
        continue

    found = False
    for i in range(len(word)):
        if c == word[i]:
            ans[i] = c
            count += 1
            found = True
    if not found:
        failed[c] = 1
        print("Incorrect guess!")
    else:
        print("Correct guess!")
    inputted[c] = True
    if count == len(word):
        print("Congratulation!")
    print(' '.join(ans), "failed:", list(k for k in failed.keys()))
    if len(failed) == limit:
        print("Game over!") 
        print("The answer is", word)