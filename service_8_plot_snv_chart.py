import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import uuid

COLOR_LIST = ['tab:blue', 'tab:cyan', 'tab:purple', 'tab:gray', 'tab:orange', 'tab:red',
              'lightcyan', 'salmon', 'wheat', 'fuchsia', 'tab:green', 'tab:brown', 'tab:pink',
              'midnightblue', 'tomato', 'yellow', 'goldenrod', 'indigo', 'violet']

def plot_snv(title, variantsPercentageDict, colorList=COLOR_LIST):
    figure_path = Path(str(uuid.uuid4())+'.png').absolute()
    _, ax = plt.subplots(figsize=(15, 15))

    variantsName  = [*variantsPercentageDict.keys()]
    variantsPercentage = [*variantsPercentageDict.values()]

    y_pos = np.arange(len(variantsName))

    ax.barh(y_pos, variantsPercentage, color=colorList[:5])
    ax.set_title(title)

    plt.yticks(y_pos, variantsName)

    for x, v in enumerate(variantsPercentage): 
        ax.text(v, x, str(v), color='black')

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  
    plt.tight_layout(h_pad=2.5, w_pad=1)

    plt.savefig(figure_path, format='png', dpi=250,bbox_inches='tight')
    # plt.show()
    return figure_path
