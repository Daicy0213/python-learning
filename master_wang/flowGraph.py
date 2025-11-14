# coding:utf-8
from igraph import *
import math
import pdb
import os
import sys
import random
import numpy
import traceback
import datetime
import time
import queue as Queue
import numpy as np;
import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2 ** 31, -1))
sys.setrecursionlimit(10 ** 6)


# ===========================LAB4
# ==================================================LAB4

def main2():
    global G_createPartGraphVar, G_createPartGraphVar_max, G_createPartGraphVar_total;
    script, op, fnm, klen = sys.argv
    if (op != "umflow"):
        return;
    g = Graph.Read_Pickle(fnm);
    g.vs["s"] = None;
    g.vs["dep"] = None;
    # 创建破碎边
    root = g.get_edgelist()[0][0];
    print("root is %d" % (root));
    g.vs[root]["dep"] = 0;
    partG = [-1] * (g.vcount() + 1);
    G_createPartGraphVar = 0;
    G_createPartGraphVar_total = 0;
    G_createPartGraphVar_max = 5;  # 每5个去一个

    createPartGraph(g, root, -1, partG);

    print("remove %d edges from %d edges" % (G_createPartGraphVar_total, g.ecount()));


# perc是perc%的比例去掉visting的边
# partG = 保存映射的边
G_createPartGraphVar = 0;
G_createPartGraphVar_max = 0;
G_createPartGraphVar_total = 0;


def createPartGraph(g, x, xfa, partG):
    # 用于保存去掉的边
    global G_createPartGraphVar, G_createPartGraphVar_max, G_createPartGraphVar_total;
    g.vs[x]["s"] = 1;
    dep = g.vs[x]["dep"];
    neibors = g.neighbors(x);
    for z in neibors:
        if (z == xfa):
            continue;

        G_createPartGraphVar += 1;
        if ("s" not in g.vs[z].attributes() or g.vs[z]["s"] is None):
            g.vs[z]["dep"] = dep + 1;
            createPartGraph(g, z, x, partG);
        elif (g.vs[z]["s"] == 1):
            # print("%d, max %d, total %d"%(G_createPartGraphVar,G_createPartGraphVar_max,G_createPartGraphVar_total));

            # 这里就是其他祖先
            if (G_createPartGraphVar >= G_createPartGraphVar_max):
                print("remove");
                G_createPartGraphVar -= G_createPartGraphVar_max;
                G_createPartGraphVar_total += 1;
                if (partG[x] == -1):
                    partG[x] = [z];
                else:
                    partG[x].append(z);
        else:
            G_createPartGraphVar -= 1;

    g.vs[x]["s"] = 2;


# ==========================LAB3
def readSLNDC(fpath):
    f = open(fpath);
    lines = f.readlines();
    g = Graph();
    edges = [];
    maxnid = 0;
    gf = {};
    gfkeys = set();
    print("lines : %d" % (len(lines)))
    # debug_i = 0;
    for line in lines:
        if (not line.startswith("#")):
            arr = line.split(" ");
            if (len(arr) < 2):
                continue;
            arr[0] = int(arr[0]);
            arr[1] = int(arr[1]);
            if (arr[0] == arr[1]):
                continue;

            if (arr[0] not in gfkeys):
                gfkeys.add(arr[0]);
                gf[arr[0]] = set();

            if (arr[1] not in gfkeys):
                gfkeys.add(arr[1]);
                gf[arr[1]] = set();

            if (arr[0] in gf[arr[1]] or arr[1] in gf[arr[0]]):
                continue;

            maxnid = max(maxnid, max(arr[0], arr[1]));
            # print("debug i: %d"%(debug_i));
            # debug_i = debug_i + 1;
            gf[arr[0]].add(arr[1]);
            gf[arr[1]].add(arr[0]);

            edges.append((arr[0], arr[1]));
            # edges.append((arr[1],arr[0]));
    g.add_vertices(maxnid + 1);
    g.add_edges(edges);
    print("node and edge num: %d %d" % (g.vcount(), g.ecount()))
    f.close();
    return g;


# def buildHighLevelGraph(g):


def subgraph(g):
    print("ALL CNT vertex edge %d %d" % (g.vcount(), g.ecount()));
    sgs = g.decompose(WEAK, 9999999, 2);
    maxvcount = 0;
    sub2 = None;
    for i in sgs:
        vcnt = i.vcount();
        ecnt = i.ecount();

        if (vcnt > maxvcount):
            sub2 = i;
            maxvcount = vcnt;

        # print("subgraph vertex edges %d %d"%(vcnt, ecnt));

    return sub2;


