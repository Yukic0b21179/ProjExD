import random

listAll = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list = []
for i in range(10):
    list.append(random.choice(listAll))
list2 = ["",""] #今回二文字のためその二文字を保管するためのList
list3 = ["",""] #同上、時間があればここもランダムにするつもりだったが今回は二文字という指定もあったため断念。

print("対象文字：")
print(*list)
print("表示文字：")

for i in range(2):
    n = random.randint(0,len(list)-1)
    list2[i] = list[n]
    del list[n]

random.shuffle(list)

print(*list)

ans = int(input("欠損文字はいくつあるでしょうか？"))

if ans == 2:
    print("正解です. それでは, 具体的に欠損文字を一つずつ入力してください")
    list3[0] = input("一つ目の文字を入力してください：")
    list3[1] = input("二つ目の文字を入力してください：")
    if list3[0] in list2:
        list2.remove(list3[0])
        if list3[1] in list2:
            print("正解です！")
            print("欠損文字")
            print(list[0],*list2)
    else:
        print("不正解です. またチャレンジしてください")
else:
    print("不正解です. またチャレンジしてください")