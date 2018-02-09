
# coding: utf-8

# # Aldez aurretik ezarritako terminoak aldatzeko itzultzailea 
# * Python Jupyter notebook. Python 3-rekin funtzionatzen du
# * Hiztegitxoa: "csv"-a aldatu jatorrizko terminologiakin 
# * Aldatzeko: ".txt" aldatu nahi diren terminoekin
# * Aldatuta: "txt" hiztegitxoarekin aldatutako terminoekin

#     Libreriak importatu

# In[37]:

import string # strings
import csv    # csv
import re     # regular expresions (letra larriak...)


#     Hiztegitxorako artxiboa ireki ("rU" edo "r" Python bertsioaren arabera)     

# In[38]:

dict_file = open("hiztegitxoa.csv", "r")


#     csv-an dagoena irakurri

# In[39]:

csv_content = csv.reader(dict_file, delimiter=';', dialect=csv.excel_tab)


#     Hiztegi hutsa sortu

# In[40]:

full_dict = {}


#     "key" eta "value"ak asignatu (row[1] = bigarren zutabea eta row[2] lehenengo zutabea da)

# In[41]:

for row in csv_content:
   full_dict[row[1]] = row[0]


# In[42]:

print (full_dict)


#     Aldatu nahi dugn testua, r+ read, edo write eta abar.

# In[43]:

file_object  = open("aldatzeko.txt", "r+")


#     Edukiarentzako sortu oinarri bat

# In[44]:

current_text = file_object.read()


# In[45]:

new_text =  current_text


#     Letra larriak eta xeheak ez bereiztu (string.capwords)

# In[46]:

for key in full_dict:
    insensitive_key = re.compile(re.escape(key), re.IGNORECASE) 
    new_text = insensitive_key.sub(string.capwords(full_dict[key]), new_text)


#     Artxibo berria sortu

# In[47]:

new_file_object = open("aldatuta.txt", "w")


# Guardar el archibo nuevo!

# In[48]:

new_file_object.write(new_text)


# Orain aldatuta.txt artxiboan terminoak itzulita agertuko dira!

# In[ ]:



