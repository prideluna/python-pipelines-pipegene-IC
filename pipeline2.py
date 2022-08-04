from service_0_mock_pipegine import read_maf
from service_1_get_title import title_from_path
# from service_2_remove_outlier import remove_hipermutated
from service_3_compute_incidence import computePercentageOfVariant
from service_4_plot_bar_chart import plot_maf
from service_15_constants import preproc_maf_file_name, maf_file_name
# from service_13_select_columns import select_columns


plot_title = title_from_path(preproc_maf_file_name) 
maf = read_maf(maf_file_name) #PUMP
# column = select_columns(maf, plot_title) #FILTER
# preproc_maf = remove_hipermutated(maf) # FILTER 
variantClassification = computePercentageOfVariant(maf, "Variant_Type") #FILTER 
plot_maf(plot_title, variantClassification)  # SINK