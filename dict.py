import sys
w = input()
w2 = input()
t1 = 0
t2 = 0
t3 = 0
t4 = 0

for i in range (len(w)):
    if "0" <= w[i] <= "9":
        sys.exit("we're working with words here, do better")
    elif "A" <= w[i] <= "Z" or "a" <= w[i] <= "z":
        t1+=1
    elif "А" <= w[i] <= "Я" or "а" <= w[i] <= "я":
        t2+=1
for i in range (len(w2)):
    if "0" <= w2[i] <= "9":
        sys.exit("we're working with words here, do better")
    elif "A" <= w2[i] <= "Z" or "a" <= w2[i] <= "z":
        t3+=1
    elif "А" <= w2[i] <= "Я" or "а" <= w2[i] <= "я":
        t4+=1
if t1==len(w) and t4==len(w2):
    print("the english word is" , w)
    print("the russian word is" , w2)
elif t2 == len(w) and t3 == len(w2):
    print("the english word is" , w2)
    print("the russian word is" , w)
else:
    print("something's wrong here")
