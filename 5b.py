


from pulp import *

# Creates the prob variable to contain the problem data
prob = LpProblem('Household Duties',LpMinimize)

x1 = LpVariable('Eve Shopping', cat = 'Binary')
x2 = LpVariable('Eve Cooking', cat = 'Binary')
x3 = LpVariable('Eve Dishwashing', cat = 'Binary')
x4 = LpVariable('Eve Laundry', cat = 'Binary')
y1 = LpVariable('Steven Shopping', cat = 'Binary')
y2 = LpVariable('Steven Cooking', cat = 'Binary')
y3 = LpVariable('Steven Dishwashing', cat = 'Binary')
y4 = LpVariable('Steven Laundry', cat = 'Binary')

#Objective function
prob += 4.5*x1 + 7.5*x2 + 3.5*x3 + 3*x4 + 5*y1 + 7.2*y2 + 4.5*y3 \
    + 3.2*y4, 'obj'

#Constraints
prob += x1 + x2 + x3 + x4 == 2, 'Eve'
prob += y1 + y2 + y3 + y4 == 2, 'Steven'
prob += x1 + y1 == 1, 'Shopping'
prob += x2 + y2 == 1, 'Cooking'
prob += x3 + y3 == 1, 'Dishwashing'
prob += x4 + y4 == 1, 'Laundry'


print(prob)

prob.solve()
print(LpStatus[prob.status])

for variable in prob.variables():
  print("{} = {}".format(variable.name, variable.varValue))

print("Optimial Function Value = {}".format(value(prob.objective)))
