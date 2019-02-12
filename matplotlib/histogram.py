# 直方图
# 直方图用来表示数值分布。常用的直方图包括频率分布、频率密度分布、概率分布和概率密度分布

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, parches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
ax1.set_title('Two Frequency Distributions')
plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()
