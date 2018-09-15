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

mergedData = pd.merge(mouse, clinical, on="Mouse ID", how="outer")

mergedData = mergedData.rename(columns={"Mouse ID":"Mouse ID", "Drug":"Drug", "Timepoint":"Timepoint", "Tumor Volume (mm3)": "Tumor Volume (mm3)", "Metastatic Sites":"Metastatic Sites"})


mergedData["Tumor Volume (mm3)"] = mergedData["Tumor Volume (mm3)"].apply(pd.to_numeric)
mergedData.dtypes

timeC = mergedData["Timepoint"].count #~50
timeC
tumorC = mergedData["Tumor Volume (mm3)"].count #~70
tumorC


#creating a scatter plot that shows how the tumor volume changes over time for each treatment

plot1 = pd.DataFrame(mergedData, columns=["Drug", "Timepoint", "Tumor Volume"], dtype="object")
plot1

mergedData.plot.scatter = (x= "Timepoint", y= "Treatment", "Tumor Volume (mm3)" c="blue", s=30)
plt.xlim(0,40)
plt.ylim(0,200)
plt.title("Tumor Volume Change Over Time")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume (mm3)")

plt.show()




