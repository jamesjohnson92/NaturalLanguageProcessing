import gender_feature
import nltk
import corpus
import Main


dev = corpus.dev_names


errors = []
for (name,tag) in dev:
    guess = Main.classifier.classify(gender_feature.gender_feature(name))
    if guess != tag:
        errors.append((tag,guess,name))

for (tag,guess,name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' %(tag,guess,name)



