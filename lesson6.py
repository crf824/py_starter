# ============ 第 6 课：读写文件 ============
# 核心：把数据"落盘"存成本地文件，下次打开电脑还能看。相当于前端的 localStorage。

# 先准备一份要存的数据（复用前面的思路）
report_lines = [
    "短线进化团 - 周复盘报告",
    "====================",
    "第 1 周：累计 1820 元 | 盈利 4 天 亏损 2 天",
    "第 2 周：累计 1550 元 | 盈利 3 天 亏损 2 天",
    "结论：出手偏少，继续执行克制纪律 👊",
]

# ---------- 1) 写文件：把报告存成 .txt ----------
# open(文件名, "w")  = 写模式（w 会覆盖原文件；想追加用 "a"）
# with ... as f:     = 自动帮你关文件，不用手动 f.close()
with open("report.txt", "w", encoding="utf-8") as f:
    for line in report_lines:
        f.write(line + "\n")     # 每行末尾加换行
print("✅ 报告已写入 report.txt")

# ---------- 2) 读文件：把刚才存的读回来 ----------
print("---- 读回内容 ----")
with open("report.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 一次性读全部
print(content)

# ---------- 3) 另一种读法：一行一行读（适合大文件） ----------
print("---- 逐行读 ----")
with open("report.txt", "r", encoding="utf-8") as f:
    for line in f:              # 文件本身可迭代，逐行吐出
        print("> ", line.strip())   # strip() 去掉首尾换行/空格

# ---------- 4) 写 CSV（用逗号分隔，Excel 能直接打开） ----------
with open("pnl.csv", "w", encoding="utf-8") as f:
    f.write("周次,累计盈亏,盈利天数,亏损天数\n")   # 表头
    f.write("第1周,1820,4,2\n")
    f.write("第2周,1550,3,2\n")
print("✅ 数据已写入 pnl.csv（可用 Excel 打开）")
