import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st


sns.set(style="whitegrid", font_scale=1.2)
pd.set_option('precision', 2)
plt.rcParams['figure.figsize'] = (15, 8)

df = pd.read_csv('sikaz.csv')

# sns.displot(df[(df['price']<df['price'].quantile(.99))]['price']);



# f, ax = plt.subplots(figsize=(15, 8))
# ax.set_xscale("log")
# sns.boxplot(x="price", y="color", data=df.sort_values('price', ascending=False),
#             whis="range", palette="vlag")
# ax.xaxis.grid(True)
# ax.set(ylabel="")
# sns.despine(trim=True, left=True)
# plt.show()


df['mileage'] = df['mileage'].astype('int32')
df['price'] = df['price'].astype('int32')


def cutter(x):
    if x < 15:
        return x
    else:
        return x / 10
    
    
df['engine'] = df['engine'].apply(cutter)

print(df.duplicated().value_counts())


df.drop_duplicates(inplace = True)


y = np.log(df['price'])
X = df.drop(['price'], axis=1)


for cat_feature in X.columns[X.dtypes == 'object']:
    X[cat_feature] = X[cat_feature].astype('category')
    X[cat_feature].cat.set_categories(X[cat_feature].unique(), inplace=True)


X = pd.get_dummies(X, columns=X.columns[X.dtypes == 'category'])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.31, shuffle=True, random_state=20)
