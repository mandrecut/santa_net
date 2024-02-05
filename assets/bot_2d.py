import ot
import numpy as np
import matplotlib.pyplot as plt

def random_graph(M,N):
    w = np.random.rand(M); w = w/np.sum(w); p = (2*np.random.rand(M,2)-1)*0.85
    g = [{"t":"s","w":w[m],"s":0,"p":p[m],"o":0} for m in range(M)]
    w = np.random.rand(N); w = w/np.sum(w); p = 2*np.random.rand(N,2)-1
    h = [{"t":"t","w":w[n],"s":0,"p":p[n],"o":0} for n in range(N)]
    return g + h

def closest(i,g,a):
    dmin,k,xx,yy = float('inf'),0,0,0
    for j in range(len(g)):
        if j != i and g[j]["s"] == 0:
            d = np.linalg.norm(np.array(g[j]["p"])-np.array(g[i]["p"]))
            if d < dmin:
                w = g[i]["w"] + g[j]["w"]
                x = ((1-a)*(g[i]["w"]*g[i]["p"][0]+g[j]["w"]*g[j]["p"][0])/w + a*g[0]["p"][0])
                y = ((1-a)*(g[i]["w"]*g[i]["p"][1]+g[j]["w"]*g[j]["p"][1])/w + a*g[0]["p"][1])
                c = ((g[i]["p"][0]-xx)*(g[j]["p"][0]-xx) + (g[i]["p"][1]-yy)*(g[j]["p"][1]-yy))
                dmin,k,xx,yy = d,j,x,y
    return k,xx,yy

def farthest(i,g):
    dmax,k = 0,0
    for j in range(1,len(g)):
        if g[j]["s"] == 0:
            d = np.linalg.norm(np.array(g[j]["p"])-np.array(g[i]["p"]))
            if d > dmax:
                dmax,k = d,j
    return k

def solve_bot(gg,f):
    for g in gg:
        while sum([g[n]["s"] for n in range(len(g))]) != len(g)-1:
            i = farthest(0,g)
            j,xx,yy = closest(i,g,f)
            if j > 0:
                g.append({"t":"b","w":g[i]["w"]+g[j]["w"],"s":0,"p":[xx,yy],"o":0})
                g[i]["s"],g[j]["s"],g[i]["o"],g[j]["o"] = 1,1,len(g)-1,len(g)-1
            else:
                g[i]["o"],g[i]["s"] = 0,1
    return gg

def solve_ot(g):
    x = [g[n]["p"] for n in range(len(g)) if g[n]["t"] == "s"]
    a = [g[n]["w"] for n in range(len(g)) if g[n]["t"] == "s"]
    y = [g[n]["p"] for n in range(len(g)) if g[n]["t"] == "t"]
    b = [g[n]["w"] for n in range(len(g)) if g[n]["t"] == "t"]
    G,h = ot.emd(a, b, ot.dist(np.array(x),np.array(y))),[]
    for i in range(len(x)):
        f = [{"t":"s","w":a[i],"s":0,"p":x[i],"o":0}]
        for j in range(len(y)):
            if G[i,j] > 0:
                f.append({"t":"t","w":b[j],"s":0,"p":y[j],"o":0})
        h.append(f)
    return h

def plot_graph(gg,fname):
    plt.figure(figsize=(13,13))
    for g in gg:
        s = ([x["p"] for x in g if x["t"] == "s"])
        t = ([x["p"] for x in g if x["t"] == "t"])
        for i in range(len(g)):
            if g[i]["t"] in ["t","b"]:
                plt.plot([g[g[i]["o"]]["p"][0], g[i]["p"][0]],
                         [g[g[i]["o"]]["p"][1], g[i]["p"][1]],
                         lw=100*g[i]["w"]+0.1,c="grey")
        plt.scatter([t[i][0] for i in range(len(t))],
                    [t[i][1] for i in range(len(t))],
                    s=10, ec=None, c="b")
        plt.scatter([s[i][0] for i in range(len(s))],
                    [s[i][1] for i in range(len(s))],
                    s=30, ec=None, c="r")
    plt.axis("off")
    plt.savefig(fname,bbox_inches='tight')
    plt.tight_layout(); plt.show()

if __name__ == "__main__":
    g = random_graph(50,1000)
    g = solve_ot(g)
    plot_graph(g,"fig_2d_1.pdf")
    g = solve_bot(g,0.25)
    plot_graph(g,"fig_2d_2.pdf")
