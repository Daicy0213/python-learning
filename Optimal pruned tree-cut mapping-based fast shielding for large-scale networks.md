## Optimal pruned tree-cut mapping-based fast shielding for large-scale networks (基于最优修剪树切割映射的大规模网络快速屏蔽)

### Abstract

Random failure is a common threat to a network, where the failure of a few edges can disconnect a large-scale sparse network. To enhance the robustness of network, the shielding of important edges is a practical strategy, where the cut is a useful entity to help locate important edges in existing shielding methods.

随机故障是对网络的常见威胁，其中一些边缘的故障可以断开大规模稀疏网络。为了提高网络的健壮性，重要边的屏蔽是一种实用的策略，在现有的屏蔽方法中，切割是帮助定位重要边的有用实体。

However, as there is no available way to quickly locate target cuts, the existing shielding algorithm is not efficient enough and can only be applied to small-scale backbone networks. Fortunately, by using the optimal pruned tree-cut mapping, we found an efficient and high-precision cut edge enumeration method, which can help quickly locate target cuts and their edges in a large-scale network, leading to a cost-effective shielding plan.

但由于没有快速定位目标切口的方法，现有的屏蔽算法效率不高，只能应用于小规模骨干网。幸运的是，通过使用最优修剪树切割映射，我们找到了一种高效、高精度的切割边缘枚举方法，可以帮助快速定位大规模网络中的目标切割及其边缘，从而实现经济高效的屏蔽方案。

Theoretical analysis indicates that more than 99% of candidate cuts can be found with a limited number of preprocessing passes, and experimental results in typical networks show that in small-scale networks, with little extra cost (< 6%), the serial implementation of the algorithm in an off-shelf computing node can be 6 orders of magnitude faster than the optimal method, while in large-scale sparse networks with a million nodes, it can also help defend at least 99.9% of random failures with only tens of seconds of preprocessing overhead.

理论分析表明，在有限的预处理次数下，可以找到超过99%的候选切割，并且在典型网络中的实验结果表明，在小型网络中，在很少的额外成本(< 6%)的情况下，该算法在一个现成计算节点上的串行实现可以比最优方法快6个数量级，而在具有100万个节点的大规模稀疏网络中，它还可以帮助防御至少99.9%的随机故障，只需要几十秒的预处理开销。





### 1. Introduction

Network robustness is a measure of the ability to continue functioning when part of the network is either naturally damaged or targeted for attack

网络健壮性是指当网络的一部分被自然损坏或被攻击时，网络继续运行的能力

When redundant resources are not feasible, a more practical way is to shield critical edges and make them no longer vulnerable to most network failures. The core idea is to select and shield critical edges for the targeted paths and optimize one or more objectives under given constraints [4, 5].

当冗余资源不可用时，更实际的方法是屏蔽关键边，使它们不再容易受到大多数网络故障的影响。其核心思想是为目标路径选择和屏蔽关键边，并在给定约束条件下优化一个或多个目标。

 To improve the reliability of the path between given ends in a telecommunication network, [4] took the laying cost and the number of repaired links as optimization targets, modeled it as a multi-objective shortest path problem and solved it using the label setting algorithm. 

为了提高电信网络中给定端点间路径的可靠性，[4]以铺设成本和修复链路数量为优化目标，将其建模为多目标最短路径问题，并采用标签设置算法求解。

Then the approximate Pareto front for the objectives was obtained within an acceptable running time. To improve the robustness of the backbone optical network and select edges to upgrade to higher-level availability, [5] investigated how to obtain the upgrade plan at the lowest cost under availability and geodiversity constraints.

然后在可接受的运行时间内获得目标的近似帕累托前沿。为了提高骨干光网络的健壮性，并选择边缘升级到更高级别的可用性，[5]研究了在可用性和地理多样性约束下，如何以最低的成本获得升级方案

The arc-based integer nonlinear programming model was relaxed and solved, and the results were further improved by a filtering procedure. In addition, **the vehicle capsize likelihood targeting algorithm** [6] and **trunk-and-branch tree topology-oriented algorithms** [7] were proposed accordingly.

