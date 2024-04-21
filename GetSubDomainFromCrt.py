#programing by bebars
import urllib.request 
import re
def GetSubdominfromcrt(website):
    
    request_url = urllib.request.urlopen(f'https://crt.sh/?q={website}') 

    html = request_url.read().decode("utf-8")
    if(re.search("<I>None found</I>",html)!=None):
        print("this website Not found")
        exit()


    ilterwebsite=re.findall(r"<TD>(\S*."+website+r")</TD>",html)
    
    return set(ilterwebsite)
    
def FixFormat(website):
    l=[]
    for item in GetSubdominfromcrt(website):
        
        if(item.find("<BR>")!=-1):
            for i in item.split("<BR>"):
                l.append(i)
        else:
            l.append(item)
    return l

def SavaDatainFile(website):
    with open("SubDomain"+website+".txt","w") as file:
        for line in FixFormat(website):
            file.write(line+"\n")

NameWebsite=str(input("Enter domain :  "))
SavaDatainFile(NameWebsite)
            
    

    
    

