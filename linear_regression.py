import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('linear_regression_data.csv')

# plt.scatter(data.hours_worked,data.total_earnings)
# plt.show()

# def loss_function(m,b,data_points):
#     total_error=0
#     for i in range(len(data_points)):
#         x=data_points.iloc[i].hours_worked
#         y=data_points.iloc[i].total_earnings
#         total_error+=(y-(m*x+b))**2
    
#     return total_error/float(len(data_points))

def gradient_descent(m_now,b_now,L,data_points): #L is learning rate
    m_gradient=0
    b_gradient=0

    n=len(data_points)

    for i in range(n):
        x=data_points.iloc[i].hours_worked
        y=data_points.iloc[i].total_earnings
        
        m_gradient+=-(2/n)*x*(y-(m_now*x + b_now))
        b_gradient+=-(2/n)*(y-(m_now*x+b_now))

    m=m_now-m_gradient*L
    b=b_now-b_gradient*L

    return m,b


m=0
b=0
L=0.0001
epochs=1000 #iterations

for i in range(epochs):
    if i%100==0:
        print(f"Epoch: {i}")
    m,b=gradient_descent(m,b,L,data)


print(m,b)

plt.scatter(data.hours_worked,data.total_earnings,color="black")
plt.plot(list(range(0,100)),[m*x+b for x in range(0,100)],color="red")
plt.show()