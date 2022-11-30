# --- Load GPyOpt
from GPyOpt.methods import BayesianOptimization
import numpy as np

# --- Define your problem
def f(x): return np.sum(x) # TODO

domain = [{'name': 'time of stimulation', 'type': 'discrete', 'domain': (2,3,4,5,6,7,8)},
            {'name': 'frequency', 'type': 'continuous', 'domain': (0.5, 10)},
            {'name': 'voltage', 'type': 'continuous', 'domain': (0, 18)}]

data = np.loadtxt('./conditions.txt', delimiter= ",", skiprows=1)
conditions = data[:, 0:3]

# --- Solve your problem
myBopt = BayesianOptimization(f=f, domain=domain, X=conditions)
myBopt.run_optimization(max_iter=15)

print(f'{myBopt.X}')