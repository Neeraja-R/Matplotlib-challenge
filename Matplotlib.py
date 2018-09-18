import pandas as pd
import numpy as np
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
tumorMean1 = mergedData.groupby(["Drug","Timepoint"]).mean()
del tumorMean1["Metastatic Sites"]
tumorMean1.reset_index()
tumorMean1_trans = tumorMean1.T
tumor=tumorMean1_trans.stack(dropna=True)

#data = {'Capomulin': [45.00000000, 44.26608642, 43.08429058, 42.06431735, 40.71632532, 39.93952783, 38.76933929, 37.81683888, 36.95800081, 36.2361138], 'Ceftamin' : [45.00000000, 46.50305096, 48.28512522, 50.09405489, 52.1570485, 54.28767406, 56.76951721, 58.82754783, 61.46789545, 64.13242134], 'Infubinol' : [45.00000000, 47.06200103, 49.40390857, 51.29639656, 53.19769093, 55.71525236, 58.29939721, 60.74246123, 63.16282442, 65.75556228], 'Ketapril' : [45.00000000, 47.38917452, 49.58226897, 52.39997374, 54.92093474, 57.67898172, 60.99450719, 63.37168605, 66.06858035, 70.66295761], 'Naftisol' : [45.00000000, 46.7960981, 48.6942096, 50.93301828, 53.64408744, 56.73196758, 59.55950856, 62.68508695, 65.60075374, 69.26550621], 'Placebo' : [45.00000000, 47.12558919, 49.42332948, 51.3597417, 54.36441703, 57.48257374, 59.80906319, 62.42061507, 65.052675, 68.08408222], 'Propriva' : [45.00000000, 47.24896703, 49.10154084, 51.06731847, 53.34673737, 55.50413765, 58.19637416, 60.35019905, 63.04553676, 66.25852869], 'Ramicane' : [45.00000000, 43.9448594, 42.5319573, 41.49506092, 40.23832486, 38.97429956, 38.70313734, 37.45199635, 36.57408068, 34.95559479], 'Stelasyn' : [45.00000000, 47.52745167, 49.46384376, 51.52940872, 54.0673949, 56.16612329, 59.8267376, 62.44069947, 65.35638598, 68.43831043], 'Zoniferol' : [45.00000000, 46.85181827, 48.68988143, 50.77905905, 53.17033369, 55.43293487, 57.71353092, 60.08937222, 62.91669188, 65.96088789]}
#columns = ['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol']
#TVdata = {'Capomulin':[[45.00000000, 44.26608642, 43.08429058, 42.06431735, 40.71632532, 39.93952783, 38.76933929, 37.81683888, 36.95800081, 36.2361138]], 'Ceftamin':[[45.00000000, 46.50305096, 48.28512522, 50.09405489, 52.1570485, 54.28767406, 56.76951721, 58.82754783, 61.46789545, 64.13242134]], 'Infubinol':[[45.00000000, 47.06200103, 49.40390857, 51.29639656, 53.19769093, 55.71525236, 58.29939721, 60.74246123, 63.16282442, 65.75556228]]}
TV = [45.00000000, 44.26608642, 43.08429058, 42.06431735, 40.71632532, 39.93952783, 38.76933929, 37.81683888, 36.95800081, 36.2361138], [45.00000000, 46.50305096, 48.28512522, 50.09405489, 52.1570485, 54.28767406, 56.76951721, 58.82754783, 61.46789545, 64.13242134], [45.00000000, 47.06200103, 49.40390857, 51.29639656, 53.19769093, 55.71525236, 58.29939721, 60.74246123, 63.16282442, 65.75556228]
timepoint=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
drug = ['Capomulin', 'Ceftamin', 'Infubinol']
tumor = pd.DataFrame(TV, index={"Timepoint":timepoint}, columns={'Drug':drug}, dtype = object, copy=False)

#indexT={"Timepoint":timepoint}
#columnsT = {"Drug":TVdata}
#tumor = pd.DataFrame(index=indexT, columns=columnsT, dtype = object, copy=False)
#tumor.reindex(columns=['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol'])
#tumor.reindex(columns=['Capomulin', 'Ceftamin', 'Infubinol'])
#tumor = pd.DataFrame(data, index={"Timepoint":indexT}, columns={'Drug':columns}, dtype = object, copy=False)



tumor.plot(kind="scatter", x=timepoint, y=TV, grid=True, figsize=(20,10), title="Tumor Volume Over Time")
#yerr = 0.1 + 0.2*np.sqrt(index)
#xerr = 0.1 + yerr
#plt.figure()
#plt.errorbar(index, data, xerr=0.2, yerr=0.4)
#plt.title("Change in Tumor Volume Over Time")

