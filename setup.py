from subprocess import run, call
import subprocess as sp
import os
import sys

sp.call(['pip','install','-r','requirements.txt'])
sp.call(['pip','install','-Iv','pandas==1.0.5'])

import pandas as pd
import scipy as sp
import sklearn
import numpy as np
import matplotlib as plt
import statsmodels as sm
import seaborn as sns