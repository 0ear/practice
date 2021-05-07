import numpy as np
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wb = openpyxl.load_workbook('assign2_data2.xlsx')
ws = wb.active
myList = [row for row in ws.values]
A = np.array(myList)
A = A[1:,:].T
A = np.array(A).astype(np.float)
print(A)
co = np.cov(A[1:,:], rowvar = False, bias = True)
print(co)  #covariance matrix
r = np.corrcoef(A)
print(r)

myList = pd.DataFrame(myList[0,:])
df = pd.DataFrame(A)
df = df.corr()
sns.set(font_scale = 1.5)
sns.heatmap(df, square=True, cmap='Blues', annot=True, annot_kws={'size': 15},
            xticklabels = myList.values,
            yticklabels = myList.values)
sns.displot(df, kde = False)
plt.show()