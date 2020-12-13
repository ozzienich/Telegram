
'''
=======================================================================================
    oracle-EM -> snmp Traps -> snmptt -> /var/log/snmptt/snmpEM.log
    
    monitor file /var/log/snmptt/snmpEM.log | sent to telegram group
    
    (c)2020 - OZZIE     
=======================================================================================
'''
import re
import time
import os
import requests

gogo = ""

def follow(thefile):
    thefile.seek(0, os.SEEK_END)

    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line


def main():
    bot_token='XXXXXXXXXX'
    chat_ids='-XXXXXXXXXX'
    
    logfile = open("/var/log/snmptt/snmpEM.log","r")
    loglines = follow(logfile)
    
    proxies = { "http": "http://xxx.xxx.xxx.xxx:8080","https": "http://xxx.xxx.xxx.xxx:8080",}

    pattern_summary = 'Ent Value 1: SNMPv2-SMI::enterprises.111.15.3.1.1.3.1='
    pattern_saverity = 'Ent Value 4: SNMPv2-SMI::enterprises.111.15.3.1.1.6.1='
    pattern_date = 'Ent Value 8: SNMPv2-SMI::enterprises.111.15.3.1.1.10.1='
    pattern_matric_alert = 'Ent Value 11: SNMPv2-SMI::enterprises.111.15.3.1.1.13.1'
    pattern_target = 'Ent Value 19: SNMPv2-SMI::enterprises.111.15.3.1.1.21.1'
    pattern_target2 ='Ent Value 21: SNMPv2-SMI::enterprises.111.15.3.1.1.23.1='
    pattern_url = 'Ent Value 2: SNMPv2-SMI::enterprises.111.15.3.1.1.4.1='

    gogo = ""
    for line in loglines:
        if re.match(pattern_summary, line):
            oo = line.split('=')
            gogo = ("ALERT: " + oo[1])

        if re.match(pattern_url, line):
            oo = line.split('4.1=')
            url = ("\U0001F449  URL: " + oo[1])

        if re.match(pattern_saverity, line):
            saver = line.split('=')
            uio = saver[1].split()
            uio = uio[0]
            if uio == 'WARNING':
              icon1 = '\U000026A0'
              print (icon1)
            elif uio == "CLEAR":
              icon1 = '\U00002705'
              print(icon1)
            elif uio == "FATAL":
              icon1 = '\U0000274C'
              print(icon1)
            elif uio == "CRITICAL":
              icon1 = '\U0001F198'
              print(icon1)
            elif uio == "MINOR_WARNING":
              icon1 = '\U00002139'
              print(icon1)
            else:
              icon1 = "\U0001F198"
            gogo = gogo + ("Severity: " + saver[1])

        if re.match(pattern_date, line):
            saverd = line.split('=')
            gogo = gogo + ("Date: " + saverd[1])

        if re.match(pattern_matric_alert, line):
            matalert = line.split('=')
            gogo = gogo + ("Event Type: " + matalert[1])

        if re.match(pattern_target, line):
            tarf = line.split('=')
            gogo = gogo + ("Target: " + tarf[1])

        if re.match(pattern_target2, line):
            tarf2 = line.split('=')
            gogo = gogo + tarf2[1]
            gogo = (icon1 + "\n" + gogo + "\n" + url)
            print (gogo)
            sent_meseg = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_ids + '&text=' + str(gogo)
            r = requests.post(sent_meseg,proxies=proxies)
            
if __name__ == '__main__':
    main()

