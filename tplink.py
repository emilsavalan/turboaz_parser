import requests

values = {'tipsFlag': '0',
'timevalue': '0',
'Login_Name': 'admin',
'Login_Pwd': 'Ha2S+eOKqmzA6nrlmTeh7w==',
'uiWebLoginhiddenUsername': '21232f297a57a5a743894a0e4a801fc3',
'uiWebLoginhiddenPassword': '21232f297a57a5a743894a0e4a801fc3'
}


headers = {'X-Frame-Options': 'sameorigin',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '196',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': '192.168.1.1',
'Origin': 'http://192.168.1.1',
'Referer': 'http://192.168.1.1/login_security.html',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}



headers_1 = {'Location': 'http://192.168.1.1/basic/home_wan.htm',
'Server': 'WebServer/1.0 UPnP/1.0',
'X-Frame-Options': 'sameorigin',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '747',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': '192.168.1.1',
'Origin': 'http://192.168.1.1',
'Referer': 'http://192.168.1.1/basic/home_wan.htm',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

values_1={'HiddenFlag': '0',
'wan_VC': 'PVC0',
'wanVCFlag': '0',
'wan_VCStatus': '1',
'Alwan_VPI': '1',
'Alwan_VCI': '32',
'Alwan_QoS': 'UBR',
'wan_PCR': '0',
'wanIPVersionRadio': '0',
'wanConTypeFlag': '0',
'wanTypeRadio': 'Two',
'wan_PPPServicename': '',
'Allow_Empty_Flag': '1',
'Check_UsrPsw_Flag': '0',
'Empty_UsrPsw_Flag': '0',
'Check_PasswordFlag': '0',
'wan_PPPUsername': '123497973',
'wan_PPPPassword': 'ffe672fb',
'wan_PPPEncap': 'PPPoE LLC',
'wan_PPPAuth': 'AUTO',
'PPPoEBIStatus': '0',
'wan_ConnectSelect': 'Connect_Keep_Alive',
'wan_TCPMSS': '1400',
'WAN_DefaultRoute': '1',
'wan_PPPGetIP': '0',
'wan_TCPMTU': '1480',
'wan_NAT': 'Enable',
'wan_RIPVersion': 'RIP2-B',
'wan_RIPDirection': 'Both',
'wan_IGMP': 'IGMP v2',
'wan_EnabledSpoof': '0',
'wan_IPv6DHCP': '1',
'wan_IPv6DHCPPDEnable': '1',
'wan_IPv6MLDProxy': '1',
'wan_IPv6DSLiteEnable': '0',
'wan_IPv6DSLiteMode': '0',
'wan_RemoteAddress': '::',
'BridgeFlag': '0',
'wanIGMPQitFlag': '0',
'wan_PVCO_Flag': '0',
'PageLockValue': '0'}

r=requests.Session()
r1 = r.post('http://192.168.1.1/')
r2 = r.post('http://192.168.1.1/Forms/login_security_1', data=values, headers=headers)
r3 = r.post('http://192.168.1.1/Forms/home_wan_1', data=values_1, headers=headers_1)