def slimcut(fpath_with_capacity):
    f = open(fpath_with_capacity);
    lines = f.readlines();
    gm = {};
    gmkeys = set();
    nid = 0;
    nkeys = set();
    ndict = {};
    ncap = {};
    edgeQueue = Queue.Queue();
    for line in lines:
        if (not line.startswith("a")):
            continue;
        eg = line.split(" ");
        eg = eg[1:];
        eg[0] = int(eg[0]);
        eg[1] = int(eg[1]);
        c = int(eg[2]);

        if (eg[0] == eg[1]):
            continue;

        if eg[0] not in nkeys:
            nkeys.add(eg[0]);
            ndict[eg[0]] = nid;
            nid += 1;

        if eg[1] not in nkeys:
            nkeys.add(eg[1]);
            ndict[eg[1]] = nid;
            nid += 1;

        nid0 = ndict[eg[0]];
        nid1 = ndict[eg[1]];

        if (nid0 > nid1):
            t = nid0;
            nid0 = nid1;
            nid1 = t;

        if (nid0 not in gmkeys):
            gm[nid0] = set();
            gmkeys.add(nid0);

        if (nid1 not in gmkeys):
            gm[nid1] = set();
            gmkeys.add(nid1);

        gm[nid0].add(nid1);
        gm[nid1].add(nid0);

        ncap[str(nid0) + "-" + str(nid1)] = c;
        ncap[str(nid1) + "-" + str(nid0)] = c;

        if (nid0 != nid1):
            edgeQueue.put((nid0, nid1));
    # print(gm[1]);
    # print(ncap["1-9"]);
    # cal each node's all edge capacity summation
    start = time.time();
    ncapsum = {}
    for tid in range(0, nid):
        # for each of tid's edge
        sum = 0;
        for tid2 in gm[tid]:
            sum += ncap[str(tid) + "-" + str(tid2)];
        ncapsum[tid] = sum;

    # newgm = {};
    # newGmKey = set();
    nodeSet = set();
    for tid in range(0, nid):
        nodeSet.add(tid);

    shrinkCount = 0;
    edgeQueue2 = Queue.Queue();

    while (edgeQueue.qsize() > 0):

        tedge = edgeQueue.get();

        tid1, tid2 = tedge;
        tid = tid1;

        if (tid1 not in nodeSet or tid2 not in nodeSet):
            continue;

        cp = ncap[str(tid1) + "-" + str(tid2)];
        if (2 * cp >= ncapsum[tid1] or 2 * cp >= ncapsum[tid2]):
            # can shrink tid with tid2
            # which means, all tid2's neigbor to tid
            # remove the edge and node
            nodeSet.remove(tid2);

            # gm[tid1].remove(tid2);
            # gm[tid2].remove(tid1);

            # shrink the edge
            shrinkCount += 1;
            # all edges of otid2 to otid1:
            for tid3 in gm[tid2]:
                if (tid3 == tid2 or tid3 == tid):
                    continue;

                # update or add edge between tid3 and tid
                if (tid3 in gm[tid]):
                    ncap[str(tid) + "-" + str(tid3)] += ncap[str(tid2) + "-" + str(tid3)];
                    # ncapsum[tid3] += 0; # no need to change
                    ncap[str(tid3) + "-" + str(tid)] = ncap[str(tid) + "-" + str(tid3)];
                    ncapsum[tid] += ncap[str(tid2) + "-" + str(tid3)] - ncap[str(tid) + "-" + str(tid2)];

                else:
                    edgeQueue.put((tid, tid3));
                    ncapsum[tid] += ncap[str(tid2) + "-" + str(tid3)] - ncap[str(tid) + "-" + str(tid2)];
                    # ncapsum[tid3] += 0; # no need to change
                    ncap[str(tid3) + "-" + str(tid)] = ncap[str(tid) + "-" + str(tid3)] = ncap[
                        str(tid2) + "-" + str(tid3)];

                # remove old edge
        else:
            edgeQueue2.put((tid1, tid2));

    # while(True):
    #     shrinkCount = 0;
    #     for tid in range(0,nid):
    #         if(ncapsum[tid] < 0):
    #             #it is incorporated into other node, all edges be with other node,
    #             continue;
    #         toupdateGmTid = gm[tid];
    #         for tid2 in gm[tid]:
    #             #untile find the node that not combined by others
    #             otid2 = tid2;
    #             while(ncapsum[tid2] < 0):
    #                 tid2 = -1 * ncapsum[tid2];    

    #             ncapsum[otid2] = -1*tid2;

    #             #NOTE: next sentence must follow above 
    #             if(tid2 == tid):
    #                 continue;

    #             cp = ncap[str(tid)+"-"+str(tid2)];
    #             if( 2* cp >= ncapsum[tid] or 2* cp >=ncapsum[tid2] ):
    #                 #can shrink tid with tid2
    #                 #which means, all tid2's neigbor to tid
    #                 shrinkCount += 1;

    #                 for tid3 in gm[tid2]:
    #                     otid3 = tid3;
    #                     while(ncapsum[tid3] < 0):
    #                         tid3 = -1 * ncapsum[tid3];    

    #                     ncapsum[otid3] = -1 * tid3;

    #                     if(tid3 == tid or tid3 == tid2):
    #                         continue;

    #                     if(tid3 in gm[tid]):
    #                         ncap[str(tid)+"-"+str(tid3)] += ncap[str(tid2)+"-"+str(tid3)];
    #                         ncap[str(tid3)+"-"+str(tid)] = ncap[str(tid)+"-"+str(tid3)];
    #                         ncapsum[tid] += ncap[str(tid2)+"-"+str(tid3)];
    #                     else:
    #                         ncapsum[tid] += ncap[str(tid2)+"-"+str(tid3)];
    #                         ncap[str(tid3)+"-"+str(tid)] = ncap[str(tid)+"-"+str(tid3)] = ncap[str(tid2)+"-"+str(tid3)];

    #                 toupdateGmTid = toupdateGmTid | gm[tid2];

    #                 if(tid in toupdateGmTid):
    #                     toupdateGmTid.remove(tid);

    #                 if(tid2 in toupdateGmTid):    
    #                     toupdateGmTid.remove(tid2);

    #                 ncapsum[tid2] = -1*tid;

    #                 #all link to tid2 ,change to tid
    #                 # for tid4 in gm[tid2]:
    #                 #     if(tid4 != tid and ncapsum[tid4] >= 0):
    #                 #         gm[tid4].remove(tid2);
    #                 #         gm[tid4].add(tid);
    #                 #         ncap[str(tid4)+"-"+str(tid1)] = ncap[str(tid)+"-"+str(tid4)] = ncap[str(tid)+"-"+str(tid2)];

    #         gm[tid] = toupdateGmTid;

    # reproduce the graph and output
    end = time.time() - start;
    print("ITER shrinkcount %d" % (shrinkCount))
    newNid = 0;
    newMap = {};
    newMapKeys = set();
    edges = 0;

    while (edgeQueue2.qsize() > 0):
        tid, tid2 = edgeQueue2.get();
        if (tid not in newMapKeys):
            newMapKeys.add(tid);
            newMap[tid] = newNid;
            newNid += 1;

        if (tid2 not in newMapKeys):
            newMapKeys.add(tid2);
            newMap[tid2] = newNid;
            newNid += 1;

        print("a %d %d %d" % (newMap[tid], newMap[tid2], ncap[str(tid) + "-" + str(tid2)]));
        print("a %d %d %d" % (newMap[tid2], newMap[tid], ncap[str(tid) + "-" + str(tid2)]));
        edges += 2;

    print("p max %d %d" % (newNid, edges));
    print("time %f" % (end));


def outputUndirected(fpath):
    f = open(fpath);
    lines = f.readlines();
    gm = {};
    gmkeys = set();
    nid = 0;
    nkeys = set();
    ndict = {};
    for line in lines:
        if (line.startswith("#")):
            continue;
        eg = line.split("\t");
        eg[0] = int(eg[0]);
        eg[1] = int(eg[1]);

        if (eg[0] == eg[1]):
            continue;

        if eg[0] not in nkeys:
            nkeys.add(eg[0]);
            ndict[eg[0]] = nid;
            nid += 1;

        if eg[1] not in nkeys:
            nkeys.add(eg[1]);
            ndict[eg[1]] = nid;
            nid += 1;

        nid0 = ndict[eg[0]];
        nid1 = ndict[eg[1]];

        if (nid0 > nid1):
            t = nid0;
            nid0 = nid1;
            nid1 = t;

        if (nid0 not in gmkeys):
            gm[nid0] = set();
            gmkeys.add(nid0);

        gm[nid0].add(nid1);

    edges = 0;
    for k in gmkeys:
        for v in gm[k]:
            print("%d %d" % (k, v));
            print("%d %d" % (v, k));
            edges += 2;
    print("p max %d %d" % (nid, edges));


# remove cut and find remaining component
def anaCut(g):
    cuts = g.cut_vertices();
    print("ana cuts");
    print("number of cuts: %d" % (len(cuts)));
    g.delete_vertices(cuts);
    sgs2 = g.decompose(WEAK, 9999999, 2);
    set1 = set();
    for k in sgs2:
        set1.add(k.vcount())
        print("subgraph edges %d %d" % (k.vcount(), k.ecount()));

    for vc in set1:
        print("vcount %d" % (vc));


def searchCut(g, x):
    g.vs[x]["low"] = sys.maxint;
    g.vs[x]["s"] = 1;  # visiting, 2 is visited
    for z in g.neighbors(x):
        # print("z is %d, with property %s"%(z,g.vs[z].attributes()));
        if ("dep" in g.vs[z].attributes() and not g.vs[z]["dep"] is None and g.vs[z]["dep"] == g.vs[x]["dep"] - 1):
            continue;
        if ("s" not in g.vs[z].attributes() or g.vs[z]["s"] is None):
            g.vs[z]["dep"] = g.vs[x]["dep"] + 1;
            searchCut(g, z);

            # print("AFTER: z is %d, with property %s"%(z,g.vs[z].attributes()));
        if (g.vs[z]["s"] == 2):
            t = g.vs[z]["low"];
        elif (g.vs[z]["s"] == 1):
            t = g.vs[z]["dep"];
        else:
            raise Exception("!!!ERRRRRRRRRRRRRRR: state is %d" % (g.vs[z]["s"]));

        if (g.vs[x]["low"] > t):
            g.vs[x]["low"] = t;

        if (g.vs[z]["s"] == 2 and g.vs[z]["low"] >= g.vs[x]["dep"]):
            g.vs[x]["c"] = 1;
    g.vs[x]["s"] = 2;


def buildHighLevel(g, o):
    hg = Graph();
    cuts = g.cut_vertices();
    for n in cuts:
        g.vs[n]["c"] = 1;
    q1 = Queue.Queue();
    q2 = Queue.Queue();
    q1.put(o);

    hg.add_vertex();
    O = hg.vcount() - 1;
    hg.vs[O]["cn"] = o;
    hg.vs[O]["hdep"] = g.vs[o]["dep"];
    g.vs[o]["hn"] = O;

    # q1 q2 has orginal node id inside
    hg_edges = [];
    while (not q1.empty()):
        x = q1.get();
        q2.put(x)
        g.vs[x]["v"] = 1;
        X = g.vs[x]["hn"];

        hg.vs[X]["gc"] = 0;  # count of node belong to the X
        # print("get hg node %d, cn %d "%(X,x));
        while (not q2.empty()):
            y = q2.get();
            for z in g.neighbors(y):
                if ("v" in g.vs[z].attributes() and g.vs[z]["v"] == 1):
                    continue;
                if (g.vs[z]["low"] < g.vs[x]["dep"]):
                    # before x
                    continue;

                if (g.vs[y]["c"] == 1 and y != x and g.vs[z]["low"] >= g.vs[y]["dep"]):
                    # before x, but after y
                    continue;

                    # add it
                g.vs[z]["v"] = 1;
                g.vs[z]["lg"] = X;
                hg.vs[X]["gc"] = hg.vs[X]["gc"] + 1;
                q2.put(z);

                # else:
                #     if("lg" not in g.vs[z].attributes() or g.vs[z]["lg"] is None ):
                #         raise Exception("z %d with low %d < x %d dep %d, but no lg,%s %s"%(z,g.vs[z]["low"],x,g.vs[x]["dep"],g.vs[z].attributes(),g.vs[x].attributes()));        

                # if z is cut, update high-level and add to q1
                if ("c" in g.vs[z].attributes() and g.vs[z]["c"] == 1):
                    hg.add_vertex();
                    Z = hg.vcount() - 1;
                    hg.vs[Z]["cn"] = z;
                    g.vs[z]["hn"] = Z;
                    hg.vs[Z]["up"] = X;
                    hg_edges.append((Z, X));
                    hg_edges.append((X, Z));
                    hg.vs[Z]["hdep"] = g.vs[z]["dep"];
                    q1.put(z);

    hg.add_edges(hg_edges);
    return hg;


