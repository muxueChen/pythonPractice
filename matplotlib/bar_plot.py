# 条形图
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# 为条形图准备数据。我创建了一个客户索引列表，因为 xticks 函数在设置标签时要求索引位置和标签值。
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]
# 创建了一个基础图
fig = plt.figure()
# 向基础图中添加了一个子图。因为可以向基础图中添加多个子图，所以必须指定要创建几行和几列子图，以及使用哪个子图。 1, 1, 1 表示创建 1 行 1 列的子图，并使用第 1 个也是唯一的一个子图。
ax1 = fig.add_subplot(1, 1, 1)
# 创建条形图。customer_index 设置条形左侧在 x 轴上的坐标。sale_amounts 设置条形的高度。align='center' 设置条形与标签中间对齐。color='darkblue' 设置条形的颜色。
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
# 通过设置刻度线位置在 x 轴底部和 y 轴左侧，使图形的上部和右侧不显示刻度线。
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')
# 向图中添加 x 轴标签、y 轴标签和图形标题
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()