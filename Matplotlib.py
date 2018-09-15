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

#creating a scatter plot that shows how the tumor volume changes over time for each treatment

tumorMean1 = mergedData.groupby(["Drug","Timepoint"]).mean()
del tumorMean1["Metastatic Sites"]
tumorMean1.head()
tumorMean1.reset_index()
tumorMean1.unstack()  #stacks rows from up/down to horizontal orientation

tumorMean1_trans = tumorMean1.T  #transpose takes rows and makes them columns
tumorMean1_trans.stack() #this reorients from horizontal to vertical (with drug as columns because of transpose()
tumorMean = tumorMean1_trans.stack()

ax1 = tumorMean.plot.scatter(x='Timepoint', y='Tumor Volume (mm3)', c='DarkBlue')

