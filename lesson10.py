# ============ 第 10 课：列表进阶 + 字符串进阶 ============
# 核心：把"一组数据"玩转（排序/切片/统计），把"一段文字"拆干净（分割/清洗）。

# =================== 一、列表 list 进阶 ===================
print("===== 列表操作 =====")

# 一组每日盈亏
pnl = [320, -150, 800, -200, 450, 600]
print("原始：", pnl)

# 末尾加一笔
pnl.append(120)
print("append 后：", pnl)

# 统计 & 聚合（算账三件套）
print("笔数 len：", len(pnl))
print("总和 sum：", sum(pnl))
print("最大 max：", max(pnl), " 最小 min：", min(pnl))

# 排序（默认从小到大；reverse=True 从大到小）
pnl.sort()
print("升序排序：", pnl)
pnl.sort(reverse=True)
print("降序排序：", pnl)

# 切片：取其中一段 [起始:结束)  左闭右开
print("前 3 笔：", pnl[:3])
print("最后 2 笔：", pnl[-2:])
print("反转整个列表：", pnl[::-1])      # [::-1] 是常用技巧

# 找位置 / 删除
print("最大值位置 index：", pnl.index(max(pnl)))
pnl.pop()                              # 删掉最后一个
print("pop 后：", pnl)
print("----")

# =================== 二、字符串 string 进阶 ===================
print("===== 字符串操作 =====")

# f-string：把变量塞进文字（最常用）
name = "何执舵"
profit = 1300.456
print(f"你好 {name}，本月盈利 {profit:.2f} 元")   # :.2f 保留 2 位小数

# 分割：把一行 "代码,盈亏" 拆成两段
line = "  600519, 1200  "
code, money = line.strip().split(",")      # strip 去首尾空格，split 按逗号切
print("代码：", code, " 盈亏：", money.strip())

# 替换 & 大小写
t = "Hello Python"
print("替换：", t.replace("Python", "量化"))
print("小写：", t.lower())

# 判断包含（类比 JS 的 includes）
print("是否含 'Hello'：", "Hello" in t)

# join：把列表拼成字符串（split 的反操作）
words = ["短线", "进化", "团"]
print("拼接：", "-".join(words))
print("----")

# =================== 三、综合：解析一段复盘文本 ===================
raw = "600519:1200; 300750:-300; 002594:800"
print("原始文本：", raw)
records = []
for item in raw.split(";"):                 # 按分号切成每一条
    item = item.strip()                      # 去空格
    if not item:
        continue
    code, money = item.split(":")            # 按冒号切
    records.append((code, int(money)))       # 存成 (代码, 盈亏) 元组
print("解析结果：", records)
total = sum(m for _, m in records)          # 推导式求和
print("合计盈亏：", total, "元")
