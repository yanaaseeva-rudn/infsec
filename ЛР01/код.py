#!/usr/bin/env python
# coding: utf-8

# In[18]:


def cesar(text, step, p=0):
    liters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяaбвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ''
    if p==1:
        for i in text:
            index = liters.find(i)
            new_index = index + step
            if i in liters:
                res += liters[new_index]
            else:
                res += i
    if p == 0:
        for i in text:
            index = liters.find(i)
            new_index = index - step
            if i in liters:
                res += liters[new_index]
            else:
                res += i
                
    return res


# In[19]:


t = 'физмат сила'


# In[20]:


print(f'{t} - {cesar(t, 3, 1)} - {cesar(cesar(t, 3, 1), 3, 0)}')


# In[23]:


def atbash(text, p=0):
    liters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    liters_r = [i for i in liters]
    liters_r.reverse()
    res=''
    if p==1:
        for i in text:
            for j,l in enumerate(liters):
                if i==l:
                    res += liters_r[j]
    if p==0:
        for i in text:
            for j,l in enumerate(liters_r):
                if i==l:
                    res += liters[j]
    
    return res


# In[24]:


print(f'{t} - {atbash(t, 1)} - {atbash(atbash(t, 1), 0)}')


# In[ ]:




