import pandas as pd
df = pd.read_csv('pyramid/newData.txt', sep = '\s+', engine = 'python', skiprows = 15)
df = df.T
#print(df)
print("swap:")
for i in range(0,df.shape[1], 1):
    if(pd.isna(df.at[df.index[4], i])):
        df[i] = df[i].shift(periods=2, freq=None, axis=0)
        
df=df.T
for i in range(1,df.shape[0], 1):
    if(pd.isna(df.at[df.index[i], 'TrgID'])):
        df.at[df.index[i], 'TrgID'] = df.at[df.index[i-1], 'TrgID']
print(df.at[df.index[2], 'TrgID'])

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


class Data():
    def __init__(self):
        self.data = [l0x,l1x,l2x,l3x]        

    def __str__(self):
        return f"{self.data}"
df

