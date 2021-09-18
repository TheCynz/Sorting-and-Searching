def get_count(sentence):
    #pass
    x=0
    vowel = ["a","e","i","o","u"]
    
    for i in sentence:
        if i in vowel:
            x += 1
    print(x)

get_count("bcdfghjklmnpqrstvwxz y")

#best
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
