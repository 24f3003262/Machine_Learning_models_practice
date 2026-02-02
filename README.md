# Machine_Learning_models_practice
Manually implementing the basic machine learning algos to understand how they work


# Supervised Learning Models

## Linear Regression

Linear regression is a foundational statistical method used to model the relationship between a dependent variable (usually denoted as $Y$) and one or more independent variables (denoted as $X$).The goal is to find the best-fitting straight line—known as the regression line—that describes how $Y$ changes as $X$ changes.

### Core equation

In its simplest form (Simple Linear Regression), the relationship is represented by the equation of a line:

                        Y=b0X+b1X+e

- Y: The target variable you want to predict (e.g., house price).
- X: The input variable used for prediction (e.g., square footage).
- b0(Intercept): The value of Y when X is zero.
- b1(Slope): The change in Y for every one-unit increase in X.
- e(Error Term): The "noise" or the difference between the actual data points and the predicted line.

### How the "best fit" is found

To determine the most accurate line, we use a method called Ordinary Least Squares (OLS).

The algorithm calculates the distance between each actual data point and the line (these distances are called residuals). It then squares these distances and sums them up. The "best" line is the one that results in the minimum possible sum of squared errors