import matplotlib.pyplot as plt
import numpy as np


def plot_with_errorbar(x, y, yerr):
    if type(x) == list:
        x = np.array(x)
    if type(y) == list:
        y = np.array(y)
    if type(yerr) == list:
        yerr = np.array(yerr)
    plt.errorbar(x, y, yerr, color="red", label="label")
    # plt.plot(x, y, linestyle="--",color='black', label="label")
    plt.title("title", fontsize=16)
    plt.xlabel("x", fontsize=16)
    plt.ylabel("y", fontsize=16)
    plt.legend(loc="upper right", fontsize=18)
    plt.show()
    fig = plt.figure()
    fig.savefig("plot.png")


if __name__ == "__main__":
    x = np.array([0.2 * i for i in range(2, 6)])
    y = [
        -0.914149704627082,
        -1.11628600686954,
        -1.13414766667709,
        -1.10115033023262,
    ]
    yerr = [
        0.01199856387181490,
        0.009760241443056540,
        0.008337800834926870,
        0.007956273324052040,
    ]
    plot_with_errorbar(x, y, yerr)
