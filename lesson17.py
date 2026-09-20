# lesson17.py - 第17课：收益归因柱状图（按板块汇总盈亏）
# 知识点：多列 CSV 读取、用字典按类别汇总(聚合)、matplotlib 柱状图 bar()、涨红跌绿着色
# 运行：pyv lesson17.py  (用装了 matplotlib 的 venv)

import csv
import matplotlib
matplotlib.use("Agg")                                  # 无屏幕环境：只存图不弹窗
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]  # 中文黑体/雅黑
matplotlib.rcParams["axes.unicode_minus"] = False     # 负号正常显示
import matplotlib.pyplot as plt


# ===== 1) 读多列 CSV，并按「板块」聚合盈亏 =====
# trades.csv 每列：sector(板块), pnl(盈亏)。一笔一行，同一板块会出现多次。
# 目标：把同一个板块的所有 pnl 加起来，得到 {板块: 累计盈亏}
by_sector = {}                                         # 汇总字典：板块名 → 该板块总盈亏

with open("trades.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                                       # 跳过表头 sector,pnl
    for row in reader:
        sector = row[0]                                # 第1列：板块
        pnl = int(row[1])                              # 第2列：盈亏（转成整数）
        # —— 聚合核心写法：同一板块累加（dict.get 给默认值 0）——
        by_sector[sector] = by_sector.get(sector, 0) + pnl

# 按盈亏从高到低排序，看图更直观。items() 返回 [(板块,盈亏), ...]
items = sorted(by_sector.items(), key=lambda kv: kv[1], reverse=True)
sectors = [k for k, v in items]                        # 板块名列表
totals  = [v for k, v in items]                        # 对应盈亏列表


# ===== 2) 画柱状图 =====
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(sectors, totals)                          # 柱子的高度 = 各板块盈亏

# 涨红跌绿：赚的用红色，亏的用绿色（A股习惯，和美股相反）
for bar, v in zip(bars, totals):
    bar.set_color("#d62728" if v >= 0 else "#2ca02c")

ax.axhline(0, color="black", linewidth=0.8)            # 0 基准线
ax.set_title("各板块收益归因（模拟 12 笔交易）")
ax.set_ylabel("盈亏（元）")
ax.grid(axis="y", alpha=0.3)

# 每根柱子上方/下方标注具体金额
for bar, v in zip(bars, totals):
    ax.text(bar.get_x() + bar.get_width() / 2, v,
            f"{v:,}", ha="center", va="bottom" if v >= 0 else "top")

fig.tight_layout()
fig.savefig("收益归因柱状图.png", dpi=120)


# ===== 3) 打印文字小结 =====
print("板块收益归因（从高到低）：")
for s, t in items:
    print(f"  {s:<8} {t:>+10,}")
print(f"\n总盈亏：{sum(totals):+,}")
