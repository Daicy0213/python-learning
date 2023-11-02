"""剩余天数计算器
"""
from datetime import datetime

# 目标日期
target_date = datetime.strptime('2023-11-3', '%Y-%m-%d')

# 当前日期
current_date = datetime.now()

# 判断目标日期是否小于当前日期
if target_date < current_date:
    print("目标日期已经过去")
else:
    # 计算剩余天数
    remaining_days = (target_date - current_date).days + 1
    print("距离目标日期还有", remaining_days, "天")
