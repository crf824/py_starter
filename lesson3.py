# ============ 第 3 课：条件判断 if ============
# 核心：让程序"做选择"。赚到了就落袋，亏了就止损。

# 一笔交易的盈亏（元）
profit = 1300
cost = 8000          # 这笔动用的成本

# 1) 最基础：if + else（二选一）
if profit > 0:
    print("✅ 盈利，可以落袋")
else:
    print("❌ 亏损，考虑止损")

print("----")

# 2) 多分支：if / elif / else（三个及以上选项）
# 按"盈亏比例"给这笔交易评级
rate = profit / cost          # 收益率

if rate >= 0.10:
    print("🌟 大赚（收益率 ≥ 10%）")
elif rate >= 0.03:
    print("👍 小赚（收益率 3%~10%）")
elif rate > 0:
    print("😐 微赚（收益率 0~3%）")
else:
    print("⚠️ 亏损，注意风控")

print("----")

# 3) 组合判断：and / or（多个条件同时成立 / 任一成立）
hold_days = 2
is_hot = True

if profit > 0 and hold_days <= 3:
    print("达标：盈利且持股不超过 3 天，符合短线纪律")

if profit > 500 or is_hot:
    print("满足：盈利超 500 元 或 是热点题材，值得关注")

print("----")

# 4) 容易踩的坑：== 才是"等于"，= 是"装进去"
guess = 5
if guess == 5:        # 注意是两个等号
    print("猜对了（用 == 比较）")
# if guess = 5:      # 这样写会报错！= 是赋值不是比较
