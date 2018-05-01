import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ntpath

path = r'./data'                 
all_files = glob.glob(os.path.join(path, "*.csv"))
names = {}
dfs={}

for i in range(len(all_files)):
	dfs[i] = pd.read_csv(all_files[i])
	dfs[i].name,ext = os.path.splitext(ntpath.basename(all_files[i]))
	names[i] = int(dfs[i].name)
	# print(dfs[i].name)
years=sorted(names.values())
plt.figure(1)
for i in range(len(years)):
	for j in range(len(dfs)):
		if str(years[i]) == dfs[j].name:
			plt.subplot(711)
			mean=pd.to_numeric(dfs[j]['DEBT_MDN'].loc[(dfs[j]['DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['DEBT_MDN'].isnull()) & (dfs[j]["INSTNM"] == "University of Colorado Boulder")], errors='coerce')
			plt.title('Mean Debt')
			plt.xlabel('years')
			plt.ylabel('Debt')
			print(mean)
			plt.scatter(years[i], mean.mean())
			plt.subplot(713)
			comp = pd.to_numeric(dfs[j]['C150_4'].loc[(dfs[j]['C150_4'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['C150_4'].isnull()) & (dfs[j]["INSTNM"] == "University of Colorado Boulder")], errors='coerce')
			plt.title('Mean Completion')
			plt.xlabel('years')
			plt.ylabel('Completion')
			print(comp)
			plt.scatter(years[i], comp.mean())
			plt.subplot(715)
			sals = pd.to_numeric(dfs[j]['AVGFACSAL'].loc[(dfs[j]['AVGFACSAL'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['AVGFACSAL'].isnull()) & (dfs[j]["INSTNM"] == "University of Colorado Boulder")], errors='coerce')
			plt.title('Mean Salary')
			plt.xlabel('years')
			plt.ylabel('Salary')
			print(sals)
			plt.scatter(years[i], sals.mean())
			plt.subplot(717)
			earns = pd.to_numeric(dfs[j]['MD_EARN_WNE_P6'].loc[(dfs[j]['MD_EARN_WNE_P6'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['MD_EARN_WNE_P6'].isnull()) & (dfs[j]["INSTNM"] == "University of Colorado Boulder")], errors='coerce')
			plt.title('Mean Earnings')
			plt.xlabel('years')
			plt.ylabel('Earnings')
			print(earns)
			plt.scatter(years[i], earns.mean())
plt.show()