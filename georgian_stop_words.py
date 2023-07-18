from nltk.corpus import stopwords
from googletrans import Translator
translator = Translator()
stop_words = set(stopwords.words('english'))
georgian_stop_words = []
for word in stop_words:
    try:
        georgian_stop_words.append(translator.translate(word, dest='ka').text)
    except Exception as ex:
        print(ex)

with open('file1.txt', 'w+') as f:
    for i in georgian_stop_words:
        f.write('%s\n' % i)

print(georgian_stop_words)
