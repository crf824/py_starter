# ============ 第 8 课：字典 dict ============
# 核心：存「键 → 值」的配对数据，比如 股票代码 → 盈亏。
# 类比前端：就是 JS 里的对象 {}（或 Map）。

# ---------- 1) 创建字典：股票代码 → 当日盈亏(元) ----------
pnl = {
    "600519": 1200,     # 贵州茅台
    "300750": -300,     # 宁德时代
    "002594": 800,      # 比亚迪
}
print("字典内容：", pnl)
print("----")

# ---------- 2) 取值 / 改值 / 加新键 ----------
print("茅台盈亏：", pnl["600519"])        # 用键取值
pnl["600519"] = 1500                       # 改值
pnl["000858"] = 600                        # 加一只新股票（之前没有的键）
print("改完后的字典：", pnl)
print("----")

# ---------- 3) 遍历字典（key + value 一起拿） ----------
print("=== 逐只股票盈亏 ===")
for code, money in pnl.items():            # .items() 同时给 键 和 值
    if money > 0:
        print(code, "盈利", money)
    else:
        print(code, "亏损", money)
print("----")

# ---------- 4) 判断键在不在（避免取不存在的键报错） ----------
if "600519" in pnl:
    print("茅台在持仓里")
# print(pnl["999999"])   # 这样会报错 KeyError；先用 in 判断 或 用 .get()
print("用 .get 安全取值：", pnl.get("999999", "无此持仓"))   # 取不到给默认值
print("----")

# ---------- 5) 实战：把复盘工具升级成「按股票分组」 ----------
from datetime import datetime

# 一周里每只股票每天的盈亏（这里用嵌套：股票 → 列表）
week_data = {
    "600519": [200, 300, -100, 500, 400],
    "300750": [-150, 100, -200, 250, 300],
    "002594": [800, -300, 500, 200, 600],
}

total_all = 0
report = []
for code, daily in week_data.items():
    s = 0
    for m in daily:                       # 第 4 课 循环嵌套
        s = s + m
    total_all = total_all + s
    report.append(f"{code} 周累计 {s} 元")

today = datetime.now().strftime("%Y-%m-%d")
print(f"📅 {today} 分组复盘")
for line in report:
    print("  ", line)
print("全市场累计：", total_all, "元")

# 落盘（复用第 6 课 文件写入）
with open("report.txt", "a", encoding="utf-8") as f:
    f.write(f"{today} 分组复盘 | 全市场累计 {total_all} 元\n")
print("✅ 已追加到 report.txt")
