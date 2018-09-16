import pandas as pd
import warnings
warnings.filterwarnings('ignore') #hides warning messages in notebook

mouse_drug_data = "data/mouse_drug_data.csv"
clinicaltrial_data = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
# merge both files, make numeric to read
mouseDrug = '/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/mouse_drug_data.csv'
mouse = pd.read_csv(mouseDrug)

ClinDrug = '/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/clinicaltrial_data.csv'
clinical = pd.read_csv(ClinDrug)
mergedData = pd.merge(mouse, clinical, how="outer", on=["Mouse ID", "Mouse ID"])
mergedData = pd.merge(mouse, clinical, how="outer", on=["Mouse ID", "Mouse ID"])
tumorMean1 = mergedData.groupby(["Drug","Timepoint"]).mean()
del tumorMean1["Metastatic Sites"]
tumorMean1.reset_index()
tumorMean1_trans = tumorMean1.T
tumor=tumorMean1_trans.stack(dropna=True)

tumor.as_matrix()
