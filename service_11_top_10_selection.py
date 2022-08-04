import pandas as pd

def select_top10(maf_data):
    top10GenesNames=[]
    variantClassificationType=[]
    for g in maf_data['Hugo_Symbol'].value_counts()[:10].index.tolist():
        top10GenesNames.append(g)
        for v in maf_data[maf_data["Hugo_Symbol"]==g]["Variant_Classification"].value_counts().index.tolist():
            variantClassificationType.append(v)

    variantClassificationType=set(variantClassificationType)
    topGenesVariations_df = pd.DataFrame(0, index=top10GenesNames, columns=variantClassificationType)
    for g in maf_data['Hugo_Symbol'].value_counts()[:10].index.tolist():
        for v in maf_data[maf_data["Hugo_Symbol"]==g]["Variant_Classification"].value_counts().items():
            topGenesVariations_df[v[0]][g]=v[1]
    topGenesVariations_df=topGenesVariations_df.append(topGenesVariations_df.agg(['sum']))
    topGenesVariations_df=topGenesVariations_df.sort_values(by ='sum', axis=1,ascending=False)

    bars=[]
    for c in topGenesVariations_df.columns:
        bars.append(list(topGenesVariations_df[c][:10]))
    
    return bars, top10GenesNames 