

from pulp import *

# Creates the prob variable to contain the problem data
prob = LpProblem('Toys-R-4-U',LpMaximize)

x1 = LpVariable('x1', lowBound = 0)
x2 = LpVariable('x2', lowBound = 0)
y1 = LpVariable('y1', lowBound = 0, cat = 'Integer')
y2 = LpVariable('y2', lowBound = 0, cat = 'Integer')
y3 = LpVariable('y3', lowBound = 0, cat = 'Integer')

#Objective function
prob += 10*x1 + 15*x2 - 50000*y1 - 75000*y2, 'obj'

bigM = 1000000

#Constraints
prob += 0.02*x1 + 0.25*x2 <= 500 + bigM*y3
prob += 0.025*x1 + 0.04*x2 <= 700 + bigM*(1-y3)
prob += x1 <= bigM*y1
prob += x2 <= bigM*y2
prob += y1 + y2 <= 2



print(prob)

#Solving the model
prob.solve()
print(LpStatus[prob.status])

for variable in prob.variables():
  print("{} = {}".format(variable.name, variable.varValue))

print("Optimial Function Value = {}".format(value(prob.objective)))
