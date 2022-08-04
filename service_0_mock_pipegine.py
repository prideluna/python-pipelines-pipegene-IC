import pandas as pd

maf_fields = ["Hugo_Symbol", "Chromosome", "Start_Position", "End_Position", "Reference_Allele",
                  "Tumor_Seq_Allele2", "Variant_Classification", "Variant_Type", "Tumor_Sample_Barcode"]

def read_maf(maf_file_name):
    return pd.read_csv(maf_file_name, sep="\t", comment="#")
