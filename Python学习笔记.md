# Python 学习笔记（含前端 JS 对照）

> 适用对象：有前端经验、后端薄弱的学员。
> 阅读约定：每节课都给「🐍 Python 写法」和「🌐 前端 JS 写法」对照，用你熟悉的前端概念搭桥。
> 运行约定：自己终端里，普通脚本用 `py xxx.py`；用第三方库（如画图）的脚本用 `pyv xxx.py`。

---

## 目录
1. [print 输出](#第1课-print-输出)
2. [变量与数据类型](#第2课-变量与数据类型)
3. [条件判断 if](#第3课-条件判断-if)
4. [循环 for / while](#第4课-循环-for--while)
5. [函数 def](#第5课-函数-def)
6. [文件读写](#第6课-文件读写)
7. [综合小项目](#第7课-综合小项目短线复盘小工具)
8. [字典 dict](#第8课-字典-dict)
9. [函数封装 + 键盘输入](#第9课-函数封装--键盘输入-input)
10. [列表 / 字符串进阶](#第10课-列表--字符串进阶)
11. [元组 / 集合 / 推导式](#第11课-元组--集合--推导式)
12. [异常处理 + 模块拆分](#第12课-异常处理--模块拆分)
13. [画净值曲线（matplotlib）](#第13课-画净值曲线matplotlib)
14. [从 CSV 读数据画图](#第14课-从-csv-读数据画图)
15. [最大回撤 + 回撤阴影](#第15课-最大回撤--回撤阴影)
16. [多只股票净值对比线](#第16课-多只股票净值对比线)
17. [收益归因柱状图（按板块汇总）](#第17课-收益归因柱状图按板块汇总)

---

## 第1课：print 输出

**核心知识点**
- `print(...)` 把内容显示到屏幕
- 文字用双引号 `"..."` 包起来，叫「字符串」
- 每个 `.py` 文件是一段小程序，用 `python`/`py` 命令运行

**🐍 Python**
```python
print("你好，世界！")
print("这一行和上一行是分开的两句话")
```

**🌐 前端 JS**
```javascript
console.log("你好，世界！");
console.log("这一行和上一行是分开的两句话");
```
> 类比：`print()` ≈ `console.log()`；`.py` 文件 ≈ `.js` 文件（都要一个解释器来跑）。

**⚠️ 易踩的坑**
- 自己终端用 `py` 命令，不是 `python`（python 只在 WorkBuddy 内有效）。

---

## 第2课：变量与数据类型

**核心知识点**
- 赋值不用写 `let`/`var`，直接 `名字 = 值`
- `=` 是「装进去」，不是「等于」
- 常见类型：字符串 `str`、整数 `int`、浮点数 `float`
- 整除 `//`、取余 `%`
- 小数计算有精度尾巴（正常现象）

**🐍 Python**
```python
name = "何执舵"        # 字符串 str
age = 30               # 整数 int
price = 12.5          # 浮点 float
print(10 // 3)         # 整除 → 3
print(10 % 3)          # 取余 → 1
profit = (9.5 - 8.2) * 1000
print(profit)          # 1300.0000000000007（浮点尾巴，正常）
```

**🌐 前端 JS**
```javascript
let name = "何执舵";    // 字符串
let age = 30;          // 数字（JS 不区分 int/float）
let price = 12.5;
console.log(Math.floor(10 / 3));  // 整除 → 3
console.log(10 % 3);             // 取余 → 1
let profit = (9.5 - 8.2) * 1000;
console.log(profit);   // 1300.0000000000007（同样有尾巴）
```
> 类比：Python 的 `name = "x"` 就是 JS 的 `let name = "x"`；Python 把整数/小数分得清，JS 统一叫 number。

**⚠️ 易踩的坑**
- `=` 是赋值，`==` 才叫「等于比较」（第 3 课会用到）。

---

## 第3课：条件判断 if

**核心知识点**
- `if / elif / else` 做分支选择
- 行尾用**冒号 `:`**，代码块靠**缩进**（没有大括号）
- 逻辑词用 `and` / `or`（不是 `&&` / `||`）
- 缩进必须对齐，同一层是一伙的

**🐍 Python**
```python
profit = 500
if profit > 0:
    print("落袋")
elif profit == 0:
    print("平盘")
else:
    print("止损")
```

**🌐 前端 JS**
```javascript
let profit = 500;
if (profit > 0) {
    console.log("落袋");
} else if (profit === 0) {
    console.log("平盘");
} else {
    console.log("止损");
}
```
> 类比：Python 用 `:` + 缩进来代替 JS 的 `{ }`；`elif` = JS 的 `else if`；`and/or` = JS 的 `&&/||`。

**⚠️ 易踩的坑**
- 缩进不对会报错或逻辑错乱（Python 看缩进，不看大括号）。
- `==` 比较、`=` 赋值，别混。

---

## 第4课：循环 for / while

**核心知识点**
- `for x in range(n):` 自动数 0~n-1
- `range(a, b)` 左闭右开（含 a 不含 b）
- `while` 要能让条件变假，否则死循环
- 加 `guard` 计数器防死循环是好习惯

**🐍 Python**
```python
for day in range(7):          # 0,1,2,3,4,5,6
    print("第", day + 1, "天")

loss = 0
guard = 0
while loss < 3 and guard < 100:   # 双保险防死循环
    loss += 1
    guard += 1
```

**🌐 前端 JS**
```javascript
for (let day = 0; day < 7; day++) {   // 0~6
    console.log("第", day + 1, "天");
}

let loss = 0;
let guard = 0;
while (loss < 3 && guard < 100) {
    loss++;
    guard++;
}
```
> 类比：`range(7)` ≈ JS 的 `for(let i=0;i<7;i++)`；`and` ≈ `&&`；遍历列表用 `for x in 列表` ≈ JS 的 `arr.forEach(x => ...)`。

**⚠️ 易踩的坑**
- `range(7)` 不含 7（左闭右开），想数 1~7 写 `range(1, 8)`。

---

## 第5课：函数 def

**核心知识点**
- `def 名(参数):` 定义函数
- 可一次返回多个值 `return a, b`（自动打包）
- 默认参数放最后
- 函数不一定要 return

**🐍 Python**
```python
def weekly_report(pnl_list, limit=3):
    total = sum(pnl_list)
    win = sum(1 for p in pnl_list if p > 0)
    return total, win             # 一次返回两个值

t, w = weekly_report([100, -50, 200])
print(t, w)
```

**🌐 前端 JS**
```javascript
function weeklyReport(pnlList, limit = 3) {
    let total = pnlList.reduce((a, b) => a + b, 0);
    let win = pnlList.filter(p => p > 0).length;
    return { total, win };          // 返回一个对象
}
let { total, win } = weeklyReport([100, -50, 200]);
console.log(total, win);
```
> 类比：`def` ≈ `function`；Python 能直接 `return a, b` 多个值，JS 通常包成一个对象返回；下划线命名 `weekly_report` 是 Python 习惯。

**⚠️ 易踩的坑**
- 默认参数必须写在参数列表最后。

---

## 第6课：文件读写

**核心知识点**
- `with open(...) as f:` 自动关文件
- 模式：`"w"` 覆盖、`"a"` 追加、`"r"` 读（默认）
- 中文必须加 `encoding="utf-8"`
- CSV = 逗号分隔，Excel 能直接打开

**🐍 Python**
```python
# 写（追加）
with open("report.txt", "a", encoding="utf-8") as f:
    f.write("今天复盘：出手 0 笔\n")

# 读
with open("report.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**🌐 前端 JS（Node.js）**
```javascript
const fs = require("fs");
fs.appendFileSync("report.txt", "今天复盘：出手 0 笔\n", "utf8");
const t = fs.readFileSync("report.txt", "utf8");
console.log(t);
```
> 类比：Python 的 `with open` 管开关，≈ JS 的 `fs.read/writeFileSync`；`"a"` 追加 ≈ `appendFileSync`。

**⚠️ 易踩的坑**
- 漏了 `encoding="utf-8"`，中文会乱码/报错。
- `"w"` 会清空原文件，想保留历史用 `"a"`。

---

## 第7课：综合小项目（短线复盘小工具）

**核心知识点**
- 把前 6 课串起来：变量 + 循环 + 判断 + 函数 + 文件
- 输入一周盈亏 → 算累计/盈亏天数 → 追加写 `report.txt`
- 这是你第一个「能落地」的小工具

**🐍 Python**
```python
def weekly_report(pnl_list):
    total = sum(pnl_list)
    win = sum(1 for p in pnl_list if p > 0)
    lose = len(pnl_list) - win
    return total, win, lose

week_pnl = [200, 300, -100, 500, 400, -150, 150]
t, w, l = weekly_report(week_pnl)
with open("report.txt", "a", encoding="utf-8") as f:
    f.write(f"累计 {t} 元 | 盈{w}/亏{l}\n")
```

**🌐 前端 JS（浏览器 + localStorage 版）**
```javascript
function weeklyReport(pnlList) {
    let total = pnlList.reduce((a, b) => a + b, 0);
    let win = pnlList.filter(p => p > 0).length;
    let lose = pnlList.length - win;
    return { total, win, lose };
}
let weekPnl = [200, 300, -100, 500, 400, -150, 150];
let { total, win, lose } = weeklyReport(weekPnl);
localStorage.setItem("report", `累计 ${total} 元 | 盈${win}/亏${lose}`);
```
> 类比：Python 落盘用文件，JS 网页版常用 `localStorage`；逻辑骨架一模一样。

**⚠️ 易踩的坑**
- `f-string` 里用 `{}` 占位，和 JS 模板字符串 `${}` 作用相同但写法不同。

---

## 第8课：字典 dict

**核心知识点**
- `{键: 值}` 存「配对」数据（如 股票代码 → 盈亏）
- 取值 `d["键"]`、改/加 `d["新键"]=值`
- 遍历用 `.items()` 同时拿键和值
- 安全取值 `.get(键, 默认值)`，避免取不到报错
- `键 in 字典` 判断是否包含

**🐍 Python**
```python
pnl = {"600519": 1200, "300750": -300}
print(pnl["600519"])            # 1200
pnl["000858"] = 600            # 新增
for code, money in pnl.items():
    print(code, money)
print(pnl.get("999999", "无此持仓"))   # 取不到给默认值
print("600519" in pnl)          # True
```

**🌐 前端 JS**
```javascript
let pnl = { "600519": 1200, "300750": -300 };
console.log(pnl["600519"]);     // 1200
pnl["000858"] = 600;            // 新增
for (let [code, money] of Object.entries(pnl)) {
    console.log(code, money);
}
console.log(pnl["999999"] ?? "无此持仓");   // 取不到给默认值
console.log("600519" in pnl);   // true
```
> 类比：Python 字典 ≈ JS 的「对象 `{}`」或 `Map`；`.items()` ≈ `Object.entries()`；`.get(k, d)` ≈ `?? 默认值`。

**⚠️ 易踩的坑**
- 直接 `pnl["不存在"]` 会报 `KeyError` 红字，用 `.get()` 或先 `in` 判断。

---

## 第9课：函数封装 + 键盘输入 input

**核心知识点**
- 把一段逻辑封装成函数，写一次到处用
- `input("提示")` 收键盘输入（≈ JS 的 `prompt`）
- 列表推导式一行把文字转数字：`[int(x) for x in 文本.split()]`

**🐍 Python**
```python
def group_report(week_data):
    lines = []
    for code, days in week_data.items():
        lines.append(f"{code} 周累计 {sum(days)}")
    return "\n".join(lines)

# 键盘录入
raw = input("输入每天盈亏（空格分开）：")   # 如 "200 300 -100"
nums = [int(x) for x in raw.split()]        # → [200, 300, -100]
```

**🌐 前端 JS**
```javascript
function groupReport(weekData) {
    return Object.entries(weekData)
        .map(([code, days]) => `${code} 周累计 ${days.reduce((a,b)=>a+b,0)}`)
        .join("\n");
}
// 浏览器：
let raw = prompt("输入每天盈亏（空格分开）：");   // "200 300 -100"
let nums = raw.split(" ").map(Number);             // → [200, 300, -100]
```
> 类比：`input()` ≈ 浏览器 `prompt()`；`[int(x) for x in raw.split()]` ≈ JS 的 `raw.split(" ").map(Number)`（都是「切开→逐个转数字」）。

**⚠️ 易踩的坑**
- `input()` 在没有真人的环境会报错，脚本里可用命令行参数控制是否进入录入模式。

---

## 第10课：列表 / 字符串进阶

**核心知识点**
- 列表：`append()` 加、`len()`/`sum()`/`max()`/`min()` 统计、`sort()` 排序、切片 `[a:b]` 左闭右开、`[::-1]` 反转
- 字符串：`f"{x:.2f}"` 保留小数、`strip()` 去空格、`split()` 切、`"-".join()` 拼、`replace()` 替换

**🐍 Python**
```python
pnl = [200, -150, 800, -200, 120, -50, 500]
pnl.append(100)                 # 加一笔
print(len(pnl), sum(pnl), max(pnl))   # 笔数 总和 最大
pnl.sort()                      # 升序
print(pnl[:3])                  # 前3笔（左闭右开）
print(f"盈利：{sum(pnl):.2f} 元")   # 保留2位小数

raw = "600519:1200; 300750:-300"
for item in raw.split(";"):     # 按分号切
    code, money = item.strip().split(":")   # 去空格 + 按冒号拆
    print(code, int(money))
```

**🌐 前端 JS**
```javascript
let pnl = [200, -150, 800, -200, 120, -50, 500];
pnl.push(100);                  // 加一笔
console.log(pnl.length, pnl.reduce((a,b)=>a+b,0), Math.max(...pnl));
pnl.sort((a,b)=>a-b);           // 升序（JS 要写比较函数）
console.log(pnl.slice(0, 3));   // 前3笔（左闭右开，和 Python 一样）
console.log(`盈利：${pnl.reduce((a,b)=>a+b,0).toFixed(2)} 元`);

let raw = "600519:1200; 300750:-300";
raw.split(";").forEach(item => {
    let [code, money] = item.trim().split(":");   // trim ≈ strip
    console.log(code, Number(money));
});
```
> 类比：Python 列表 ≈ JS 数组；`append` ≈ `push`；`len` ≈ `length`；`split/strip/join` 两边几乎同名；`f-string` 的 `{:.2f}` ≈ JS 的 `.toFixed(2)`。

**⚠️ 易踩的坑**
- 切片 `[a:b]` 永远左闭右开（含 a 不含 b），和 JS `slice` 一致。
- JS 的 `sort()` 默认按字符串排，数字要写 `(a,b)=>a-b`。

---

## 第11课：元组 / 集合 / 推导式

**核心知识点**
- **元组 tuple**：`(a, b)` 成对存，一旦创建不能改；能当字典的键（列表不行）
- **集合 set**：自动去重；交集 `&`、并集 `|`、差集 `-`（用于板块重叠股）
- **推导式**：一行完成「生成 + 过滤」，记住套路 `[结果 for 元素 in 可迭代 if 条件]`

**🐍 Python**
```python
# 元组：不可改，能当字典键
trade = ("600519", 1200)
code, money = trade            # 解包
key = ("600519", "2026-09-10") # 复合键

# 集合：板块运算
chip  = {"600519", "300750", "002049"}
robot = {"300750", "002472", "601012"}
print(chip & robot)            # 交集：{'300750'} 抱团股
print(chip | robot)            # 并集：去重关注池

# 推导式
pnl = [200, -150, 800, -200]
doubled = [x * 2 for x in pnl]            # [400, -300, 1600, -400]
wins   = [x for x in pnl if x > 0]        # [200, 800]
```

**🌐 前端 JS**
```javascript
// JS 没有「不可变数组」原生类型，const 只是引用不可改，内容仍可改
const trade = ["600519", 1200];
const [code, money] = trade;

// Set
const chip  = new Set(["600519", "300750", "002049"]);
const robot = new Set(["300750", "002472", "601012"]);
const inter = [...chip].filter(x => robot.has(x));   // 交集
const union = new Set([...chip, ...robot]);           // 并集

// 推导式（用 map/filter 表达）
const pnl = [200, -150, 800, -200];
const doubled = pnl.map(x => x * 2);
const wins   = pnl.filter(x => x > 0);
```
> 类比：元组 ≈ 用 `const` 声明且语义上锁死的数组；集合 = JS 的 `Set`；推导式 = JS 的 `map()` + `filter()` 一行版。

**⚠️ 易踩的坑**
- 元组不能被修改（`trade[1]=999` 会 `TypeError`），这是特性不是 bug。
- 列表不能当字典键，元组可以。

---

## 第12课：异常处理 + 模块拆分

**核心知识点**
- `try / except / else / finally` 让程序报错也不崩（≈ JS 的 try/catch/finally）
- 常见错误：`ZeroDivisionError`、`FileNotFoundError`、`ValueError`
- 跨文件复用：`import 模块名` 调用别人的函数（`模块名.函数()`）

**🐍 Python**
```python
def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default          # 转不成数字就给默认值
    finally:
        pass                    # 无论对错都执行（如关资源）

# 跨文件调用 tools.py 里的函数
import tools
total, win, lose = tools.weekly_report([100, -50, 200])
```

**🌐 前端 JS**
```javascript
function safeInt(text, default = 0) {
    try {
        return parseInt(text);
    } catch (e) {
        return default;
    } finally {
        // 无论对错都执行
    }
}
// 跨文件：ES Module
import { weeklyReport } from "./tools.js";
let [total, win, lose] = Object.values(weeklyReport([100, -50, 200]));
```
> 类比：Python 的 `try/except` ≈ JS 的 `try/catch`；Python 的 `import 模块` ≈ JS 的 `import { 函数 }`；`else` 块（没错才跑）是 Python 独有。

**⚠️ 易踩的坑**
- `import` 的模块顶层不要放执行代码，否则一导入就乱跑。

---

## 第13课：画净值曲线（matplotlib）

**核心知识点**
- **pip = Python 的 npm**；第三方库装在隔离 `venv` 里，用 `pyv` 启动器调用
- 画图流程：开画布 → 画线 → 设标题/轴 → 存图 `savefig()`（无屏幕环境不用 `show()`）
- 无屏幕要用 `Agg` 后端；中文要设 `rcParams` 字体，否则变方块

**🐍 Python**
```python
import matplotlib
matplotlib.use("Agg")                       # 无屏幕：只存图
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(days, net_value, marker="o", color="red", label="净值")
plt.title("账户净值曲线")
plt.savefig("净值曲线.png")                 # 存成图片
```

**🌐 前端 JS**
```javascript
// 用 npm 装库： npm install chart.js
// 浏览器里画：
import Chart from "chart.js";
new Chart(ctx, {
  type: "line",
  data: { labels: days, datasets: [{ label: "净值", data: netValue, borderColor: "red" }] }
});
// 浏览器直接渲染到 <canvas>，不用 savefig
```
> 类比：`pip install` ≈ `npm install`；`plt.savefig("x.png")` ≈ 浏览器直接把图渲染到 `<canvas>`（前端天然有屏幕）。

**⚠️ 易踩的坑**
- 跑绘图脚本必须用 `pyv`（带库的 venv），普通 `py` 找不到 matplotlib。
- 每个新画图脚本都要重新设中文字体，否则中文变方块。

---

## 第14课：从 CSV 读数据画图

**核心知识点**
- 标准库 `csv` 比手动 `split(",")` 更稳（能处理引号里的逗号）
- `next(reader)` 跳过表头
- **x 轴和 y 轴长度必须相等**，否则画图报错
- 中文字体每个脚本都要设

**🐍 Python**
```python
import csv
with open("pnl_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                       # 跳过表头 date,pnl
    for row in reader:                 # 每行是列表 [日期, 盈亏]
        dates.append(row[0])
        pnls.append(int(row[1]))

# 关键：x/y 等长，给 dates 补一个建仓日
dates.insert(0, START_DATE)
plt.plot(dates, net_value, ...)       # 两边都是 13 个
```

**🌐 前端 JS**
```javascript
// 浏览器：用 fetch 拿 CSV，或 papaparse 库解析
import Papa from "papaparse";
Papa.parse(csvText, {
    header: true,                      // 自动把首行当表头
    complete: (res) => {
        res.data.forEach(row => {      // row.date / row.pnl
            dates.push(row.date);
            pnls.push(Number(row.pnl));
        });
    }
});
```
> 类比：Python 的 `csv.reader` + `next()` 跳表头 ≈ JS 的 `papaparse` 设 `header: true`；都要保证 x/y 数据一一对应。

**⚠️ 易踩的坑**
- 报错 `x and y must have same first dimension` = x/y 长度不等，检查有没有漏掉建仓日/表头。
- `csv` 模块的 `next(reader)` 忘了写，会把表头 `"date","pnl"` 当数据读，转数字直接报错。

---

## 第15课：最大回撤 + 回撤阴影

**核心知识点**
- 最大回撤 = 账户从「历史最高点」回落的最大幅度（负数，越接近 0 越好）
- 算法：遍历净值，维护 `peak`（历史最高），每点回撤 = `(当前 - peak) / peak`，取最惨的那个
- `fill_between` 在两条线之间填色，直观看回撤区

**🐍 Python**
```python
def max_drawdown(equity):
    peak = equity[0]
    mdd = 0.0
    for x in equity:
        if x > peak:
            peak = x
        dd = (x - peak) / peak
        if dd < mdd:
            mdd = dd
    return mdd

# 画回撤阴影：在净值线和历史最高水位线之间填色
ax.fill_between(days, net_value, peaks, color="red", alpha=0.15, label="回撤区")
```

**🌐 前端 JS（chart.js）**
```javascript
function maxDrawdown(equity) {
    let peak = equity[0], mdd = 0;
    for (const x of equity) {
        if (x > peak) peak = x;
        const dd = (x - peak) / peak;
        if (dd < mdd) mdd = dd;
    }
    return mdd;
}
// chart.js 用 fill 选项在两条数据集之间填色：
// dataset: { data: netValue, fill: "+1", backgroundColor: "rgba(255,0,0,0.15)" }
```
> 类比：算法骨架 Python 和 JS **完全一样**；`for x in equity:` ≈ `for (const x of equity)`；`fill_between` ≈ chart.js 的 `fill`（两条线之间填色）。

**⚠️ 易踩的坑**
- 最大回撤是「相对历史最高」不是「相对起点」。+50% 后回落到 +20%，回撤约 -20%，但总账仍赚。
- `mdd` 初值设 0，只会越跌越负，用 `dd < mdd` 取最小。

---

## 第16课：多只股票净值对比线

**核心知识点**
- 用字典 `{"股票名": [每日盈亏]}` 存多只股票的数据（第8课 dict）
- `zip(字典.items(), 颜色列表)` 把「每只股票」和「一个颜色」一一配对，循环一次画一条线
- 复用之前的 `net_value_series` / `max_drawdown` 函数，写一次到处用
- **x 轴长度 = 净值点数 = 盈亏天数 + 1**（多一个起始日），否则 x/y 不等长报错

**🐍 Python**
```python
stock_pnl = {
    "600519 茅台": [200, 300, -100, ...],
    "300750 宁德": [-150, 200, 300, ...],
}
colors = ["#d62728", "#1f77b4", "#2ca02c"]
days = list(range(len(stock_pnl["600519 茅台"]) + 1))   # +1 对齐起始日

for (name, pnls), color in zip(stock_pnl.items(), colors):
    nv = net_value_series(pnls, START_CAPITAL)   # 复用函数
    mdd = max_drawdown(nv)
    ax.plot(days, nv, color=color, label=f"{name} 回撤{mdd:.2%}")
```

**🌐 前端 JS（chart.js）**
```javascript
const stockPnl = {
    "600519 茅台": [200, 300, -100, /*...*/],
    "300750 宁德": [-150, 200, 300, /*...*/],
};
const colors = ["#d62728", "#1f77b4", "#2ca02c"];
const datasets = Object.entries(stockPnl).map(([name, pnls], i) => {
    const nv = netValueSeries(pnls, START);   // 复用函数
    return { label: `${name} 回撤${maxDrawdown(nv).toFixed(2)}%`, data: nv, borderColor: colors[i] };
});
// new Chart(ctx, { type: "line", data: { labels: days, datasets } });
```
> 类比：Python `for (k, v), c in zip(d.items(), colors)` ≈ JS `Object.entries(d).map(([k, v], i) => ...)`；都是「遍历 + 按索引取对应颜色」。

**⚠️ 易踩的坑**
- 净值比 pnl 多一个点（多一个起始日），`days` 记得 `+1`，否则 `ValueError: x and y must have same first dimension`。
- 颜色数比股票数多/少都会错位，保持一一对应。

---

## 第17课：收益归因柱状图（按板块汇总）

**核心知识点**
- **多列 CSV**：`csv.reader` 每行是 `['板块','盈亏']` 这样的列表，用下标 `row[0]`/`row[1]` 取列
- **按类别汇总（聚合 / group by）**：用空字典，遇到同一类别就累加 —— 交易、报表里最常用
- 聚合核心写法：`d[key] = d.get(key, 0) + 值`（没有就当 0）
- `plt.bar(类别, 高度)` 画柱状图；`bar.set_color()` 单根改色
- **涨红跌绿**：A股习惯，赚红色 `#d62728`、亏绿色 `#2ca02c`（和美股相反）
- `sorted(d.items(), key=lambda kv: kv[1], reverse=True)` 按值排序

**🐍 Python**
```python
by_sector = {}
with open("trades.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                          # 跳过表头
    for row in reader:
        sector = row[0]
        pnl = int(row[1])
        by_sector[sector] = by_sector.get(sector, 0) + pnl   # 聚合

items = sorted(by_sector.items(), key=lambda kv: kv[1], reverse=True)
sectors, totals = [k for k, v in items], [v for k, v in items]

bars = ax.bar(sectors, totals)
for bar, v in zip(bars, totals):
    bar.set_color("#d62728" if v >= 0 else "#2ca02c")   # 涨红跌绿
```

**🌐 前端 JS（chart.js）**
```javascript
const bySector = {};
trades.forEach(({ sector, pnl }) => {
    bySector[sector] = (bySector[sector] || 0) + pnl;    // 聚合
});
// 或用 reduce 一步到位：
const bySector2 = trades.reduce((acc, t) => {
    acc[t.sector] = (acc[t.sector] || 0) + t.pnl;
    return acc;
}, {});

// chart.js 柱状图：data 是数组，颜色按正负映射
const datasets = [{
    label: "各板块盈亏",
    data: totals,
    backgroundColor: totals.map(v => v >= 0 ? "#d62728" : "#2ca02c"),
}];
// new Chart(ctx, { type: "bar", data: { labels: sectors, datasets } });
```
> 类比：Python `d.get(k, 0) + v` ≈ JS `acc[k] = (acc[k] || 0) + v`；`plt.bar` ≈ chart.js `type:"bar"`；都是「类别 + 数值」两列就能出图。

**⚠️ 易踩的坑**
- 格式串写反：`f"{x:,+}"` 会报错，正确是 `f"{x:+,}"`（符号在前、千分位在后）。
- 忘记 `next(reader)` 跳过表头，会把 `"sector"` 当板块名、`"pnl"` 转 int 直接崩。
- 涨红跌绿是 A股习惯；若做美股/全球视图要反过来，别写死。

---

## 速查表：Python ↔ 前端 JS 对照

| 概念 | 🐍 Python | 🌐 前端 JS |
|------|-----------|-----------|
| 输出 | `print(x)` | `console.log(x)` |
| 变量 | `x = 1` | `let x = 1` |
| 相等比较 | `==` | `===` |
| 且 / 或 | `and` / `or` | `&&` / `\|\|` |
| 代码块 | 冒号 + 缩进 | `{ }` |
| 否则如果 | `elif` | `else if` |
| 计数循环 | `for i in range(n):` | `for(let i=0;i<n;i++)` |
| 遍历数组 | `for x in arr:` | `arr.forEach(x =>)` |
| 函数 | `def f():` | `function f(){}` |
| 多返回值 | `return a, b` | `return {a, b}` |
| 字典/对象 | `d = {"k": v}` | `let d = {k: v}` |
| 遍历键值 | `for k, v in d.items():` | `for (let [k,v] of Object.entries(d))` |
| 数组加元素 | `arr.append(x)` | `arr.push(x)` |
| 长度 | `len(arr)` | `arr.length` |
| 切分文本 | `s.split(",")` | `s.split(",")` |
| 模板字符串 | `f"{x}"` | `` `${x}` `` |
| 保留小数 | `f"{x:.2f}"` | `x.toFixed(2)` |
| 异常处理 | `try/except` | `try/catch` |
| 导入模块 | `import m` | `import m` |
| 装库 | `pip install m` | `npm install m` |
| 读写文件 | `open()` + `with` | `fs.readFileSync()` |
| 画折线图 | `matplotlib` | `chart.js` |
| 画柱状图 | `plt.bar(x, h)` | `type:"bar"` |
| 字典取值带默认 | `d.get(k, 0)` | `d[k] || 0` |
| 按值排序 | `sorted(d.items(), key=lambda kv: kv[1])` | `arr.sort((a,b)=>a.v-b.v)` |
| 聚合分组 | `d[k] = d.get(k,0)+v` | `reduce((acc,t)=>..., {})` |

---

> 本笔记覆盖第 1~17 课。后续新课会按同样格式，每节课都给「🐍 Python ↔ 🌐 前端 JS」对照。
