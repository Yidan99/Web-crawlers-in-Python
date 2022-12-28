import requests
import json
import openpyxl

w=openpyxl.Workbook()
sheet=w.create_sheet()

resp= requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=6234767&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
res=resp.text
rest=res.replace('fetchJSON_comment98(','').replace(');','')
#print(rest)
j=json.loads(rest)
comments=j['comments']
for item in comments:
  col=item['productColor']
  size=item['productSize']
  #print (size)
  #print (col)
  sheet.append([col,size])
  w.save('data/yd_15952860753.xlsx')