###### Calc

Calculation Steps:

Calculate the Mean of the Dependent Variable (Y):
Find the average of all the Y values.

Calculate the Predicted Values (Y-hat):
Use the regression equation to predict the Y value for each X value.

Calculate SSR:
For each data point:

Calculate the difference between the actual Y value and the predicted Y value.
Square this difference.
Sum up these squared differences for all data points.
Calculate SST:
For each data point:

Calculate the difference between the actual Y value and the mean of Y.
Square this difference.
Sum up these squared differences for all data points.
Formula:

SSR = Σ(Y - Y-hat)²
SST = Σ(Y - Y-mean)²

y = 1.178 * x + 2.467

|X	| Y|
|---|--|
|1	|4 |
|-2	|3 |
|3	|6 |
|4.5 |	8|
|0	|2 |
|-4	|-3 |
|-1	|-2 |
|4	| 7 |
|-1	 |2.5|

Mean of Y: (4+3+6+8+2-3-2+7+2.5)/9 = 3.2778
Predicted Y values(Y-hat): 3.645, 1.089, 6.011, 7.691, 2.467, -2.263, 1.29, 7.101, 1.29

Calculating SSR:

|X	|Y	|Y-hat	|(Y-Y-hat)^2|
|---|---|-------|-----------|
|1	|4	|3.645	|0.127|
|-2	|3	|1.089	|3.644|
|3	|6	|6.011	|0.002|
|4.5	|8	|7.691	|0.096|
|0	|2	|2.467	|0.218|
|-4	|-3	|-2.263	|0.544|
|-1	|-2	|1.29	|10.444|
|4	|7	|7.101	|0.008|
|-1	|2.5	|1.29	|1.464|

SSR = Σ(Y - Y-hat)² = 17.586


Calculating SST:

|X	|Y	|(Y-Y-mean)^2|
|---|---|------------|
|1	|4	|0.533|
|-2	|3	|0.084|
|3	|6	|7.533|
|4.5	|8	|22.323|
|0	|2	|1.833|
|-4	|-3	|38.833|
|-1	|-2	|28.323|
|4	|7	|13.723|
|-1	|2.5	|0.603|

SST = Σ(Y - Y-mean)² = 115.708

R² = 1 - (SSR / SST) = 1- (17.586/115.708) = 0.848013966190756
