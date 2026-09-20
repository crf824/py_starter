# lesson16.py - 第16课：多只股票净值对比线
# 知识点：字典遍历、zip 配色、复用回撤函数、多条曲线画在同一张图
# 运行：pyv lesson16.py  (用装了 matplotlib 的 venv)

import matplotlib
matplotlib.use("Agg")                                  # 无屏幕环境：只存图不弹窗
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]  # 中文黑体/雅黑
matplotlib.rcParams["axes.unicode_minus"] = False     # 负号正常显示
import matplotlib.pyplot as plt


# ===== 1) 数据：三只股票各 12 天的每日盈亏（模拟，单位元）=====
# 用字典把「股票名 → 每日盈亏列表」配对存起来（第8课学的 dict）
stock_pnl = {
    "600519 贵州茅台": [200, 300, -100, 500, 400, -150, 150, 600, -200, 300, 250, 100],
    "300750 宁德时代": [-150, 200, 300, -50, 250, 100, -300, 400, 150, -100, 200, 300],
    "000858 五粮液":   [100, -50, 200, 150, 300, -100, 250, -200, 100, 200, -150, 400],
}
START_CAPITAL = 1_000_000                            # 每只起始 100 万，公平对比


# ===== 2) 复用第15课的两个函数（封装好直接拿来用）=====
def net_value_series(pnls, start):
    """起始资金 + 逐日累加 → 净值序列"""
    nv = [start]
    for p in pnls:
        nv.append(nv[-1] + p)
    return nv

def max_drawdown(equity):
    """最大回撤：净值从历史最高回落的最大幅度（负数）"""
    peak = equity[0]
    mdd = 0.0
    for x in equity:
        if x > peak:
            peak = x
        dd = (x - peak) / peak
        if dd < mdd:
            mdd = dd
    return mdd


# ===== 3) 画图：三只股票画在同一张图，用不同颜色 + zip 配色 =====
colors = ["#d62728", "#1f77b4", "#2ca02c"]          # 红 / 蓝 / 绿
first_len = len(next(iter(stock_pnl.values())))      # 第一只的盈亏天数（12）
# 净值序列 = [起始] + 12天累加 → 共 13 个点，所以 x 轴要 +1（和净值对齐）
days = list(range(first_len + 1))

fig, ax = plt.subplots(figsize=(11, 6))
# zip 把「股票名+盈亏」和「颜色」一一配对，循环一次画一条线
for (name, pnls), color in zip(stock_pnl.items(), colors):
    nv = net_value_series(pnls, START_CAPITAL)
    mdd = max_drawdown(nv)
    ax.plot(days, nv, marker="o", color=color,
            label=f"{name}  终值{nv[-1]:,}  回撤{mdd:.2%}")

ax.set_title("多只股票净值对比（起始各 100 万）")
ax.set_xlabel("交易日")
ax.set_ylabel("净值（元）")
ax.set_xticks(days)
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig("多股票净值对比.png", dpi=120)


# ===== 4) 打印每只的终值 / 区间收益 / 最大回撤，做个文字小结 =====
print(f"{'股票':<18} {'终值':>14} {'区间收益':>14} {'最大回撤':>10}")
for name, pnls in stock_pnl.items():
    nv = net_value_series(pnls, START_CAPITAL)
    print(f"{name:<18} {nv[-1]:>14,} {nv[-1]-START_CAPITAL:>+14,} {max_drawdown(nv):>10.2%}")
