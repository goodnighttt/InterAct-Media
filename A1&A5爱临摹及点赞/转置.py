import csv

# 读取数据
data = []
with open('like1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# 顺时针旋转90度
rotated_data = list(zip(*data[::-1]))

# 将转置后的数据写入txt文件
with open('rotated_data.txt', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(rotated_data)
