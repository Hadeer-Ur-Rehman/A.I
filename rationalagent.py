import random

action=['smile','frown','nod','blink']
content=['positive','negative','happy']
mood=['happy','sad','neutral']
act=random.choice(action)
con=random.choice(content)
mod=random.choice(mood)

def agent_seq():
    word=input("Enter sentence: ")
    str=word.split('')
    for h in str: #first loop for mood
        for s in str: #second loop for content
            if h==('happy') and s==('positive') or s==('negative'):
                print("smile")
            elif h==('happy') and s==('unsure'):
                print("nod")