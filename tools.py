# tools.py —— 复盘工具函数库
# 只放函数定义，不在顶层执行任何代码（这样被 import 时不会乱跑）
# 以后 lesson12.py 用 import tools 调用这里的函数

def weekly_report(pnl_list):
    """输入一周每日盈亏列表，返回 (总盈亏, 盈利天数, 亏损天数)"""
    total = 0
    win = 0
    lose = 0
    for pnl in pnl_list:
        total += pnl
        if pnl > 0:
            win += 1
        elif pnl < 0:
            lose += 1
    return total, win, lose


def group_report(week_data):
    """输入 {代码: [每日盈亏]}，返回每只股票周累计的字典"""
    result = {}
    for code, days in week_data.items():
        result[code] = sum(days)
    return result


def safe_int(text, default=0):
    """把文字安全转成整数；转不了（比如输成字母）就返回 default"""
    try:
        return int(text)
    except ValueError:
        return default
