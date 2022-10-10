from lib2to3.pgen2.pgen import DFAState
from envtest import pd_loc
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)))
print(pd_loc(df,0,0))