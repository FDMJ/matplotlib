import matplotlib.pyplot as plt

revenue_2022 = [6436,2355,5533,6334,5332,5466,7576,4356,3256,2356,2545,5255]
revenue_2023 = [3542,5243,5121,7321,9511,5541,8851,3574,4215,5678,8422,7512]

month = [1,2,3,4,5,6,7,8,9,10,11,12]

plt.style.use('seaborn-v0_8')

fig,ax = plt.subplots()

plt.xticks(month)
ax.plot(month, revenue_2022, label = "2022")
ax.plot(month, revenue_2023, label = "2023")

plt.legend()
ax.set_title("Revenue by month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue in €")

plt.show()