对基于圆弧的整数非线性规划模型进行了松弛和求解，并通过滤波过程对结果进行了进一步改进。此外，提出了车辆倾覆似然目标算法[6]和面向树干-分支树拓扑的算法[7]。



Specifically, the cut is the set of edges whose removal will separate the given graph into disconnected parts, and the graph's edge connection is the minimum cut size among all its node pairs. **To improve edge connectivity, the algorithm needs to find all edges in cuts with sizes smaller than the given edge connectivity and selectively shield them.** To speed up the process, the direct way is to improve the efficiency of algorithms. In addition to graph shrinking-based acceleration [9, 10], many algorithmic variants have recently been proposed to improve efficiency

具体来说，切割是将给定图分割为不连接部分的边的集合，而图的边连接是其所有节点对中最小的切割尺寸。为了提高边缘连通性，该算法需要找到所有尺寸小于给定边缘连通性的切口中的边，并有选择地屏蔽它们。要加快这一过程，最直接的方法就是提高算法的效率。除了基于图收缩的加速[9,10]，最近还提出了许多算法变体来提高效率

However, the existing per-pair efficiency improvement is still not efficient enough for the edge shielding problem in large-scale networks. Since the edge shielding problem needs to identify edges in small cuts, which can be solved by the currently known fastest algorithm [16] in O(N 2β log(N )) > O(N 2log(N )) time in a graph with N nodes, which is a significantly higher complexity for large graphs since β > 1. If edge identification and shielding are considered together [8], the resulting mixed integer linear programming optimal algorithm has far more time complexity than [16]. The low accuracy of available efficient heuristic rules also renders them useless, such as shielding edges between selected nodes in a greedy manner.

然而，现有的每对效率改进方法对于大规模网络中的边缘屏蔽问题仍然不够有效。由于边缘屏蔽问题需要在小切口中识别边缘，目前已知的最快算法[16]可以在N个节点的图中在O(N 2β log(N)) > O(N 2log(N))时间内解决，这对于β > 1以来的大图来说，复杂度明显更高。如果同时考虑边缘识别和屏蔽[8]，得到的混合整数线性规划优化算法的时间复杂度远高于[16]。可用的有效启发式规则的低准确性也使它们无用，例如以贪婪的方式在所选节点之间屏蔽边。

> 为什么在n个节点中的图识别边缘的时间复杂度是O(N^2 log(n))?

The main objective of the paper is to effectively solve the edge shielding of large-scale networks with high accuracy. Specifically, it is to find a suitable algorithm according to the characteristics of the shielding problem, which can significantly reduce the computational complexity and guarantee the same or similar accuracy. **Unlike the traditional idea of using the cutting algorithm to locate shielding candidate edges in small cuts, the novelty is the optimal pruned tree-cut mapping-based cut enumeration, which is used to quickly obtain a batch of cuts to which each edge belongs, and then approximate the minimum cut of each edge through a Monte Carlo-like method, thus greatly reducing computational complexity and ensuring high solution accuracy.**

本文的主要目的是为了更有效的解决具有高精度的大规模网络的边缘屏蔽问题。具体来说，就是根据屏蔽问题的特点找到合适的算法，能够显著降低计算复杂度，保证相同或相似的精度。与传统的利用切割算法在小切口中定位屏蔽候选边缘的思路不同，新颖之处在于基于最优剪枝树切割映射的切割枚举，快速获取每条边所属的一批切割，然后通过类蒙特卡罗方法逼近每条边的最小切割，大大降低了计算复杂度，保证了较高的求解精度。

