import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ntpath

path = r'./data'                     
all_files = glob.glob(os.path.join(path, "*.csv"))
dfs = {}
dfs = [pd.read_csv(filename) for filename in all_files]
ov=0
tot = 0
sup = 0
es = 0
tot2 = 0
sup2 = 0
es2 = 0
for dframes in dfs:
		data=dframes[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull())]
		dataSup=data[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[pd.to_numeric(data['GRAD_DEBT_MDN'], errors='coerce')<15000]
		dataEarn = dataSup[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[(dataSup['MD_EARN_WNE_P6'].astype(str) != 'PrivacySuppressed') & (~dataSup['MD_EARN_WNE_P6'].isnull())]
		earnSup = dataEarn[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[pd.to_numeric(dataEarn['MD_EARN_WNE_P6'], errors='coerce')>30000]
		es = es + len(earnSup)
		ov = ov + len(dframes)
		tot = tot+len(data) 
		sup = sup+len(dataSup)
		data3=dframes[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[(dframes['GRAD_DEBT_MDN'].astype(str) != 'PrivacySuppressed') & (~dframes['GRAD_DEBT_MDN'].isnull()) & (dframes['C150_4'].astype(str) != 'PrivacySuppressed') & (~dframes['C150_4'].isnull())]
		data2=dframes[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[(dframes['C150_4'].astype(str) != 'PrivacySuppressed') & (~dframes['C150_4'].isnull())]
		data2Sup=data2[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[pd.to_numeric(data2['C150_4'], errors='coerce')<.5]
		dataEarner = data2Sup[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[(data2Sup['MD_EARN_WNE_P6'].astype(str) != 'PrivacySuppressed') & (~data2Sup['MD_EARN_WNE_P6'].isnull())]
		earnSup2 = dataEarner[['GRAD_DEBT_MDN','C150_4','AVGFACSAL','MD_EARN_WNE_P6']].loc[pd.to_numeric(dataEarner['MD_EARN_WNE_P6'], errors='coerce')>30000]
		tot2 = tot2 + len(data2)
		sup2 = sup2 + len(data2Sup)
		es2 = es2 + len(earnSup2)
		print("CORR:",np.corrcoef(pd.to_numeric(data3["GRAD_DEBT_MDN"].tolist(),errors='coerce'),pd.to_numeric((data3["C150_4"].tolist()),errors='coerce')))
print(tot/ov)
print("Debt Sup",sup/tot)
print("Debt=>earn above 30k", es/sup)
print(tot2/ov)
print("Comp Sup",sup2/tot2)
print("Comp => earn above 30k", es2/sup2)