from typing import Tuple
import matplotlib.pyplot as plt
from matplotlib.image import AxesImage
import numpy as np


def create_plot(fig: plt.Figure, u: np.ndarray, fig_counter: int, T_cold: float, T_hot: float, dt: float, n: int) -> Tuple[int, AxesImage]:
    fig_counter += 1
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))

    return fig_counter, im


def output_plots(fig: plt.Figure, im: AxesImage) -> None:
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