Then, we propose the optimal pruned tree-cut mapping-based fast shielding algorithm (OPTFS) for large-scale networks. The pruned tree-cut mapping is the mapping between pruned depth-first traversal trees to cuts, i.e., enumerating cuts can be achieved by enumerating pruned depth-first traversal trees. Formal definitions and explanations with figures are provided in Section 2.1. With several depth-first traversals in a large network, the minimum cuts for the high percentage of all edges can be obtained while the edges in the target cuts can be efficiently collected, and then an improved minimum cost spanning tree is generated to find the near-optimal solution. Experimental results show that compared with the optimal algorithm in small-scale networks, when the network robustness is 100%, the proposed algorithm can find the near optimal solution with the acceleration ratio of up to 6 orders of magnitude; in large-scale networks with 1 million nodes, the network robustness can also be maintained at no less than 99.9% by running the proposed algorithm for tens of seconds in an offshelf computing node. A more detailed explanation of the proposed algorithm is given near Figure 1, including how it works and how it differs from previous work.

然后，我们提出了一种基于最优修剪树切割映射的大规模网络快速屏蔽算法(OPTFS)。修剪树切割映射是修剪深度优先遍历树与切点之间的映射，也就是说，可以通过枚举修剪深度优先遍历树来实现枚举切点。2.1节提供了正式的定义和图表解释。通过在一个大型网络中进行多次深度优先遍历，可以在有效地收集目标切口中的边的同时，获得高比例所有边的最小切口，然后生成改进的最小代价生成树来寻找近最优解。实验结果表明，与小尺度网络中的最优算法相比，当网络健壮性为100%时，所提算法可以找到加速度比高达6个数量级的近最优解;在100万节点的大型网络中，该算法在一个离线计算节点上运行数十秒，网络健壮性也可以保持在不低于99.9%。图1附近给出了所提出算法的更详细的解释，包括它是如何工作的，以及它与以前的工作有什么不同。

The drawback of the algorithm is that the preprocessing overhead needs to be adjusted in different dense graphs to ensure accuracy. For example, the experiment shows that in dense graphs, the accuracy is reduced by 0.1% due to the higher proportion of large cut sizes. Fortunately, the reduction is relatively small and can be detected in time by sampling to check whether the accuracy **meets** expectations. And because the number of search passes determines the accuracy of the search, it can be slightly increased accordingly in the dense graph to maintain the expected accuracy.

该算法的缺点是需要在不同密度图上调整预处理开销以保证精度。例如，实验表明，在密集图中，由于大切割尺寸的比例较高，精度降低了0.1%。幸运的是，减少量相对较小，可以通过采样及时检测，以检查精度是否符合预期。并且由于搜索的遍数决定了搜索的精度，所以在稠密图中可以相应地稍微增加，以保持预期的精度。



### 2. Background

**Definition 1.** An undirected graph G(V, E) is composed of a set of nodes Vand a set of edges E disjoint from V , together with an incidence function that associates with each edge of G an unordered pair of (not necessarily distinct) nodes in G. 

The concept of edge cut can be given in an undirected graph.

定义1. 无向图G(V, E)由一组节点V和一组与V不相交的边E，以及与G的每条边关联的关联函数组成，G中的每条边都是一对无序的(不一定是不同的)节点。

切边的概念可以在无向图中给出。

**Definition 2**. In an undirected graph G(V, E), for any subset of node X ⊂ V , the set of edges connecting nodes in X to nodes in its complement set  ̄X = V −Xis a (edge) cut of G.

Note that only the cut containing no other cut (i.e., bond) is considered, because for an edge, the shielding problem only needs to consider its belonging edge sets that cannot be reduced.

定义2. 在无向图G(V, E)中，对于节点X V的任何子集，将X中的节点与其补集中的节点连接在一起的边的集合是G.的边切。

注意，只考虑不包含其他切(即键合)的切，因为对于边，屏蔽问题只需要考虑其不能约简的所属边集。

**Definition 3.** A graph bond is a minimal nonempty edge cut, i.e., a nonempty edge cut none of whose proper nonempty subsets is an edge cut.

A bond can only separate the original graph into two connected graph parts:

定义3. 图键合是一个最小的非空边切，也就是说，一个非空边切没有一个适当的非空子集是边切

键合只能将原图分离成两个连通的图部分:

**Lemma 1.** In a connected graph G(V, E), a nonempty edge cut associated with a subset of nodes X is a bond if and only if both the subgraph G[X] and G[V −X]are connected.

引理1. 在连通图G(V, E)中，当且仅当子图G[X]和G[V−X]都连通时，与节点X的子集相关联的非空切边是键合。

Denote the size of the cut as the number of edges in the cut, the edge connectivity can be defined accordingly:

将切割的大小表示为切割中的边的数量，可以相应地定义边缘连通性

**Definition 4.** In an undirected graph G, the local edge connectivity between nodes x and y is the maximum number of pairwise edge-disjoint xy-paths, denoted p(x, y). The edge connectivity of a graph is K if p(x, y) ≥ K for any two distinct nodes x and y of G

定义4. 在无向图G中，节点x和y之间的局部边连通性是成对边不相交的xy路径的最大数目，记作p(x, y)。对于G中的任意两个不同的节点x和y，如果p(x, y)≥K，则图的边连通性为K。

The edge connectivity is also the smallest cut size of any cut in the graph by definition. In order to maintain the connectivity of a given network by shielding, the problem investigated (i.e., the minimum cost edge connectivity increase by shielding) can be formally stated as follows:

根据定义，边缘连通性也是图中任何切口中最小的切口大小。为了通过屏蔽来保持给定网络的连通性，所研究的问题(即通过屏蔽增加的最小代价边连通性)可以正式表述如下:

**Definition 5.** In an undirected graph G(V, E) with its current edge-connectivityK′ and the cost for each edge, given the target edge-connectivity K > K′, the problem is to shield a set of edges with the lowest cost, so that G(V, E) is connected after removing any K − 1 unshielded edges (i.e., the edge-connectivity ofG(V, E) is increased to K).

定义5. 在无向图G(V, E)中，其当前边连通性K '和每条边的代价，给定目标边连通性K > K '，问题是屏蔽一组代价最低的边，使G(V, E)在删除任何K−1条未屏蔽边后连通(即G(V, E)的边连通性增加到K)。

In other words, any K − 1 unshielded edges will not form a cut in the shielded graph, and edge shielding increases graph connectivity to K. It has been shown that the optimal shielding problem is a NP-hard problem [8], and even the approximate solution guaranteeing high accuracy results for large-scale networks cannot be solved efficiently using the fastest cut algorithm.

换句话说，任何K−1条未屏蔽的边都不会在屏蔽图中形成切割，边缘屏蔽使图连通性增加到K。已经证明，最优屏蔽问题是NP-hard问题[8]，即使是保证大规模网络高精度结果的近似解，也不能用最快切割算法有效求解。

Lemma 2. The optimal shielding problem is NP-hard.

Proof. This can be proved by its equivalent set covering problem (SCP) which has already been shown to be a NP-hard problem. Given a complete set U , and a set S containing several subsets of U whose union is U , the set covering problem is to find a minimum subset of S (i.e., C), so that the union of subsets in C is equal to the complete set U . 

这可以用它的等价集覆盖问题(SCP)来证明，SCP已经被证明是一个np-hard问题。给定一个完整集U和一个包含U的几个并集为U的子集的集合S，集合覆盖问题是寻找S的一个最小子集(即C)，使C中的子集的并集等于完整集U。

The minimum can be measured in many different ways, and the basic one is the number of subsets in C.

最小值可以用许多不同的方法来测量，最基本的方法是C中子集的数量。

In an undirected graph, each cut is assigned a unique ID, and each edge is assigned a set of cut IDs containing it. 

在无向图中，每个切被分配一个唯一的ID，每条边被分配一组包含它的切ID。

Define the cut size as the number of edges in it, denote U as the complete set of all cut IDs with cut size less than K in the graph, denoteS′ as the de-duplicated set generated by including all the edges of the cut IDs in U , and S as the set generated by mapping each edge in S′ to the set of its belonged cut IDs. 

定义切割大小为其中的边数，表示U为图中切割大小小于K的所有切割id的完整集合，表示'为包含U中切割id的所有边而生成的去重集，S为将S '中的每条边映射到其所属切割id的集合而生成的集合。