def checkPrintG(g):
    total = 0;
    for i in range(g.vcount()):
        if (g.vs[i]["c"] == 1):
            total += 1;
        if ("lg" not in g.vs[i].attributes() or g.vs[i]["lg"] is None):
            # print("%d lg is None, %s "%(i,g.vs[i].attributes()));
            if (i != 0):
                raise Exception("%d lg is None" % (i));
    print("lg has %d cuts" % (total));
    return total;


def findPrintPath(hg, s, t):
    path = []
    U = g.vs[s]["lg"];
    V = g.vs[t]["lg"];
    # u = hg.vs[U]["cn"];
    # v = hg.vs[V]["cn"];

    while (1 == 1):
        if (U == V):
            path.append(hg.vs[U]["gc"]);
            break;
        elif (hg.vs[U]["hdep"] >= hg.vs[V]["hdep"]):
            path.append(hg.vs[U]["gc"]);
            U = hg.vs[U]["up"];
        else:
            path.append(hg.vs[V]["gc"]);
            V = hg.vs[V]["up"];

    print("PATH\t%s" % ("\t".join(map(str, path))));


def printHG(hg):
    print("h_mapreduce\t%d\t%d" % (hg.vcount(), hg.ecount()));
    if (hg.vcount() * 2 - 2 != hg.ecount()):
        raise Exception("hg node %d * 2 -2 != edge %d" % (hg.vcount(), hg.ecount()));
    hmap = {};
    for i in range(hg.vcount()):
        gc = hg.vs[i]["gc"];
        if (gc not in hmap):
            hmap[gc] = 1;
        else:
            hmap[gc] = hmap[gc] + 1;
        # print("%d\t%d\t%d"%(i,hg.vs[i]["gc"],hg.vs[i]["cn"]));
    total = 0;
    skeys = hmap.keys();
    skeys.sort(reverse=True);
    prev5 = [];
    for gc in skeys:
        total = total + hmap[gc] * gc;
        print("%d\t%d" % (gc, hmap[gc]));
        for i in range(0, hmap[gc]):
            prev5.append(gc);
    print("total is %d" % (total));
    print("PREV5\t%s" % ("\t".join(map(str, prev5[0:4]))));
    vcnt = hg.vcount();

    arr_s = np.random.randint(0, vcnt, 100);
    arr_t = np.random.randint(0, vcnt, 100);
    # for i in range(0,100):
    #     findPrintPath(hg,arr_s[i],arr_t[i]);

    return total;


def maximalClique(g):
    tim1 = time.time()
    # mc = g.maximal_cliques();
    mc = g.community_infomap();
    print("time %d ms" % (time.time() * 1000 - tim1 * 1000));
    gset = set();
    subnode = 0;  # number of subed nodes
    gs = mc;  # .as_clustering();
    for ig in gs:
        if (len(ig) > 2):
            print(ig);
            subnode += len(ig) - 1;
    print("subnode %d" % (subnode));
    # tim1 = time.time();
    # g.cut_vertices();
    # print("cut time %d"%(time.time()-tim1));
    # for i in range(0,len(mc)):
    #     print("######%d"%(i));
    #     print(mc[i]);
    # #     if(len(mc[i])<=2):
    #         continue;
    #     isProc = True;
    #     for n in mc[i]:
    #         if n in gset:
    #             isProc = False;
    #             break;
    #     if isProc:
    #         subnode += len(mc[i]) - 1;
    #         print mc[i];
    #         for n in mc[i]:
    #             gset.add(n);
    # print("subnodes: %d"%(subnode));


# gen connected undirected graph


def weightShuffle(ids, ws):
    # 根据权重返回ids
    if (len(ids) != len(ws)):
        print("ERRR in weightShuffle, len not equal, exit!");
        exit(1);
    # wsum = sum(ws);
    # cu_ws = range(len(ws));
    arr = [];
    for a in range(len(ids)):
        arr += [ids[a] for x in range(ws[a])];

    retarr = [];
    for i in range(len(ids)):
        tid = random.choice(arr);
        retarr.append(tid);
        while (tid in arr):
            arr.remove(tid);

    return retarr;


# =================================================LAB3
def findLargestBCC(g, f):
    cover = g.biconnected_components();
    maxsz = 0;
    maxi = None;
    for i in range(len(cover)):
        if (len(cover[i]) > maxsz):
            maxi = i;
            maxsz = len(cover[i]);

    maxsg = cover.subgraph(maxi);
    print("largest: vcount %d, ecount %d, cut_count %d" % (maxsg.vcount(), maxsg.ecount(), len(maxsg.cut_vertices())))
    # print(dir(maxsg));
    maxsg.write_pickle(f);


gDepMap = dict();
gCandidate = {};
gklen = 10;
gktreecount = 50;
gtotal = 100;

"""
每种遍历顺序下，每个节点对应一个边割长度，子树和外部的边割大小!
    对任意两个节点，找他们之间相隔的最小的
	比如对s,t
		对s,可以向上溯源，找最小的x
		对t,也可以向上溯源，找最小的x
	    复杂度远小于O(M)
    还可以优化：
        比如[1]
            (1)s和t迅速知道共享祖先
            (2)再迅速知道到共同祖先路径中最小的是多少
        比如[2]
    问题：
        (1)x的不同子节点到相同的祖先有无可能？
            也可能，肯定不同边，还是可以单独算的呀！
"""


# def OLD_markECutValue_Stable(g,x):
#     g.vs[x]["s"] = 1; #visiting, 2 is visited
#     g.vs[x]['cv'] = 0; #cut value, each edge is 1
#     tc = 1;
#     # if(isDebug):
#     #     if(dep %1000 == 0):
#     #         print("d %d"%(dep));
#     dep = g.vs[x]["dep"];

#     #ver1:
#     neibors = g.neighbors(x);
#     random.shuffle(neibors);

#     #ver2: weight random, get edge weight
#     # neibors = g.neighbors(x);
#     # # print("before");
#     # # print(neibors);
#     # ws = [];
#     # for z in neibors:
#     #     ws.append(g.es[g.get_eid(x,z)]["capacity"]);

#     # neibors = weightShuffle(neibors,ws);

#     #ver3: shuffle but excluding minimal value


#     # print("after");
#     # print(neibors);
#     cap = 0;
#     for z in neibors:
#         #print("z is %d, with property %s"%(z,g.vs[z].attributes()));
#         # if("dep" in g.vs[z].attributes() and not g.vs[z]["dep"] is None and g.vs[z]["dep"] == g.vs[x]["dep"] -1 ):
#         #     g.vs[x]['cv'] = g.vs[x]['cv'] + 1; 
#         #     g.vs[z]['cv'] = g.vs[z]['cv'] - 1; 
#         #     continue;

#         if(g.vs[z]["s"] == 1):
#             cap = g.es[g.get_eid(x,z)]["capacity"];
#             #cap = g.es["capacity"][g.get_eid(x,z)];
#             g.vs[x]['cv'] = g.vs[x]['cv'] + cap; 
#             g.vs[z]['cv'] = g.vs[z]['cv'] - cap; 


#         elif("s" not in g.vs[z].attributes() or (g.vs[z]["s"] !=1 and g.vs[z]["s"] !=2)):
#             g.vs[z]["fa"] = x;
#             # if(g.vs[z]["fa"] is None):
#             #     print("FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKK fa is None");
#             g.vs[z]["dep"]  = dep + 1;
#             markECutValue(g,z);
#             g.vs[x]['cv'] = g.vs[x]['cv'] + g.vs[z]['cv']; 


