# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:26:53 2020

@author: Rachit
"""

from sklearn import tree

#[height,weight,shoe_size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

x = int(input('Enter the Height: '))
y = int(input('Enter the Weight: '))
z =  int(input('Enter the Shoe Size: '))

pred = clf.predict([[x,y,z]])


print(pred)

