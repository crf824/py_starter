import matplotlib
matplotlib.use("Agg")         
import matplotlib.pyplot as plt

matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
matplotlib.rcParams["axes.unicode_minus"] = False   

start_capital = 5_000_000
daily_pnl = [12000, -8000, 25000, 5000, -15000, 30000,
             18000, -5000, 22000, -10000, 27000, 9000]
net_value = [start_capital]
for p in daily_pnl:
	net_value.append(net_value[-1] + p)
days = list(range(len(net_value)))


plt.figue(figsize=(10,8))
plt.plot(days, net_value, marker="o", color="#d62728", linewidth=2, label="账户净值")
plt.axhline(start_capital, color="gray", linestyle="--", label="起始资金 500万")
plt.title("账户净值曲线（模拟 12 个交易日）")
plt.xlabel("交易日")
plt.ylabel("净值（元）")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("净值曲线.png", dpi=120)   # 存成图片，不弹窗
plt.close()