#     g.vs[x]["s"] = 2;
#     #don't add father node of x
#     #ks.add(dep-1);


def markECutValue(g, x):
    g.vs[x]["s"] = 1;  # visiting, 2 is visited
    g.vs[x]['cv'] = 0;  # cut value, each edge is 1
    tc = 1;
    dep = g.vs[x]["dep"];

    # ver1:
    neibors = g.neighbors(x);
    random.shuffle(neibors);

    # ver2: weight random, get edge weight
    # neibors = g.neighbors(x);
    # # print("before");
    # # print(neibors);
    # ws = [];
    # for z in neibors:
    #     wt = int(g.es[g.get_eid(x,z)]["capacity"]);
    #     if wt < 1:
    #         wt = 1;
    #     ws.append(wt);

    # neibors = weightShuffle(neibors,ws);
    # neibors.reverse();

    # ver3: 总是按最小边长
    # neibors = g.neighbors(x);
    # neibors = sorted(neibors, key=lambda z: -1 * int(g.es[g.get_eid(x,z)]["capacity"]));

    cap = 0;
    for z in neibors:

        if (g.vs[z]["s"] == 1):
            # cap = g.es[g.get_eid(x,z)]["capacity"];
            # cap = g.es["capacity"][g.get_eid(x,z)];
            g.vs[x]['cv'] = g.vs[x]['cv'] + 1;
            g.vs[z]['cv'] = g.vs[z]['cv'] - 1;


        elif ("s" not in g.vs[z].attributes() or (g.vs[z]["s"] != 1 and g.vs[z]["s"] != 2)):
            g.vs[z]["fa"] = x;
            # if(g.vs[z]["fa"] is None):
            #     print("FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKK fa is None");
            g.vs[z]["dep"] = dep + 1;
            markECutValue(g, z);
            g.vs[x]['cv'] = g.vs[x]['cv'] + g.vs[z]['cv'];

    g.vs[x]["s"] = 2;
    # don't add father node of x
    # ks.add(dep-1);


# 标记最小值的同时，支持两种模式：(1)随机但更新每边的出现次数ECNT (2)按出现次数ECNT随机，且不更新次数ECNT
# dg2用于存储对应值
def markECutValue_ver2(g, x, dg, mode):
    g.vs[x]["s"] = 1;  # visiting, 2 is visited
    g.vs[x]['cv'] = 0;  # cut value, each edge is 1
    tc = 1;
    dep = g.vs[x]["dep"];

    # ver1:
    neibors = g.neighbors(x);

    if mode == 1:
        # 按容量随机
        # random.shuffle(neibors);
        neibors = sorted(neibors,
                         key=lambda z, ig=g, ox=x: -1 * random.random() * int(ig.es[ig.get_eid(x, z)]["capacity"]))
    elif mode == 2:
        # 按出现次数随机，次数越大的越倾向靠后
        # 这里复杂度可以比常规排序低，先从确定数值位置开始搜索，复杂度大大降低，接近O(D)
        # random.shuffle(neibors)
        # neibors = sorted(neibors,key=lambda z,ig=g,og=dg,ox=x: random.random()*og[ox,z]/ig.es[ig.get_eid(x,z)]["capacity"])
        neibors = sorted(neibors, key=lambda z, ig=g, og=dg, ox=x: random.random() * og[ox, z])

    # ver2: weight random, get edge weight
    # neibors = g.neighbors(x);
    # # print("before");
    # # print(neibors);
    # ws = [];
    # for z in neibors:
    #     wt = int(g.es[g.get_eid(x,z)]["capacity"]);
    #     if wt < 1:
    #         wt = 1;
    #     ws.append(wt);

    # neibors = weightShuffle(neibors,ws);
    # neibors.reverse();

    # ver3: 总是按最小边长
    # neibors = g.neighbors(x);
    # neibors = sorted(neibors, key=lambda z: -1 * int(g.es[g.get_eid(x,z)]["capacity"]));

    cap = 0;
    for z in neibors:

        if (g.vs[z]["s"] == 1):
            cap = g.es[g.get_eid(x, z)]["capacity"];
            # cap = g.es["capacity"][g.get_eid(x,z)];
            g.vs[x]['cv'] = g.vs[x]['cv'] + cap;
            g.vs[z]['cv'] = g.vs[z]['cv'] - cap;
            if (mode == 1 and g.vs[z]["dep"] != g.vs[x]["dep"] - 1):
                dg[x, z] += 1
                dg[z, x] += 1




        elif ("s" not in g.vs[z].attributes() or (g.vs[z]["s"] != 1 and g.vs[z]["s"] != 2)):
            g.vs[z]["fa"] = x;
            # if(g.vs[z]["fa"] is None):
            #     print("FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKK fa is None");
            g.vs[z]["dep"] = dep + 1;
            markECutValue_ver2(g, z, dg, mode);
            g.vs[x]['cv'] = g.vs[x]['cv'] + g.vs[z]['cv'];

    g.vs[x]["s"] = 2;


#################################LAB5

# no zero nodes

def output_direct(g):
    ecnt = 0;
    arr = [];
    for i in range(g.vcount()):
        for j in g.neighbors(i):
            if (j < i):
                arr.append((j, i));

    g.add_edges(arr);

    caps = range(g.ecount());
    for a in range(g.ecount()):
        caps[a] = 1 + int(random.random() * 1000);

    g.es["capacity"] = caps;

    for i in range(g.vcount()):
        for j in set(g.neighbors(i)):
            if (j != i):
                print("a %d %d %d" % ((i + 1), (j + 1), g.es[g.get_eid(i, j)]["capacity"]));
                ecnt += 1;

    print("p max %d %d" % (g.vcount(), ecnt));


g_addEmptyEdge = True;


def output_undirect(g):
    ecnt = 0;
    arr = [];
    for i in range(g.vcount()):
        for j in g.neighbors(i):
            if (j < i):
                arr.append((j, i));

    g.add_edges(arr);

    caps = list(range(g.ecount()));
    for a in range(g.ecount()):
        caps[a] = 1 + int(random.random() * 1000);

    g.es["capacity"] = caps;

    # for i in range(g.vcount()):
    #     print("n %d %d"%(i,len(set(g.neighbors(i)))))

    print("-----------------输出undirect");

    for i in range(g.vcount()):
        gnset = set(g.neighbors(i));
        for j in gnset:
            if (j > i):
                print("a %d %d %d" % ((i + 1), (j + 1), g.es[g.get_eid(i, j)]["capacity"]));
                ecnt += 1;

    print("p max %d %d" % (g.vcount(), ecnt));

    lastecnt = ecnt;

    print("-----------------输出direct")

    for i in range(g.vcount()):
        gnset = set(g.neighbors(i));
        for j in gnset:
            if (j != i):
                print("a %d %d %d" % ((i + 1), (j + 1), g.es[g.get_eid(i, j)]["capacity"]));
                ecnt += 1;

    print("p max %d %d" % (g.vcount(), ecnt - lastecnt));


