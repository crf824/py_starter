l1 = {"0001","0002","0003"}
l2 = {'0003',"0004","0005"}

print("0",l1&l2,l1|l2,l1-l2)

pnl = [100,200,-300]
raw = [1,2,3,4,5,4,3]
codes = {"a":[100,200,300,400],"b":[100,200,300,400],"c":[100,200,300,-1400]}

x1 = [x*2 for x in pnl]
x2 = [x for x in pnl if x>0]
x3 = [x for x in raw if x > 2]
x4 = {k:sum(v) for k,v in codes.items()}
x5 = {k:v for k,v in x4.items() if v >0}

print(x1,x2,x3,x5)
			