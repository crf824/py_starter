# ===== 第 2 课：变量 =====
# 变量 = 给一个"盒子"贴标签，往里塞数据，以后用标签就能拿到数据
# 类比前端：let name = "何执舵"  —— Python 里不用写 let，直接 名字 = 值

# 1) 字符串(string)：包在引号里的文字，跟 JS 的 "..." 一样
name = "何执舵"
print("名字是：", name)

# 2) 整数(int)：没有小数点的数字
age = 30
print("年龄是：", age)

# 3) 浮点数(float)：带小数点的数字
price = 12.5
print("股价是：", price)

# 4) 变量之间能直接做算术（跟计算器一样）
a = 10
b = 3
print("a + b =", a + b)        # 加
print("a - b =", a - b)        # 减
print("a * b =", a * b)        # 乘
print("a / b =", a / b)        # 除，结果是 3.333...（带小数）
print("a // b =", a // b)      # 整除，只留整数 3
print("a % b =", a % b)        # 取余数 1

# 5) 用变量"记账"——给你一个交易场景感受一下
hold_count = 1000          # 持仓股数
buy_price = 8.2            # 买入价
sell_price = 9.5           # 卖出价
profit = (sell_price - buy_price) * hold_count   # 总盈利
print("这笔交易盈利：", profit, "元")

# 6) 变量可以随时"换盒子里的内容"
counter = 0
print("初始计数：", counter)
counter = counter + 1      # 自己加 1（前端里常写成 counter++，Python 里要写全）
print("加 1 后：", counter)
