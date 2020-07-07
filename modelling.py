import csv
from matplotlib import pyplot as plt
data = []
date, actual, expect, quantile = [],[],[],[]

with open("data/193.csv",newline="") as file:

    reader = csv.reader(file, delimiter = ",", quotechar = "|")
    x = 0

    for row in reader:

        dt = [row[3],row[4],row[6]]
        data.append(dt)


        x += 1

data = data[2:]



for i in data:
    actual.append(float(i[0]))
    expect.append(float(i[1]))
    quantile.append(float(i[2]))
    # date.append(i[3])


print(actual)

plt.plot(actual)
plt.plot(expect)
# plt.plot(date,quantile)
plt.xlabel("date")
plt.ylabel("actual")
plt.title("ML Model Analysis")
plt.show()