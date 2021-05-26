#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy.stats import pearsonr
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


x=np.array([30, 40, 40, 20, 12, 31, 10]).reshape((-1,1))
y=np.array([160, 160, 170, 50, 110, 160, 100])
print(x)
print(y)


# In[46]:


corr, _ = pearsonr(x.reshape(-1),y)
print("Pearson correlation:%.3f" % corr)


# In[ ]:





# In[47]:


model = LinearRegression().fit(x,y)


# In[48]:


r_sq=model.score(x, y)
print('coefficient of determination:',r_sq)


# In[49]:


print('beta0 =', model.intercept_)
print('beta1= ' , model.coef_)


# In[50]:


y_pred0=model.intercept_ + model.coef_*x.reshape(-1)
print('predicted response:', y_pred0, sep='\n')


# In[51]:


y_pred = model.predict(x)
print('predicted response:',y_pred, sep='\n')


# In[52]:


real= plt.scatter(x,y)
plt.plot(x,y_pred0, color='red')

pred=plt.scatter(x,y_pred,c='green');

plt.legend((real,pred), 
           ('Real y', 'Predicted y'),
           scatterpoints=1,
           loc='lower right',
           ncol=3,
           fontsize=8)
plt.show()


# In[ ]:




