import pandas as pd
from service_5_indicator_from_maf import get_indicators_from_maf 
from service_0_mock_pipegine import read_maf
from pathlib import Path
import uuid

def indicators_dataframe(name_maf, original_maf_file_name,preproc_maf_file_name):### we can change name_maf to list_maf_names in the future
    csv_path = Path(str(uuid.uuid4())+'.csv').absolute()
    dict_indicators = {'Cancer':[],'# Mutations':[],'# Mutated Genes':[], '# Mutated patients':[]}
    original_maf = read_maf(original_maf_file_name)
    preproc_maf = read_maf(preproc_maf_file_name)

    mutations_count, genes_count, patients_count = get_indicators_from_maf(original_maf)  
    dict_indicators["Cancer"].append("Original " + str(name_maf))
    dict_indicators['# Mutations'].append(str(mutations_count))
    dict_indicators['# Mutated Genes'].append(str(genes_count))
    dict_indicators['# Mutated patients'].append(str(patients_count))
    
    mutations_count, genes_count, patients_count = get_indicators_from_maf(preproc_maf) 
    dict_indicators["Cancer"].append("Preprocessed " + str(name_maf))
    dict_indicators['# Mutations'].append(str(mutations_count))
    dict_indicators['# Mutated Genes'].append(str(genes_count))
    dict_indicators['# Mutated patients'].append(str(patients_count))
    
    df = pd.DataFrame(dict_indicators)
    df.to_csv(csv_path)
    return csv_path