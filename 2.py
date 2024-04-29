import openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_excel(r"C:\Users\karpo\OneDrive\Desktop\WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.xlsx")
population_rus = population[1:152]
population_ind = population[152:303]
population_fra = population[303:454]
fig, ax = plt.subplots(3, figsize=(12, 18))

years_rus = population_rus["Unnamed: 10"].to_numpy()

birth_rus = population_rus["Unnamed: 34"].to_numpy()
by_15_rus = population_rus["Unnamed: 37"].to_numpy()
by_65_rus = population_rus["Unnamed: 40"].to_numpy()
by_80_rus = population_rus["Unnamed: 43"].to_numpy()

ax[0].plot(years_rus, by_80_rus, color='g',  label='80 y.o.')
ax[0].plot(years_rus, by_65_rus,  label='65 y.o.')
ax[0].plot(years_rus, by_15_rus, color='r', label='15 y.o.')
ax[0].plot(years_rus, birth_rus, color='b', label='0 y.o.')

ax[0].set_xlabel("years")
ax[0].set_ylabel("Average Life Expectancy")

ax[0].set_title("Russia", fontweight ="bold")
ax[0].legend()

years_ind = population_ind["Unnamed: 10"].to_numpy()

birth_ind = population_ind["Unnamed: 34"].to_numpy()

by_15_ind = population_ind["Unnamed: 37"].to_numpy()
by_65_ind = population_ind["Unnamed: 40"].to_numpy()
by_80_ind = population_ind["Unnamed: 43"].to_numpy()

ax[1].plot(years_ind, by_80_ind, color='g',  label='80 y.o.')
ax[1].plot(years_ind, by_65_ind, label='65 y.o.')
ax[1].plot(years_ind, by_15_ind, color='r', label='15 y.o.')
ax[1].plot(years_ind, birth_ind, color='b',  label='0 y.o.')

ax[1].set_xlabel("years")
ax[1].set_ylabel("Average Life Expectancy")
ax[1].set_title("India", fontweight ="bold")
ax[1].legend()



years_fra = population_fra["Unnamed: 10"].to_numpy()


birth_fra = population_fra["Unnamed: 34"].to_numpy()
by_15_fra = population_fra["Unnamed: 37"].to_numpy()
by_65_fra = population_fra["Unnamed: 40"].to_numpy()
by_80_fra = population_fra["Unnamed: 43"].to_numpy()

ax[2].plot(years_fra, by_80_fra, color='g', label='80 y.o.')
ax[2].plot(years_fra, by_65_fra, label='65 y.o.')
ax[2].plot(years_fra, by_15_fra, color='r', label='15 y.o.')
ax[2].plot(years_fra, birth_fra, color='b',label='0 y.o.')

ax[2].set_xlabel("years")
ax[2].set_ylabel("Average Life Expectancy")
ax[2].set_title("France", fontweight ="bold")
ax[2].legend(loc=4)
plt.show()