def output_undirect_ver_special(g):
    ecnt = 0;
    arr = [];
    for i in range(g.vcount()):
        for j in g.neighbors(i):
            if (j < i):
                arr.append((j, i));

    g.add_edges(arr);

    caps = list(range(g.ecount()));
    for a in range(g.ecount()):
        caps[a] = 1 + int(random.random() * 1000);

    g.es["capacity"] = caps;

    # for i in range(g.vcount()):
    #     print("n %d %d"%(i,len(set(g.neighbors(i)))))

    print("-----------------输出undirect");

    zeroNeibors = {};
    zeroCountDirect = {};  # 记录每个点的输出的有向边的数量
    for i in range(g.vcount()):
        gnset = set(g.neighbors(i));
        for j in gnset:
            if (j != i):
                print("a %d %d %d" % ((i + 1), (j + 1), g.es[g.get_eid(i, j)]["capacity"]));
                ecnt += 1;
        if (g_addEmptyEdge):
            # 把不在neighbors里面的加进去
            zeroNeibors[i] = set();
            cnt = 4 * len(g.neighbors(i));
            while (len(zeroNeibors[i]) <= cnt):
                toAddJ = int(random.random() * g.vcount())
                if (toAddJ != i and (toAddJ not in gnset)):
                    zeroNeibors[i].add(toAddJ);  # 因为undirect是给hprf用，不需要0容量
                    # print("a %d %d %d"%((i+1),(toAddJ+1),0));
                    # ecnt += 1;

    print("p max %d %d" % (g.vcount(), ecnt));

    lastecnt = ecnt;

    print("-----------------输出direct")

    for i in range(g.vcount()):
        gnset = set(g.neighbors(i));
        for j in gnset:
            if (j > i):
                cap = g.es[g.get_eid(i, j)]["capacity"];
                # if( random.random() < 0.8):
                #     cap = 0; #80%容量为空
                print("a %d %d %d" % ((i + 1), (j + 1), cap));
                ecnt += 1;
        if (g_addEmptyEdge):
            # 这里生成0容量边,按比例，这里固定是4倍比例，即2个邻居，这里还要添加8个邻居且容量是0
            for j in zeroNeibors[i]:
                if (j > i):
                    print("a %d %d %d" % ((i + 1), (j + 1), 0));
                    ecnt += 1;

    print("p max %d %d" % (g.vcount(), ecnt - lastecnt));


# ----------------------------------------------- depth first version
def mainLab5():
    global globalg, lastfnm;

    script, gtype, op, is_debug, fnm, klen, edge_p, perc = sys.argv
    klen = int(klen);
    edge_p = int(edge_p);
    if (op == "gen_random_erdos_graph"):  # erdos
        randomSaveGrph(klen, int(klen * edge_p));
        sys.exit(0);

    if (op == "gen_random_scalefree_graph"):
        randomScaleFreeGraph(klen, int(klen * edge_p), 1);
        sys.exit(0);

    if (op == "gen_random_unitdisk_graph"):
        perc = float(perc);
        print("perc is %lf" % (perc));
        randomUnitDiskGraph(klen, perc);
        sys.exit(0);

    if (op == "gen_random_grid_graph"):
        genGridGraph(int(klen ** 0.5));
        sys.exit(0);

    if (op == "gen_random_full_graph"):
        genFullGraph(int(klen));
        sys.exit(0);

    perc = int(perc)
    dg = reloadSameGraphWithSameCaps(gtype, fnm, None);
    globalg = None;
    lastfnm = "";
    g = reloadSameGraphWithSameCaps(gtype, fnm, None);

    if (not g.is_connected()):
        print("Err: graph is not connected");
        exit(1);

    elif (op == "output_undirect"):
        output_undirect(g);
    elif (op == "output_direct"):
        output_direct(g);
    elif (op == "du_markvcut"):
        gs = [];
        klen = int(klen);
        if (klen < 0):
            tn = g.vcount();
            tm = g.ecount();
            klen = int(min(pow(tn, 2.0 / 3), pow(tm, 1.0 / 2)) / 2);
            print(("k is chaged to %d") % (klen));
        dg.es["weight"] = 1;
        # perc = 50; #20% in mode 1 80% in mode 2
        klen_small = int(klen * perc / 100);
        print("klen and small %d %d" % (klen, klen_small));
        cycle_cnt = 0
        while (cycle_cnt < 50):
            cycle_cnt += 1
            for i in range(klen):
                egs = g.get_edgelist();
                root = egs[random.randint(0, len(egs) - 1)][0];
                # print("nodes:");
                # print(g.get_edgelist());   
                if (root is None):
                    print("!!!ERRRRRRRRR: root is None, set to 0");
                    root = 0;
                print("iter%d: root is %d, vcnt %d ecnt %d" % (i, root, g.vcount(), g.ecount()));
                g.vs[root]["dep"] = 0;
                mode = 1;
                if (i >= klen_small):
                    mode = 2;
                markECutValue_ver2(g, root, dg, mode);
                hint = "";
                # print("markECutValue finished for "+str(i));
                deps = zeros(g.vcount());
                cvs = zeros(g.vcount());
                fas = zeros(g.vcount());
                for e in g.get_edgelist():
                    for n in e:
                        deps[n] = g.vs[n]["dep"];
                        cvs[n] = g.vs[n]["cv"];
                        fas[n] = g.vs[n]["fa"];
                        if (fas[n] is None):
                            if (n == root):
                                fas[n] = -1;
                            else:
                                print("FFFFFFFFFFFFFFFFFFFFnode %d fa is None" % (n));
                gs.append((deps, cvs, fas, root));

                g = reloadSameGraphWithSameCaps(gtype, fnm, g.es["capacity"]);

            # find random s,t
            egs = g.get_edgelist();
            vlen = len(egs);
            difftm = 0;
            difftotal = 0;
            maxtotal = 0;
            ourtotal = 0;
            theirtotal = 0;
            iter_num = int(edge_p);
            avg_stlen_all = 0;
            for iter in range(iter_num):
                s = egs[random.randint(0, vlen - 1)][0];
                t = egs[random.randint(0, vlen - 1)][0];
                if (s == t):
                    print("s==t, exit");
                    iter -= 1;
                    continue;

                if (s is None or t is None):
                    print("!!!!!!!!!!!!!s or t is None");
                    continue;

                print("cal maxflow for %d <-> %d" % (s, t));

                # starttime = datetime.datetime.now()
                (m1, ourtm, avg_stlen) = findMaxflowMulti(g, gs, s, t);
                avg_stlen_all = avg_stlen_all + avg_stlen * 1.0 / iter_num;
                # ourtm = datetime.datetime.now() -starttime;
                ourtotal = ourtotal + ourtm;

                starttime = datetime.datetime.now()
                m2 = g.maxflow(s, t, "capacity");
                # m2 = g.maxflow(s,t);
                theirtm = datetime.datetime.now() - starttime;
                theirtotal = theirtotal + theirtm.microseconds;

                difftotal = difftotal + m1 - m2.value;
                maxtotal = maxtotal + m2.value;
                print("caliter %d m1 m2: %d %d" % (iter, m1, m2.value));
                if (m1 != m2.value):
                    difftm = difftm + 1;

                if (m1 < m2.value):
                    print("fuckXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX %d %d" % (m1, m2.value));

            bratio = 0;
            if (difftm > 0):
                bratio = (difftotal / difftm) / (maxtotal / iter_num);
            print(
                "avgst: %f, difftm: %d  /%d, vratio_when_diff %f, difftotal %d, maxtotal: %d, time our v.s. their: %d(%d) %d  | %s" % (
                    avg_stlen_all, difftm, iter_num, bratio, difftotal, maxtotal, ourtotal / 30, ourtotal, theirtotal,
                    fnm));

            # print("maxflow:");
            # print(m1);
            # print(m2.value);
            # print(len(m2.flow));
            # print(m2.cut);
            # # print(m2.partition);
            # print(m2.es);
            print("klen and small %d %d" % (klen, klen_small));
            prom = "y";  # input(("contineu another %d preprocess and cal? (y/n)")%(klen));
            # print(dg.es["weight"]);
            if (prom == "y"):
                print("go on!");
            else:
                print("exit");
                exit();
    else:
        print("not supported oper, exit");
        exit();


def findMaxflowMulti(g, gs, s, t):
    m1 = sys.maxint;
    intvtotal = 0;
    avg_iternum = 0;
    glen = len(gs);
    for i in range(glen):
        # s,t = 2850 11000
        igs = gs[i];
        (tmpm, intv, iter_num) = findMaxflow(igs, s, t);
        # (tmpm,intv,iter_num) = opFindMaxflow(g,igs,s,t);
        avg_iternum = avg_iternum + iter_num * 1.0 / glen;
        intvtotal = intvtotal + intv;
        if (m1 > tmpm):
            m1 = tmpm;
    return (m1, intvtotal, avg_iternum);


def findMaxflow(g, s, t):
    # print("s t is %d %d"%(s,t));
    minfv = sys.maxint;
    deps = g[0];
    cvs = g[1];
    fas = g[2];
    root = g[3];

    # print(deps);
    # print(fas);
    wter_num = 0;
    starttime = datetime.datetime.now()
    # print("deps");
    # print(deps);
    while (True):
        wter_num = wter_num + 1;
        if (s < 0 or t < 0):
            print("!EEEEEEEEEEEEEEEEEEEEERRRRRR, backtrace to root's uppper");
            exit(1);
        if (deps[s] > deps[t]):
            if (minfv > cvs[s]):
                minfv = cvs[s];
            s = fas[s];
        elif (deps[s] < deps[t]):
            if (minfv > cvs[t]):
                minfv = cvs[t];
            t = fas[t];
        else:
            if (s == t):
                break;
            else:
                if (minfv > cvs[s]):
                    minfv = cvs[s];
                if (minfv > cvs[t]):
                    minfv = cvs[t];
                s = fas[s];
                t = fas[t];
                wter_num = wter_num + 1;  # more 1 iters

    intv = datetime.datetime.now() - starttime;

    return (minfv, intv.microseconds, wter_num);


# 更优化的算法，有望能有更少的遍数
def opFindMaxflow(g, gs, os, ot):
    # print("s t is %d %d"%(s,t));
    s = os;
    t = ot;
    minfv = sys.maxint;
    deps = gs[0];
    cvs = gs[1];
    fas = gs[2];

    # for i in range(len(deps)):
    #     print("%d dep %d"%(i,deps[i]));

    # print(deps);
    # print(fas);
    wter_num = 0;
    starttime = datetime.datetime.now()
    # print("deps");
    # print(deps);
    # 构建深度到节点id的链
    # 构建深度到节点dep的链
    cseqt = [];
    cseqs = [];
    while (True):
        wter_num = wter_num + 1;
        if (s < 0 or t < 0):
            print("!EEEEEEEEEEEEEEEEEEEEERRRRRR, backtrace to root's uppper");
            exit(1);
        if (deps[s] > deps[t]):
            cseqs.append(s);
            s = fas[s];
        elif (deps[s] < deps[t]):
            cseqt.append(t);
            t = fas[t];
        else:
            if (s == t):
                break;
            else:
                cseqs.append(s);
                cseqt.append(t);
                s = fas[s];
                t = fas[t];
                wter_num = wter_num + 1;  # more 1 iters

    # 现在拿到common
    com = s;
    bothseqs = (cseqs, cseqt);
    globalMin = [sys.maxint];
    for nseq in bothseqs:
        # check the seq v to com
        # init dep chain
        if (len(nseq) <= 0):
            continue;

        nseq.append(com);

        # print("len %d nseq %s "%(len(nseq),str(nseq)));

        dep2cvs = [cvs[x] for x in nseq];
        deph = deps[nseq[0]];
        id2AddCut = [0 for i in range(g.vcount())];
        globalMin[0] = min(globalMin[0], min(dep2cvs[0:len(dep2cvs) - 1]));
        # minCutArr = [sys.maxint for i in range(g.vcount())];
        # dep to cv:  dseq[a-deps[x]];
        globalgans = [-1];  # 保存当前z所有递归访问中能访问到的最靠前的祖先的dep
        for i in range(len(nseq) - 1):
            x = nseq[i];
            # print("i %d x %d (dep %d), gans: %s"%(i,x,deps[x],globalgans));
            for z in g.neighbors(x):
                # print("z %d (dep %d)"%(z,deps[z]));    
                if (i > 0 and z == nseq[i - 1]):  # the child in the chain
                    # print("continue: child in the chain")
                    continue;
                if (deps[z] == deps[x] + 1):  # child not in the chain
                    # print("proc: child not in the chain")
                    # print("proc for: x %d(%d) , z %d(%d) "%(x,deps[x],z,deps[z]));
                    dep2decr = [0 for a in range(len(dep2cvs))];
                    opMaxflowProcTree(globalMin, dep2cvs, id2AddCut, deps, x, z, deps[com], deph, dep2decr, z);
            # 对2个链中的一个已处理完毕，现在要更新并获取最小值

        # globalMin[0] = min(globalMin[0],min(dep2cvs[0:len(dep2cvs)-1]));
        # """
        # gnum = 0;
        # # print (dep2cvs);
        # lnseq = len(nseq);
        # for i in range(lnseq):
        #     depIdx = lnseq - 1 -i;
        #     dep2cvs[depIdx] -= gnum;
        #     gnum += dep2decr[depIdx];
        # # """
        # tmpMin = min(dep2cvs[0:len(dep2cvs)-1]);
        # if(tmpMin < minfv):
        #     minfv = tmpMin;
        # print (dep2cvs);
    # print("globalMin %s"%(str(globalMin)));
    # print("id2AddCut %s"%(str(id2AddCut)));    
    # print("dep2cvs %s"%(str(dep2cvs)));

    intv = datetime.datetime.now() - starttime;

    return (globalMin[0], intv.microseconds, wter_num);


"""
		当前链上节点x (即启动这个深度调用的x)
		z
		全局深度最小节点 ans的深度 gans (初始化为INF)
		当前遍历节点v
"""


def opMaxflowProcTree(globalMin, dep2cvs, id2AddCut, deps, x, z, dcom, deph, dep2decr, v):
    dx = deps[x];
    dvp1 = deps[v] + 1;
    dxidx = deph - deps[x];
    dv = deps[v];
    # innerCut = id2AddCut[v]; #v和v之前x后的连接树，包括v的父亲的，这些就是v的代价去掉v后cut的增加值
    # dcom = deph-len(dep2decr)+1;
    # if(dcom != dcom2):
    #     print("ERRRRRRRRRRRRRRRRRRRRRRRR dcom != dcom2");
    #     exit;

    decrcnt = 0;
    addCntBefore = id2AddCut[v];
    # print("call opMaxflowProcTree x %d(%d) z %d(%d)"%(x,deps[x],z,deps[z]));
    for w in g.neighbors(v):
        dw = deps[w];
        if (dw == dvp1):
            dep2decr2 = [0 for a in range(len(dep2decr))];
            opMaxflowProcTree(globalMin, dep2cvs, id2AddCut, deps, x, z, dcom, deph, dep2decr2, w);
            id2AddCut[v] += id2AddCut[w];
            for i in range(len(dep2decr)):
                dep2decr[i] += dep2decr2[i];
            continue;
        elif (dw >= dx):
            # v在x后的祖先，包括直接父亲
            if (dw < dv):
                id2AddCut[w] -= 1;  # 祖先w的代价减少一些，因为递增上去的数值提前预支了
                id2AddCut[v] += 1;  # 即去掉v的代价增加了

            continue;

        decrcnt += 1;
        # print("DEBUG: x %d(%d) , z %d(%d) remove edge with %d(%d)"%(x,deps[x],z,deps[z],w,deps[w]));
        # 现在w是在x之前的节点了
        deptmpidx = deph - max(dw, dcom);
        if (deptmpidx >= len(dep2decr) or deptmpidx < 0):
            print(("ERRRRRRRRRRRRRR: dvp1 %d dx %d dw %d dcom %d deph %d len %d") % (
                dvp1, dx, dw, dcom, deph, len(dep2decr)));
            sys.exit(1);
        if (deptmpidx <= dxidx):
            print("EEEEEEEEEEEEEEEEEEEEEErr idx error: %d %d" % (deptmpidx, dxidx));

        dep2decr[deptmpidx] += 1;
        dep2decr[dxidx] -= 1;

        # if(ganarr[0] < 0): #第一个遍历到到祖先的边
        #     # dep2decr[deptmpidx] -=1;
        #     # dep2decr[dxidx] +=1;
        #     #啥也不做，只更新gans
        #     #因为去掉这个边，不会对(deptmpidx,dxidx]的dv有影响
        #     ganarr[0] = deptmpidx;
        # elif(deptmpidx == ganarr[0]):
        #     #这个就是迄今最远的，上次肯定背过锅了，这次可以了
        #     #下面相当于(deptmpidx, dxidx] 所有cv 减1，相当于去掉这个边和之前的边，这个区间所有cv都减少1
        #     dep2decr[deptmpidx] +=1;
        #     dep2decr[dxidx] -= 1;
        # elif(deptmpidx > ganarr[0]): #此时idx > 说明是dep小于，要换锅了
        #     #只用恢复gans的，不用更新这次的
        #     dep2decr[ganarr[0]] +=1;
        #     dep2decr[dxidx] -=1;
        #     ganarr[0] = deptmpidx;
        # else: # 此时w在gans之后,正常更新
        #     dep2decr[deptmpidx] +=1;
        #     dep2decr[dxidx] -= 1;     

    # print("----------------func print: x %d(%d) , z %d(%d) "%(x,deps[x],z,deps[z]));
    # print("globalMin %s"%(str(globalMin)));
    # print("id2AddCut %s"%(str(id2AddCut)));    
    # print("dep2decr %s"%(str(dep2decr)));
    # print("dep2cvs %s"%(str(dep2cvs)));    
    # 现在开始计算整个队列的minv

    if (id2AddCut[v] - addCntBefore > decrcnt):
        return;

    gnum = 0;
    minTV = sys.maxint;
    lnseq = len(dep2decr);
    for i in range(lnseq):
        depIdx = lnseq - 1 - i;
        # print("minTV before %d"%(minTV));
        if (i > 0):
            minTV = min(dep2cvs[depIdx] - gnum + id2AddCut[v], minTV);
            # print("depIdx %d, depcvs %d - gnum %d + id2add %d v %d"%(depIdx,dep2cvs[depIdx],gnum,id2AddCut[v],v));
            # print("minTV after %d"%(minTV));
        gnum += dep2decr[depIdx];
    # 得到最终最小值
    if (minTV < globalMin[0]):
        globalMin[0] = minTV;


def findVCutSet(g, x):
    g.vs[x]["s"] = 1;  # visiting, 2 is visited
    ks = set();
    tc = 1;
    dep = g.vs[x]["dep"];
    if (isDebug):
        if (dep % 1000 == 0):
            print("d %d" % (dep));
    neibors = g.neighbors(x);
    random.shuffle(neibors);
    for z in neibors:
        # print("z is %d, with property %s"%(z,g.vs[z].attributes()));
        if ("dep" in g.vs[z].attributes() and not g.vs[z]["dep"] is None and g.vs[z]["dep"] == g.vs[x]["dep"] - 1):
            continue;

        if ("s" not in g.vs[z].attributes() or g.vs[z]["s"] is None):
            g.vs[z]["dep"] = dep + 1;
            gDepMap[dep + 1] = z;
            findVCutSet(g, z);
            zks = g.vs[z]["ks"];
            ztc = g.vs[z]["tc"];
            tc = tc + ztc;
            for kkk in zks:
                if (kkk < dep):
                    ks.add(kkk);

            if (len(zks) < gklen and dep > 0 and ztc >= gktreecount and ztc <= gtotal - gktreecount):
                vset = set();
                vset.add(x);
                for tdep in zks:
                    vset.add(gDepMap[tdep]);
                gCandidate[z] = vset;

            g.vs[z]["ks"] = None;

        if (g.vs[z]["s"] == 1):
            ks.add(g.vs[z]["dep"]);

    g.vs[x]["s"] = 2;
    # don't add father node of x
    # ks.add(dep-1);

    g.vs[x]["ks"] = ks;
    g.vs[x]["tc"] = tc;

    # if (len(g.vs[x]["ks"]) <= klen):

    # print("AFTER: z is %d, with property %s"%(z,g.vs[z].attributes()));
    # if(g.vs[z]["s"] == 2 ):
    #     t = g.vs[z]["low"];
    # elif(g.vs[z]["s"] == 1):
    #     t = g.vs[z]["dep"];
    # else:
    #     raise Exception("!!!ERRRRRRRRRRRRRRR: state is %d"%(g.vs[z]["s"]));

    # if(g.vs[x]["low"] > t):
    #     g.vs[x]["low"] = t;

    # if(g.vs[z]["s"] == 2 and g.vs[z]["low"] >= g.vs[x]["dep"]):
    #     g.vs[x]["c"] = 1;


# -------------------------------------------width first version


isDebug = 0;


def randomSaveGrph(n, m):
    while (True):
        n = int(n);
        m = int(m);
        p = 2.0 * m / (n * n);
        g = Graph.Erdos_Renyi(n, p);
        m = len(g.get_edgelist());

        if (not g.is_connected()):
            print("not connected, try again");
            time.sleep(1);
            continue;

        fnm = ("rand_%d_%d.pickle") % (n, m);
        print("n: %d, m %d, degree %f, save to %s" % (n, m, m * 1.0 / n, fnm));

        g.write_pickle(fnm);

        break;


def randomScaleFreeGraph(n, m, r):
    while (True):
        n = int(n);
        pm = int(m * 1.0 / n);  # per node m
        g = Graph.Barabasi(n, pm, power=r);
        m = len(g.get_edgelist());

        if (not g.is_connected()):
            print("not connected, try again");
            time.sleep(1);
            continue;

        fnm = ("sfrand_%d_%d.pickle") % (n, m);
        print("n: %d, m %d, degree %f, save to %s" % (n, m, m * 1.0 / n, fnm));

        g.write_pickle(fnm);

        break;


# radius ia a fraction between (0,1.0]
def randomUnitDiskGraph(n, radius):
    while (True):
        n = int(n);
        g = Graph.GRG(n, radius);
        m = len(g.get_edgelist());

        if (not g.is_connected()):
            print("not connected, try again");
            # print("%s"%(str(g.vs["x"][0:100])))
            time.sleep(1);
            continue;

        fnm = ("udskrand_%d_%d.pickle") % (n, m);
        print("n: %d, m %d, degree %f, save to %s" % (n, m, m * 1.0 / n, fnm));

        g.write_pickle(fnm);

        break;


def genFullGraph(n):
    while (True):
        n = int(n);
        g = Graph.Full(n);
        m = len(g.get_edgelist());

        if (not g.is_connected()):
            print("not connected, try again");
            # print("%s"%(str(g.vs["x"][0:100])))
            time.sleep(1);
            continue;

        fnm = ("ufullrand_%d_%d.pickle") % (n, m);
        print("n: %d, m %d, degree %f, save to %s" % (n, m, m * 1.0 / n, fnm));

        g.write_pickle(fnm);

        break;


def genGridGraph(sn):
    print("sn is %d" % (sn));
    g = Graph();
    n = sn * sn;
    m = n * 2;
    # vers = range(n+1);
    # vers = vers[1:];
    # print(vers);
    g.add_vertices(n);
    edges = [];

    for x in range(sn):
        for y in range(sn):

            i = x * sn + y;
            # print("i is %d"%(i));

            ailist = [];  # to add with node

            # west
            if (y > 0):
                ailist.append(i - 1);

            # #east
            # if(y < sn-1):
            #   ailist.append(i+1);

            # north
            if (x > 0):
                ailist.append((x - 1) * sn + y);

            # #south
            # if(x < sn-1):
            #     ailist.append((x+1)*10+y+1);

            for kn in ailist:
                edges.append((i, kn));

    # print(edges);
    g.add_edges(edges);

    if (not g.is_connected()):
        print("vcount %d ecount %d, not connected, try again" % (g.vcount(), g.ecount()));

        # print("%s"%(str(g.vs["x"][0:100])))
        time.sleep(1);
        sys.exit(1);

    # for i in range(n):
    #     print("node %d neighbors %s"%(i,str(g.neighbors(i))))   

    fnm = ("grid_%d_%d.pickle") % (n, m);
    print("n: %d, m %d, degree %f, save to %s" % (n, m, m * 1.0 / n, fnm));

    g.write_pickle(fnm);


lastfnm = "";
globalg = None;


def reloadSameGraphWithSameCaps(gtype, fnm, caps):
    global lastfnm, globalg;
    g = None;

    if (gtype == "pickle"):
        print("read from " + fnm);
        if (fnm != lastfnm):
            g = Graph.Read_Pickle(fnm);  # need to reload, because all states should be discarded
            lastfnm = fnm;
            globalg = g;
        else:
            g = globalg;
            g.vs["s"] = None;
            g.vs["cv"] = None;
            g.vs["dep"] = None;
            g.vs["fa"] = None;

    # fvs =  list(numpy.random.rand(g.ecount()).round(2)*100);
    # caps = range(g.ecount());
    # caps[0] = caps[0] +1;
    # for a in range(g.ecount()):
    #     caps[a] = caps[a] + fvs[a];
    # g.es["capacity"] = caps;    

    # gen randomly cap
    if (caps is None):
        caps = list(range(g.ecount()));
        for a in range(g.ecount()):
            caps[a] = 1 + int(random.random() * 1000);

    g.es["capacity"] = caps;
    # print(g.es["capacity"]);
    # sys.exit(1);

    # print("caps");
    # print(caps);

    # for e in g.get_edgelist():
    #     print(g.es[e]["capacity"]);
    return g;


