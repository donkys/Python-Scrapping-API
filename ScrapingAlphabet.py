import bs4
from lxml import html
import requests
from rwjson import *

#data
data = []
#ID
id = 0
#query
query=[ 'ก','ข','ค','ฆ','ง','จ','ฉ','ช','ซ','ญ','ด','ต','ถ','ท','ธ','น',
        'บ','ป','ผ','ฝ','พ','ภ','ม','ย','ร','ล','ว','ศ','ส','ห','อ','ฮ']

#loop all query
for i in range(len(query)):
    data = []
    url ='https://www.myhora.com/ดูดวง-ทำนายฝัน.aspx?dream='+str(query[i])
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #request URL
    response = requests.get(url=url, headers=headers)
    tree = html.fromstring(html=response.text)

    #put data in soup
    soup = bs4.BeautifulSoup(response.text)

    #get length
    length = len(soup.find_all('div',{'class':'dn'})) * 5
    if(length > 47):
        for j in range(2,47,5) :
            id+=1
            print(f'{id} is {query[i]} number {j}')
            #get name
            nameindex = '//*[@id="p_display_result"]/div/div['+str(j)+']/a'
            name = tree.xpath(nameindex)[0].text

            #get number
            numberindex = '//*[@id="p_display_result"]/div/div['+str(j+2)+']/font/font[3]'
            try:
                number = tree.xpath(numberindex)[0].text
            except:
                number = ''
                
            #append data
            try :
                data.append({'id':id, 'name': name, 'number': list(map(int, number.split(',')))})
            except:
                data.append({'id':id, 'name': name, 'number': []})
    else:
        for j in range(2,length,5) :
            id+=1
            print(f'{id} is {query[i]} number {j}')            #get name
            nameindex = '//*[@id="p_display_result"]/div/div['+str(j)+']/a'
            name = tree.xpath(nameindex)[0].text

            #get number
            numberindex = '//*[@id="p_display_result"]/div/div['+str(j+2)+']/font/font[3]'
            try:
                number = tree.xpath(numberindex)[0].text
            except:
                number = ''
                
            #append data
            try :
                data.append({'id':id, 'name': name, 'number': list(map(int, number.split(',')))})
            except:
                data.append({'id':id, 'name': name, 'number': []})


    for j in range(49,length,5) :
        id+=1
        print(f'{id} is {query[i]} number {j}')
        #get name
        nameindex = '//*[@id="p_display_result"]/div/div['+str(j)+']/a'
        name = tree.xpath(nameindex)[0].text

        #get number
        numberindex = '//*[@id="p_display_result"]/div/div['+str(j+2)+']/font/font[3]'
        try:
            number = tree.xpath(numberindex)[0].text
        except:
            number = ''
            
        #append data
        try :
            data.append({'id':id, 'name': name, 'number': list(map(int, number.split(',')))})
        except:
            data.append({'id':id, 'name': name, 'number': []})

    writeJson(str(query[i]),data)


print(data)
