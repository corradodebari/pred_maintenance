# ---------------------------------------------------
# Script that merges the IMS files in blocks of
# BATCH number of records and create a last file as: 
#   Mergedataset_FINAL.csv
# 
# ---------------------------------------------------
import glob
import ntpath
import pandas as pd 
from datetime import datetime

DIR="./1st_test"

files_=glob.glob(DIR+"/*")
BATCH=3000
files=[ fd[1] for fd in (ntpath.split(f) for f in files_ )]
files.sort()
dfex = pd.DataFrame(
    columns=['time_id','b11','b12','b21','b22','b31','b32','b41','b42']
)

i=1
for f in files:
    print(str(i)+": "+f, end="\r", flush=True)
    #print(str(i)+": "+f)
    df = pd.read_csv(DIR+"/"+f, header=None , sep='\t', lineterminator='\n')
    df.columns=['b11','b12','b21','b22','b31','b32','b41','b42']
    date_col=[None]*df.shape[0]
    df['time_id']=date_col
    for idx, val in enumerate(df['time_id']):
        df.at[idx,'time_id']=datetime(int(f[0:4]),int(f[5:7]),
                                 int(f[8:10]), int(f[11:13]), 
                                 int(f[14:16]),int(f[17:19]), 5*idx+1)
    #print(df)
    dfex=dfex.append(df, ignore_index=True)
    if (i%BATCH == 0):
        print("\n--------------------")
        dfex.sort_values(by=['time_id'], inplace=True, ascending=True)
        dfex.to_csv(DIR+"/Mergedataset"+str(int(i/BATCH))+".csv", index = False,float_format='%.3f')
        dfex = pd.DataFrame(columns=['time_id','b11','b12','b21','b22','b31','b32','b41','b42'])
        print("saved: Mergedataset"+str(int(i/BATCH))+".csv")
        print(dfex.shape[0])
    
    i=i+1
dfex.sort_values(by=['time_id'], inplace=True, ascending=True)
dfex.to_csv(DIR+"/Mergedataset_FINAL.csv", index = False,float_format='%.3f')
print("saved: Mergedataset_FINAL.csv")
     
