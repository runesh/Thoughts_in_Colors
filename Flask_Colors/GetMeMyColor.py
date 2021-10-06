#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bing_image_downloader import downloader
import cv2
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt
import os


# In[22]:


colorz = []


# In[2]:


def downloadimagesBing(query):
    downloader.download(query, limit=5,  output_dir='BingImg', adult_filter_off=True, force_replace=False, timeout=60)


# In[23]:


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image 

def convert(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_colours (image):
    img = cv2.resize(image, (600, 400))
    img = img.reshape(img.shape[0] * img.shape[1], 3)
    cluster = KMeans(n_clusters = 3)
    labels = cluster.fit_predict(img)
    ct = Counter(labels)
    center = cluster.cluster_centers_
    order = [center[i] for i in ct.keys()]
    hex_color = [convert(order[i]) for i in ct.keys()]
    return hex_color
    
def get_eachImgColor(path):
    global colorz
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = get_image(path)
    colorz.extend(get_colours(img))


# In[28]:


def fetchColors(query):
    global colorz
    colorz = []
    downloadimagesBing(query)
    myPath = os.path.abspath(os.getcwd())
    for i in range(1,6):
        pathI = myPath+f'\\BingImg\\{query}\\Image_{i}.jpg'
        get_eachImgColor(pathI)
    
    return colorz

