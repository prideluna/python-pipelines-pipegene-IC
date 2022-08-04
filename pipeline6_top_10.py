from service_11_top_10_selection import select_top10
from service_12_plot_top_10 import plot_top10
from service_1_get_title import title_from_path
from service_0_mock_pipegine import read_maf
from service_15_constants import PREPROC_MAF_FILE_NAME


maf = read_maf(PREPROC_MAF_FILE_NAME)
bars, top10GenesNames = select_top10(maf)
title = title_from_path(PREPROC_MAF_FILE_NAME)
plot_top10(bars,top10GenesNames, title)


########## GENERATE PIPELINE PLOTTING TOP10 GENES ############### 
