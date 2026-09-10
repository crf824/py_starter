# lesson14.py —— 第14课：从 CSV 读真实复盘数据，画账户净值曲线
import csv                                   # Python 自带的标准库，专门读/写 CSV
import matplotlib
matplotlib.use("Agg")                        # 无屏幕环境：只存图不弹窗（同第13课）
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]  # 中文显示
matplotlib.rcParams["axes.unicode_minus"] = False                        # 负号正常
import matplotlib.pyplot as plt

CSV_FILE = "pnl_data.csv"
START_CAPITAL = 5_000_000                    # 起始资金 500 万
START_DATE = "2026-08-21"                   # 建仓日（第 0 天，对应起始资金）

# ---- 1) 读 CSV：把"文件里的文字"变成程序能算的列表 ----
dates = [START_DATE]   # x 轴第一个点 = 建仓日；先放进去，保证和 net_value 一样长(13)
pnls = []              # 存每行的每日盈亏，用来累加净值
try:
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)               # 得到一个"逐行读取"的对象
        next(reader)                         # 跳过第一行表头 date,pnl
        for row in reader:                   # 每一行 row 是个列表：[日期, 盈亏]
            dates.append(row[0])             # row[0] = 日期字符串
            pnls.append(int(row[1]))         # row[1] = 盈亏，转成整数
except FileNotFoundError:
    print(f"找不到文件 {CSV_FILE}，请确认它在同目录下")
    raise

# ---- 2) 算每日净值：起始资金 + 逐日累加（同第13课逻辑）----
net_value = [START_CAPITAL]
for p in pnls:
    net_value.append(net_value[-1] + p)

# ---- 3) 画图：x 轴用真实日期，不再是 0,1,2... ----
plt.figure(figsize=(11, 5))
plt.plot(dates, net_value, marker="o", color="#d62728", linewidth=2, label="账户净值")
plt.axhline(START_CAPITAL, color="gray", linestyle="--", label="起始资金 500万")
plt.title("账户净值曲线（数据来自 CSV 复盘记录）")
plt.xlabel("交易日")
plt.ylabel("净值（元）")
plt.xticks(rotation=45)                      # 日期太长，斜着显示避免重叠
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("净值曲线_来自CSV.png", dpi=120)
plt.close()

print("✅ 图已保存为 净值曲线_来自CSV.png")
print(f"读取交易日数：{len(dates)} 天")
print(f"起始净值：{net_value[0]:,} 元")
print(f"最终净值：{net_value[-1]:,} 元")
print(f"区间收益：{net_value[-1] - net_value[0]:,} 元")
