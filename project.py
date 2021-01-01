import csv
import numpy as np 
def getdatasrc(datapath):
    Marks = []
    
    with open(datapath) as f:
        csvreader = csv.DictReader(f)
        for r in csvreader:
            Marks.append(float(r["Days Present"]))
            
    
    return{"x":Marks}
def correlation1(datasrc):
    c = np.corrcoef(datasrc['x'])
    print(c)
def setup():
    datapath = 'rawdata.csv'
    datasrc = getdatasrc(datapath)
    correlation1(datasrc)
setup()


