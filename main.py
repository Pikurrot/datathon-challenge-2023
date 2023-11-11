import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('dataset.csv')

print(df.describe)
print(df.head)