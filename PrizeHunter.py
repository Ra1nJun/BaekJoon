# 15953 - 상금 헌터
T = input()

for _ in range(int(T)):
    KCF_2017, KCF_2018 = map(int, input().split( ))

    prize = 0
    if KCF_2017 <= 21:
        if KCF_2017 == 0:
            pass
        elif KCF_2017 == 1:
            prize += 5000000
        elif KCF_2017 <= 3:
            prize += 3000000
        elif KCF_2017 <= 6:
            prize += 2000000
        elif KCF_2017 <= 10:
            prize += 500000
        elif KCF_2017 <= 15:
            prize += 300000
        else:
            prize += 100000

    if KCF_2018 <= 31:
        if KCF_2018 == 0:
            pass
        elif KCF_2018 == 1:
            prize += 5120000
        elif KCF_2018 <= 3:
            prize += 2560000
        elif KCF_2018 <= 7:
            prize += 1280000
        elif KCF_2018 <= 15:
            prize += 640000
        elif KCF_2018 <= 31:
            prize += 320000

    print(prize)