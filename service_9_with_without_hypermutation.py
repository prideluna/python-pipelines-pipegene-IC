from service_0_mock_pipegine import read_maf
from service_2_remove_outlier import get_mutations_per_patient

def mutation_count(original_maf, preproc_maf):
    data = []
    original = read_maf(original_maf)
    preproc = read_maf(preproc_maf)

    mutations_per_patient = get_mutations_per_patient(original)
    data.append(mutations_per_patient)
    mutations_per_patient = get_mutations_per_patient(preproc)
    data.append(mutations_per_patient)
    return data