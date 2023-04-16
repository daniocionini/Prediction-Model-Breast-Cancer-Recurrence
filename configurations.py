# this file includes variables and configurations from the EDA notebook
# --------------------- Libraries
# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 

from statsmodels.stats.power import TTestIndPower
from scipy import stats
import warnings
import missingno as msno

from sklearn.model_selection import train_test_split

pd.set_option('display.max_colwidth', None) #setting max colwidth to view the entire dataset when using the print() command
from IPython.display import display
import matplotlib.patches as mpatches


# set fixed random seed
np.random.seed(42)


# --------------------- Data Import
data = pd.read_csv('./dataset/breast-cancer.data', header=None)
data.columns = ['class', 'age', 'menopause', 'tumour_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irrad']


# --------------------- Data Processing
data = data.replace("?", np.nan)



# --------------------- Train & Test Split
TARGET_NAME = "class"
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=[TARGET_NAME]), 
                                                    data[TARGET_NAME], 
                                                    test_size=0.30,
                                                    stratify=data[TARGET_NAME],
                                                    random_state=42)


# --------------------- Train & Test CSV
data_train = pd.read_csv("./dataset/data_train.csv")
data_test = pd.read_csv("./dataset/data_test.csv")