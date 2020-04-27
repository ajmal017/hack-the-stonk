import pandas as pd
import os
import quandl
import time

auth_tok = "Nv1rJgRR7u88iz_dg7Y6"

data = quandl.get("LBMA/GOLD", trim_start = "2000-12-12", trim_end = "2020-04-20", authtoken=auth_tok)

print(data)