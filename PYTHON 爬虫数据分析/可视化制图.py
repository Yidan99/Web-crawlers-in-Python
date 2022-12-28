import openpyxl
import matplotlib.pyplot as plt
w=openpyxl.load_workbook('data/yd_15952860753.xlsx')
sheet=w['Sheet1']
col=[]
size=[]
for i in range(1,21):
  col.append(sheet['A'+str(i)].value)
  size.append(sheet['B'+str(i)].value)
col_class=set(col)
count=len(col)
col_percent=[]
for clr in col_class:
  col_percent.append(col.count(clr)/count)

plt.pie(x=col_percent,labels=col_class,autopct='%1.1f%%')
plt.rcParams['font.sans-serif']=['SimHei']
plt.legend()
plt.savefig('data/yd_15952860753.png')