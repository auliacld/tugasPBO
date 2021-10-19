#!/usr/bin/env python
# coding: utf-8

# In[16]:


class kambing:
    def __init__(self,kaki,berat,nama):
        self.kaki=kaki
        self.berat=berat
        self.nama=nama
    
    def bunyi(self):
        print(f"mbee.. saya berkaki ",self.kaki, "berat saya ", self.berat, "saya adalah ", self.nama)
        
class sapi:
    def __init__(self,kaki,berat,nama):
        self.kaki=kaki
        self.berat=berat
        self.nama=nama
    
    def bunyi(self):
        print(f"moo.. saya berkaki ",self.kaki, "berat saya ", self.berat, "saya adalah ", self.nama)
        
hewan1 = kambing("Empat","30 Kg","Kambing")
hewan2 = sapi("Empat","230 Kg","Kapi")

for hewan in (hewan1,hewan2):
    hewan.bunyi()


# In[ ]:




