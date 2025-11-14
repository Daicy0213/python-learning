demoFun(){
 echo "the first shee"
 echo " 1 number"
 read aNam
 
 echo " 2 number"
 read bNam

 return $(($aNam+$bNam))
}

demoFun
echo "the return is $? !"
