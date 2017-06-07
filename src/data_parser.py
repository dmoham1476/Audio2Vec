#!/usr/bin/env python3
import sklearn
import argparse
import numpy as np
import csv

def read_csv_file(filename):
    lab = []
    feats = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            feats.append(list(map(float,row[:-1])))
            lab.append(int(row[-1]))
    return feats, lab

def build_dic(filename):
    dic = {}
    rev_dic = {}
    with open(filename,'r') as f:
        for line in f:
            word, ID= line.rstrip().split()
            dic[word] = int(ID)
            rev_dic[int(ID)] = word

    return dic, rev_dic

def build_targets(filename, dic):
    targets = []
    with open(filename,'r') as f:
        for line in f:
            targets.append(dic[line.rstrip()])

    return targets

def build_label_color_list(target_list, color_list):
    ''' assume the targets are in pairs 


    '''
    word_color_dict = {}
    for i, target in enumerate(target_list):
        word_color_dict[target] = color_list[i%len(color_list)]

    return word_color_dict

def write_feat_lab(filename, feats, labs, delimiter=' '):
    ''' write a csv like file with feature list and label list
    args:
      filename: The output filename
      feats: the feature list with (num_occur, feat_dim)
      labs: the label list with length = num_occur
      delimiter: the delimiter in csv file
    '''
    with open(filename,'w') as f:
        for i, feat_list in enumerate(feats):
            for j in feat_list:
                f.write(str(j)+ delimiter)
            f.write(str(labs[i])+'\n')

    return 

