# ============ 第 4 课：循环 for / while ============
# 核心：让程序"重复干活"。比如连续算 7 天的盈亏，不用手写 7 行。

# ---------- 1) for + range：重复固定次数 ----------
# range(7) 产生 0,1,2,3,4,5,6（从 0 到 6，共 7 个数）
print("=== 模拟连续 7 个交易日 ===")
for day in range(7):
    print("第", day + 1, "个交易日")      # day 从 0 开始，+1 更直观
print("----")

# ---------- 2) 遍历一个"列表"里的每个元素 ----------
# 列表 list 用 [] 包起来，相当于 JS 的数组
pnl_list = [320, -150, 800, 0, -200, 450, 600]     # 一周每笔盈亏
print("=== 逐笔检查盈亏 ===")
for pnl in pnl_list:
    if pnl > 0:
        print("盈利", pnl, "元")
    else:
        print("亏损/持平", pnl, "元")
print("----")

# ---------- 3) 用循环做累加（累计总盈亏） ----------
total = 0
for pnl in pnl_list:
    total = total + pnl          # 每笔都加进 total
print("本周累计盈亏：", total, "元")
print("----")

# ---------- 4) while：条件满足就一直循环 ----------
# 模拟"连亏 3 天就停手"的风控纪律
loss_streak = 0
guard = 0                        # 保险计数器，防止死循环
while loss_streak < 3 and guard < 10:
    print("当前连亏天数：", loss_streak, "（继续交易）")
    loss_streak = loss_streak + 1
    guard = guard + 1
print("达到连亏上限，暂停交易 ⛔")
