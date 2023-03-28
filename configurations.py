# this file includes variables and configurations from the EDA notebook
# --------------------- Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from statsmodels.stats.power import TTestIndPower
from scipy.stats import chi2_contingency
import missingno as msno

from sklearn.model_selection import train_test_split

pd.set_option('display.max_colwidth', None) #setting max colwidth to view the entire dataset when using the print() command
from IPython.display import display
import matplotlib.patches as mpatches


# set random seed
np.random.seed(42)


# --------------------- Data Import
data = pd.read_csv('./dataset/breast-cancer.data', header=None)
data.columns = ['class', 'age', 'menopause', 'tumour_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irrad']


# --------------------- Data Processing
data = data.replace("?", np.nan)



# --------------------- Train & Test Split
X = data.drop(['class'], axis = 1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)