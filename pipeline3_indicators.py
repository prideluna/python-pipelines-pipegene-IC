# from service_0_mock_pipegine import read_maf
from service_1_get_title import title_from_path
from service_6_indicators_to_dataframe import indicators_dataframe
from service_15_constants import MAF_FILE_NAME, PREPROC_MAF_FILE_NAME
   
title = title_from_path(PREPROC_MAF_FILE_NAME) 
# maf = read_maf(preproc_maf_file_name)
df_indicators = indicators_dataframe(title, MAF_FILE_NAME, PREPROC_MAF_FILE_NAME)

df_indicators.to_csv('indicators.csv') # SINK


##################### GENERATE A TABLE WITH ORIGINAL AND PREPROCESSED MAF ########################

