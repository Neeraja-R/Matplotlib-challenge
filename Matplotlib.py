
import pandas as pd
import warnings
warnings.filterwarnings('ignore') #hides warning messages in notebook

mouse_drug_data = "data/mouse_drug_data.csv"
clinicaltrial_data = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouseDrug = os.path.join('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/mouse_drug_data.csv')
with open (mouseDrug, newline="") as Mcsvfile:
    Mcsvreader = csv.reader(Mcsvfile, delimiter = "|")
    for Mrow in Mcsvreader:
        print(Mrow)

ClinDrug = os.path.join('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/clinicaltrial_data.csv')
with open (ClinDrug, newline="") as Ccsvfile:
    Ccsvreader = csv.reader(Ccsvfile, delimiter = "|")
    for Crow in Ccsvreader:
        print(Crow)



#alternate to concat lists

import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore') #hides warning messages in notebook

mouse_drug_data = "data/mouse_drug_data.csv"
clinicaltrial_data = "data/clinicaltrial_data.csv"

mdd = []
ctd = []
output = []

# Read the Mouse and Drug Data and the Clinical Trial Data
mouseDrug = os.path.join('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/mouse_drug_data.csv')
with open (mouseDrug, newline="") as Mcsvfile:
    Mcsvreader = csv.reader(Mcsvfile, delimiter = ",")
    for Mrow in Mcsvreader:
        mdd.append(Mrow)

ClinDrug = os.path.join('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/05 - Python Matplotlib/HW5 - Matplotlib/Pymaceuticals/data/clinicaltrial_data.csv')
with open (ClinDrug, newline="") as Ccsvfile:
    Ccsvreader = csv.reader(Ccsvfile, delimiter = ",")
    for Crow in Ccsvreader:
        ctd.append(Crow)

for Mrow in mdd:
    Crow = ctd.get(Mrow[2]) #if key matches, Crow contains string match, else - none
    if Crow:
        Mrow.append(Crow) #appends the field
        output.append(Mrow) #appends row to the result list

print(output)


#got example from:

import csv

sg = []
fqdn = {}
output = []
with open(r'file2.csv', 'rb') as src:
    read = csv.reader(src, delimiter=',')
    for dataset in read:
        sg.append(dataset)

with open(r'file1.csv', 'rb') as src1:
    read1 = csv.reader(src1, delimiter=',')
    for to_append, to_match in read1:
        fqdn[to_match.lower()] = to_append

for dataset in sg:
    to_append = fqdn.get(dataset[2].lower()) # If the key matched, to_append now contains the string to append, else it becomes None
    if to_append:
        dataset.append(to_append) # Append the field
        output.append(dataset) # Append the row to the result list

print(output)

