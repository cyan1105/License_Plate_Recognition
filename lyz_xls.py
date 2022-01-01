import csv
import xlrd
f = open('newdata.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['广东车牌数量', '非广东车牌数量','绿牌车数量','蓝牌车数量','黄牌车数量'])
csv_writer.writeheader()
data = xlrd.open_workbook('data.xls') # 打开xls文件
table = data.sheets()[0]
nrows = table.nrows      # 获取表的行数
a = 0
b = 0
c = 0
d = 0
e = 0

for i in range(nrows):   # 循环逐行打印
    # print (table.row_values(i))
    for j in table.row_values(i):
        if "不是" in j:
            a = a + 1
        elif "牌是" in j:
            b = b + 1
        elif "blue" in j:
            c = c + 1
        elif "green" in j:
            d = d + 1
        elif "yellow" in j:
            e = e + 1

# print(a)
dic = {
    "广东车牌数量": b,
    "非广东车牌数量": a,
    "绿牌车数量": d,
    "蓝牌车数量": c,
    "黄牌车数量": e
}
# print(dic)
csv_writer.writerow(dic)
