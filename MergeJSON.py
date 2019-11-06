import json
import os
from collections import defaultdict
from sys import getsizeof

FolderPath=input()
IP_BaseName=input()
OP_BaseName=input()
Max_Size=int(input())
FinalData=defaultdict(list)


def Merge(FName,Path):
    global FinalData
    with open(Path+'/'+FName) as DummyName:
        data= json.load(DummyName)
        DataKeys=list(data.keys())
        DataValues=list(data.values())
        for items in DataValues:
              FinalData[DataKeys[0]].append(items[0])
    

FolderFiles=os.listdir(FolderPath)
for data in FolderFiles:
    Name,Extension=data.split('.')
    if(Name.count(IP_BaseName)):
        Merge(data,FolderPath)

if(getsizeof(FinalData)<=Max_Size):
    with open(OP_BaseName+"1.json",'w') as json_file:
      json.dump(FinalData, json_file)
    #print("Merge Successful")
#else:
    #print("Size is greater than ",Max_Size)
        
