import requests
import urllib
from bs4 import BeautifulSoup

keyword=input("Enter keyword: ")
url = input ("Enter url: ")
key_break_down = keyword.split(' ')
q=''
for key in key_break_down:
	q=q+'+'+key

page = 10

for j in range(30):
	request_params = {
		'start' : page*j,
		'q' : q,
	}

	print(urllib.parse.urlencode(request_params))
	response = requests.get(
	                    'https://www.google.com.np/search',
	                    params=urllib.parse.urlencode(request_params),
	                    verify=False,
	                    timeout=30,
	                    headers=None
	                )

	soup = BeautifulSoup(response.text, 'html.parser')
	list1=soup.find_all('cite')
	list2 = [str(x).replace('</b>','') for x in list1]
	list3 = [str(x).replace('<b>','') for x in list2]
	list4 = [str(x).replace('<cite>','') for x in list3]
	list5 = [str(x).replace('</cite>','') for x in list4] 
	list6 = []
	for urla in list5:
		for i,letter in enumerate(urla):
			try:
				urla[i+1]
			except Exception as e:
				list6.append(urla[:i])
				break
			if letter=='/' and not urla[i+1]=='/' and not urla[i-1]=='/':
				list6.append(urla[:i])
				break
	result=0
	flag=0
	for i,val in enumerate(list6):
		print("val=",val)
		if val in url:
			result = i+1
			flag=1
			print("RANK = ",10*j+result)
			break
	if flag:
		break







