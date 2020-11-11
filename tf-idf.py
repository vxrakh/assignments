import math
import collections
from collections import Counter

def tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

text1 = []
text2 = []
text3 = []
with open('t1.txt','r') as a:
    for word in a.read().split():
        text1.append (word)
with open('t2.txt','r') as a:
    for word in a.read().split():
        text2.append (word)
with open('t3.txt','r') as a:
    for word in a.read().split():
        text3.append (word)

print(tf(text1))
print(tf(text2))
print(tf(text3))


text1 = []
text2 = []
text3 = []
with open('t1.txt','r') as a:
    for word in a.read().split():
        text1.append (word)
with open('t2.txt','r') as a:
    for word in a.read().split():
        text2.append (word)
with open('t3.txt','r') as a:
    for word in a.read().split():
        text3.append (word)
        
corpus = [text1, text2, text3]

def idf(word,corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

print (idf('он',[text1,text2,text3]))
print (idf('она',[text1,text2,text3]))

def tfidf(corpus):
    def tf(text):
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/float(len(text))
        return tf_text
    def idf(word, corpus):
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
    b = []
    for text in corpus:
        tf_idf = {}
        tf1 = tf(text)
        for word in tf1:
            tf_idf[word] = tf1[word] * idf(word, corpus)
        b.append(tf_idf)
    return b

text1 = []
text2 = []
text3 = []
with open('t1.txt','r') as a:
    for word in a.read().split():
        text1.append (word)
with open('t2.txt','r') as a:
    for word in a.read().split():
        text2.append (word)
with open('t3.txt','r') as a:
    for word in a.read().split():
        text3.append (word)
        
corpus = [text1, text2, text3]

print (tfidf([text1,text2,text3]))
    
