import pandas as pd
import matplotlib.pyplot as plt

gas=pd.read_csv("gas_prices.csv")

plt.figure(figsize=(9,7))

plt.title("Gas Prices over time (in USD)",size=15)

#plt.plot(gas["Year"],gas["USA"],label="United States")
#plt.plot(gas["Year"],gas["Canada"],label="Canada")
#plt.plot(gas["Year"],gas["South Korea"],label="South Korea")
#plt.plot(gas.Year,gas.Australia,label="Australia")

for country in gas:
    if country != "Year":
        plt.plot(gas.Year,gas[country],label=country,marker=".")



plt.xticks(gas["Year"][::3])
plt.xlabel("Year")


















plt.ylabel("US DOLLARS")
plt.legend()

plt.savefig("gas_price_figure.png",dpi=300)
plt.show()