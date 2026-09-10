# ============ 第 5 课：函数 def ============
# 核心：把一段逻辑"打包"成工具，以后喂数据就出结果，不用重写循环。

# ---------- 1) 定义一个函数：算一周盈亏报告 ----------
# def 函数名(参数):    冒号 + 缩进 还是那套规则
def weekly_report(pnl_list):
    total = 0
    win = 0
    lose = 0
    for pnl in pnl_list:
        total = total + pnl
        if pnl > 0:
            win = win + 1
        elif pnl < 0:
            lose = lose + 1
    # return 把结果"交出来"，交给调用者
    return total, win, lose


# ---------- 2) 调用函数（喂不同的数据） ----------
week1 = [320, -150, 800, 0, -200, 450, 600]
week2 = [500, -300, 1200, -800, 950]

t1, w1, l1 = weekly_report(week1)     # 用逗号一次接住多个返回值
t2, w2, l2 = weekly_report(week2)

print("第 1 周：累计", t1, "元 | 盈利", w1, "天 亏损", l1, "天")
print("第 2 周：累计", t2, "元 | 盈利", w2, "天 亏损", l2, "天")
print("----")

# ---------- 3) 参数可以设"默认值" ----------
# 比如默认风控上限是连亏 3 天（不用每次传）
def risk_stop(loss_streak, limit=3):
    if loss_streak >= limit:
        return "⛔ 停手"
    return "✅ 继续"

print(risk_stop(2))          # 不传 limit，用默认的 3
print(risk_stop(4))          # 4 >= 3 → 停手
print(risk_stop(4, 5))       # 传了 5，变成上限 5 → 4<5 继续
print("----")

# ---------- 4) 没有 return，函数也能"做事"（只打印） ----------
def greet(name):
    print("你好，", name, "，今天也要克制交易 👊")

greet("何执舵")
