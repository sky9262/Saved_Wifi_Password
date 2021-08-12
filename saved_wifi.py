import glob,os,subprocess

def run(cmd):
    # In subprocess.call arrgument, write "stdout=subprocess.PIPE" as secound arrgument to don't show output
    subprocess.call(cmd, stdout=subprocess.PIPE)

def DoNotShowHiddenFiles():
    # In os.system command, write " > NUL " at end of command to don't show output
    os.system('REG QUERY "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Hidden" | Find "0x0" > NUl')
    os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /f /d 0 > NUl')
    os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ShowSuperHidden /t REG_DWORD /f /d 0 > NUl')

def ShowHiddenFiles():
    # In os.system command, write " > NUL " at end of command to don't show output
    os.system('REG QUERY "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Hidden" | Find "0x0" > NUl')
    os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /f /d 1 > NUl')
    os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ShowSuperHidden /t REG_DWORD /f /d 1 > NUl')



def HideFiles(filename):
    if isinstance(filename, list):
        for name in filename:
            run(f'attrib +h "{name}"')
    else :
        run(f'attrib +h "{filename}"')

def GetWifiDetails():
    run('netsh wlan export profile key=clear')
    wifianmes = []
    for file in glob.glob("*.xml"):
        wifianmes.append(file)
    return wifianmes

  
def SavedWifi():
    os.system("cls")    
    os.system("color 0A")    
    print("==============================================")
    print(f"          WELCOME TO SKY-FI.")
    print("==============================================")

    print("\n1. Saved wifi.\n0. Exit")

    ask = int(input("\nEnter your choice :"))

    if ask == 1:
        DoNotShowHiddenFiles()
        wifinames = GetWifiDetails()
        HideFiles(wifinames)
        os.system("cls")  
        print("============= All Saved Wifi ==============\n")
        i = 0
        for name in wifinames:
            i += 1
            print(f"{i}. ",(name.replace("Wi-Fi-", "")).replace(".xml", ""))
        try:
            ask = int(input("\nEnter wifi no. to show password :"))

            if ask <= i and ask > 0:
                with open(wifinames[ask-1]) as f:
                    contents = f.read() 
                password = (contents.split("keyMaterial>"))
                try:
                    print("Password : ",password[1].replace("</", ""))
                except:
                    print("{No Password required for this wifi}")    
                input("\n\nPress ENTER to continue.............")
                SavedWifi()
            else:
                print("\nYou entred wrong key.\nPlease try again later !!!")
                input("\n\nPress ENTER to continue.............")
                SavedWifi()
        except:
            print("\nYou entred wrong key.\nPlease try again later !!!")
            input("\n\nPress ENTER to continue.............")  

            SavedWifi()         
    elif ask == 0:
        exit()
    else:
        print("\nYou entred wrong key.\nPlease try again later !!!")
        print(ask) 
        input("\n\nPress ENTER to continue.............") 
        SavedWifi()      


SavedWifi()        
