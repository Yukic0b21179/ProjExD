ans = [4,6,14]

while True:
    yourAns = int(input("問題１　今は令和何年？(半角数字で入力)"))
    if yourAns == ans[0]:
        print("正解！")
        break
    else:
        print("ちげーよばーか")

while True:
    yourAns = int(input("問題２　今は何月？(半角数字で入力)"))
    if yourAns == ans[1]:
        print("正解！")
        break
    else:
        print("ちげーよばーか")

while True:
    yourAns = int(input("問題３　今は何日？(半角数字で入力)"))
    if yourAns == ans[2]:
        print("正解！")
        break
    else:
        print("ちげーよばーか")

print("")