
from pulp import *
#define the model
prob = LpProblem("Investment.", LpMaximize)
A = LpVariable('A', lowBound = 0)
B = LpVariable('B', lowBound = 0)
C = LpVariable('C', lowBound = 0)
D = LpVariable('D', lowBound = 0)
E = LpVariable('E', lowBound = 0)

prob += 0.095*A + 0.08*B + 0.09*C + 0.09*D + 0.09*E, "Obj"
# Constraints
prob += A + B + C + D + E == 500000, 'Investing'
prob += B + E >= 0.5 * 500000 , 'Short Term'
prob += A + D + E <= 0.5 * 500000, 'High Risk'
prob += A + B + D >=  0.3 * 500000, 'Tax-Free'
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
    
for v in prob.variables():
    print('\n',v,name, '=', v.varValue, ', Reduced Cost =', v.dj)

