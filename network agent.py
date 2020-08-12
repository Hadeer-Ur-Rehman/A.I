import random
from numpy.random import choice
from copy import deepcopy

vowels = ['a','e'] #producer
personalities = ['f','s'] #f-flexible s-stubborn

#simple function create agent
def makeAgent(vowel,personality):
    return [vowel,personality]

agent_one = makeAgent(vowels[1],personalities[0])
print("\nfrom make agent")
print(agent_one)

#call the function make a population of 5 identical
def makePop_identical(n):
    population = []
    for i in range(n):
        agnt=makeAgent(vowels[1],personalities[0])
        population.append(agnt)
    return population

pop_test = makePop_identical(5)
print("\nfrom make agent identical")
print(pop_test)

#create a function that generate of population of n agent with randomly
def makePop_Random(n):
    population = []
    for i in range(n):
        v=random.choice(vowels)
        p=random.choice(personalities)
        agnt = makeAgent(v,p)
        population.append(agnt)
    return population

popolate1 = makePop_Random(5)
print("\nfrom make agent random")
print(popolate1)

#repeat random interection with differnt method
def makePop(n):
    population = []
    for i in range(n):
        v=random.randint(0,1)
        p=random.randint(0,1)
        agnt = makeAgent(vowels[v],personalities[p])
        population.append(agnt)
    return population

popolate2 = makePop_Random(5)
print("\nfrom make population")
print(popolate2)

#create func. that calculate proportion of agent with the variant 'a'
def count(population):
    t=0 #must be float
    for agent in population:
        if agent[0] == 'a':
            t+=1
    return t/len(population)

ferman = count(makePop(5))
print("\nfrom count")
print("proportion of [a] is ",ferman)

#here we use numpy which is import above
#so first, we need to make a function that randomly select two agentsfrom the population.
def choose_pair(population):
    i = random.randint(0,len(population)-1)#python count from 0, so pop(5) is an error
    j = random.randint(0,len(population)-1)
    while i==j: #makeSure  same agent
        j = random.randint(0,len(population)-1) #makeSure the same agent is not select twice
    return population[i],population[j]

hira=makePop(5)
listner,producer = choose_pair(hira)
print("\nfrom choose pair")
print("the population ",popolate2)
print("choosen pair ",listner,producer)
print("the listner ",listner)
print("the producer ",producer)

#here we use deepcopy which is import above.
def interect_test(listner,producer):
    if listner[0] == producer[0]:
        return listner
    else:
        if listner[1]=='s':
            return listner #if the listner is stubborn, no change
        else:
            listner[0]=deepcopy(producer[0])
            return listner

#you can check the o/p of loop by running code line below multiple line.

# uma=makePop(5) #you can also use this method.
# randomlister,randomproducer=choose_pair(uma)

randomlister,randomproducer=choose_pair(makePop(5)) #direct method
print("\nfrom interect")
print("The listner is: ",randomlister)
print("The Producer is: ",randomproducer)
updateListner=interect_test(randomlister,randomproducer)
print("After interecting, the listner is: ",updateListner)