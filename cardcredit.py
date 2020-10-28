# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from pathlib import Path
from sklearn.preprocessing import RobustScaler
warnings.filterwarnings("ignore")
plt.style.use('bmh')


class fraudDetector:
    def getfile(fileName):
        arr=[]
        
# %%
        
        df = data = pd.read_csv(fileName)
        df.head()


# %%
        df.describe()


# %%
        df.isnull().sum() # find out the number of empty rows


# %%
        df.dtypes
        fileName=Path(fileName).name
        fileNoExtension=fileName.rsplit('.', 1)[0]

# %%
        sns_plot=sns.countplot(x='Class', data=df, palette = 'CMRmap')
        sns_plot.get_figure().savefig("firstGraph_"+fileNoExtension+".png")
      
        
        
       # print('List of Non Fraudulent transactions: {}%'.format(round(df.Class.value_counts()[0]/len(df)*100.0,2)))
        arr.append('List of Non Fraudulent transactions: {}%'.format(round(df.Class.value_counts()[0]/len(df)*100.0,2)))
      
        #print('Fraud transactions: {}%'.format(round(df.Class.value_counts()[1]/len(df)*100.0,2)))
        arr.append('Fraud transactions: {}%'.format(round(df.Class.value_counts()[1]/len(df)*100.0,2)))
        
        arr.append("firstGraph_"+fileNoExtension+".png")
#null.tpl [markdown]
# ### Severely imbalanced as you can see from the percentage and fraud transactions only 0.17%. Algorithms most likely move the new data to the majority class and high accuracy won't be able to tell much from it.
# ### Oversampling and undersampling can be used as data approach techniques, oversampling increases number of minority class members in training set, no information is lost.
# ### Undersampling is when all observations from minority and majority class are kept. 

# %%
        print("first graph?")
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        ax1 = sns.distplot(df['Time'], ax=ax1, color='y')
        ax2 = sns.distplot(df['Amount'], ax=ax2, color='r')
        ax1.set_title('Distribution of Time', fontsize=13)
        ax2.set_title('Distribution of Amount', fontsize=13)
        plt.savefig("secondGraph_"+fileNoExtension+".png")  
        arr.append("secondGraph_"+fileNoExtension+".png")
        
#null.tpl [markdown]
# ### Seeing distributions of transaction times and amount, seeing how skewed the features are.
# ### They went through Principal Component Analysis, which is a faster algorithm, which shows that the models were previously scaled before!
#null.tpl [markdown]
# #### Normalising distribution using Robustscaler

# %%

        rs = RobustScaler()
        df['scaled_amount'] = rs.fit_transform(df['Amount'].values.reshape(-1,1))
        df['scaled_time'] = rs.fit_transform(df['Time'].values.reshape(-1,1))
        df.drop(['Time', 'Amount'], axis=1, inplace=True)
## Normalising distribution, use Robust Scaler Algorithm. Robust to outliers


# %%
        scaled_amount = df['scaled_amount']
        scaled_time = df['scaled_time']
        df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
        df.insert(0, 'scaled_amount', scaled_amount)
        df.insert(0, 'scaled_time', scaled_time)
        df.head()
        
        return arr
    
fraudDetector.getfile(r'creditcard.csv')

#null.tpl [markdown]
# ### Scaling out the time and amount. 
#null.tpl [markdown]
# ### Synthetic Minority over-sampling technique
