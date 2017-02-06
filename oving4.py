import matplotlib.pyplot as plt
import numpy as np


# rho - charge density
xvals = np.arange(0, 1.01, 0.01)
yvals = 1-xvals
plt.plot(xvals, yvals, "b-", label=r"${\rho}$")
xvals = np.arange(1, 2, 0.01)
yvals = xvals * 0
plt.plot(xvals, yvals, "b-")

# Q - enclosed charge
xvals = np.arange(0, 1.01, 0.01)
yvals = 4 * xvals**3 - 3 * xvals**4
plt.plot(xvals, yvals, "r-", label="Q")
xvals = np.arange(1, 2, 0.01)
yvals = xvals / xvals
plt.plot(xvals, yvals, "r-")

# E - electric field
xvals = np.arange(0, 1.01, 0.01)
yvals = 4 * xvals - 3 * xvals**2
plt.plot(xvals, yvals, "g-", label="E")
xvals = np.arange(1, 2, 0.01)
yvals = xvals**(-2)
plt.plot(xvals, yvals, "g-")

# v - electric potential
xvals = np.arange(0, 1.01, 0.01)
yvals = 2 - 2 * xvals**2 + xvals**3
plt.plot(xvals, yvals, "k-", label="V")
xvals = np.arange(1, 2, 0.01)
yvals = xvals**(-1)
plt.plot(xvals, yvals, "k-")

# labeling axes
plt.xlabel("r/R")
plt.ylabel(r"${\rho}(r/R)/4{\rho}_o$" ", " r"$Q(r/R)3/4{\pi}{\rho}_o R^3$" ", " r"$E(r/R)3{\epsilon}_o/{\rho}_o R$" " og " r"$V(r/R)3{\epsilon}_o/{\rho}_o R^2$")
plt.legend()

plt.show()
plt.savefig("plot4.pdf") # lagrer figur