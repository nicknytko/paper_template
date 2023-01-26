import matplotlib.pyplot as plt
import numpy as np
from common import data_load, set_figure, fig_size, save_or_show

x = np.linspace(0, 1, 100)
y = np.sin(2 * x * np.pi)

fs = fig_size.singlefull
set_figure(width=fs['width'], height=fs['height'])

plt.plot(x, y, 'o-', label='$\\sin(2\\pi x)$', markersize=0.5)
plt.grid()
plt.legend()

save_or_show()
