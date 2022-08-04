import numpy as np
import matplotlib.pyplot as plt
from service_0_mock_pipegine import read_maf
from service_15_constants import COLOR_LIST
from pathlib import Path
import uuid

from service_11_top_10_selection import select_top10


def plot_top10(bars,top10GenesNames, title):
    figure_path = Path(str(uuid.uuid4())+'.png').absolute()
    _, ax = plt.subplots(figsize=(15, 8))
    npBars=np.array(bars)
    plotBars=[]

    ind = [9,8,7,6,5,4,3,2,1,0]
    plt.yticks(ind, top10GenesNames)

    for index in range(len(bars)):
        if(index==0):        
            plotBars.append(ax.barh(ind,bars[index],color=COLOR_LIST[index]))
            sumPrevious=npBars[index]
        else:
            plotBars.append(ax.barh(ind,bars[index],left=sumPrevious,color=COLOR_LIST[index]))
            sumPrevious+=npBars[index]

    ax.set_title(title)

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  
    plt.tight_layout(h_pad=2.5, w_pad=1)

    plt.savefig(figure_path, format='png', dpi=250,bbox_inches='tight')
    #plt.show()
    return figure_path

MAF_FILE_NAME=  "./CancerData/" + "BRCA1" + "_data_mutations_extended.txt"
PREPROC_MAF_FILE_NAME = "./CancerData/" + "BRCA1" + ".maf"

maf = read_maf(PREPROC_MAF_FILE_NAME)


bars, top10GenesNames = select_top10(maf)
title="BRCA1"
plot_top10(bars,top10GenesNames, title)