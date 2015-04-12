from nltk.corpus import names

names = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])

train_names = names[1500:]
dev_names = names[500:1500]
test_names = names[:500]


