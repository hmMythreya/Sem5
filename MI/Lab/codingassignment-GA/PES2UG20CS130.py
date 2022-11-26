import numpy as np
import random
gen=50
pop=10

def ReLU(x):
    return max(0.0, x)

class neu:
    def __init__(self,bias,w1,w2):
        self.inp1=0
        self.inp2=0
        self.we1=w1
        self.we2=w2
        self.bi=bias
    
    def giveOut(self,inp1,inp2):
        self.inp1=inp1
        self.inp2=inp2
        temp=self.inp1*self.we1+self.inp2*self.we2+self.bi
        return ReLU(temp)

class chrm:
    def __init__(self,new=None):
        self.dna=[0,0,0,0,0,0]
        self.fitscore=0
        if not new:
            for i in range(6):
                self.dna[i]=random.uniform(-1,1)
        else:
            self.dna=new
    
    def newFitness(self, fitness):
        self.fitscore=fitness
    
    def mutate(self):
        if random.uniform(0,1)<0.1:
            tg=int(random.uniform(0,6))
            self.dna[tg]=random.uniform(-1,1)
    
    def crossover(self,newdna):
        re=[]
        for i in range(6):
            choose=random.random()
            if choose>0.5:
                re.append(newdna[i])
            else:
                re.append(self.dna[i])
        return re

def matingPool(public):
    re=[]
    for i in range(10):
        fitness=int(public[i].fitness*10)
        for _ in range(fitness):
            re.append(public[i])
    return re

def newKids(people):
    newGen=[]
    no=len(people)
    for i in range(10):
        parent1=people[random.randint(0,no-1)]
        parent2=people[random.randint(0,no-1)]
        childdna=parent1.crossover(parent2.dna)
        child=chrm(childdna)
        child.mutate()
        newGen.append(child)
    return newGen

def main():
    print(random.random(),random.uniform(-1,1),random.uniform(-1,1))
    soc=[]
    for _ in range(pop):
        soc.append(chrm())
    for _ in range(gen):
        for i in range(pop):
            correct=0
            neu1=neu(1,soc[i].dna[0],soc[i].dna[1])
            neu2=neu(1,soc[i].dna[2],soc[i].dna[3])
            neu3=neu(1,soc[i].dna[4],soc[i].dna[5])
            for tests in range(100):
                inp1=random.randint(0,1)
                inp2=random.randint(0,1)
                i1 = 0
                i2 = 0
                if inp1 == inp2:
                    i1=1
                else:
                    i2=0
                n1out=neu1.giveOut(i1,i2)
                n2out=neu2.giveOut(i1,i2)
                n3out=neu3.giveOut(n1out,n2out)
                triedOutput=0
                if n3out>0.5:
                    triedOutput=1
                if (inp1^inp2) == triedOutput:
                    correct+=1
            fitness=correct/100
            soc[i].fitness=fitness
        grpInHeat=matingPool(soc)
        soc=newKids(grpInHeat)
     
if __name__=="__main__":
    main()