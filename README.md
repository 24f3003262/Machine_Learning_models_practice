# Machine_Learning_models_practice
Manually implementing the basic machine learning algos to understand how they work


# Supervised Learning Models

## Linear Regression

Linear regression is a foundational statistical method used to model the relationship between a dependent variable (usually denoted as $Y$) and one or more independent variables (denoted as $X$).The goal is to find the best-fitting straight line—known as the regression line—that describes how $Y$ changes as $X$ changes.

### Core equation

In its simplest form (Simple Linear Regression), the relationship is represented by the equation of a line:

                        Y=b0+b1X+e

- Y: The target variable you want to predict (e.g., house price).
- X: The input variable used for prediction (e.g., square footage).
- b0(Intercept): The value of Y when X is zero.
- b1(Slope): The change in Y for every one-unit increase in X.
- e(Error Term): The "noise" or the difference between the actual data points and the predicted line.

### How the "best fit" is found

To determine the most accurate line, we use a method called Ordinary Least Squares (OLS).

The algorithm calculates the distance between each actual data point and the line (these distances are called residuals). It then squares these distances and sums them up. The "best" line is the one that results in the minimum possible sum of squared errors. (MEAN SQUARED ERROR)

### Implementation

To find the minimum error, we will take the partial derivatives w.r.t slope and intercept of the error function and find the steepest descent.

Then we use gradient descent on the slope and also on the intercept to find their best solutions.

The learning rate in gradient descent - if too big, not effectively best solution. If too small, too many iterations.

Second approach (Closed-form):- Mathematically
We find the residual sum of squares.....sum of the square of difference of actual y values and the predicted y values
This process can be used for multiple dimensions :- y=m1x1+m2x2+...+mnxn+b 
To convert it into matrix we can consider last term as :- m0=b and x0=1

so one vector will be [1 x1 x2 x3 ...]^T (let's call it X)  and another [b m1 m2 m3 ....]^T (coefficients)(parameters)(let's call it beta)

so it's just XB (B=beta)

on a smallest scale we can say y_i_predicted=x_i*B

RSS(B)=(y-X.B)^T(y-X.B) [for squaring we do A^2=A^TA]

We need to find optimal B for a problem

for that we find partial derivative of RSS w.r.t B which is = -2X^Ty+2X^TXB and make that equal to zero to find the extremum

then X^Ty=X^TXB
multiplying both sides by (X^TX)^-1

we get (X^TX)^-1.X^Ty=B here B is the most efficient B