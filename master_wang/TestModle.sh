#从包含图中所有节点对的图中一行一行读，然后将节点对的id插入到有像图，然后计算出所有的最小连通性的和




#记录总共的割
allcut=0

#the diret.inp file，也就是有向图的文件名
dirfi=./testsample.inp


#the nodepair.txt 包含所有的节点对
nodepairfi=./nodepair.txt

#用来记录是不是第一次插入 源节点和汇节点  
tempi=1

#从所有节点对的文件里一行一行读，然后插入到有像图的文件里
cat ${nodepairfi} | while read LINE
do



echo "start --------------------"





#1find the the point count.找到一共有几个点,心里有个数，也能通过它来判断全排列有多少
pointcount=`sed -n '1p' ${dirfi} | awk '{print $3}'`
echo "the point count is $pointcount"


#源节点和汇节点的id
sid=`echo $LINE | awk '{print $1}'`
pid=`echo $LINE | awk '{print $2}'`


#如果是第一次插入s点和t点  (这里的逻辑也能到时候变一下，比如每一次把数据搞到程序里)
if(($tempi== 1))
then
#there is no n1s   n2t  so we add the first time  第一次没有

echo "it is the first time there is no n1s n2t"
sed -i '1 a n 1 s' ${dirfi} 
sed -i '2 a n 2 t' ${dirfi}



else
  echo "now we replce the s and t"
  sed -i '2c n '"${sid}"' s' ${dirfi}
  sed -i '3c n '"${pid}"' t' ${dirfi}
  echo "now have replaced it"

fi

echo "now we calculte  the real cut of s=${sid}  t=${pid}"
#现在计算精确解

#把当前带有源点和汇点的文件输入 hi_pr程序，得到结果
hipr_result=`cat ${dirfi} | ../hi_pr | grep "c flow"`
hipr_flow=`echo $hipr_result | awk '{print $3}'`
echo "the ${tempi}th  flow of ${sid} and ${pid} is ${hipr_flow}"


#将这一次算的解加到总共的解里
let allcut+=${hipr_flow}

echo "the allcut is ${allcut}"
#只有第一次是增加之后都是改变第二行和第三行
let tempi+=1

done
#

