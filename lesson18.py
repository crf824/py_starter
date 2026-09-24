# lesson18.py - 第18课：用 Pandas 一行搞定板块收益归因
# 知识点：pandas 读 CSV → DataFrame、groupby 聚合、sort_values 排序、画柱状图（复用 matplotlib）
# 运行：pyv lesson18.py  (venv 里已有 pandas / numpy)

import pandas as pd
import matplotlib
matplotlib.use("Agg")                                  # 无屏幕：只存图
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
matplotlib.rcParams["axes.unicode_minus"] = False
import matplotlib.pyplot as plt


# ===== 1) 读 CSV：一行变成一个"表格对象" DataFrame =====
df = pd.read_csv("trades.csv")                         # 列：sector(板块), pnl(盈亏)
print("原始表（前几行）：")
print(df.head(), "\n")


# ===== 2) 按板块汇总盈亏 =====
# 第17课你用手搓字典写了 8 行；用 Pandas 只要「一行链式调用」：
result = (df.groupby("sector")["pnl"]                 # 按板块分组，只取 pnl 列
            .sum()                                     # 每组求和
            .sort_values(ascending=False))             # 从高到低排序
print("板块归因（Pandas 一行搞定）：")
print(result, "\n")


# ===== 3) 画图（和第17课一样用 matplotlib，但数据来自 DataFrame）=====
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(result.index, result.values)
for bar, v in zip(bars, result.values):
    bar.set_color("#d62728" if v >= 0 else "#2ca02c")  # 涨红跌绿
ax.axhline(0, color="black", linewidth=0.8)
ax.set_title("各板块收益归因（Pandas 版）")
ax.set_ylabel("盈亏（元）")
ax.grid(axis="y", alpha=0.3)
for bar, v in zip(bars, result.values):
    ax.text(bar.get_x() + bar.get_width() / 2, v,
            f"{v:,}", ha="center", va="bottom" if v >= 0 else "top")
fig.tight_layout()
fig.savefig("收益归因_Pandas版.png", dpi=120)


# ===== 4) 文字小结 =====
print(f"总盈亏：{result.sum():+,}")
print(f"赚钱板块数：{(result > 0).sum()} / 总板块数：{result.shape[0]}")
