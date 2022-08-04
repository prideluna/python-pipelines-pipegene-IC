import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from service_15_constants import COLOR_LIST
import uuid


def plot_maf(title, variants_percentage_dict):
    figure_path = Path(str(uuid.uuid4())+'.png').absolute()
    _, ax = plt.subplots(figsize=(15, 15))

    variants_name = [* variants_percentage_dict.keys()]
    variants_percentage = [* variants_percentage_dict.values()]

    y_pos = np.arange(len(variants_name))

    ax.barh(y_pos, variants_percentage, color=COLOR_LIST[:5])
    ax.set_title(title)

    plt.yticks(y_pos, variants_name)

    for x, v in enumerate(variants_percentage):
        ax.text(v, x, str(v)+'%', color='black')

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.tight_layout(h_pad=2.5, w_pad=1)

    plt.savefig(figure_path, format='png', dpi=250, bbox_inches='tight')
    # plt.show()
    return figure_path