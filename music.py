import pandas as pd
from scipy.spatial.distance import cosine
 
fullData = pd.read_csv('C:/Users/Abhay Bhat/Downloads/lastfm-matrix-germany.csv')

musicData = fullData.drop('user', 1)
 
# Creating artist vs astist matrix
itemBased = pd.DataFrame(index = musicData.columns, columns = musicData.columns)

# Filling values to the matrix with cosine similarities

for i in range(0, len(itemBased.columns)) :
    for j in range(0, len(itemBased.columns)) :
      itemBased.ix[i,j] = 1-cosine(musicData.ix[:,i],musicData.ix[:,j])

predictions = pd.DataFrame(index = itemBased.columns, columns=[range(1,11)])
 
for i in range(0, len(itemBased.columns)):
    predictions.ix[i,:10] = itemBased.ix[1:,i].sort_values(ascending = False)[:10].index

print(predictions.head(5).ix[5,2:5])
    