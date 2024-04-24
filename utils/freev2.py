import requests,random,string
import urllib3
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
from cfscrape import CloudflareScraper

scraper = CloudflareScraper()

sites=[
    {
        "name":"bingo",
        "url":"https://cn.bingovpn.cyou/",
        "reg_url":"https://cn.bingovpn.cyou/api/v1/passport/auth/register",
        "sub":"https://v.haoyun.nl/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"bingovip",
        "url":"https://user.bingo100.vip/",
        "reg_url":"https://x612.bingo100.vip/binapi/passport/auth/register",
        "sub":"http://dog.haoyun.nl:8080/hi/binapi/client/subscribe?token={token}"
    },
    {
        "name":"giaoyun",
        "url":"https://ww1.giaoyun.xyz/",
        "reg_url":"https://ww1.giaoyun.xyz/api/v1/passport/auth/register",
        "sub":"https://ww1.giaoyun.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"ckcloud",
        "url":"https://www.ckcloud.xyz/",
        "reg_url":"https://www.ckcloud.xyz/api/v1/passport/auth/register",
        "sub":"https://www.ckcloud.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"tizioo",
        "url":"https://tizioo12.top/",
        "reg_url":"https://tizioo12.top/api/v1/passport/auth/register",
        "sub":"https://tizioo12.top/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"coo",
        "url":"https://web.coo.wiki/",
        "reg_url":"https://web.coo.wiki/api/v1/passport/auth/register",
        "sub":"https://web.coo.wiki/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"scloud",
        "url":"https://fzdwz.top/",
        "reg_url":"http://fzdwz.top/api/v1/passport/auth/register",
        "sub":"http://fzdwz.top/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"daxun",
        "url":"https://daxun.club/",
        "reg_url":"http://daxun.club/api/v1/passport/auth/register",
        "sub":"http://daxun.buzz/api/v1/client/subscribe?token={token}"
    }
    
]

class tempsite():
    def __init__(self,site):
        self.reg_url=site["reg_url"]
        self.ref=site["url"]
        self.name=site["name"]
        self.sub=site["sub"]

    def register(self,email,password,proxy=None):
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": self.ref
        }
        data={
            "email":email,
            "password":password,
            "invite_code":None,
            "email_code":None
        }
        req=scraper.post(self.reg_url,headers=headers,data=data,timeout=10,proxies=proxy)
        return req
        
    def getSubscribe(self):
        password=''.join(random.sample(string.ascii_letters + string.digits + string.ascii_lowercase, 10))
        email=password+"@gmail.com"
        req=self.register(email,password)
        token=req.json()["data"]["token"]
        subscribe=self.sub.format(token=token)
        return subscribe

    def saveconf(self):
        url=self.getSubscribe()
        for k in range(3):
            try:
                req=scraper.get(url,timeout=5)
                v2conf=req.text
                break
            except:
                v2conf=""
        with open("./freev2/"+self.name,"w") as f:
                    f.write(v2conf)

def getconf():
    for v2site in sites:
        obj=tempsite(v2site)
        try:
            obj.saveconf()
        except:
            pass  
    
