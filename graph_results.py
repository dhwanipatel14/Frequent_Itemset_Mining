from cProfile import label
import matplotlib.pyplot as plt

from apriori import Apriori
Dataset =  [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
threshold = [1,5,10]

PcyTime1 =  [32.0, 182.0, 331.0, 619.02, 1057.98, 1244.95, 1487.04, 1745.96, 1988.99, 2369.01, 2785.31, 3078.2]
MultihashTime1 = [77.0, 529.99, 991.0, 2031.05, 3110.96, 4128.0, 4923.03, 5890.0, 6914.62, 7949.18, 9233.0, 10242.01]
MultistageTime1 = [111.97, 777.04, 1533.01, 2674.96, 4500.03, 5773.0, 7280.01, 8072.0, 9162.99, 10599.0, 12313.9, 15909.64]
AprioriTime1 = [139.04, 805.0, 1692.0, 3279.0, 5195.0, 6754.34, 8130.04, 9628.58, 11066.0, 12737.02, 14645.52, 16330.09]

plt.plot(Dataset, AprioriTime1, color="red", label="Apriori" ,marker="o")
plt.plot(Dataset, PcyTime1, color="green", label="Pcy", marker="o")
plt.plot(Dataset, MultistageTime1, color="magenta",label="Multistage", marker="o")
plt.plot(Dataset, MultihashTime1, color="blue",label="Multihash", marker="o")

plt.xlabel('Dataset Size', fontsize=12)
plt.ylabel('Run Time(ms)', fontsize=12)
plt.text(30,15000,"support threshold : 1%",fontsize=12, fontweight = "bold")
plt.grid(True)
plt.legend()
plt.show()

AprioriTime5 =  [13.0, 58.04, 111.01, 235.0, 370.0, 514.0, 582.08, 722.05, 969.05, 1057.97, 1187.25, 1320.0]
PcyTime5 = [70.0, 420.0, 772.01, 1425.96, 2229.12, 2923.0, 3819.0, 4709.99, 5527.7, 6587.96, 7008.96, 7750.97]
MultistageTime5 = [63.0, 396.04, 931.97, 2039.02, 2892.0, 4231.05, 5177.0, 5825.04, 6533.02, 7462.97, 8496.05, 9560.97]
MultihashTime5 = [93.96, 627.44, 1332.99, 2581.1, 4181.04, 5607.21, 7263.0, 8813.03, 9995.03, 11590.92, 13306.79, 15044.12]

plt.plot(Dataset, AprioriTime5, color="red", label="Apriori" ,marker="o")
plt.plot(Dataset, PcyTime5, color="green", label="Pcy", marker="o")
plt.plot(Dataset, MultistageTime5, color="magenta",label="Multistage", marker="o")
plt.plot(Dataset, MultihashTime5, color="blue",label="Multihash", marker="o")

plt.xlabel('Dataset Size', fontsize=14)
plt.ylabel('Run Time(ms)', fontsize=14)
plt.text(30,15000,"support threshold : 5%",fontsize=12, fontweight = "bold")
plt.grid(True)
plt.legend()
plt.show()


AprioriTime10 =  [11.0, 56.01, 109.01, 246.99, 350.97, 577.08, 579.96, 756.01, 820.0, 933.0, 1047.00, 1360.91]
PcyTime10 = [54.99, 353.0, 771.96, 1488.96, 2518.01, 2950.97, 3698.01, 4372.96, 5166.96, 6301.0, 6597.47, 7812.95]
MultistageTime10 = [83.99, 392.0, 907.0, 1852.97, 2659.04, 3283.01, 4211.04, 5492.96, 6076.0, 7047.99, 7670.99, 9074.96]
MultihashTime10 = [100.0, 678.0, 1523.52, 2865.63, 4599.99, 6152.0, 7546.01, 9071.72, 10266.03, 12592.03, 14303.03, 15548.01]

plt.plot(Dataset, AprioriTime10, color="red", label="Apriori" ,marker="o")
plt.plot(Dataset, PcyTime10, color="green", label="Pcy", marker="o")
plt.plot(Dataset, MultistageTime10, color="magenta",label="Multistage", marker="o")
plt.plot(Dataset, MultihashTime10, color="blue",label="Multihash", marker="o")

plt.xlabel('Dataset Size', fontsize=14)
plt.ylabel('Run Time(ms)', fontsize=14)
plt.text(30,15000,"support threshold : 10%",fontsize=12, fontweight = "bold")
plt.legend()
plt.grid(True)
plt.show()