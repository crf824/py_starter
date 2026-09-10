# ============ 第 7 课：综合小项目「短线复盘小工具」 ============
# 把前 6 课学的全串起来：变量 / if / for / 函数 / 文件读写
# 用法：改最下面的 week_pnl，然后 py lesson7.py 跑一遍

from datetime import datetime


# ---------- 函数：算一周盈亏报告（第 5 课 def） ----------
def weekly_report(pnl_list):
    total = 0
    win = 0
    lose = 0
    for pnl in pnl_list:               # 第 4 课 for 循环
        total = total + pnl
        if pnl > 0:                     # 第 3 课 if 判断
            win = win + 1
        elif pnl < 0:
            lose = lose + 1
    return total, win, lose


# ---------- 函数：给这周打个评语（第 3 课 多分支） ----------
def verdict(total, win, lose):
    if total > 0 and win >= lose:
        return "✅ 盈利且胜率不差，节奏 OK"
    elif total > 0:
        return "⚠️ 总账盈利但输多赢少，注意出手质量"
    else:
        return "❌ 本周亏损，严格执行克制纪律，少动"


# =================== 主程序 ===================
# 👇 这里换成你自己的数据（单位：元，正数盈利 / 负数亏损）
week_pnl = [320, -150, 800, 0, -200, 450, 600]

total, win, lose = weekly_report(week_pnl)
comment = verdict(total, win, lose)

today = datetime.now().strftime("%Y-%m-%d")

# 屏幕输出（第 1 课 print）
print("📅", today, "复盘")
print("累计盈亏：", total, "元")
print("盈利", win, "天，亏损", lose, "天")
print(comment)

# 落盘：追加写入 report.txt（第 6 课 文件 + 第 2 课 变量）
with open("report.txt", "a", encoding="utf-8") as f:
    f.write(f"{today} | 累计 {total} 元 | 盈{win}/亏{lose} | {comment}\n")

print("✅ 已追加一行到 report.txt")
