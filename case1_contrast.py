# -*- coding:utf-8-*-


from tkinter import *
from sklearn.metrics.pairwise import rbf_kernel

import csv
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster,cut_tree,cophenet,inconsistent
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot as plt
from matplotlib.pyplot import xticks
import pandas as pd
from scipy.spatial import distance
from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来
import json
from sklearn.metrics.pairwise import euclidean_distances
import re
from orangecontrib.associate.fpgrowth import *
from collections import Counter
from gensim.models import KeyedVectors
from sklearn.metrics import silhouette_samples, silhouette_score, davies_bouldin_score






'''
Case1对比结果展示
'''
class contrast_display:
    def __init__(self):
        self.contrast_lb = Tk()
        self.contrast_lb.title('对比结果展示')
