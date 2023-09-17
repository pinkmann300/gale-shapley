# The below is an implementation of the Gale-Shapley algorithmn which is used to provide a solution to the Stable-Matching problem.
# A definition of the stable matching problem can be found in the "Algorithms Design" book by Eva Tardos. 


import random 

class Man:
    def __init__(self,name,prefLis=[],matched=None):
        self.name = name
        self.prefLis = prefLis
        self.matched = matched

    def updatePref(self,l1):
        self.prefLis = l1
        return 

        
class Woman:
    def __init__(self,name,prefLis=[],matched=None):
        self.name = name 
        self.prefLis = prefLis
        self.matched = matched  

    def updatePref(self, l2):
        self.prefLis = l2
        return 
    

# Dummy data set. 

w1 = Woman("Woman 1", [], None)
w2 = Woman("Woman 2", [], None)
w3 = Woman("Woman 3", [], None)
w4 = Woman("Woman 4", [], None)

m1 = Man("Man 1",[],None)
m2 = Man("Man 2",[],None)
m3 = Man("Man 3",[],None)
m4 = Man("Man 4",[],None)

womenList = [w1,w2,w3,w4]
menList = [m1,m2,m3,m4]


stable_match = []


for i in range(len(menList)):
    menList[i].updatePref(random.sample(womenList, len(womenList)))
    womenList[i].updatePref(random.sample(menList, len(menList)))



for j in range(len(menList)):
    print(menList[j].name,"-> ",end=' ') 
    for k in (menList[j].prefLis):
        print(k.name, end=",")
    print("")


for m in range(len(womenList)):
    print(womenList[m].name,"->", end=' ')
    for l in (womenList[m].prefLis):
        print(l.name, end=',')
    print("")


def isAllMatch(l1):
    match = True 
    for k in l1:
        if k.matched is not None:
            match = match and True 
        else:
            match = match and False 

    return match 


def propose(man1,woman1):
    if woman1.matched is None:
        woman1.matched = man1
        man1.matched = woman1 
    else:
        woman1_curr = woman1.matched 
        wom_pref = woman1.prefLis
        if wom_pref.index(woman1_curr) < wom_pref.index(man1):
            woman1.matched = woman1_curr
            propose(man1,man1.prefLis[man1.prefLis.index(woman1) + 1])
        else: 
            woman1_curr.matched = None 
            woman1.matched = man1
            man1.matched = woman1
            propose(woman1_curr,woman1_curr.prefLis[woman1_curr.prefLis.index(woman1) + 1])
        

def gale_shapley(mList,wList):
    if len(mList) != len(wList):
        print("Not acceptable")
        
    else:
        for k in mList:
            propose(k, k.prefLis[0])

        for m in mList:
            tupel = (m.name, m.matched.name)
            stable_match.append(tupel)


gale_shapley(menList,womenList)
print(stable_match)
