import os
import sys
import random
from colorama import Fore as Col

os.system('cls' if os.name == 'nt' else 'clear')

width = input(Col.CYAN+"Width_"+Col.BLUE)
height = input(Col.CYAN+"Height_"+Col.BLUE)

width = 133 if width == "" else int(width)
height = 32 if height == "" else int(height)

Map = {}

Map.update({-1:{}})
Map.update({height:{}})
for c in range(-1,width+1) :
    Map[-1].update({c:""})
    Map[height].update({c:""})

for c in range(height) :
    Map.update({c:{}})
for c in range(height) :
    Map[c].update({-1:""})
    Map[c].update({width:""})
    for i in range(width) :
        Map[c].update({i:"-"})

edge = {}

def render() :
    os.system('cls' if os.name == 'nt' else 'clear')
    for c in range(height) :
        for i in range(width) :
            col = Col.LIGHTBLACK_EX
            if Map[c][i] == "#" :
                col = Col.GREEN
            for k in edge :
                if c in edge[k] :
                    if i == edge[k][c] :
                        col = Col.MAGENTA
            sys.stdout.write(col+Map[c][i])
        sys.stdout.write("\n")

def grow(amount,renderProcess = False) :
    basepointone = random.randint(0,height-1)
    basepointtwo = random.randint(0,width-1)

    if amount > width*height :
        print(Col.RED+"Amount too high.")
        return(False)

    Map[basepointone][basepointtwo] = "#"

    edge.clear()
    for c in range(0,height) :
        for i in range(0,width) :
            if Map[c][i] != "-" :
                if c+1 < height and Map[c+1][i] == "-" or c-1 >= 0 and Map[c-1][i] == "-" or i+1 < width and Map[c][i+1] == "-" or i-1 >= 0 and Map[c][i-1] == "-":
                    edge.update({len(edge): {c: i}})

    growpointone = random.randint(basepointone-1,basepointone+1)
    growpointtwo = random.randint(basepointtwo-1,basepointtwo+1)

    for c in range(amount-1) :
        attempts = random.randint(1,2)
        growpointone = random.randint(basepointone-1,basepointone+1)
        growpointtwo = random.randint(basepointtwo-1,basepointtwo+1)
        while Map[growpointone][growpointtwo] != "-" :
            for i in range(attempts) :
                if Map[growpointone][growpointtwo] != "-" :
                    growpointone = random.randint(basepointone-1,basepointone+1)
                    growpointtwo = random.randint(basepointtwo-1,basepointtwo+1)
            if Map[growpointone][growpointtwo] != "-" :
                basesetno = random.randint(0,len(edge)-1)

                if len(str(edge[basesetno].keys())) == 14:
                    basepointone = int(str(edge[basesetno].keys())[11])
                else :
                    basepointone = int(str(edge[basesetno].keys())[11]+str(edge[basesetno].keys())[12])
                if len(str(edge[basesetno].keys())) == 14 :
                    basepointtwo = edge[basesetno][int(str(edge[basesetno].keys())[11])]
                else :
                    basepointtwo = edge[basesetno][int(str(edge[basesetno].keys())[11]+str(edge[basesetno].keys())[12])]
        Map[growpointone][growpointtwo] = "#"
        edge.clear()
        for c in range(0,height) :
            for i in range(0,width) :
                if Map[c][i] != "-" :
                    if c+1 < height and Map[c+1][i] == "-" or c-1 >= 0 and Map[c-1][i] == "-" or i+1 < width and Map[c][i+1] == "-" or i-1 >= 0 and Map[c][i-1] == "-":
                        edge.update({len(edge): {c: i}})
        if renderProcess :
            render()

grow(int(input(Col.CYAN+"Growth-Cycles_"+Col.BLUE)),eval(input(Col.CYAN+"Render-Growth-Process_"+Col.BLUE)))
render()
print(Col.LIGHTMAGENTA_EX+"Complete.")

while True :
    pass