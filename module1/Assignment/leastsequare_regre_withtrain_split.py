from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

excel_file = Path("./DeepLearning_MasteringNeuralNetworks.xlsx")
df = pd.read_excel(excel_file)

x = df['X'].values.reshape(-1, 1)
y = df['Y'].values.reshape(-1, 1)
print(f"{x.shape=}, {y.shape=}")

print(x)
print(y)
# TODO: OLS
regression = LinearRegression().fit(x, y)

R2= regression.score(x, y)
print(f"R2 = {R2}")
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"r2 = {r2}")

x_range = np.arange(-5, 5, 0.01).reshape(-1, 1)
plt.figure("my figure", figsize=(20,10))
plt.title("Ordinary Least Squares Regression")
plt.plot(df['X'], df['Y'], '.k', markersize=20, label='raw data')
plt.plot(x_range, regression.predict(x_range), 'b-', linewidth=3,
label=f'Ordinary Least Squares Regression\ny = {regression.coef_[0,0]:.3f}x + {regression.intercept_[0]:.3f},\nR^2: {R2:.3f}')
plt.legend()
plt.show()