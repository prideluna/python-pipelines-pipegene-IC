from service_9_with_without_hypermutation import mutation_count
from service_10_plot_chart_with_without_hypermutation import plot_with_without_hypermutation
from service_15_constants import MAF_FILE_NAME, PREPROC_MAF_FILE_NAME

data = mutation_count(MAF_FILE_NAME, PREPROC_MAF_FILE_NAME)
plot_with_without_hypermutation(data)
