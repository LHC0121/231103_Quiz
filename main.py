number = int(input("크리스마스 트리의 높이를 설정하세요"))
def chritsmastree(number):
    for x in range(1,number+1):
        print(" "*(number*2-x)+"*"*(2*x-1)+" "*(number*2-x))

chritsmastree(number)
