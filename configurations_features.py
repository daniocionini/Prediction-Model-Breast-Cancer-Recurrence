from configurations import *
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest, chi2, f_classif, f_regression
from sklearn.model_selection import GridSearchCV

"""
- nominal features
    - menopause
    - node_caps
    - breast
    - breast_quad
    - irrad
    - class (*target feature*)
- ordinal features
    - age
    - tumour_size
    - inv_nodes
- numerical feature
    - deg_malig
"""

# Encode nominal features using one-hot encoding with drop_first=True
X_train_nominal = pd.get_dummies(X_train[['node_caps', 'breast_quad', 'irrad']], drop_first=True)

# Perform label encoding for ordinal features
label_encoder = preprocessing.LabelEncoder()
X_train_ordinal = X_train[['inv_nodes', 'tumour_size']].copy()  
for col in X_train_ordinal.columns:
    X_train_ordinal.loc[:, col] = label_encoder.fit_transform(X_train_ordinal[col])

X_train_numerical = X_train[['deg_malig']]

X_train_encoded = pd.concat([X_train_nominal, X_train_ordinal, X_train_numerical], axis=1)

y_train_encoded = y_train.replace(['no-recurrence-events', 'recurrence-events'], [0,1])