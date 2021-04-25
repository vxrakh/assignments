import collections 

def tf(text): 
  tf_text = collections.Counter(text) 
  for i in tf_text: 
    tf_text[i] = tf_text[i]/float(len(text)) 
  return tf_text 

dic = {} 
with open ('text_for_test.txt', encoding = 'utf-8') as file: 
  txt = file.read().replace('...', '.').replace('!', '.').replace('?', '.').replace('\n', '') 
  for i in txt.split('.'): 
    dic[i] = len([j for j in i.split() if len(j) == 1]) 
print('средняя к-во слов в предложении:', len(txt.split(' '))/txt.count('.')) 

s1 = sorted(dic.items(), key = lambda x: -x[1]) 
print(s1[0][0], 'contains', s1[0][1], 'one-character words(max).') 
with open ('text_for_test.txt', encoding = 'utf-8') as file: 
  x = [word for word in file.read().split()] 
tfw = input('введите слово для расчета:') 
tf1 = tf(x) 
print('частотность:', "%.4f" % tf1[tfw])
