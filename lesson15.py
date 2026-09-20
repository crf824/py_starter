# lesson15.py - 第15课：最大回撤 + 净值曲线回撤阴影
# 知识点：函数封装、遍历求历史峰值、绘图 fill_between 阴影、🐍Python ↔ 🌐JS 对照
# 运行：pyv lesson15.py  (用装了 matplotlib 的 venv)

import csv
import matplotlib
matplotlib.use("Agg")                                  # 无屏幕环境：只存图不弹窗
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]  # 中文黑体/雅黑
matplotlib.rcParams["axes.unicode_minus"] = False     # 负号正常显示
import matplotlib.pyplot as plt

CSV_FILE = "pnl_data.csv"
START_CAPITAL = 5_000_000                            # 起始资金 500 万
START_DATE = "建仓日"


# ---- 1) 读 CSV：把"文件里的文字"变成程序能算的列表 ----
dates = [START_DATE]        # x 轴标签，开头补一个建仓日，和净值长度对齐
pnls = []                  # 每日盈亏
with open(CSV_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)           # 跳过表头 date,pnl
    for row in reader:
        dates.append(row[0])
        pnls.append(int(row[1]))


# ---- 2) 算净值序列：起始资金 + 逐日累加 ----
net_value = [START_CAPITAL]
for p in pnls:
    net_value.append(net_value[-1] + p)


# ---- 3) 两个核心函数：历史峰值序列 & 最大回撤 ----
def peak_series(equity):
    """返回每个时点对应的'历史最高水位'列表（用于画灰色虚线 + 回撤阴影）"""
    peaks = []
    peak = equity[0]
    for x in equity:
        if x > peak:
            peak = x
        peaks.append(peak)
    return peaks


def max_drawdown(equity):
    """最大回撤：净值从历史最高回落的最大幅度（负数，如 -0.05 = 回撤 5%）"""
    peak = equity[0]
    mdd = 0.0                                  # 0 代表没回撤；只会越跌越负
    for x in equity:
        if x > peak:
            peak = x                           # 刷新历史最高
        dd = (x - peak) / peak                # 当前相对峰值的回撤比例
        if dd < mdd:
            mdd = dd                           # 记住最惨的那次
    return mdd


peaks = peak_series(net_value)
mdd = max_drawdown(net_value)
days = list(range(len(net_value)))             # x 轴刻度：[0,1,2,...]


# ---- 4) 画图：净值红线 + 历史水位灰虚线 + 回撤红阴影 ----
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(days, net_value, color="#d62728", marker="o", linewidth=2, label="账户净值")
ax.plot(days, peaks, color="#7f7f7f", linestyle="--", linewidth=1.2, label="历史最高水位")
# fill_between：在 net_value 和 peaks 两条线之间填充 → 直观看到"回落区"
ax.fill_between(days, net_value, peaks, color="#d62728", alpha=0.15, label="回撤区")

ax.set_title(f"账户净值与最大回撤（最大回撤 {mdd:.2%}）")
ax.set_xlabel("交易日")
ax.set_ylabel("净值（元）")
ax.set_xticks(days)
ax.set_xticklabels(dates, rotation=45, ha="right")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig("净值曲线_回撤.png", dpi=120)

print(f"读取交易日数：{len(pnls)} 天")
print(f"起始净值：{START_CAPITAL:,} 元")
print(f"最终净值：{net_value[-1]:,} 元")
print(f"区间收益：{net_value[-1] - START_CAPITAL:,} 元")
print(f"最大回撤：{mdd:.2%}")
