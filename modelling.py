import csv
from matplotlib import pyplot as plt


data = []
date, actual, expect, quantile, r_quantile = [], [], [], [], []


''' CHANGE NUMBER HERE TO CHANGE CSV'''


number = 184

'''

'''
with open(f"data/{number}.csv", newline="") as file:

    reader = csv.reader(file, delimiter=",", quotechar="|")
    x = 0

    for row in reader:

        dt = [row[3], row[4], row[6], row[8]]
        data.append(dt)

        # if x > 1000:
        #     break
        # x += 1

data = data[2:]


# add data to lists of according columns
for i in data:
    actual.append(float(i[0]))
    expect.append(float(i[1]))
    quantile.append(float(i[2]))

    if i[3] == "":

        r_quantile.append(0)
    else:
        r_quantile.append(float(i[3]))

# determines the beginning of rolling quantile (in case of change to calculation of rolling quantile time

days = 0
y = 0
total_days = []
for x in r_quantile:
    total_days.append(y)
    if x == 0:
        days += 1
    y += 1


# plot graph

plt.plot(actual, label="Actual")
plt.plot(expect, label="Expected")

# plot quantiles
plt.plot(quantile, label="Quantile")
plt.plot(total_days[days:], r_quantile[days:], label="Rolling Quantile")

# boundries for quantiles
plt.hlines(0.0005, 0, len(total_days), colors="#DA3E1C", linestyles="--", alpha=0.7, label="Quantile Threshold")
plt.hlines(0.9995, 0, len(total_days), colors="#DA3E1C", linestyles="--", alpha=0.7)

# Boundries for rolling quantiles
plt.hlines(0.7, 0, len(total_days), colors="#000000", linestyles="--", alpha=0.7, label="Rolling Quantile Threshold")
plt.hlines(0.3, 0, len(total_days), colors="#000000", linestyles="--", alpha=0.7)

# format graph
plt.xlabel("Time (Indexed)")
plt.ylabel("")
plt.title(f"ML Model Analysis ({number})")
plt.legend()
plt.grid(True)

plt.show()
