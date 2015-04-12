'''
improved feature set function
'''

def gender_feature(word):
    return {'suffix1':word[-1:],'suffix2':word[-2:]}



'''
basic feature set

def gender_feature(word):
    return { 'lastletter':word[-1]}

'''


'''
Improving the feature set function


def gender_feature(word):
    features = {}
    features["firstletter"]  = word[0].lower()
    features["lastletter"] = word[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" %(letter) ] = word.lower().count(letter)
        features["has(%s)" %(letter) ] = ( letter in word.lower() )
    return features
'''

