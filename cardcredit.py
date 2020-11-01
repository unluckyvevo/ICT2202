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
from sklearn.model_selection import train_test_split as holdout
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_recall_curve, classification_report, precision_score, recall_score, accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier as rfc
import xgboost as xgb
warnings.filterwarnings("ignore")
plt.style.use('bmh')


class fraudDetector:
    def getfile(fileName):
        arr=[]
        
# %%
        
        df = pd.read_csv(fileName)
        df.head() 
        #arr.append(df.head().to_string())

# %%
        df.describe()


# %%
        df.isnull().sum() # find out the number of empty rows


# %%
        df.dtypes
        fileName=Path(fileName).name
        fileNoExtension=fileName.rsplit('.', 1)[0]

# %%
        plt.figure()
        sns_plot=sns.countplot(x='Class', data=df, palette = 'CMRmap')
        sns_plot.get_figure().savefig("firstGraph_"+fileNoExtension+".png")
      
        
        
       # print('List of Non Fraudulent transactions: {}%'.format(round(df.Class.value_counts()[0]/len(df)*100.0,2)))
        arr.append('List of Non Fraudulent transactions: {}%'.format(round(df.Class.value_counts()[0]/len(df)*100.0,2)))
      
        #print('Fraud transactions: {}%'.format(round(df.Class.value_counts()[1]/len(df)*100.0,2)))
        arr.append('Fraud transactions: {}%'.format(round(df.Class.value_counts()[1]/len(df)*100.0,2)))
        arr.append('Imbalanced Class Graph')
        arr.append('===========================')
        arr.append("firstGraph_"+fileNoExtension+".png") # 4 
        
        
        
#null.tpl [markdown]
# ### Severely imbalanced as you can see from the percentage and fraud transactions only 0.17%. Algorithms most likely move the new data to the majority class and high accuracy won't be able to tell much from it.
# ### Oversampling and undersampling can be used as data approach techniques, oversampling increases number of minority class members in training set, no information is lost.
# ### Undersampling is when all observations from minority and majority class are kept. 

# %%
      
        plt.figure()
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        ax1 = sns.distplot(df['Time'], ax=ax1, color='y')
        ax2 = sns.distplot(df['Amount'], ax=ax2, color='r')
        ax1.set_title('Distribution of Time', fontsize=13)
        ax2.set_title('Distribution of Amount', fontsize=13)
        plt.savefig("secondGraph_"+fileNoExtension+".png")
        arr.append('show how skewed the features are:')
        arr.append('================================')
        arr.append("secondGraph_"+fileNoExtension+".png") # 7
        
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
        
        

# %%

        plt.figure()
        x = np.array(df.iloc[:, df.columns != 'Class'])
        y = np.array(df.iloc[:, df.columns == 'Class'])
        x_train, x_test, y_train, y_test = holdout(x, y, test_size=0.2, random_state=0)
        arr.append(("Transaction Number x_train dataset: "+ str(x_train.shape)))
        arr.append(("Transaction Number y_train dataset: "+ str(y_train.shape)))
        arr.append(("Transaction Number x_test dataset: "+ str(x_test.shape)))
        arr.append(("Transaction Number y_test dataset: "+ str(y_test.shape)))

        arr.append(str("Before OverSampling, counts of label '1': {}".format(sum(y_train==1))))
        arr.append(str("Before OverSampling, counts of label '0': {} \n".format(sum(y_train==0))))
        
        
        
        sm = SMOTE(random_state=2)
        x_train_s, y_train_s = sm.fit_sample(x_train, y_train.ravel())
        arr.append(str('After OverSampling, the shape of train_x: {}'.format(x_train_s.shape)))
        arr.append(str('After OverSampling, the shape of train_y: {} \n'.format(y_train_s.shape)))
        arr.append(str("After OverSampling, counts of label '1', %: {}".format(sum(y_train_s==1)/len(y_train_s)*100.0,2)))
        arr.append(str("After OverSampling, counts of label '0', %: {}".format(sum(y_train_s==0)/len(y_train_s)*100.0,2)))
        
        

        sns.countplot(x=y_train_s, data=df, palette='CMRmap')
        labels = ['Non-fraud', 'Fraud']
        
        plt.savefig("Balanced Dataset_"+fileNoExtension+".png")
        arr.append('Balanced Dataset')
        arr.append('================================')
       # arr.append((classification_report(y_test, y_pred, target_names=labels)).to_string())
        arr.append("Balanced Dataset_"+fileNoExtension+".png") #20
        

