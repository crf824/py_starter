pnl = [1,2,3,4,5]
print("1",pnl)

pnl.append(6)
print("2",pnl)

print("3",len(pnl),sum(pnl),max(pnl))

pnl_sort = pnl.sort()
pnl_sort2 = pnl.sort(reverse=True)

print("4",pnl_sort,pnl_sort2)

print("5",pnl[:3],pnl[-2:],pnl[::-1])

print("6",pnl.index(max(pnl)),pnl.pop())