def zeros(length):
    ret = range(length);
    for i in range(length):
        ret[i] = 0;

    return ret;


if __name__ == '__main__':
    # a = getSequence(10,30)
    # print(sum(a))
    # print(a)
    # exit(0)
    # NOTE!!!: edge_per_node is the number in undirected graph
    # pdb.set_trace();

    mainLab5();
    sys.exit(0);

    # script,gtype,op,isDebug,fnm,klen,edge_p= sys.argv  

    # if(isDebug == 1):
    #     pdb.set_trace();

    # if(op == "random_erdos"):
    #     print("gen and save");
    #     randomSaveGrph(fnm,edge_p);
    #     print("save done");
    #     exit(1);

    # if(op == "random_scalefree"):
    #     print("gen and save");
    #     randomScaleFreeGraph(fnm,edge_p,3);
    #     print("save done");
    #     exit(1);

    # g = reloadSameGraphWithSameCaps(gtype,fnm,None);

    # if(not g.is_connected()):
    #     print("Err: graph is not connected");
    #     exit(1);

    # if(op == "findvcuts"):
    #     gtotal = g.vcount();
    #     klen = int(klen);
    #     gklen = klen;
    #     gktreecount = int(gtotal*0.01);
    #     print("largest: vcount %d, ecount %d, number of components %d, cut_count %d"%(g.vcount(),g.ecount(),len(g.components()),len(g.cut_vertices())))
    #     print("run par: gklen %d gtreecount %d, gtotal %d"%(gklen,gktreecount,gtotal));

    #     root = g.get_edgelist()[0][0];
    #     print("root is %d"%(root));
    #     g.vs[root]["dep"] = 0;
    #     gDepMap[0] = root;
    #     findVCutSet(g,root);
    #     hint = "";
    #     print("findVCutSet finished");
    #     for x in gCandidate:
    #         print("print for "+str(x));
    #         hint = "";
    #         vset = gCandidate[x];
    #         sg = g.copy();
    #         #vset.add(x); #no need to adding
    #         if(root in vset):
    #             hint = "neglect-has root";
    #         sg.delete_vertices(list(vset));
    #         comps = sg.components();
    #         csize = set();
    #         for cidx in range(len(comps)):
    #             csize.add(comps.size(cidx));
    #         l_vset = list(vset);
    #         l_vset.sort();
    #         print ("_XSET: %s + %d ||| %s: x %d increase component count to %d, details: %s "%(str(l_vset),len(comps),hint,x,len(comps),str(csize)));

    # elif(op == "markvcut"):
    #     gs = [];
    #     klen = int(klen);
    #     if(klen < 0):
    #         tn = g.vcount();
    #         tm = g.ecount();
    #         klen = int(min(pow(tn,2.0/3),pow(tm,1.0/2))/2);
    #         print(("k is chaged to %d")%(klen));
    #     while(True):
    #         for i in range(klen):
    #             egs = g.get_edgelist();
    #             root =egs[random.randint(0,len(egs)-1)][0];
    #             # print("nodes:");
    #             # print(g.get_edgelist());   
    #             if(root is None):
    #                 print("!!!ERRRRRRRRR: root is None, set to 0");
    #                 root = 0;         
    #             print("iter%d: root is %d, vcnt %d ecnt %d"%(i,root,g.vcount(), g.ecount()));
    #             g.vs[root]["dep"] = 0;
    #             markECutValue(g,root);
    #             hint = "";
    #             # print("markECutValue finished for "+str(i));
    #             deps = zeros(g.vcount());
    #             cvs = zeros(g.vcount());
    #             fas = zeros(g.vcount());
    #             for e in g.get_edgelist() :
    #                 for n in e:
    #                     deps[n] = g.vs[n]["dep"];
    #                     cvs[n] = g.vs[n]["cv"];
    #                     fas[n] = g.vs[n]["fa"];  
    #                     if(fas[n] is None):
    #                         if(n == root):
    #                             fas[n] = -1;
    #                         else:
    #                             print("FFFFFFFFFFFFFFFFFFFFnode %d fa is None"%(n));    
    #             gs.append((deps,cvs,fas,root));

    #             g = reloadSameGraphWithSameCaps(gtype,fnm);

    #         #find random s,t
    #         egs = g.get_edgelist();
    #         vlen = len(egs);
    #         difftm = 0;
    #         difftotal = 0;
    #         maxtotal = 0;
    #         ourtotal =0;
    #         theirtotal = 0;
    #         iter_num = int(edge_p);
    #         avg_stlen_all = 0;
    #         for iter in range(iter_num):
    #             s = egs[random.randint(0,vlen-1)][0];
    #             t = egs[random.randint(0,vlen-1)][0];
    #             if(s==t):
    #                 print("s==t, exit");
    #                 iter -=1;
    #                 continue;

    #             if(s is None or t is None):
    #                 print("!!!!!!!!!!!!!s or t is None");
    #                 continue;

    #             print("cal maxflow for %d <-> %d"%(s,t));

    #             # starttime = datetime.datetime.now()
    #             (m1,ourtm,avg_stlen) = findMaxflowMulti(g,gs,s,t);
    #             avg_stlen_all = avg_stlen_all + avg_stlen*1.0/iter_num;
    #             # ourtm = datetime.datetime.now() -starttime;
    #             ourtotal = ourtotal + ourtm;

    #             starttime = datetime.datetime.now()                            
    #             # m2 = g.maxflow(s,t,"capacity");
    #             m2 = g.maxflow(s,t);
    #             theirtm = datetime.datetime.now() -starttime;
    #             theirtotal = theirtotal + theirtm.microseconds;

    #             difftotal = difftotal + m1 - m2.value;
    #             maxtotal = maxtotal + m2.value;
    #             print("caliter %d m1 m2: %d %d"%(iter,m1,m2.value));
    #             if (m1 != m2.value):
    #                 difftm = difftm +1;

    #             if(m1 < m2.value):
    #                 print("fuckXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX %d %d"%(m1,m2.value));

    #         bratio = 0;
    #         if(difftm > 0):
    #             bratio = (difftotal/difftm)/(maxtotal/iter_num);
    #         print("avgst: %f, difftm: %d/%d, vratio_when_diff %f, difftotal %d, maxtotal: %d, time our v.s. their: %d(%d) %d  | %s"%(avg_stlen_all,difftm,iter_num,bratio,difftotal,maxtotal,ourtotal/30, ourtotal,theirtotal,fnm));

    #             # print("maxflow:");
    #             # print(m1);
    #             # print(m2.value);
    #             # print(len(m2.flow));
    #             # print(m2.cut);
    #             # # print(m2.partition);
    #             # print(m2.es);
    #         prom = "n"; #input(("contineu another %d preprocess and cal? (y/n)")%(klen));
    #         if(prom == "y"):
    #             print("go on!");
    #         else:
    #             print("exit");
    #             exit();

    # elif(gtype == "SLNDC"):
    #     g = readSLNDC(fnm)
    #     if(op == "savebcc2pickle"):
    #         findLargestBCC(g,fnm+".pickle");

    #     elif(op == "showcut"):
    #         print("number of cuts: %d"%(len(g.cut_vertices())));
    #         sub2 = subgraph(g);
    #         anaCut(sub2);

    #     elif(op == "maximalClique"):
    #         maximalClique(g);
    #     elif(op == "pcsp"):
    #         sg = g;
    #         print("original graph node edge %d %d"%(sg.vcount(), sg.ecount()));
    #         g = subgraph(sg);
    #         print("chosen graph node edge %d %d"%(g.vcount(), g.ecount()));
    #         g.vs[0]["dep"] = 0;
    #         searchCut(g,0);
    #         hg = buildHighLevel(g,0);
    #         #print info of hg, node, edges, gc of each node in hg
    #         total = printHG(hg);
    #         total2 = checkPrintG(g);
    #         if(total2 != hg.vcount()):
    #             raise Exception("num of cut in g %d != %d in hg"%(total2,hg.vcount()));
    #         if(total != g.vcount() -1):
    #             raise Exception("not all node in g included in hg %d != %d -1"%(total,g.vcount()));
    # elif(gtype == "transform"):
    #     if(op == "outHIPR"):
    #         outputUndirected(fnm);
    #     if(op == "slimcut"):
    #         slimcut(fnm);
