# 散点图
# 散点图表示两个数值变量之间的相对关系，这两个变量分别位于两个数轴上。例如，身高与体重，或者供给与需求。散点图有助于识别出变量之间是否具有正相关（图中的点集中于某个具体参数）或负相关（图中的点像云一样发散）。你还可以画一条回归曲线，也就是使方差最小的曲线，通过图中的点基于一个变量的值预测另一个变量的值。

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = np.arange(start=1., stop=15., step=1.)
y_linear = x + 5 * np.random.randn(14)
y_quadratic = x**2 + 10. * np.random.randn(14)
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go',x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Scatter Plots Regression Lines')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim((min(x)-1., max(x)+1.))
plt.ylim((min(y_quadratic)-10., max(y_quadratic)+10.))
plt.savefig('scatter_plot.png', dpi=400, bbox_inches='tight')
plt.show()