print("구구단을 출력\n")
for x in range(1, 10): # 9단까지
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("---------------------")