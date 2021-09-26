#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class univ:
    def __init__ (self,akreditasi,jmlmhs,jmldosen):
        self.akreditasi=akreditasi
        self.jmlmhs=jmlmhs
        self.jmldosen=jmldosen
    def printname(self):
        print(self.akreditasi)
        print(self.jmlmhs)
        print(self.jmldosen)
        
class prodi(univ):
    def __init__ (self,akreditasi,jmlmhs,jmldosen):
        univ.__init__(self, akreditasi, jmlmhs, jmldosen)
        self.namamahasiswa="Aulia"
    
class kamda(univ):
    def __init__ (self,akreditasi,jmlmhs,jmldosen):
        univ.__init__(self,akreditasi,jmlmhs,jmldosen)
        self.namamahasiswa="Claudia"

x = prodi("C",170,"20")
y = kamda("B",1200,"60")

x.printname()
print(x.namamahasiswa)
y.printname()
print(y.namamahasiswa)


# In[ ]:





# In[ ]:




