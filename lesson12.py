# lesson12.py —— 第12课：异常处理 try/except + 模块拆分 import
import tools   # 导入同目录下的 tools.py（里面是我们写好的函数库）

print("=== 1) try/except 基础：包住会崩的操作 ===")
# 场景：除以 0 在 Python 里会直接红字崩溃；用 try 包住就不崩，程序继续跑
try:
    result = 10 / 0
    print("结果：", result)
except ZeroDivisionError:
    print("捕获到除零错误，已安全跳过，程序继续 ✅")

print("\n=== 2) 读文件容错：文件不存在也不崩 ===")
# 类比 JS 的 try/catch；你以后读行情 CSV 时文件可能还没生成
filename = "不存在的文件.csv"
try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"文件 {filename} 没找到，已跳过（不影响后续）")

print("\n=== 3) 用户输入容错：文字转数字，输错也不崩 ===")
# 实际用 input() 时同理：用户手滑输了字母，int() 会抛 ValueError
user_input = "abc"                 # 假装用户输成了字母
num = tools.safe_int(user_input, default=0)
print(f"用户输入 '{user_input}' 转数字失败，用默认值 {num}")

print("\n=== 4) 模块拆分：调用 tools.py 里的函数 ===")
# tools.py 是我们自己的"工具箱"，import 后直接 tools.xxx() 用
pnl = [500, -300, 1200, -800, 950]
total, win, lose = tools.weekly_report(pnl)
print(f"周报：累计 {total} 元，盈利 {win} 天 / 亏损 {lose} 天")

week_data = {
    "600519": [200, 300, -100, 500, 400],
    "300750": [-200, 150, 300, -50, 250],
}
print("分组周累计：", tools.group_report(week_data))

print("\n=== 5) else / finally：干净的收错与收尾 ===")
# else：没出错才执行；finally：无论对错都执行（常用于关文件/释放资源）
try:
    x = int("123")
except ValueError:
    print("转换失败")
else:
    print(f"转换成功：{x}")
finally:
    print("finally：这里一定执行（比如释放资源）")
