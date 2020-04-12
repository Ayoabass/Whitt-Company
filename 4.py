#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:36:23 2020

@author: AyodejiAbass
"""


from pulp import *
# Define the Model
prob = LpProblem("CitruSun Corporation", LpMinimize) 

x1 = LpVariable('Miami Eustis', lowBound = 0, cat='Integer') 
x2 = LpVariable('Orlando Eustis', lowBound = 0, cat='Integer')
x3 = LpVariable('Tallahassee Eustis', lowBound = 0, cat='Integer') 
y1 = LpVariable('Miami Clermont', lowBound = 0, cat='Integer') 
y2 = LpVariable('Orlando Clermont', lowBound = 0, cat='Integer') 
y3 = LpVariable('Tallahassee Clermont', lowBound = 0, cat='Integer')  
#Objective function
prob += 260*x1 + 220*x2 + 290*x3 + 220*y1 + 240*y2 + 320*y3 , "obj"

#Constaints
prob += x1 + x2 + x3 <= 20, 'Eustis'
prob += y1 + y2 + y3 <= 20, 'Clermont'
prob += x1 + y1 == 10, 'Miami'
prob += x2 + y2 == 15, 'Orlando'
prob += x3 + y3 == 10, 'Tallahassee'
print(prob)

prob.solve()
print('status:' + LpStatus[prob.status])
## Optimal
for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))

print('The Objective value = ',value(prob.objective))