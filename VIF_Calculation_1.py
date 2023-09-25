#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(data_path):
    # Loading the data from specified path
    data =pd.read_csv(data_path)

    # Drop the 'Target' Column
    x = data.drop(columns=["Target"])
    y = data["Target"]

    # Seperate the Numerical and Categorical Culumns
    df_c = x.select_dtypes(include = "object")
    df_n = x.select_dtypes(include = "number")

    # convert categorical variables into dummy variables
    df = pd.get_dummies(df_c, drop_first = True)

    # Concatinate Numerical and Dummy varibles
    result = pd.concat([df, df_n], axis = 1)

    #Initilaize a dataframe to store VIF values
    vif = pd.DataFrame()
    vif["Variable"] = result.columns

    #Calculate VIF and assign values to the "VIF" column
    vif["VIF"] = [variance_inflation_factor(result.values, i) for i in range(result.shape[1])]
    
    return vif

if __name__ == "__main__":
    data_path = r"C:\Users\venka\OneDrive\Documents\PROJECTS\bank_dataset.csv"
    vif_result = calculate_vif(data_path)
    print("VIF Values: ")
    print(vif_result)


# In[ ]:




