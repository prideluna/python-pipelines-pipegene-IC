def computePercentageOfVariant(maf, variantColumnName):
    variantsType = maf[variantColumnName] 
    numberOfMutations = len(variantsType)
    variantQuantityDic  = variantsType.value_counts().to_dict()
    
    variantPercentageDict = {}
    for k, v in variantQuantityDic.items():
        variantPercentageDict[k] = round(v/numberOfMutations*100)

    return dict(sorted(zip(variantPercentageDict.keys(), variantPercentageDict.values()), reverse=True))