The optimal shielding problem is simply to find the optimal subset of S (i.e., C) covering all IDs in U , which is just the set covering problem and is NP-hard. 

最优屏蔽问题就是简单地找到S的最优子集(即C)覆盖U中的所有id，这就是集合覆盖问题，也是是NP-hard的。

The lemma is proved.

引理得证。

NP-hard is also shown in [8] using another similar problem. Given the equivalent problem pair, i.e., a simplified version of the optimal shielding problem of increasing (edge) connectivity by only 1 (problem 1) and a simplified version of the graph augmentation problem of increasing (edge) connectivity by only 1 (problem 2 defined as Definition 6), since problem 2 has been shown to be NPhard [8], problem 1 is also NP-hard. Therefore, the optimal shielding problem is also NP-hard, or its instance of problem equal to problem 1 is not NP-hard and there is a contradiction.

NP-hard也在[8]中使用了另一个类似的问题。给定等价问题对，即仅增加(边)连通性的最优屏蔽问题的简化版本(问题1)和仅增加(边)连通性的图增强问题的简化版本(问题2定义为定义6)，由于问题2已被证明是NP-hard[8]，问题1也是np-hard的。因此，最优屏蔽问题也是NP-hard问题，或其等于问题1的问题实例不是NP-hard问题，存在矛盾。

> NP-hard 问题貌似是问题的关键

**Definition 6.** The simplified version of the graph augmentation problem is to increase (edge) connectivity by only 1 through adding parallel edges to each existing edge, where only one more edge can be added to both ends of an existing edge.

定义6. 图增强问题的简化版本是通过向每个现有边添加并行边来仅将(边)连通性增加1，其中只能向现有边的两端添加一条边。

As for the challenges introduced by the optimal shielding problem, the same as the SCP problem, it has no polynomial time solution. It is also difficult to approximate by enumerating all the candidate cuts. For example, all cuts in a graph need to be collected in advance to enable the following SCP solution, where the currently known fastest approximation algorithm [16] has a significantly high time complexity of O(N 2β log(N )) > O(N 2log(N )) in a graph withN nodes, where β > 1 is a problem-dependent number. 

至于最优屏蔽问题所带来的挑战，与SCP问题一样，它没有多项式时间解。通过列举所有候选削减来近似也是困难的。例如，需要提前收集图中的所有切点以实现以下SCP解决方案，其中目前已知的最快逼近算法[16]在具有N个节点的图中具有O(N 2β log(N)) > O(N 2log(N))的高时间复杂度，其中β > 1是一个与问题相关的数。

This means that even given some efficient approximated solution to the SCP problem, the high complexity of the entire optimal shielding problem makes it difficult to apply to large-scale graphs.

这意味着即使对SCP问题给出了一些有效的近似解，整个最优屏蔽问题的高度复杂性也使得它难以应用于大规模图。

To solve the problem, we seek to find an efficient approximate solution for large-scale networks. It is clear that two key issues need to be addressed to solve the problem: (1) How to find all cuts smaller than K (i.e., the set of cuts φK ); (2) How to cost-effectively shield at least one edge in each cut, so that any cut in φK has at least one shielded edge and any K − 1 unshielded edges do not form a cut to separate the graph.

为了解决这一问题，我们寻求大规模网络的有效近似解。很明显，要解决这个问题需要解决两个关键问题:

(1)如何找到所有小于K的切割(即φK的切割集);

(2)如何经济有效地在每个切割中屏蔽至少一条边，使φK的任何切割都至少有一条屏蔽边，并且任何K−1条未屏蔽边都不会形成切割来分离图形。



### 2.1. Finding targeted cuts

As for the first sub-problem of finding all cuts smaller than K, the existing high-precision approximation algorithm is not applicable in a large-scale network. Instead, we found an efficient way to find the desired cuts with high precision, i.e., mapping between cuts and depth-first traversal trees (DTTs).

对于第一个子问题寻找所有小于K的切点，现有的高精度逼近算法不适用于大规模网络。相反，我们找到了一种高效的方法来高精度地找到所需的切点，即切点和深度优先遍历树(dtt)之间的映射。

**Definition 7.** The depth-first traversal tree (DTT) rooted at a node is the tree consisting of all its traversal descents and the edges connecting these descents to their parent nodes.

定义7。以节点为根的深度优先遍历树(DTT)是由其所有遍历下降和将这些下降连接到它们的父节点的边组成的树。

A depth-first traversal procedure will traverse the graph in depth-first order from a selected root node and obtain a global DTT rooted at the root node. In each node x there is also a local DTT rooted at it, which can be written as DTTx. Obviously, all nodes in the global DTT form the node set V in Definition 2. All nodes in each DTTx form a node set X that has a corresponding cut. Further, by defining a pruned DTT (PDTT) as follows, each of the various PDTTs of a DTT can also be mapped to a cut.

深度优先遍历过程将以深度优先顺序从选定的根节点遍历图，并获得根节点上的全局DTT。在每个节点x中也有一个植根于它的本地DTT，可以写成DTTx。显然，全局DTT中的所有节点都形成定义2中的节点集V。每个DTTx中的所有节点组成一个节点集X，该节点集X具有相应的切割。此外，通过如下定义修剪的DTT (PDTT)， DTT的每个不同的**PDTT（修剪的深度优先遍历树）**也可以映射到一个切割。

**Definition 8.** The pruned DTT (PDTT) rooted at node x is the remaining portion of DTTx by removing a combination of DTTs rooted at nodes insideDTTx.

定义8。根于节点x的修剪DTT (PDTT)是通过移除根于节点DTTx的DTT组合而得到的DTTx的剩余部分

Since DTT can be seen as a special kind of PDTT without pruning, the tree cut can be defined accordingly.

由于DTT可以看作是一种特殊的没有修剪的PDTT，因此可以相应地定义树的切。

**Definition 9.** The tree cut of a PDTT is made up of edges connecting nodes inside the PDTT to nodes outside the PDTT.

定义9。PDTT的树切由连接PDTT内部节点和PDTT外部节点的边组成。

An illustrative example of PDTT is given in Figure 1. In Figure 1, node 1 is the root of the global DTT, nodes with the same depth are at the same height, two cuts are shown as dashed curves, and each cut contains edges crossed by the respective curve. The DTT rooted at node 3 (i.e., DTT3) contains nodes 3/6/7/10/11 and its tree cut C1 contains edges (1, 3)/(1, 7). A PDTT rooted at 3 is generated by removing DTT7 from DTT3 and contains nodes 3/6/10/11, its tree cut C2 contains edges (1, 3)/(3, 7).

图1给出了PDTT的一个示例。在图1中，节点1为全局DTT的根，相同深度的节点在相同高度，两个切点以虚线曲线表示，每个切点包含各自曲线交叉的边。根于节点3的DTT(即DTT3)包含节点3/6/7/10/11，其树切C1包含边(1,3)/(1,7)，根于3的PDTT由DTT3去除DTT7生成，其树切C2包含边(1,3)/(3,7)

Thus, many cuts in the graph can be enumerated by enumerating pruned DTTs. Only by keeping the pruned DTTs at the desired cut value can the special set of cuts be found effectively. The pruned tree-cut mapping can be defined as follows. It is obvious that mapping is a bijection in a traversal result, i.e., each PDTT can only be mapped to one cut, and the cuts are different for different PDTTs.

因此，图中的许多切点可以通过枚举修剪后的dtt来枚举。只有将修剪后的dtt保持在所需的切割值上，才能有效地找到特殊的切割集。修剪后的树切割映射可以定义如下。很明显，映射在遍历结果中是双射，即每个PDTT只能映射到一个切割，并且对于不同的PDTT，切割是不同的。

**Definition 10.** **The pruned tree-cut mapping** is the mapping between a PDTT and its tree cut.

定义10。**修剪树切割映射**是PDTT与其树切割之间的映射。

​	An example is given to explain how the algorithm works. It can be found in Figure 1 that edge (1, 5) is included in the tree cuts of some DTTs (i.e.,DTT5, DTT2) and some PDTTs generated by pruning these DTTs, e.g., edge (1, 5) is also included in the tree cut of the PDTT generated by removing DTT4 from DTT2.

通过实例说明了该算法的工作原理。从图1中可以发现，边(1,5)包含在一些dtt(即DTT5, DTT2)的树切中，而对这些dtt进行剪枝生成的一些PDTT中，例如边(1,5)也包含在从DTT2中去除DTT4生成的PDTT的树切中。

During the traversal process, the cut values of these DTTs and PDTTs can be calculated and stored in the corresponding tree root or root of the removed DTTs, and the relationship between edge and cut can be quickly determined by whether the edge is connected to nodes outside the corresponding tree.

在遍历过程中，可以计算这些dtt和pdtt的cut值，并将其存储在相应的树根或被移除的dtt的根中，并且可以通过边是否连接到相应树外的节点来快速确定edge和cut的关系。

In addition, a local search is performed in the traversal process to find PDTTs with small cuts. Thus, once traversed, the values of these cuts, as well as the inclusion relationship between cuts and edges, are embedded in the tree structure, and then the candidate edges can be quickly found by checking the minimum cut value of each edge through another traversal pass.

此外，在遍历过程中执行本地搜索以查找具有小切口的ptt。因此，一旦遍历，这些切割的值以及切割与边之间的包含关系就嵌入到树结构中，然后通过另一次遍历检查每条边的最小切割值就可以快速找到候选边。

To increase accuracy, through multiple random traversals using a **Monte Carlo-like** process, more cuts can be obtained per edge, thus identifying edges in smaller cuts more precisely.

为了增加准确性, 通过使用类似蒙特卡罗的过程进行多次随机遍历，每条边可以获得更多的切割，从而更精确地识别较小切割中的边。

​	Regarding how it differs from previous work, since the idea of tree-based cut enumeration was not adopted in previous work, the core difference is that it is a cut enumeration algorithm adapted to the need of the shielding problem to calculate the minimum cut of each edge and identify candidate edges. Unlike the highly complex step in the previous algorithm, which calculates the minimum cut value for each edge based on the minimum cut algorithm, the proposed algorithm uses suitable data structures to enumerate the small cuts while recording the corresponding relationship between the cut and the edge, and then traverses again to enumerate and identify the candidate edges.

与以往的工作不同的是，由于之前的工作没有采用基于树的切割枚举思想，最核心的区别在于它是一种适应屏蔽问题需要的切割枚举算法，计算每条边的最小切割并识别候选边。与之前算法中基于最小切割算法计算每条边的最小切割值的高度复杂步骤不同，本文算法使用合适的数据结构枚举小切割，同时记录切割与边的对应关系，然后再次遍历枚举和识别候选边。

​	Since there is randomness in the algorithm, it is useful to know the probability of finding a cut as a tree cut. Since there are no edges between sibling nodes in the depth-first traversal tree, as shown in Figure 1, all edges in a graph can be classified as two types by a given global DTT: the tree edge (parent-child edge) and the non-tree edge (ancestor-descendent edge). Accordingly, a combination of tree and non-tree edges constitutes any given cut, and there are important conclusions:

由于算法中存在随机性，因此知道找到切割的概率是有用的。由于在深度优先遍历树中兄弟节点之间没有边，如图1所示，一个图中的所有边都可以被给定的全局DTT分为两种类型:树边(父-子边)和非树边(祖先-后代边)。因此，树边和非树边的组合构成了任何给定的切割，并得到了重要的结论:

<img src="Optimal pruned tree-cut mapping-based fast shielding for large-scale networks.assets/image-20230409163047641.png" alt="image-20230409163047641" style="zoom: 50%;" />

**Lemma 3.** If only one edge of a cut C is a tree edge, the cut must be found as a tree cut of a DTT.

