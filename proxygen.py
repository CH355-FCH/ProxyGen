# Tools originally by PhynX
# Note : This tool will eat more CPUs, Please use this tool carefully.
# -*- coding: utf-8 -*-

import os,sys,time,random

def banner():
    print('''
            ___  ____ ____ _  _ _   _ ____ ____ _  _ 
            |__] |__/ |  |  \/   \_/  | __ |___ |\ | 
            |    |  \ |__| _/\_   |   |__] |___ | \| 
                                            By:PhynX                      
    ''')

def ponik():
    global ttlgen, output
    if sys.platform.startswith("linux"):
        os.system('clear')
    if sys.platform.startswith("freebsd"):
        os.system('clear')
    if sys.platform.startswith("win32"):
        os.system('cls')
    else:
        os.system('clear')
    banner()
    ttlgen = int(input('How many Proxy? [1-Unlimited] : '))
    output = str(input('Output Name : '))
    if ttlgen == '':
        banner()
        ponik()
    elif ttlgen >= 100000:
        huh = str(input('\nAre you sure want generate ' + str(ttlgen) + ' Proxy? [PRESS ENTER TO CONTINUE]'))
        if huh == "":
           gen()
        else:
            banner()
            ponik()
    else:
        if sys.platform.startswith("linux"):
            os.system('clear')
        if sys.platform.startswith("freebsd"):
            os.system('clear')
        if sys.platform.startswith("win32"):
            os.system('cls')
        else:
            os.system('clear')
        banner()
        gen()
        
def gen():
    global i, startgen
    startgen = True
    file = open(str(output), 'wb')
    i = 0
    while startgen:
        for x in range(ttlgen):
            try:
                randr = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + ":" + str(random.choice(['80', '1080', '3128', '8080', '8081']))
                file.write(str.encode(randr + "\n"))
                i+=1
                print(str(i) + " Proxy Generated...\r".format(i), end='')
            except KeyboardInterrupt:
                startgen = False
                if sys.platform.startswith("linux"):
                    os.system('clear')
                if sys.platform.startswith("freebsd"):
                    os.system('clear')
                if sys.platform.startswith("win32"):
                    os.system('cls')
                else:
                    os.system('clear')
                print(str(i) + ' Proxies was Generated.\n')
                file.close()
                break
            except:
                if sys.platform.startswith("linux"):
                    os.system('clear')
                if sys.platform.startswith("freebsd"):
                    os.system('clear')
                if sys.platform.startswith("win32"):
                    os.system('cls')
                else:
                    os.system('clear')
                break
                continue
                sys.stdout.flush()
                print(str(i) + " Proxies Was Generated.")
                file.close()
        else:
            sys.stdout.flush()
            print(str(i) + " Proxies Was Generated.")
            break
            continue
        
if __name__ == '__main__':
    ponik()
