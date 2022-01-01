import xlwt  # 需要的模块


def txt2xls(filename, xlsname):  # 文本转换成xls的函数，filename 表示一个要被转换的txt文本，xlsname 表示转换后的文件名
    # print('converting xls ... ')
    f = open(filename)  # 打开txt文本进行读取
    x = 0  # 在excel开始写的位置（y）
    y = 0  # 在excel开始写的位置（x）
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)  # 生成excel的方法，声明excel
    while True:  # 循环，读取文本里面的所有内容
        line = f.readline()  # 一行一行读取
        if not line:  # 如果没有内容，则退出循环
            break
        for i in line.split('\t'):  # 读取出相应的内容写到x
            item = i.strip()
            sheet.write(x, y, item)
            y += 1  # 另起一列
        x += 1  # 另起一行
        y = 0  # 初始成第一列
    f.close()
    xls.save(xlsname)  # 保存


if __name__ == "__main__":
    filename = 'D:\python\License_Plate_Recognition\data.txt'
    xlsname = 'D:\python\License_Plate_Recognition\data.xls'
    txt2xls(filename, xlsname)