#!/usr/bin/env python
# coding: utf-8

# In[1]:


class kucing:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
    
    def bersuara(self):
        print("meow")
        
class dog:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=nama
    
    def bersuara(self):
        print("guk guk..")

kucing1=kucing("Tom",3)
dog1=dog("Spike",3)

for hewan in (kucing1,dog1):
    hewan.bersuara()


# In[3]:


class kucing:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
    
    def bersuara(self):
        print(f"meow.. perkenalkan nama saya ",self.nama, "umur saya ", self.umur)
        
class dog:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=nama
    
    def bersuara(self):
        print(f"guk guk.. perkenalkan nama saya ",self.nama, "umur saya ", self.umur)

kucing1=kucing("Tom",3)
dog1=dog("Spike",3)

for hewan in (kucing1,dog1):
    hewan.bersuara()


# In[ ]:




