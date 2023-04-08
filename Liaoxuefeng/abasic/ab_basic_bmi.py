"""
四.条件判断
"""
# 输入身高(cm)和体重(kg),计算bmi来判断体重是否过重
h = input('height:')
w = input('weight:')
height = int(h) / 100
weight = int(w)
bmi = weight / height ** 2
print(bmi)
print('BMI: %.2f' % bmi)
if bmi < 18.5:
    print('体重过轻')
elif bmi < 25:
    print('体重正常')
elif bmi < 28:
    print('体重过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
