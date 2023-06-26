import pandas as pd
df = pd.read_csv('pyramid/newData.txt', sep = '\s+', engine = 'python', skiprows = 15)
df = df.T
#print(df)
#print("swap:")
for i in range(0,df.shape[1], 1):
    if(pd.isna(df.at[df.index[4], i])):
        df[i] = df[i].shift(periods=2, freq=None, axis=0)
        
df=df.T
for i in range(1,df.shape[0], 1):
    if(pd.isna(df.at[df.index[i], 'TrgID'])):
        df.at[df.index[i], 'TrgID'] = df.at[df.index[i-1], 'TrgID']
#print(df.at[df.index[2], 'TrgID'])
#Outdated method
l0x = [[0] * 28, [0]*28, [0]*28]
l1x = [[0] * 28, [0]*28, [0]*28]
l2x = [[0] * 28, [0]*28, [0]*28]
l3x = [[0] * 28, [0]*28, [0]*28]

i = 0
while(df.at[df.index[i], 'TrgID'] == 0):
    l0x[int((df.at[df.index[i], 'Brd'])/2)][int(df.at[df.index[i], 'Ch'])] = df.at[df.index[i], 'LG']
    i+=1
while(df.at[df.index[i], 'TrgID'] == 1):
    l1x[int((df.at[df.index[i], 'Brd'])/2)][int(df.at[df.index[i], 'Ch'])] = df.at[df.index[i], 'LG']
    i+=1
while(df.at[df.index[i], 'TrgID'] == 2):
    l2x[int((df.at[df.index[i], 'Brd'])/2)][int(df.at[df.index[i], 'Ch'])] = df.at[df.index[i], 'LG']
    i+=1
while(i< df.shape[0] and df.at[df.index[i], 'TrgID'] == 3):
    l3x[int((df.at[df.index[i], 'Brd'])/2)][int(df.at[df.index[i], 'Ch'])] = df.at[df.index[i], 'LG']
    i+=1

#print("Event 0:")
#print(l0x)
#print("Event 1:")
#print(l1x)
#print("Event 2:")
#print(l2x)
##print("Event 3:")
#print(l3x)

#New method    total[event][detector level: 0 = top][channel: 0 = rightmost triangle]
total = []
id = 0
i=0
while(id <= int(df.at[df.index[df.shape[0]-1], 'TrgID'])):
    #print(df.at[df.index[df.shape[0]-1], 'TrgID'])
    
    total.append([[0] * 28, [0]*28, [0]*28])
    while(i< df.shape[0] and df.at[df.index[i], 'TrgID'] == id):
        #print("Entry:")
        #print(id)
        #print(int((df.at[df.index[i], 'Brd'])/2))
        #print(int(df.at[df.index[i], 'Ch']))
        #print(df.at[df.index[i], 'LG'])
        total[id][int((df.at[df.index[i], 'Brd'])/2)][int(df.at[df.index[i], 'Ch'])] = df.at[df.index[i], 'LG']
        i+=1
    id +=1
    
print("3D array of awsomeness:")
print(total)

class Data():
    def __init__(self):
        self.data = total
df


