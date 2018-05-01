import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ntpath

path = r'./data'                 
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
dfs = {}
names = {}

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
			mean=pd.to_numeric(dfs[j]['DEBT_MDN'].loc[(dfs[j]['DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['DEBT_MDN'].isnull())], errors='coerce')
			plt.title('Mean Debt')
			plt.xlabel('years')
			plt.ylabel('Debt')
			plt.scatter(years[i], mean.mean())
			plt.subplot(713)
			comp = pd.to_numeric(dfs[j]['C150_4'].loc[(dfs[j]['C150_4'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['C150_4'].isnull())], errors='coerce')
			plt.title('Mean Completion')
			plt.xlabel('years')
			plt.ylabel('Completion')
			plt.scatter(years[i], comp.mean())
			plt.subplot(715)
			sals = pd.to_numeric(dfs[j]['AVGFACSAL'].loc[(dfs[j]['AVGFACSAL'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['AVGFACSAL'].isnull())], errors='coerce')
			plt.title('Mean Salary')
			plt.xlabel('years')
			plt.ylabel('Salary')
			plt.scatter(years[i], sals.mean())
			plt.subplot(717)
			earns = pd.to_numeric(dfs[j]['MD_EARN_WNE_P6'].loc[(dfs[j]['MD_EARN_WNE_P6'].astype(str) != 'PrivacySuppressed') & (~dfs[j]['MD_EARN_WNE_P6'].isnull())], errors='coerce')
			plt.title('Mean Earnings')
			plt.xlabel('years')
			plt.ylabel('Earnings')
			plt.scatter(years[i], earns.mean())
plt.show()
dfs = [pd.read_csv(filename) for filename in all_files]
plt.figure(2)
for dframes in dfs:
	data=dframes[['GRAD_DEBT_MDN','MN_EARN_WNE_INC1_P6']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (dframes['MN_EARN_WNE_INC1_P6'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull()) & (~dframes['MN_EARN_WNE_INC1_P6'].isnull())]
	plt.subplot(511)
	plt.scatter(data['GRAD_DEBT_MDN'],data['MN_EARN_WNE_INC1_P6'])
	plt.title("Low Earnings VS Debt (<30k)")
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_ticklabels([])
	cur_axes.axes.get_yaxis().set_ticklabels([])
	try:
		plt.xlabel((np.nanmin(pd.to_numeric(data['GRAD_DEBT_MDN'])),"-",np.nanmax(pd.to_numeric(data['GRAD_DEBT_MDN']))))
	except ValueError:
		pass
	plt.ylabel('Earnings')
	print(data.corr())	
# null_columns=dframes.columns[dframes.isnull().any()]
# 	# print(dframes[null_columns].isnull().sum())

for dframes in dfs:
	data=dframes[['GRAD_DEBT_MDN','MN_EARN_WNE_INC2_P6']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (dframes['MN_EARN_WNE_INC2_P6'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull()) & (~dframes['MN_EARN_WNE_INC2_P6'].isnull())]
	plt.subplot(513)
	plt.scatter(data['GRAD_DEBT_MDN'],data['MN_EARN_WNE_INC2_P6'])
	plt.title("Medium Earnings VS Debt(30k<earn<75k)")
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_ticklabels([])
	cur_axes.axes.get_yaxis().set_ticklabels([])
	try:
		plt.xlabel((np.nanmin(pd.to_numeric(data['GRAD_DEBT_MDN'])),"-",np.nanmax(pd.to_numeric(data['GRAD_DEBT_MDN']))))
	except ValueError:
		pass
	plt.ylabel('Earnings')
	# null_columns=dframes.columns[dframes.isnull().any()]
# 	# print(dframes[null_columns].isnull().sum())

for dframes in dfs:
	data=dframes[['GRAD_DEBT_MDN','MN_EARN_WNE_INC3_P6']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (dframes['MN_EARN_WNE_INC3_P6'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull()) & (~dframes['MN_EARN_WNE_INC3_P6'].isnull())]
	plt.subplot(515)
	plt.scatter(data['GRAD_DEBT_MDN'],data['MN_EARN_WNE_INC3_P6'])
	plt.title("High Earnings VS Debt(>75k)")
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_ticklabels([])
	cur_axes.axes.get_yaxis().set_ticklabels([])
	try:
		plt.xlabel((np.nanmin(pd.to_numeric(data['GRAD_DEBT_MDN'])),"-",np.nanmax(pd.to_numeric(data['GRAD_DEBT_MDN']))))
	except ValueError:
		pass
	plt.ylabel('Earnings')
	# null_columns=dframes.columns[dframes.isnull().any()]
	# print(dframes[null_columns].isnull().sum())
plt.show()

plt.figure(3)
for dframes in dfs:
	data=dframes[['AVGFACSAL','C150_4']].loc[(dframes['C150_4'].astype(str) != 'PrivacySuppressed') & (dframes['AVGFACSAL'].astype(str) != 'PrivacySuppressed') & (~dframes['C150_4'].isnull()) & (~dframes['AVGFACSAL'].isnull())]
	plt.subplot(511)
	plt.scatter(data['AVGFACSAL'],data['C150_4'])
	plt.title("Salary VS Completion")
	plt.xlabel('Salary')
	plt.ylabel('Completion Rate')
# 	# null_columns=dframes.columns[dframes.isnull().any()]
# 	# print(dframes[null_columns].isnull().sum())

for dframes in dfs:
	data=dframes[['GRAD_DEBT_MDN','ADM_RATE']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (dframes['ADM_RATE'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull()) & (~dframes['ADM_RATE'].isnull())]
	plt.subplot(513)
	plt.scatter(data['GRAD_DEBT_MDN'],data['ADM_RATE'])
	plt.title("Acceptance vs Debt")
	plt.xlabel('Debt')
	plt.ylabel('Acceptance Rate')
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_ticklabels([])

for dframes in dfs:
	data=dframes[['DEBT_MDN','C150_4']].loc[(dframes['C150_4'].astype(str) != 'PrivacySuppressed') & (dframes['DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (~dframes['C150_4'].isnull()) & (~dframes['DEBT_MDN'].isnull())]
	plt.subplot(515)
	plt.scatter(data['DEBT_MDN'],data['C150_4'])
	plt.title("Completion VS Debt")
	plt.ylabel("Completion Rate")
	plt.xlabel("Debt")
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_ticklabels([])
	print(data.corr())
plt.show()

# plt.figure(1):
# for dframes in dfs:
# 	print(dframes)