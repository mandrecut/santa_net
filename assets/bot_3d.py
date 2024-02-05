import sys
import json
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def random_graph(N):
    g = [{"type":-1,"weight":1,"status":0,"pos":[0,0,0],"out":0}]
    for n in range(N):
        r = {"type":0,"weight":random.random(),"status":0,"pos":[2*random.random()-1,2*random.random()-1,2*random.random()-1],"out":0}
        g.append(r)
    s = sum([x["weight"] for x in g[1:]])
    for x in g[1:]:
        x["weight"] /= s
    return g

def distance2(x,y):
    dx,dy,dz = x[0] - y[0],x[1] - y[1],x[2] - y[2]
    return (dx*dx + dy*dy + dz*dz)**0.5

def plot_graph(g,txt):
    sources = ([x["pos"] for x in g if x["type"] == 0])
    forks =   ([x["pos"] for x in g if x["type"] > 0])
    plt.figure(figsize=(13,13))
    ax = plt.axes(projection='3d')
    for i in range(len(g)):
        if g[i]["type"] > -1:
            ax.plot([g[g[i]["out"]]["pos"][0],g[i]["pos"][0]],[g[g[i]["out"]]["pos"][1],g[i]["pos"][1]],[g[g[i]["out"]]["pos"][2],g[i]["pos"][2]],linewidth=25*g[i]["weight"]+0.15,color="grey")
    ax.scatter([sources[i][0] for i in range(len(sources))], [sources[i][1] for i in range(len(sources))], [sources[i][2] for i in range(len(sources))], s=15, edgecolors=None,color="blue")
    ax.scatter([0], [0], [0], s=50, edgecolors=None,color="red")
    if txt:
        if len(forks) > 0:
            ax.scatter([forks[i][0] for i in range(len(forks))], [forks[i][1] for i in range(len(forks))], [forks[i][2] for i in range(len(forks))], s=15, edgecolors=None,color="orange")
    ax.grid(False)
    plt.tight_layout()
    plt.show()

def closest(i,g):
    dmin,k,xxx,yyy,zzz = float('inf'),0,0,0,0
    f = 1 - 0.25
    for j in range(len(g)):
        if j != i and g[j]["status"] == 0:
            d = distance2(g[j]["pos"],g[i]["pos"])
            w = g[i]["weight"] + g[j]["weight"]
            xx = f*(g[i]["weight"]*g[i]["pos"][0] + g[j]["weight"]*g[j]["pos"][0])/w
            yy = f*(g[i]["weight"]*g[i]["pos"][1] + g[j]["weight"]*g[j]["pos"][1])/w
            zz = f*(g[i]["weight"]*g[i]["pos"][2] + g[j]["weight"]*g[j]["pos"][2])/w
            if d < dmin:# and a > 0:
                dmin,k,xxx,yyy,zzz = d,j,xx,yy,zz
    return k,xxx,yyy,zzz

def farthest(i,g):
    dmax,k = 0,1
    for j in range(1,len(g)):
        if g[j]["status"] == 0:
            d =  distance2(g[j]["pos"],g[i]["pos"])
            if d > dmax:
                dmax,k = d,j
    return k

def check_status(g):
    s = 0
    for n in range(1,len(g)):
        s += g[n]["status"]
    if s == len(g)-1:
        return False
    else:
        return True

def optimize(g):
    while check_status(g):
        i = farthest(0,g)
        j,xx,yy,zz = closest(i,g)
        if j > 0:
            r = {"type":1,"weight":g[i]["weight"]+g[j]["weight"],"status":0,"pos":[xx,yy,zz],"out":0}
            g.append(r)
            g[i]["status"],g[j]["status"] = 1,1
            g[i]["out"],g[j]["out"] = len(g)-1,len(g)-1
        else:
            g[i]["out"],g[i]["status"] = 0,1
    return g

if __name__ == "__main__":
    g = random_graph(100)
    g = optimize(g)
    plot_graph(g,False)
