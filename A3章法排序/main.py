
import matplotlib.pyplot as plt
plt.rcParams[ 'font.sans-serif' ] = [ 'SimHei' ] # 步骤一(替换sans-serif字体)
plt.rcParams[ 'axes.unicode_minus' ] = False  # 步骤二(解决坐标轴负数的负号显示问题)

# 各类别的标签和比例
labels = ['排列是否规律','大小','字列宽窄', '多少','形状', '疏密', '直觉', '是否规律','其他']
sizes = [5,53,1, 15,2, 20, 5,5,9]

# 饼状图中各部分的颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','#8256A5']
# 绘制饼状图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# 显示图形
plt.show()
