import csv

# 下面这种加了encoding的写法需要在python3环境下运行

f = open('new1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['广东车牌数量', '非广东车牌数量', '绿牌车数量', '蓝牌车数量', '黄牌车数量'])
csv_writer.writeheader()
csv_reader = csv.reader(open('1.csv', encoding='utf-8'))
a = 0
b = 0
c = 0
d = 0
e = 0

for row in csv_reader:
    print(row)
    for i in row:
        if "不是" in i:
            a = a + 1
        elif "牌是" in i:
            b = b + 1
        elif "blue" in i:
            c = c + 1
        elif "green" in i:
            d = d + 1
        elif "yellow" in i:
            e = e + 1
dic = {
    "广东车牌数量": b,
    "非广东车牌数量": a,
    "绿牌车数量": d,
    "蓝牌车数量": c,
    "黄牌车数量": e
}
csv_writer.writerow(dic)