# %%        
        
        plt.figure()
        logreg = LogisticRegression()
        logreg.fit(x_train_s, y_train_s)
        y_pred = logreg.predict(x_test)
        cnf_matrix = confusion_matrix(y_test, y_pred)

        sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
        plt.ylabel('Actual Label')
        plt.xlabel('Predicted Label')
        arr.append('Logistic Regression With SMOTE')
        arr.append('================================')
        
        
        plt.savefig("LogisticRegressionSMOTE_"+fileNoExtension+".png")
        arr.append("LogisticRegressionSMOTE_"+fileNoExtension+".png") # 23
        with open('LogisticRegressionSMOTE.txt', 'w') as f:
            print(classification_report(y_test, y_pred), file=f)
        f = open("LogisticRegressionSMOTE.txt", "r")
        contents=f.read()
        arr.append(contents)
        
        

# %%
        
        plt.figure()
        y_pred_problem = logreg.predict_proba(x_test)[:,1]
        precision, recall, thresholds = precision_recall_curve(y_test, y_pred_problem)
        plt.plot(precision, recall)
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Precision Recall Curve')
        arr.append('By analysing this graph, you can see the model is able to detect huge numbers of fraudulent transactions as the recall is very high from 0.8 -1 but the precision starts to drop at the end of the model, telling us that the model treats non-fraud cases as fraud. This causes mistrust of companies that uses these models, hence its important that the precision must be kept as high as possible.')
        arr.append('================================')
        
        
        plt.savefig("LogRegprecisionrecallGraph_"+fileNoExtension+".png")
        arr.append("LogRegprecisionrecallGraph_"+fileNoExtension+".png") # 26



    

# %%
        
        #random Forest
        plt.figure()
        rand_f = rfc(n_estimators=1000, min_samples_split=10, min_samples_leaf=1,
           max_features='auto', max_depth=6, verbose=3, max_leaf_nodes=None,
           oob_score=True, n_jobs=-1, random_state=1)
        rand_f.fit(x_train_s, y_train_s)
        y_pred = rand_f.predict(x_test)

        cnf_matrix = confusion_matrix(y_test, y_pred)
        sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
        plt.ylabel('Actual Label')
        plt.xlabel('Predicted Label')
        plt.savefig("randomForestHeat_"+fileNoExtension+".png")
        
        #8
        
        arr.append("randomForestHeat_"+fileNoExtension+".png") # 27
        with open('randomForest_HeatMap.txt', 'w') as f:
            print(classification_report(y_test, y_pred), file=f)
        f = open("randomForest_HeatMap.txt", "r")
        contents=f.read()
        arr.append(contents) 
      
# %%            
        
        plt.figure()
        y_pred_prob = rand_f.predict_proba(x_test)[:,1]
        precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)
        plt.plot(precision, recall)
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Precision Recall Curve')
        arr.append('Random Forest With SMOTE')
        arr.append('================================')
        plt.savefig("randomForestRecall_"+fileNoExtension+".png")
        arr.append("randomForestRecall_"+fileNoExtension+".png") #31
        
        
        

# %%         
        return arr
    
fraudDetector.getfile(r'creditcard.csv')

#null.tpl [markdown]
# ### Scaling out the time and amount. 
#null.tpl [markdown]
# ### Synthetic Minority over-sampling technique