如果切割C只有一条边是树边，则该切割必须作为DTT的树切。

Proof. Denote only one tree edge as that with end nodes (f ax, x) where f axis the parent node of x. For any non-tree edge with end nodes a and b in the cut, denote the tree path between them as p(a,b). If both a and b are not inDTTx or both are in DTTx, p(a,b) will not contain (f ax, x) according to the structure of the depth-first traversal tree, but p(a,b) must contain at least one cut edge since a and b are in different parts separated by the cut C, i.e., the cut edge is a tree edge in addition to (f ax, x), which is a contradiction. It indicates that for the two nodes a and b, one is in DTTx and the other is not in DTTx, which will surely be found as the non-tree edge in the tree cut of DTTx. Since (f ax, x) is also a tree cut of DTTx, all edges in the cut are included in the tree cut of DTTx. Since any subset of edges in the tree cut ofDTTx cannot separate the graph while C can separate the graph, C cannot be any subset of the tree cut but must be the exact tree cut of DTTx.

证明. 只将一条树边表示为带有结束节点(f ax, x)的树边，其中f轴为x的父节点。对于切割中任何带有结束节点a和b的非树边，将它们之间的树路径表示为p(a,b)。如果a和b都不是inDT Tx或都在DT Tx中，根据深度优先遍历树的结构，p(a,b)将不包含(f ax, x)，但p(a,b)必须包含至少一条切边，因为a和b在被切割C分隔的不同部分，即切边是(f ax, x)之外的树边，这是一个矛盾。它表明,a和b两个节点,一个在DT Tx和其他DT Tx,肯定会发现的非树木树中的边切DT Tx。因为(f ax, x)也是一个树的DT Tx,削减所有边缘都包含在树的DT Tx。因为任何子集树的边缘切ofDT Tx时不能单独的图C可以单独的图形,C不能任何子集树的削减,但必须完全树的DT Tx。

Similarly, the case of two edges can also allow the cut to be found as a tree cut:

类似地，两条边的情况也可以让切割被发现为树切割:

**Lemma 4.** If only two edges of a cut C are tree edges, the cut must be found as a PDTT tree cut.

如果切割C中只有两条边是树边，则该切割必须作为PDTT树切割找到

Proof. Denote the two tree edges as (f ax, x) and (f ay , y) where the depth of y is greater than x, there is:

(1) The two edges must be in the same tree path from y to the root r of the global DTT.

Proof. If (f ax, x) and (f ay , y) are not on the same tree path, the two edges will be on different tree paths to r, i.e., (f ax, x) is on the tree path from x to r and (f ay , y) is on the tree path from y to r, where the join point is above f axand f ay or is just f ax when f ax and f ay are the same node.

Two different nodes, f ax and f ay must be in the same part of the graph separated by C. Or if f ax and f ay are in different parts, because according to the tree structure, the tree path between f ax and f ay will not contain (f ax, x) and (f ay , y) but must contain at least one other tree edge as the cut edge, i.e., the third tree edge as the cut edge, which is a contradiction. 

Accordingly, in a bond it means that x and y are in another part. All nodes in DT Tx must be in the same part as x or there will be a third tree edge as the cut edge because the tree path inside DT Tx will not contain any of (f ax, x) and (f ay , y). It is similar to DT Ty , and all nodes in DT Tx and DT Ty are in the same part as x and y.

All nodes outside DT Tx and DT Ty must be in the same part as f ax andf ay or there will be a third tree edge as the cut edge since the tree path outsideDT Tx and DT Ty will not contain any of (f ax, x) and (f ay , y).

Since each edge in the tree cut of DT Tx and DT Ty has both ends in different parts, they are also edges in cut C. But since DT Tx and DT Ty are not overlapped and y is outside DT Tx, it means that any path between x and ymust contain at least one edge in the tree cut of DT Tx, i.e., must contain at least one cut in C, which contradicts the fact that x and y are in the same part. 

In conclusion, if (f ax, x) and (f ay , y) are not in the same tree path, it will lead to a contradiction.
