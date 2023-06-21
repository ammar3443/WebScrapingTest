#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.firefox.options import Options


driver = webdriver.Firefox()
driver.get("https://github.com/collections/machine-learning")
project_list = {}
projects = driver.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']//a")

for proj in projects:
    proj_name = proj.text 
    project_url = proj.get_attribute('href')
    project_list[proj_name] = project_url

print(project_list)    
driver.quit()




# In[74]:


import pandas as pd
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)
project_df.to_csv('project_list.csv')


# In[ ]:




