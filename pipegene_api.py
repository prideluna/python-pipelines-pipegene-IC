from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from service_0_mock_pipegine import read_maf
from service_1_get_title import title_from_path
from service_3_compute_incidence import computePercentageOfVariant
from service_4_plot_bar_chart import plot_maf
from service_6_get_indicators import indicators_dataframe
from service_7_generate_svn_Dict import snvDict
from service_8_plot_snv_chart import plot_snv
from service_9_with_without_hypermutation import mutation_count
from service_15_constants import MAF_FILE_NAME, PREPROC_MAF_FILE_NAME
from service_10_plot_chart_with_without_hypermutation import plot_with_without_hypermutation
# from fastapi import FastAPI, Response
   
app = FastAPI()

@app.post("/plot-chart-variant-classification-or-variant-type", response_class=FileResponse)
def plot_variant_classification(column):
    title = title_from_path(MAF_FILE_NAME) 
    maf = read_maf(MAF_FILE_NAME) 
    variantClassification = computePercentageOfVariant(maf, column)
    png_variants = plot_maf(title, variantClassification) 
    return str(png_variants)
   

@app.post("/indicators")
def download_indicators_csv():
    title = title_from_path(PREPROC_MAF_FILE_NAME) 
    indicators = indicators_dataframe(title, MAF_FILE_NAME, PREPROC_MAF_FILE_NAME)
    csv = str(indicators)
    return FileResponse(path=csv, filename=csv)


@app.post("/plot-snv", response_class=FileResponse)
def plot_snv_chart():
    title = title_from_path(PREPROC_MAF_FILE_NAME) 
    preproc_maf = read_maf(PREPROC_MAF_FILE_NAME)
    variantsPercentageDict  = snvDict(preproc_maf)
    png_snv = plot_snv(title, variantsPercentageDict)
    return str(png_snv)


@app.post("/plot_with_without_hypermutation_chart", response_class=FileResponse)
def plot_with_without_hypermutation_chart():
    data = mutation_count(MAF_FILE_NAME, PREPROC_MAF_FILE_NAME)
    png_hipermutation = plot_with_without_hypermutation(data)
    return str(png_hipermutation)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8005)
    print("running")

