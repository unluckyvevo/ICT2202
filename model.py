import xgboost as xgb
from data import Data
from xgboost import XGBRegressor
from xgboost import XGBClassifier
from xgboost import XGBRanker
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold


class Model:

    cv = KFold(n_splits=4, random_state=0, shuffle=True)
    param_grid = {}

    param_classifier = {
                        "n_estimators"      : [i for i in range(1, 100, 5)],
                        "max_depth"         : [5, 6, 7],
                        "min_child_weight"  : [1, 2, 3],
                        "eta"               : [0.2, 0.3, 0.4],
                        "subsample"         : [0.7, 0.8, 0.9],
                        "colsample_bytree"  : [0.7, 0.8, 0.9],
                        "gamma"             : [0.0, 0.5, 1.0]
                        }

    param_regressor =  {
                        "objective"       : "reg:squarederror",   # * 
                        "booster"         : "gbtree",             # *
                        "n_estimators"    : [i for i in range(1, 100, 5)],
                        "max_depth"       : [5, 6, 7],            # * 6
                        "min_child_weight": [1, 2, 3],            # * 1
                        "eta"             : [0.2, 0.3, 0.4],      # * 0.3
                        "subsample"       : [0.7, 0.8, 0.9],      # * 1
                        "colsample_bytree": [0.7, 0.8, 0.9],      # * 1
                        "gamma"           : [0.0, 0.5, 1.0]       # * 0
                        }     

    param_fit = {}

    def __init__(self, model, train, test, target):
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
        self.model = model
        self.param_fit["eval_set"] = [[self.xvalid, self.yvalid]]

        if isinstance(self.model, XGBRegressor):
            self.scoring="neg_mean_squared_error"
            self.param_grid = self.param_regressor
            self.model.objective = "reg:squarederror"
            self.param_fit["eval_metric"] = "rmse"

        elif isinstance(self.model, XGBClassifier):
            self.scoring="accuracy"
            self.param_grid = self.param_classifier
            self.param_fit["eval_metric"] = "error"

        else:
            self.scoring="precision"
            self.param_grid = self.param_classifier
            self.param_fit["eval_metric"] = "map"


    # ? Quick fit, no tuning
    def quick(self):
        self.model.fit(self.xtrain, self.ytrain, **self.param_fit)
        return self.predict()
        

    # ? Fit with some basic tuning
    def train(self):
        param_grid = {"n_estimators": [i for i in range(1, 50, 2)]}
        self.model = GridSearchCV(self.model, param_grid=param_grid, scoring=self.scoring, n_jobs=4, verbose=2)
        self.model.fit(self.xtrain, self.ytrain, **self.param_fit)
        print(self.model.best_params_)
        print(self.model.best_score_)
        return self.predict()


    # ? Fit with extreme tuning
    def tune(self):
        self.model = GridSearchCV(self.model, param_grid=self.param_grid, scoring=self.scoring, n_jobs=4, verbose=2)
        self.model.fit(self.xtrain, self.ytrain, **self.param_fit)
        print(self.model.best_params_)
        print(self.model.best_score_)
        return self.predict()


    def predict(self, filename="creditcard.csv"):        
        predictions = Data(self.model.predict(self.xtest))
        predictions.to_csv("creditcard.csv")
        return predictions