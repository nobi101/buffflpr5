import requests, os, sys, threading
from time import sleep
from time import strftime
from datetime import datetime
from pystyle import Write,Colors
os.system('title TOOL BUFF FOLLOW PRO5')
try:
    import requests
except:
    Write.Print ("Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải \n",Colors.blue_to_red,interval=0.0001)
    os.system('pip install requests && pip install bs4 && pip install pystyle')

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
clr()
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)

def idelay(o):
    while(o>0):
        o=o-1
        Write.Print(f"[FRIVE][.....""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][X....""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XX...""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXX..""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXXX.""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXXXX""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)

list_id_name_page = []
cookie = Write.Input('Nhập Cookie: ',Colors.blue_to_red,interval=0.0001)
headers_check_live = {
    'authority': 'mbasic.facebook.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://mbasic.facebook.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookie
}
try:
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers_check_live).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    Write.Print('KHÔNG GET ĐƯỢC THÔNG TIN - KIỂM TRA COOKIE\n',Colors.blue_to_red,interval=0.0001)
    exit()

headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
clr()
Write.Print(f'Đã Tìm Thấy '+str(len(list_id_name_page))+' Page\n',Colors.blue_to_red,interval=0.0001)
uid_profile = int(Write.Input(f'NHẬP UID CẦN TĂNG FOLLOW: ',Colors.blue_to_red,interval=0.0001))
link_profile = f'https://www.facebook.com/profile.php?id={uid_profile}'
soluong = int(Write.Input(f'NHẬP SỐ LƯỢNG FOLLOW CẦN TĂNG: ',Colors.blue_to_red,interval=0.0001))
delay_follow = int(Write.Input(f'NHẬP DELAY TĂNG FOLLOW: ',Colors.blue_to_red,interval=0.0001))
dem = 0
def SentFollow(x, cookie, link_profile):
    uid_page = list_id_name_page[x].split('|')[0] 
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers_ = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-length': '1496',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie9,
        'origin': 'https://www.facebook.com',
        'referer': link_profile,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'viewport-width': '1078',
        'x-fb-friendly-name': 'CometUserFollowMutation',
        'x-fb-lsd': 'ut-hiPpuPkfxGazKnTVgag',
    }

    data_ = {
        'av': uid_page,
        '__user': uid_page, 
        '__a': '1',
        '__dyn': '7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgU765QdwSxucyU8EW1twYwJyEiwsobo6u3y4o1DU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y1lUlDw-waCm7-8wywdG7FobpEbUGdwb6223908O3216AzUjwTwNxe6Uak1xwJwxw',
        '__csr': 'gvgV4Ovdczgx2nkT5_kQy8AyjZjiJQdtEDZ9lOt4nl9VZVrIzheKAJruK-GAWQF9WGIDAKbGLyalaAcy8PKbKm-nGUyeAVUgUigGmfCCydyUjxi8x55ADWBzUhy8C9Byo9UOjyFFUlK3eq5ooBx2EgxDKcyoG263a8xa4oiyE8U-3fQi9zof8zwIy84y6o5-0zo524ooxu0zE2swNwExm1zx-E5aawm86e3y0VU0d5U0Di034200GF812U0EG17wc-0uO09Tw2IkdzA4u08yg0qwCg8o1dE0pFw2E21G01e3w1ou2t038U0Fa0aFw8q482ewkU',
        '__req': '12',
        '__hs': '19361.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1006781724',
        '__s': 'o58w4y:qt2tx8:sqhpjl',
        '__hsi': '7184674895444929347',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': 'ut-hiPpuPkfxGazKnTVgag',
        '__aaid': '891806128653375',
        '__spin_r': '1006781724',
        '__spin_b': 'trunk',
        '__spin_t': '1672812480',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUserFollowMutation',
        'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1672812480978,651446,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+ str(uid_profile) +'","actor_id":"'+uid_page+'","client_mutation_id":"2"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5032256523527306',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers_, data=data_).text
    time = datetime.now().strftime("%H:%M:%S")
    Write.Print(f'{time} | SUCCESS | {uid_profile} | PAGE | {uid_page} | {name_page} | FOLLOW | \n',Colors.blue_to_red,interval=0.0001)
for x in range(soluong):
    dem=dem+1
    threading.Thread(target=SentFollow,args=(x, cookie, link_profile)).start()
    idelay(delay_follow)

