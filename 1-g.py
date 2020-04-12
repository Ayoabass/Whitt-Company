#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:42:36 2020

@author: AyodejiAbass
"""



from pulp import *
#define the model
prob = LpProblem("Whitt Window Company.", LpMaximize)
x1 = LpVariable('x_1', lowBound = 0)
x2 = LpVariable('x_2', lowBound = 0)

prob += 300*x1 + 180*x2, "Obj"
# Constraints
prob += x1 <= 5, 'Wood-frame'
prob += x2 <= 5, 'Aluminium-frame'
prob += 6*x1 + 8*x2 <= 48, 'Glass'
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
    