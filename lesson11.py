# lesson11.py - 第11课：元组 tuple / 集合 set / 推导式 comprehension
# 类比前端：元组≈const数组(定好不改)，集合≈JS的Set(去重)，推导式≈一行map+filter

print("=== 1) 元组 tuple：定好就改不了的小盒子 ===")
# 元组用圆括号，常用来存"成对/成组且不应被改动"的数据
trade = ("600519", 1200)          # (股票代码, 盈亏)
print("一笔交易：", trade)
print("取代码：", trade[0], "取盈亏：", trade[1])

# 解包：一次性把元组里的值分给多个变量（函数多返回值就是这原理）
code, money = trade
print("解包后 -> code:", code, "money:", money)

# 不可变：下面这行若取消注释会报错 TypeError: 'tuple' object does not support item assignment
# trade[1] = 999   # 元组不能改，强行改会崩 —— 这正是它比列表"安全"的地方

# 元组能当字典的键（因为不可变），列表不行
pos = {("600519", "2026-09-10"): 1200}   # 用(代码,日期)作键，避免同日重名冲突
print("按(代码,日期)查盈亏：", pos[("600519", "2026-09-10")])

print("\n=== 2) 集合 set：自动去重 + 集合运算 ===")
# 你关注了多个板块，一只股票可能同时属于几个板块，去重看一共多少只
chip = {"600519", "300750", "002049"}          # 芯片板块
robot = {"300750", "002472", "601012"}          # 机器人板块
print("芯片板块：", chip)
print("机器人板块：", robot)

all_stocks = chip | robot        # 并集：两个板块合起来自动去重
print("去重后共关注：", all_stocks)
common = chip & robot            # 交集：同时属于两个板块
print("同时在两个板块的：", common)
only_chip = chip - robot         # 差集：只在芯片、不在机器人
print("只在芯片板块的：", only_chip)

print("\n=== 3) 列表推导式：一行批量算 ===")
pnl = [500, -300, 1200, -800, 950, -200]
doubled = [x * 2 for x in pnl]               # 每笔盈亏翻倍(模拟杠杆)
print("翻倍后：", doubled)
wins = [x for x in pnl if x > 0]             # 只留盈利的笔
print("盈利的笔：", wins)
net = [x - 5 for x in pnl if x > 0]          # 盈利笔再扣5元手续费
print("盈利笔扣5元手续费：", net)

print("\n=== 4) 字典推导式：一行批量建字典 ===")
codes = ["600519", "300750", "002049"]
track = {c: [] for c in codes}               # 给每只股票初始化一个空盈亏列表
print("初始化跟踪表：", track)
pnl_map = {"600519": 1200, "300750": -300}
reversed_map = {v: k for k, v in pnl_map.items()}   # 反转 代码:盈亏 -> 盈亏:代码
print("反转后(盈亏:代码)：", reversed_map)

print("\n=== 5) 集合推导式：一行去重 ===")
raw_nums = [1, 2, 2, 3, 3, 3, 5]
uniq = {x for x in raw_nums}
print("去重结果：", uniq)

print("\n=== 6) 综合：用推导式给持仓做统计 ===")
week_data = {
    "600519": [200, 300, -100, 500, 400],
    "300750": [-200, 150, 300, -50, 250],
}
week_total = {code: sum(days) for code, days in week_data.items()}  # 每只周累计
print("每只周累计：", week_total)
good = [code for code, t in week_total.items() if t > 0]            # 周累计为正的
print("本周赚钱的股票：", good)
