from datetime import datetime

report_lines = [5000,-100,0,30,-1000]

def weekly_report(pnt):
	total=0
	win=0
	lose=0
	for pnl in pnt :
		total = total+pnl
		if pnl>0 :
			win = win+pnl
		elif pnl<0 :
			lose = lose+pnl
	return total,win,lose

def verdict(total,win,lose):
	if total > 0 and win >= lose:
		return "牛鼻"
	elif total > 0:
		return "一般"
	else:
		return "菜"

total,win,lose = weekly_report(report_lines)

content = verdict(total,win,lose)

with open("text.txt","w",encoding="utf-8") as f:
	f.write(f"{total}元 | 赢{win} | 输{lose}")
