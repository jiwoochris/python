삼성전자주가_list = [80000, 79000, 79500, 80200, 80000, 79600, 79800, 80100]
현재잔고 = 350000

i = 0

while i < 8:
    if 현재잔고 >= 삼성전자주가_list[i]:
        print("매수")
        현재잔고 -= 삼성전자주가_list[i]
    else:
        print("잔고부족")
    
    i += 1

분할매수 = 0

for p in 삼성전자주가_list:
    분할매수 += p

분할매수 /= len(삼성전자주가_list)

print(분할매수)
print(80000)