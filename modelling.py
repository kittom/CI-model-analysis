import csv
from matplotlib import pyplot as plt
data = []
date, actual, expect, quantile, r_quantile = [],[],[],[],[]


''' CHANGE NUMBER HERE TO CHANGE CSV'''


number = 193

'''

'''
with open(f"data/{number}.csv",newline="") as file:

    reader = csv.reader(file, delimiter = ",", quotechar = "|")
    x = 0

    for row in reader:

        dt = [row[3],row[4],row[6],row[8]]
        data.append(dt)

        if x > 1000:
            break
        x += 1

data = data[2:]



for i in data:
    actual.append(float(i[0]))
    expect.append(float(i[1]))
    quantile.append(float(i[2]))
    print(len(i))

    if i[3] == "":

        r_quantile.append(0)
    else:
        r_quantile.append(float(i[3]))


print(r_quantile)

plt.plot(actual, label = "Actual")
plt.plot(expect, label = "Expected")
plt.plot(quantile, label = "Quantile")
plt.plot(r_quantile, label = "Rolling Quantile")
plt.xlabel("Time (Indexed)")
plt.ylabel("")
plt.title(f"ML Model Analysis ({number})")
plt.legend()
plt.grid(True)

plt.show()