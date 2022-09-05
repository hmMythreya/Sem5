import numpy as np
import pandas as pd
import random
import math

def get_entropy_of_dataset(df):
    target = list(df.iloc[:, -1])
    classes = []
    for i in target:
        if i not in classes: 
            classes.append(i)
    total = len(target)
    entropy = 0
    for i in classes:
        t_i = target.count(i)
        entropy = entropy - t_i/total * math.log2(t_i/total)
    return entropy

def get_avg_info_of_attribute(df, attribute):
    di = dict()
    for _,i in df.iterrows():
        selector = i[attribute]
        keys = list(di.keys())
        if selector in keys: 
            _class = i[-1]
            if(_class in list(di[selector].keys())):
                di[selector][_class] +=1
            else:
                di[selector][_class] = 1
            di[selector]["T0T41"] += 1
        else:
            _class = i[-1]
            di[selector] = dict()
            di[selector]["T0T41"] = 1
            di[selector][_class] = 1
    aia = 0
    for i in list(di.keys()):
        i_ele = di[i]
        total = i_ele["T0T41"]
        i_aia = 0
        for j in list(i_ele.keys()):
            if j!="T0T41":
                val = i_ele[j]
                i_aia = i_aia - (val/total) * math.log2((val/total))
        t_total = len(list(df.iloc[:, -1]))
        aia = aia + i_aia * total/t_total
    return aia

def get_information_gain(df, attribute):
    sample_entropy = get_entropy_of_dataset(df)
    attribute_info_gain = get_avg_info_of_attribute(df, attribute)
    return sample_entropy - attribute_info_gain

def get_selected_attribute(df):
    max_ = 0
    max_st = ""
    di = dict()
    for i in (df.columns)[:-1]:
        if i not in list(di.keys()):
            di[i] = get_information_gain(df, i)
            if di[i] > max_:
                max_ = di[i]
                max_st = i
    return (di,max_st)