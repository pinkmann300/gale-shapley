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
w5 = Woman("Woman 5", [], None)

m1 = Man("Man 1",[],None)
m2 = Man("Man 2",[],None)
m3 = Man("Man 3",[],None)
m4 = Man("Man 4",[],None)

womenList = [w1,w2,w3,w4,w5]
menList = [m1,m2,m3,m4]


# Writing code to test out the single man condition and making appropriate changes to the "propose" function to handle the same.

for i in range(len(menList)):
    menList[i].updatePref(random.sample(womenList,len(womenList)))

for j in range(len(womenList)):
    womenList[j].updatePref(random.sample(menList, len(menList)))



def generateData(m,w):
    menArr = []
    womenArr = []
    for i in range(m):
        menstr = "Man " + str(i+1)
        menArr.append(Man(menstr,[],None))
    
    for l in range(w):
        womenstr = "Woman " + str(l+1)
        womenArr.append(Woman(womenstr,[],None))

    return [menArr, womenArr]


print("Men's preference list: ")
print("\n")
for l in range(len(menList)):
    print(menList[l].name,"-> ",end=' ') 
    for k in (menList[l].prefLis):
        print(k.name, end=",")
    print("")

print("\n")
print("Women's preference list: ")
print("\n")
for r in range(len(womenList)):
    print(womenList[r].name,"->", end=' ')
    for c in (womenList[r].prefLis):
        print(c.name, end=',')
    print("")

print("\n")


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
            if man1.prefLis.index(woman1) + 1 > (len(man1.prefLis) - 1):
                man1.matched = None
            else:
                propose(man1,man1.prefLis[man1.prefLis.index(woman1) + 1])

        else: 
            woman1_curr.matched = None 
            woman1.matched = man1
            man1.matched = woman1
            if woman1_curr.prefLis.index(woman1) + 1 > (len(woman1_curr.prefLis) -1):
                woman1_curr.matched = None
            else:
                propose(woman1_curr,woman1_curr.prefLis[woman1_curr.prefLis.index(woman1) + 1])
        

def gale_shapley(mList,wList):
    stable_match = []
    for k in mList:
        propose(k, k.prefLis[0])
            
    for m in mList:
        if m.matched is None:
            m.matched = Man("None", [], None)
        tupel = (m.name, m.matched.name)
        stable_match.append(tupel)

    return stable_match



print("Stable Matching: ", gale_shapley(menList,womenList))


# Improvements : Add blocking pairs test to prove correctness and the fact that it is a stable matching. 
#                Improve the function that generates the data for which the gale shapley algorithm is run better. 