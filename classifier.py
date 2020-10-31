import xgboost as xgb
from xgboost import XGBClassifier
from data import Data
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, cross_validate, cross_val_predict, GridSearchCV, KFold


""" 
# ! eval_metric for train
# ! metric for cv
? Evaluation metrics for validation data, a default metric will be assigned according to objective 
* rmse for regression, 
* error for classification
* mean average precision for ranking 
"""

class Model:
    model  = XGBClassifier()
    cv   = KFold(n_splits=4, random_state=0, shuffle=True)


    def __init__(self, train, target, test=None):
        x, y = train.drop(target, axis=1), train[target]
        x_train, x_valid, y_train, y_valid = train_test_split(x, y, random_state=0, test_size=.2)

        if test is not None:
            if test.shape[1] != (x.shape[1]):
                print("Test and Train has different number of columns")
            test = test[[col for col in x.columns if col not in [target]]]
            self.xtest = test.values

        self.xtrain = x_train.values
        self.xvalid = x_valid.values
        self.ytrain = y_train.values
        self.yvalid = y_valid.values

    # ? Quick fit, no tuning
    def quick(self):
        self.model.fit(self.xtrain, self.ytrain)

    # ? Fit with some basic tuning
    def train(self):
        param_grid = {"n_estimators": [i for i in range(50, 1000, 50)]}
        self.model = GridSearchCV(self.model, param_grid=param_grid, scoring="accuracy", n_jobs=-1, verbose=2)
        self.model.fit(self.xtrain, self.ytrain)
        print(self.model.best_params_)
        print(self.model.best_score_)

    # ? Fit with extreme tuning, slowest time, need optimise all the parameters
    def tune(self):
        param_grid = {"n_estimators"      : [i for i in range(50, 2000, 50)],
                      "max_depth"         : [6, 7, 8, 9],
                      "learning_rate"     : [0.01, 0.05, 0.1, 0.2, 0.3],
                      "colsample_bytree"  : [0.5, 0.6, 0.7, 0.8],
                      "gamma"             : [float(i/10.0) for i in range(0,10)],
                      "min_child_weight"  : [1, 2, 3],
                      "subsample"         : [0.8, 1]}

        self.model = GridSearchCV(self.model, param_grid=param_grid, scoring="accuracy", n_jobs=-1, verbose=2)
        self.model.fit(self.xtrain, self.ytrain)
        print(self.model.best_params_)
        print(self.model.best_score_)


    def predict(self, filename="creditcard.csv"):        
        predictions = Data(self.model.predict(self.xtest))
        predictions.to_csv(filename)
        return predictions