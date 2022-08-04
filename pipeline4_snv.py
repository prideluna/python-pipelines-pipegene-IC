from service_0_mock_pipegine import read_maf
from service_1_get_title import title_from_path
from service_8_plot_snv_chart import plot_snv
from service_7_generate_svn_Dict import snvDict
from service_15_constants import PREPROC_MAF_FILE_NAME
   
mafField = title_from_path(PREPROC_MAF_FILE_NAME) 
preproc_maf = read_maf(PREPROC_MAF_FILE_NAME)
variantsPercentageDict  = snvDict(preproc_maf)# change this name: variantsPercentageDict
plot_snv(mafField, variantsPercentageDict) #SINK


########## GENERATE PIPELINE PLOTTING SNV ############### 