#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# ![image.png](attachment:image.png)

# In[2]:


data = pd.read_csv(r'https://raw.githubusercontent.com/nttuan8/DL_Tutorial/master/L1/data_square.csv')
data


# In[35]:


# diện tích 
X = [30, 32.4138,34.8276,37.2414,39.6552, 42.069, 44.4828, 46.8966, 49.3103, 51.7241, 54.1379, 56.5517, 58.9655,61.3793,63.7931,66.2069,68.6207,71.0345,73.4483,75.8621,78.2759,80.6897,83.1034,85.5172,87.931,90.3448,92.7586,95.1724,97.5862,100]
# Giá 
Y = [-100, -190.725, -269.798, -337.218, -392.985, -437.099, -469.56, -490.369, -499.524, -497.027, -482.878, -457.075, -419.62, -370.511, -309.75, -237.337, -153.27, -57.5505, 49.8216, 168.847, 299.524, 441.855, 595.838, 761.474, 938.763, 1127.71, 1328.3, 1540.55, 1764.45, 2000]


# In[36]:


curve = np.polyfit(X,Y,2)
print(curve)


# In[37]:


poly = np.poly1d(curve)
print (poly)


# In[38]:


Y_new = []

for i in X:
    value = poly(i)
    Y_new.append(value)
    


# In[39]:


print (Y_new)


# In[40]:


plt.plot(X, Y_new)


# In[41]:


plt.plot(X, Y_new)
plt.scatter(X, Y_new)
plt.show()


# ![image.png](attachment:image.png)

# In[47]:


# Fit đa thức bậc b0 

X1= [0,0.2,0.25,0.3,0.45,0.5,0.7,0.8,0.85,1]
Y1= [0.3,0.75,1,0.9,0,0.05,-0.95,-0.5,-0.6,0.2]


# In[48]:


plt.plot(X1,Y1)


# In[49]:


curve_0 = np.polyfit(X1,Y1,0)
print(curve)


# In[51]:


poly1 = np.poly1d(curve_0)
print(poly1)


# In[79]:


Y0_new = []

for i in X1:
    result = poly1(i)
    Y0_new.append(result)


# In[80]:


print (Y0_new)


# In[81]:


plt.plot(X1,Y0_new)


# In[82]:


plt.plot(X1, Y0_new)
plt.scatter(X1, Y1)
plt.show()


# In[83]:


# fit đa thức bậc 1 

curve_1 = np.polyfit(X1,Y1,1)
print (curve_1)


# In[84]:


poly2 = np.poly1d(curve_1)
print (poly2)


# In[86]:


Y1_new = []

for i in X1:
    result = poly2(i)
    Y1_new.append(result)


# In[87]:


print ( Y1_new)


# In[88]:


plt.plot(X1, Y1_new)
plt.scatter(X1, Y1)
plt.show()


# In[89]:


# fit đa thức bậc 3 


curve_3 = np.polyfit(X1,Y1,3)
print (curve_3)


# In[90]:


poly3 = np.poly1d(curve_3)
print (poly3)


# In[91]:


Y3_new = []

for i in X1:
    result = poly3(i)
    Y3_new.append(result)


# In[92]:


print (Y3_new)


# In[93]:


plt.plot(X1, Y3_new)
plt.scatter(X1, Y1)
plt.show()


# In[94]:


# fit đa thức bậc 6

curve_6 = np.polyfit(X1,Y1,6)
print (curve_6)


# In[95]:


poly6 = np.poly1d(curve_6)
print (poly6)


# In[96]:


Y6_new = []

for i in X1:
    result = poly6(i)
    Y6_new.append(result)


# In[97]:


print (Y6_new)


# In[98]:


plt.plot(X1, Y6_new)
plt.scatter(X1, Y1)
plt.show()


# In[99]:


# fit đa thức bậc 9 

curve_9 = np.polyfit(X1,Y1,9)
print (curve_9)


# In[100]:


poly9 = np.poly1d(curve_9)
print (poly9)


# In[101]:


Y9_new = []

for i in X1:
    result = poly9(i)
    Y9_new.append(result)


# In[102]:


print (Y9_new)


# In[103]:


plt.plot(X1, Y9_new)
plt.scatter(X1, Y1)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




