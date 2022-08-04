import numpy as np
    
def get_mutations_per_patient(maf):
    mutations_per_patient = {}
    patients = set(maf["Tumor_Sample_Barcode"])
    for patient in patients:
        maf_one_gene = maf[maf.Tumor_Sample_Barcode.isin([patient])]
        mutations_per_patient[patient] = len(maf_one_gene)
    return mutations_per_patient

def remove_hipermutated_patients(maf, mutations_per_patient):
    mutations_per_patient_count = list(mutations_per_patient.values())
    q1 = np.quantile(mutations_per_patient_count, .25)
    q3 = np.quantile(mutations_per_patient_count, .75)
    iqr = q3 - q1
    threshold_hm = q3 + 4.5*iqr
    mutations_per_patient_filtered = dict(filter(lambda elem: elem[1] <= threshold_hm, mutations_per_patient.items()))
    maf = maf[maf.Tumor_Sample_Barcode.isin(list(mutations_per_patient_filtered))]
    return maf

def remove_hipermutated(maf):
    mutations_per_patient = get_mutations_per_patient(maf)
    return remove_hipermutated_patients(maf, mutations_per_patient)
