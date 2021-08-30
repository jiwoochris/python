하림 = 136480
종목코드 = "A" + str(하림)
print(종목코드[1:])

전날종가 = 9300
오늘시가 = 10100

# 전날종가 < 오늘시가
# 전날종가 == 오늘시가
# 전날종가 <= 오늘시가
# 전날종가 >= 오늘시가
# 전날종가 > 오늘시가

날짜_list = ['8/1', '8/2', '8/3', '8/4', '8/5']
전일종가_dict = {'8/1':9900, '8/2':10200, '8/3':9300, '8/4':8900, '8/5':9500} # 9900원은 8/1 기준 전일의 종가입니다
오늘시가_dict = {'8/1':10100, '8/2':9500, '8/3':9100, '8/4':9200, '8/5':9900}

for i in 날짜_list:
    if 전일종가_dict[i] < 오늘시가_dict[i]:
        print("매수")

    else:
        print("매도")