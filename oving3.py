import matplotlib.pyplot as plt
import numpy as np


xvals = np.arange(0, 0.51, 0.01)
yvals = 32/15*xvals
plt.plot(xvals, yvals, "b-", label="E")
xvals = np.arange(0.5, 1.01, 0.01)
yvals = 64/15*xvals-16/5*xvals**2-1/15*xvals**(-2)
plt.plot(xvals, yvals, "b-")
xvals = np.arange(1, 2, 0.01)
yvals = xvals**(-2)
plt.plot(xvals, yvals, "b-")

xvals = np.arange(0, 0.51, 0.01)
yvals = xvals/xvals
plt.plot(xvals, yvals, "r--", label=r"${\rho}$")
xvals = np.arange(0.5, 1.01, 0.01)
yvals = 2-2*xvals
plt.plot(xvals, yvals, "r--")
xvals = np.arange(1, 2, 0.01)
yvals = 0*xvals
plt.plot(xvals, yvals, "r--")

plt.xlabel("r/R")
plt.ylabel(r"$E(r/R) R^2/kQ$ og ${\rho}(r/R)/{\alpha}$")
plt.legend()

plt.show()
plt.savefig("plot.pdf")