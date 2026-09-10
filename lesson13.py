# lesson13.py —— 第13课：用 matplotlib 画账户净值曲线图
# 这台机器没有屏幕，必须用 Agg 后端把图"存成文件"而不是"弹窗显示"
import matplotlib
matplotlib.use("Agg")          # 关键：无显示环境，先指定后端再 import pyplot
import matplotlib.pyplot as plt

# 让图里的中文正常显示（Windows 自带黑体/雅黑，否则中文会变成方块）
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
matplotlib.rcParams["axes.unicode_minus"] = False   # 解决负号显示成方块的问题

# 模拟你的账户：500 万起步，12 个交易日的每日盈亏
start_capital = 5_000_000          # 数字里的下划线是千分位分隔，纯好看，等价于 5000000
daily_pnl = [12000, -8000, 25000, 5000, -15000, 30000,
             18000, -5000, 22000, -10000, 27000, 9000]

# 计算每日收盘净值：第 0 天=起始资金，之后逐日累加
net_value = [start_capital]
for p in daily_pnl:
    net_value.append(net_value[-1] + p)
days = list(range(len(net_value)))   # [0, 1, 2, ..., 12]

# ---- 画图 ----
plt.figure(figsize=(10, 5))
# 净值线：用红色（A股习惯：红=涨/资产上行），圆点标记每个交易日
plt.plot(days, net_value, marker="o", color="#d62728", linewidth=2, label="账户净值")
# 一条灰色虚线标出起始资金，方便看盈亏水位
plt.axhline(start_capital, color="gray", linestyle="--", label="起始资金 500万")
plt.title("账户净值曲线（模拟 12 个交易日）")
plt.xlabel("交易日")
plt.ylabel("净值（元）")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("净值曲线.png", dpi=120)   # 存成图片，不弹窗
plt.close()

# 顺便在终端打印关键数字（f-string 千分位格式化）
print("✅ 图已保存为 净值曲线.png")
print(f"起始净值：{net_value[0]:,} 元")
print(f"最终净值：{net_value[-1]:,} 元")
print(f"区间收益：{net_value[-1] - net_value[0]:,} 元")
