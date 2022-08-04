from service_0_mock_pipegine import read_maf
from service_1_get_title import title_from_path
# from service_2_remove_outlier import remove_hipermutated
from service_3_compute_incidence import computePercentageOfVariant
from service_4_plot_bar_chart import plot_maf
from service_13_select_columns import select_columns
from service_15_constants import MAF_FILE_NAME, PREPROC_MAF_FILE_NAME

plot_title = title_from_path(PREPROC_MAF_FILE_NAME) 
maf = read_maf(MAF_FILE_NAME) #PUMP
column = select_columns(maf, plot_title) #FILTER
# preproc_maf = remove_hipermutated(maf) # FILTER 
variantClassification = computePercentageOfVariant(maf,column) #FILTER 
plot_maf(plot_title, variantClassification)  # SINK
