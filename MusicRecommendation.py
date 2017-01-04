import pandas as pd
from scipy.spatial.distance import cosine
 
fullData = pd.read_csv('musicdata.csv')

musicData = fullData.drop('user', 1)
 
# Creating artist vs astist matrix with blanks
itemBased = pd.DataFrame(index = musicData.columns, columns = musicData.columns)

# Filling values to the blank matrix with cosine similarities

for i in range(0, len(itemBased.columns)) :
    for j in range(0, len(itemBased.columns)) :
      itemBased.ix[i,j] = 1-cosine(musicData.ix[:,i],musicData.ix[:,j])

predictions = pd.DataFrame(index = itemBased.columns, columns=[range(1,21)])
 
for i in range(0, len(itemBased.columns)):
    predictions.ix[i,:20] = itemBased.ix[1:,i].sort_values(ascending = False)[:20].index

print(predictions.head(10).ix[10,2:5])
    
