
def get_indicators_from_maf(maf):
    mutations_count = len(maf["Hugo_Symbol"])
    genes_count     = len(maf["Hugo_Symbol"].unique())
    patients_count  = len(maf["Tumor_Sample_Barcode"].unique())
    return mutations_count, genes_count, patients_count