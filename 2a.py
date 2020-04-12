#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:16:37 2020

@author: AyodejiAbass
"""


from pulp import *
prob = LpProblem("Problem 2.", LpMinimize)
x1 = LpVariable('x_1', lowBound = 0)
x2 = LpVariable('x_2', lowBound = 0)
x3 = LpVariable('x_3', lowBound = 0)
# Objective function
prob += 3*x1 + 3*x2 + 5*x3, "Obj"
# Constraints
prob += 2*x1 + x3 >= 8
prob += x2 + x3 >= 6
prob += 6*x1 + 8*x2 >= 48
print(prob)

prob.solve()
print('status:' + LpStatus[prob.status])

## Optimal
for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))

print('The Objective value = ',value(prob.objective))

# We add these lines for sensitivity analysis
print('\n Sensitivity Analysis')

for name, c in prob.constraints.items():
    print('\n', name,':',c,',Slacks = ',c.slack,'Shadow Price =',c.pi)

#reduced cost
for v in prob.variables():
    print('\n',v,name, '=', v.varValue, ', Reduced Cost =', v.dj)
    