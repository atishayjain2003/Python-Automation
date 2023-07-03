#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pywhatkit as pw


# In[ ]:


y=input("Enter the message")
pw.sendwhatmsg_instantly("+91XXXXXXXX",y)
#+91XXXXXXXX represents the phone number to which message has to be sent 
#the instant function is used to send messages instantly 
#Condition 1, the user must be login through whatsapp web 
#Condition 2, the user needs to click the send or press enter button manually
#The messages being sent can also be scheduled, the just require hour and minute at which the message needs to be sent


# In[ ]:




