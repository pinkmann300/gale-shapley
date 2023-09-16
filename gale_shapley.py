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

for i in range(len(menList)):
    menList[i].updatePref(random.sample(womenList, len(womenList)))
    womenList[i].updatePref(random.sample(menList, len(menList)))


for j in range(len(menList)):
    print(menList[j].name,"-> ",end=' ') 
    for k in (menList[j].prefLis):
        print(k.name, end=",")
    print("")



