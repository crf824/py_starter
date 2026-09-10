# ============ 第 9 课：函数封装 + 键盘输入 input() ============
# 目标：把第 8 课的分组复盘打包成一个函数，再加「手动输入数据」的入口，
#       让它变成真正能天天用的小工具。

from datetime import datetime


# ---------- 1) 打包成函数：给数据，出报告 ----------
def group_report(week_data):
    """week_data: {股票代码: [每天盈亏,...]}  返回 (各行报告, 全市场累计)"""
    report = []
    total_all = 0
    for code, daily in week_data.items():
        s = 0
        for m in daily:
            s = s + m
        total_all = total_all + s
        report.append(f"{code} 周累计 {s} 元")
    return report, total_all


# ---------- 2) 演示调用（直接用现成数据） ----------
sample = {
    "600519": [200, 300, -100, 500, 400],
    "300750": [-150, 100, -200, 250, 300],
    "002594": [800, -300, 500, 200, 600],
}

lines, total = group_report(sample)
today = datetime.now().strftime("%Y-%m-%d")
print(f"📅 {today} 分组复盘（演示）")
for line in lines:
    print("  ", line)
print("全市场累计：", total, "元")

# 落盘
with open("report.txt", "a", encoding="utf-8") as f:
    f.write(f"{today} 演示复盘 | 全市场累计 {total} 元\n")
print("✅ 已追加到 report.txt")
print("----")


# ---------- 3) 键盘输入版（只在你真在终端里跑时才启用） ----------
import sys

if len(sys.argv) > 1 and sys.argv[1] == "input":   # 只有敲 `py lesson9.py input` 才进手动录入
    print("=== 手动录入模式（输入空行结束）===")
    user_data = {}
    while True:
        code = input("股票代码（空行结束）: ").strip()
        if code == "":
            break
        raw = input("这周每天盈亏，用空格分开: ").strip()
        # 把输入的文字变成数字列表： "200 300 -100" -> [200, 300, -100]
        nums = [int(x) for x in raw.split()]
        user_data[code] = nums

    if user_data:
        lines2, total2 = group_report(user_data)
        print(f"\n📅 你的复盘")
        for line in lines2:
            print("  ", line)
        print("全市场累计：", total2, "元")
        with open("report.txt", "a", encoding="utf-8") as f:
            f.write(f"{today} 手动复盘 | 全市场累计 {total2} 元\n")
        print("✅ 已追加到 report.txt")
