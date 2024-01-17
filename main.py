from bs4 import BeautifulSoup
import json

files=['index.html','index2.html']
res={"capitals":[]}
for file in files:
    f=open(file,'r')
    html=f.read()
    parser = BeautifulSoup(html,'html.parser')
    root=parser.ul
    lst1=root.find_all(class_="capital")
    lst2=root.find_all(class_="state")
    
    for i in range(len(lst1)):
        x={}
        x["capital"]=lst1[i].text.strip()
        x["state"]=lst2[i].text.strip()
        res["capitals"].append(x)
    f.close()
res["summary"]={"numberOfCapitals":len(res["capitals"])}
print(res)
fout=open("result.json",'w')
fout.write(json.dumps(res))
fout.close()

