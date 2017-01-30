import math
import matplotlib.pyplot as plt


def delta_v(theta, delta_t, g):
    dv = -g * math.sin(theta) * delta_t
    return dv


def new_v(old_v, theta, delta_t, g):
    v = old_v + delta_v(theta, delta_t, g)
    return v


def delta_theta(v, delta_t):
    d_theta = v * delta_t
    return d_theta


def new_theta(old_theta, v, delta_t):
    theta = old_theta + delta_theta(v, delta_t)
    return theta


def plot_theta(list_t, list_theta):
    plt.plot(list_t, list_theta)
    plt.title("v = 7 m/s")
    plt.ylabel(r"${\theta}$ (grader)")
    plt.xlabel("t ($s$)")


def plot_energy(list_t, list_e, list_pot, list_kin):
    plt.plot(list_t, list_e, "r", label="Mekanisk energi")
    plt.plot(list_t, list_pot, 'b--', label="Potensiell energi")
    plt.plot(list_t, list_kin, 'g--', label="Kinetisk energi")
    plt.title("v = 7 m/s")
    plt.xlabel(r"t ($s$)")
    plt.ylabel(r"E/m ($m^2/s^2$)")
    plt.legend()


def main():
    f = open("plot.txt", "w")
    g = 9.81
    theta = math.pi
    v = 0
    t = 0
    delta_t = 0.0001
    list_t = []
    list_theta = []
    list_e = []
    list_kin = []
    list_pot = []
    for i in range(200000):
        e_pot = (1 - math.cos(theta)) * g
        e_kin = v**2 / 2
        e = e_kin + e_pot
        list_e.append(e)
        list_kin.append(e_kin)
        list_pot.append(e_pot)
        list_t.append(t)
        list_theta.append(math.degrees(theta))
        theta = new_theta(theta, v, delta_t)
        v = new_v(v, theta, delta_t, g)
        t += delta_t
        f.write(str(t) + "\t" + str(math.degrees(theta)) + "\t" + str(e) + "\n")
    f.close()
    plot_theta(list_t, list_theta)
    # plot_energy(list_t, list_e, list_pot, list_kin)
    plt.show()

main()
