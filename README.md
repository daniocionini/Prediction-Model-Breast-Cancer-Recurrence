# Breast Cancer Recurrence Prediction using Machine Learning
Breast cancer is the most commonly diagnosed cancer among women around the world.<br>In 2020 there were more than 2.26 million new cases of breast cancer worldwide and are estimated to grow in the future.<br><br>**On average, 7% to 11% of women experience recurrence within 10 years.**<br><br>
<img src="https://media.springernature.com/w735h400/nature-cms/uploads/cms/pages/1997/top_item_image/breastcancer_hero_01-34debb425f7e3e9fab5bf94575b49234.jpg" width="250">
## Key Informations about Breast Cancer
### What Causes Breast Cancer?
There are many risk factors known to cause breast cancer such as lifestyle-related risk factors and changes or mutations in genes. Certain inherited gene changes can greatly increase the risk for developing certain cancers.<br>The BRCA genes (*BRCA1 and BRCA2*) are tumor suppressor genes, a mutation in these genes can interupt the task to suppress abnormal cell growth, and cancer is more likely to develop.
### Types of Breast Cancer Overview
Most breast cancers are carcinomas, which are tumors that start in the epithelial cells that line organs and tissues throughout the body.<br>The cancer can also be considered **In situ** (the cancer has spread) or also **invasive** to describe any type of breast cancer that has spread into surrounding breast tissue.
### Key Statistics for Breast Cancer
Key survival element for breast cancer is early detection through screening and increased awareness, as well as better treatments.<br> At this time there are more than 3.8 million breast cancer survivors in the United States, including women still being treated and those who have completed treatment. At this time, a relative survival rate to a 5-year period is about 90%, depending on the type of breast cancer diagnosed.
### Immunotherapy for Breast Cancer
Immunotherapy is used to treat some types of breast cancer. Specific drugs target checkpoint proteins, used sometimes by breast cancer cells to avoid being attacked by the immune system. This therapy helps restore the immune response against breast cancer cells. **PD-1 inhibitor** (*Pembrolizumab*) is an example of this drug.
### Treatments for Breast Cancer
#### Radiation
Radiation therapy is a treatment with high-energy rays that destroy cancer cells.
#### Chemotherapy
Chemotherapy uses anti-cancer drugs that may be given intravenously or by mouth.
### Follow-up Care After Breast Cancer Treatment
*"On average, 7% to 11% of women experience recurrence within 10 years."*<br>
For some women with advanced breast cancer, the cancer may never go away completely. Follow-up care after Breast Cancer treatment can diagnose in time a recurrence of the cancer.<br>At the current time, the standard approach for monitoring patients is a physical exam and a review of symptoms anywhere from every three to six months for the first two or three years, then every six months until year five, and annually thereafter.<br><br> 
*It’s important to know that women who have had breast cancer can also still get other types of cancer, so it’s important to follow the <a href="https://www.cancer.org/healthy/find-cancer-early/american-cancer-society-guidelines-for-the-early-detection-of-cancer.html" target="_blank">American Cancer Society guidelines for the early detection of cancer</a>, such as those for colorectal cancer and cervical cancer.*
<br><br>
## Using Machine Learning to Predict the Recurrence of Breast Cancer
<img src="https://openexpoeurope.com/wp-content/uploads/2019/03/ai.png" width="400">
Machine Learning can be used to predict the risk of recurrence of the cancer on women based on cancer features and metrics.<br><br>

***This machine learning model is not a substitute to scheduled medical follow-up after cancer treatment.***

### Dataset
The dataset used for this model includes 286 instances of patient data collected by the Istitute of Oncology (University Medical Center) of Ljubljana, Yugoslavia and is available at <a href="https://archive.ics.uci.edu/ml/datasets/Breast+Cancer" target="_blank">UCI Machine Learning Repository</a>.<br><br> Variables in this dataset are:
- *Class*: whether or not there have been recurrence of the cancer
- *Age*: patient's age at the time of diagnosis
- *Monopause*: menopausal status of the patient at the time of diagnosis, pre-menopausal or post-menopausal at the time of diagnosis:
  - *ge40*: no further details have been provided
  - *lt40*: no further details have been provided
  - *premeno*: if the patient was on pre-menopause at the time of diagnosis
- *Tumor Size*: size of tumor (mm) at the time of diagnosis
- *Invasive Nodes*: the total number of lymph nodes confirming Breast Cancer at the time of the histological examination
- *Node Caps*: whether the tumor penetrated in the lymph node capsule
- *Degree of Malignancy*: divided into 1 -2 or 3, depending on the malignancy of the tumor
- *Breast*: the postion of the tumor (left or right breast)
- *Breast Quadrant*: the quadrant of the breast where the tumor is present
- *Irradiation*: wether radiation therapy has been used as treatment to destroy cancer cells
### The Model
This model is a **Classification** model. We want to predict whether a patient could get a recurrence of the cancer (*no-recurrence-events, recurrence-events*). The model can then be further implemented to predict using %.

<br>
<br>
<br>

*Reference Links:*<br>
https://www.linkedin.com/pulse/using-machine-learning-techniques-predict-recurrence-breast-alva/
https://archive.ics.uci.edu/ml/datasets/Breast+Cancer
https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/
https://github.com/NanditaA/ML-Supervised-Classification
https://www.cancer.org/cancer/breast-cancer.html
https://www.cancer.org/cancer/breast-cancer/living-as-a-breast-cancer-survivor/follow-up-care-after-breast-cancer-treatment.html
https://www.cancer.org/cancer/breast-cancer/living-as-a-breast-cancer-survivor/can-i-lower-my-risk-of-breast-cancer-progressing-or-coming-back.html
https://www.kaggle.com/code/najibmozahem/breast-cancer-python
