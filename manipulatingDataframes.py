import pandas as pd
import numpy as np

test_date = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataframe = pd.DataFrame(test_date, index=labels)

# Print the first three rows
print("First three rows:")
print(dataframe.head(3))

dataframe.dropna(inplace=True)

name_score_dataframe = dataframe[['name', 'score']]
print("\nExtracted 'name' and 'score' columns:")
print(name_score_dataframe)

new_row = pd.Series({'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}, name='k')
dataframe = dataframe.append(new_row)

dataframe.drop(columns=['attempts'], inplace=True)

dataframe['Success'] = dataframe['score'].apply(lambda x: 1 if x > 10 else 0)

print("\nFinal DataFrame:")
print(dataframe)

dataframe.to_csv('my_data.csv')
