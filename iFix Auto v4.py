import os
import sys
import time
import threading
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Chrome
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


#current_time = datetime.datetime.now()
#print("\n")
#print(current_time)
logcheck = 'unchecked'
#date = datetime.now().strftime("%b %d %Y %H:%M:%S")
key = Fernet.generate_key()
fernet = Fernet(key)
##global flag
##flag = 'Running'

def Distribution(username,psswd,SrRadio,SrAssigned,Tickets,TopTicket,Shift,HomeButton):
    flagout = False
    print("Inside the thread.")
    time.sleep(10)
    #print(username,psswd)
    browser2 = webdriver.Chrome(options=opts)
    print("[*]Browser Instances Created.")
    time.sleep(1)
    
    browser2.get('https://idp.larsentoubro.com/adfs/ls/?SAMLRequest=hVFNb8IwDP0rUe40SUGii6CIjcOQmIag7LDLlKYpRKRJFyeIn7%2BuDI1d2NH28%2FuwJ7NzY9BJedDOTjFLKJ7lExCNafk8hoPdqM%2BoIKAOZoH3gymO3nInQAO3olHAg%2BTb%2BcuKpwnlrXfBSWcwWi6m%2BENmrByNmRjWaTrOavVQVyOM3q6C3UYHBIhqaSEIG7oWTdmAsQFNC8o4zfhomGTj9B2j9Q%2F1o7aVtvv7PsoLCPhzUawH69dtgdGiS6KtCL30IYQWOCG6ahMjPCgbXCy9S6RriKhqIAYIRnMA5b83npyF2Ci%2FVf6kpdptVr8cxoaDMm2l4JjoWp%2BlcbHqiIhxe22JFMaUQh7x5bS8D%2Bxvbno%2FirhawPn%2Fgn0SyibkRim%2FVH9fmn8B&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=Hec6pBk7TGe097AB351I1zGOi4W2J280URtnx8kmaIoyTCX0qFdajTln2yhtz4ZSRoM%2FdnG0RaJ7W8w4EsHndVeOfTEWfvPGITPU8X%2BuMl9i4uxk2aXO8LBCTYUqoJdXJE6glQYHifEakCwq97CIk8VkbSAERBCjHjFI94%2Fz76lwxHrFIWNyENnATpOCwtcnfezZ0pjRIn3yvLVuxF2mC6kqbGMlyJBLzmNlJr5LH02u%2FQE%2FxnTKel3%2FgYTnx%2BEVskrzyKjALl0H1HoJBAwCPxsVrmwyK34If7qTKk0VqZ19hKK1LKzIPB787pTgnqObu1r9mry7lYQZFhhOBO4H%2FNG3hy2WddjL3B6g5EcgFZ%2BOvLAFehjz4I1h8mFFx6VQS19rwxeWlVM%2BpYk4uoq%2Fs2rUFej%2F9Pq4eUvBpwJelQhC1%2FYwVg4WTVoFm06ouPQVNnokKrjtiwYucDQojkfRFNNgTYfpacIEmqiJipLns9EsuyGgNsbcmG5wL1%2BDU%2FmymIScy27s8LLVwAdh%2BylvZjdsu0UiXIajWuaxLz31GwCb5AGWwdjMnLPDiA6Q9RrCK4nm4YBm28421dFcLFV4l9CAMTz8%2FRol%2FlEohJ3MDYqc0qmtQi1DzowAqlDK5vNRl0ajDHNjMGEBpeqJffD45C04fGWYVkkY1TKrEU7JyS4%3D')
    print("[*]Distribution URL Redirection Sucessful")

    time.sleep(2)
    
    browser2.find_element("id","userNameInput").send_keys(username)
    browser2.find_element("id","passwordInput").send_keys(psswd)
    browser2.find_element("id", "submitButton").click()

    time.sleep(2)

    select = Select(browser2.find_element(By.CLASS_NAME,"form-control"))
    select.select_by_value("3")
    print("[*]Logged In")

    print("Thread waiting for 10 seconds.")
    for x in range(11):
        time.sleep(1)
        #print(x)

    while True:
        try:
            #print("[Dist] Trying to click SrRadio")
            browser2.find_element(By.XPATH,SrRadio).click()
            print("[Dist][Done] Trying to click SrRadio")
        except:
            print("[Dist] Failed to click SrRadio")
            browser2.refresh()
            print("Browser refreshed retrying after 5 seconds.")
            time.sleep(5)
            continue
        try:
            Workspace = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[1]/div[2]/mat-form-field/div/div[1]/div/mat-select"
            browser2.find_element(By.XPATH,Workspace).click()
            print("[Dist][Done] Clicked on Workspace")
            Team_Workspace = "/html/body/div[2]/div[2]/div/div/div/mat-option[2]/span"
            browser2.find_element(By.XPATH,Team_Workspace).click()
            print("[Dist][Done] Clicked on Team Workspace")
        except:
            print("[Dist][ERROR] Failed to click on Workspace or Team Workspace.")
            time.sleep(2)
            
        while True:
            try:
                #print("[Dist] Trying to click SrAssigned")
                browser2.find_element(By.XPATH,SrAssigned).click()
                print("[Dist][Done] Trying to click SrAssigned")
                time.sleep(2)
                #break
                
            except:
                print("[Dist][ERROR] Failed to click SrAssigned")
                browser2.refresh()
                print("[Dist][Done]Browser refreshed.")
                time.sleep(3)
                
                try:
                    browser2.find_element(By.XPATH,HomeButton).click()
                    time.sleep(2)
                except:
                    browser2.refresh()
                    print("[Dist][Done]Browser Refresh")
                    time.sleep(2)                          
                continue
            DistTopTicketIndex = 1
            print(f"Changed to : {DistTopTicketIndex}")

#********

            for Engineer in Shift:
                time.sleep(1)
                ActionForAnalystREFRESH = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[1]/div[5]/ul/li[1]"
                                           
                print("*" * 50)
                print(f"Selected Engineer '{Engineer}'")
                QueCount = 1
                while(len(Tickets) == 0):
                    print(f"No tickets in Queue({QueCount}) : {Engineer}")
                    DistTopTicketIndex = 1000
                    time.sleep(4)
                    QueCount = QueCount + 1
                    continue


                browser2.refresh()
                print("[Dist][Done]Browser Refresh")
                time.sleep(3)
                AssignedUser = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/span[2]"
                EngineerList = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/select"
                EngineerIndex = 12
                Options = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div[1]/select/option[{EngineerIndex}]"
                FwdButton = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[7]/div[2]/button"
                #FwdCommentIndex = 4
                FwdComment = "/html/body/div[2]/div[2]/div/mat-dialog-container/div[1]/textarea"
                              
                #Submit = "/html/body/div[2]/div[2]/div/mat-dialog-container/div[2]/button"
                Submit = "/html/body/div[2]/div[2]/div/mat-dialog-container"
                actions = ActionChains(browser2)
                
                          
                
                #DistTicketName = DistTopTicket+"/div[2]"
                
                while True:
                    try:
                        #browser2.refresh()
                        #print("[Dist][Done]Browser refreshed.")
                        #time.sleep(3)
                        DistTopTicket = f"/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[2]/div/div[2]/angular-slickgrid/div/div/div[4]/div[3]/div/div[{DistTopTicketIndex}]"
                        DistTicketID = DistTopTicket+"/div[1]"    
                        print(f"Tickets in Thread {Tickets}")
                        #browser2.refresh()
                        DistTicketID = browser2.find_element(By.XPATH,DistTicketID).text
                        print(f"[Dist][Done] Fetched Ticket ID : {DistTicketID}")

                        if(DistTicketID not in Tickets):
                            print(f"{Engineer} Index is : {DistTopTicketIndex}")
                            DistTopTicketIndex = DistTopTicketIndex + 1
                            print(f"{Engineer} Changed to : {DistTopTicketIndex}")

                            print("Fetched Ticket is not in the list. Going back to the first ticket.Browser refresh.")
                            if (DistTopTicketIndex == 1):
                                #browser2.refresh()
                                #Tickets.remove(DistTicketID)
                                print("[Dist][Done]DistTopTicketIndex == 1")
                                #time.sleep(3)
                            continue
                        break
                    except:
                        time.sleep(2)
                        print("No ticket fetched. Retrying...")
                        print(f"{Engineer} Index is : {DistTopTicketIndex}")
                        DistTopTicketIndex = 1
                        print(f"{Engineer} Changed to : {DistTopTicketIndex}")
                        print(Tickets)
                        Tickets.clear()
                        browser2.refresh()
                        print("[Dist][Done]Ticket not found hence cleared the Queue and Browser refreshed..")
                        while(len(Tickets) == 0):
                            print(f"No.tickets in Queue({QueCount}) : {Engineer}.")
                            DistTopTicketIndex = 1000
                            time.sleep(4)
                            QueCount = QueCount + 1
                            continue
                        #DistTopTicketIndex = DistTopTicketIndex + 1
                        continue
                
                if Engineer == 'Self':
                    print(f"{Engineer} Index is : {DistTopTicketIndex}")
                    #DistTopTicketIndex = DistTopTicketIndex + 1
                    DistTopTicketIndex = 1
                    print(f"{Engineer} Changed to : {DistTopTicketIndex}")
                    print(f"Skipping this ticket[{DistTicketID}] for self")
                    Tickets.remove(DistTicketID)
                    continue
                if DistTicketID in Tickets:
                    while True:
                        print(f"This is the current top ticket: {DistTicketID}")
                        while True:
                            try:
                                browser2.find_element(By.XPATH,DistTopTicket).click()
                                print("[Dist][Done] Inside the top ticket")
                                time.sleep(3)
                                break
                            except:
                                print(f"{Engineer} Index is : {DistTopTicketIndex}")
                                DistTopTicketIndex = 1
                                print(f"{Engineer} Changed to : {DistTopTicketIndex}")
                                print("[Dist][exception] NOT Inside the top ticket")
                                flagout = True
                                DistTopTicketIndex = 1000
                                Tickets.remove(DistTicketID)
                                continue
   
                        if(flagout == True):
                            flagout = False
                            print("Flagedout TopTicket")
                            break
                        while True:
                            try:
                                temp = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/span[2]"
                                browser2.find_element(By.XPATH,temp).click()
                                temp = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/select"
                                #browser2.find_element(By.XPATH,temp).click()
                                print("[Dist][Done] Inside the Engineer list")
                                select = Select(browser2.find_element(By.XPATH,temp))
                                time.sleep(2)

                                select.select_by_visible_text(Engineer.strip())
                                time.sleep(1)
                                print("[Dist][Done] Found the engineer")
                                break
                            except:
                                print("[Dist][exception] NOT Found the engineer")
                                browser2.refresh()
                                print("[Dist][Done]Browser refresh")
                                time.sleep(3)
                                flagout = True
                                #continue
                                break
                        if(flagout == True):
                            flagout = False
                            print("Flagedout")
                            continue
                        while True:
                            try:                    
                                browser2.find_element(By.XPATH,FwdButton).click()
                                comment = f"Assigned to {Engineer}"
                                print("[Dist][Done] clicked on the FWD button")
                                time.sleep(5)
                                break
                            except:
                                print("[Dist][exception]")
                                browser2.refresh()
                                print("[Dist][Done]Browser Refresh")
                                time.sleep(3)
                                flagout = True
                                #continue
                                break
                        if(flagout == True):
                            flagout = False
                            print("Flagedout")
                            continue
                        while True:
                            try:
                                #browser.find_element("placeholder","Enter Comments before forwarding").send_keys(comments)
                                browser2.find_element(By.XPATH,FwdComment).click()
                                print("[Dist][Done] Click on the text area")
                            except:
                                try:
                                    FwdComment = '/html/body/div[4]/div[2]/div/mat-dialog-container/div[1]/textarea'
                                    print("[Dist][Done] Clicked on the updated text area xpath")
                                    #continue
                                except:
                                    print('Updated text area xpath not working.')
                                    browser2.refresh()
                                    print("[Dist][Done]Browser Refresh")
                                    time.sleep(3)
                                    flagout = True
                                    #continue
                                    break
                            try:                            
                                browser2.find_element(By.XPATH,FwdComment).send_keys(comment)
                                time.sleep(1)
                                print("[Dist][Done] Comment added")
                            except:
                                print("[Dist][exception] Comment not added. Retrying")
                                browser2.refresh
                                time.sleep(2)
                                flagout = True
                                break
                                #continue
                            try:
                                browser2.find_element(By.XPATH,FwdComment).send_keys(Keys.TAB)
                                print("[Dist][Done] Pressed TAB")
                                time.sleep(2)
                                #browser2.find_element(By.XPATH,Submit).send_keys(Keys.ENTER)
                                actions.send_keys(Keys.ENTER)
                                actions.perform()
                                print("[Dist][Done] Pressed ENTER")
                                #browser2.find_element(By.XPATH,Submit).click()
                                time.sleep(2)
                                print("[Dist][Done] clicked on submit.")
                                #FwdCommentIndex = 2
                                break
                            except:
                                #FwdCommentIndex = 4
                                print("[Dist][exception] TAB ENTER not pressed. Retrying")
                                browser2.refresh()
                                print("Browser refresh")
                                time.sleep(3)
                                flagout = True
                                #continue
                                break
                        if(flagout == True):
                            flagout = False
                            print("Flagedout")
                            continue
                        while True:
                            try:
                                print("[Dist][Done] Alert accepted.")
                                browser2.switch_to.alert.accept()
                                print(f"{Engineer} Index is : {DistTopTicketIndex}")
                                DistTopTicketIndex = 1
                                print(f"{Engineer} Changed to : {DistTopTicketIndex}")
                                Tickets.remove(DistTicketID)
                                    
                                print("[Dist][Done] Ticket removed from the Queue.")
                                break
                            except:
                                print("[Dist][exception] NOT Alert accepted.")
                                browser2.refresh()
                                print("[Dist][Done]Browser refresh")
                                time.sleep(3)
                                flagout = True
                                #continue
                                break
                            
                        
                        if(flagout == True):
                            flagout = False
                            print("Flagedout")
                            continue
                        break
                        
                else:
                    print("No Ticket Found in the List.")
                    continue
        #break
#def UpdateEngineerName(Engineer):
    #return Engineer


def encrypt(line1,line2,fernet,cred):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    nl="\n"
    line1 = fernet.encrypt(line1.encode())
    line1_str = str(line1)
    line1_str = "$"+line1_str[2:-1]
    line2 = fernet.encrypt(line2.encode())
    line2_str = str(line2)
    line2_str = "$"+line2_str[2:-1]
    keydecode = key.decode()
    cred = open('cred.txt', 'w')
    cred.writelines([line1_str,nl,line2_str,nl,keydecode])
    cred.close()

def decrypt(line1,line2,fernet):
    cred = open('cred.txt','r')
    lines = cred.readlines()
    key = lines[2]
    key = bytes(key.encode())
    fernet = Fernet(key)
    user = fernet.decrypt(line1).decode()
    passw = fernet.decrypt(line2).decode()
    return user,passw
    

def login(fernet):
    user = ""
    passw = ""
    try:
        cred = open('cred.txt', 'r')
    except:
        os.system("'' > cred.txt")
        #os.system("###########################################################################" >> log.txt)
        os.system(f'echo Logged in at {datetime.now().strftime("%b %d %Y %H:%M:%S")} >> ../log/log.txt')
        #os.system("powershell hostname >> log.txt")
        os.system("echo [*] cred.txt file is generated in the current folder. Paste you Email ID(username) and Password each on a new line. >> ../log/log.txt")
        logcheck = 'checked'
        sys.exit()
        
    Line = cred.readlines()

    try:
        line1 = Line[0]
    except:
        os.system("echo [*] Credential file is empty. >> ../log/log.txt")
        sys.exit()
    line2 = Line[1]
    cred.close()

    if(line1[0:1] == "$"):
        line1 = line1[1:]
        line2 = line2[1:]
        user,passw = decrypt(line1,line2,fernet)
        return user,passw
    else:
        line1 = line1.strip()
        line2 = line2.strip()
        encrypt(line1,line2,fernet,cred)
        return line1,line2

username,psswd = login(fernet)
#print(username.strip())
#print('a')
#type(username)

#os.system("powershell hostname >> log.txt")
if(logcheck != 'checked'):
    #os.system("echo ########################################################################### >> log.txt")
    os.system(f'echo Logged in at {datetime.now().strftime("%b %d %Y %H:%M:%S")} >> ../log/log.txt')
    hostname = subprocess.check_output("powershell hostname")
    hostname = hostname[:-2].decode()
    userhost = f"{hostname} - {username.strip()}"
    os.system(f"echo {userhost} >> ../log/log.txt")
        
SR_num = 1
INC_num = 1

IncRadio = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[1]/div[1]/mat-radio-group/mat-radio-button[1]/label/div[2]"
SrRadio = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[1]/div[1]/mat-radio-group/mat-radio-button[2]/label/div[2]"
SrUassigned = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[2]/div[5]/div/div[1]/h4"
SrAssigned = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[2]/div[4]/div/div[1]/h4"
IncUnassigned = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-dashboard-cit/div/div[2]/div[2]/div[5]/div/div[1]/h4"
TopTicketIndex = 1
TopTicket = f"/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[2]/div/div[2]/angular-slickgrid/div/div/div[4]/div[3]/div/div[{TopTicketIndex}]"
AssignToSelf = "/html/body/ngb-modal-window/div/div/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div[2]/button"
HomeButton = "/html/body/app-root/app-navbar-lt/nav/div/div[1]/a[1]/img"
InnerIncRadio = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[1]/div[3]/mat-radio-group/mat-radio-button[1]/label/div[2]"
InnerSrRadio = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[1]/div[3]/mat-radio-group/mat-radio-button[2]/label/div[2]"
InnerUnassigned = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[1]/div[5]/ul/li[2]"
                  #"/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[1]/div[5]/ul/li[2]"
TicketIdPath = "/html/body/app-root/app-navbar-lt/mat-sidenav-container/mat-sidenav-content/app-view-ticket-cit/div[1]/div[2]/div[2]/div/div[2]/angular-slickgrid/div/div/div[4]/div[3]/div/div[1]/div[1]"
Tickets = []
Shift = ['Self']


while True:
    try:
        ShiftInp = open('shift.txt' , 'r')
        #print('[shift] File imported')
        line = ShiftInp.readlines()
        #print('[shift] lines read')
        for x in line:
            if x[0] == '#':
                continue
            x = x[0:-1]
            Shift.append(x)
        #print('[shift] # excluded')
        for x in Shift:
            if x == '' or x == ' ':
                Shift.remove(x)
        #print('[shift] List ready')
        break
    except KeyboardInterrupt:
        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
        os.system("echo ########################################################################### >> ../log/log.txt")
        sys.exit()
    except:
        print("[*] Unable to read the shifts file. shift.txt has been created.Make the necessary changes and Run the script again")
        os.system(f"echo [*]shift file was not present. Created a shift.txt in the working directory. >> ../log/log.txt")
        os.system("powershell $null > shift.txt")
        EngineerList = """#Vineeth Rane 
#jaydip patil 
#Jaied Ali Juned Ghori 
#Nihal Dhepe 
#Hansika Gupta 
#Patwa Avinash Dhannulal 
#Dharmendra 
#Prathmesh Shirish Haware 
#Karan Kumar Kundanmal Suthar 
#SUSHILKUMAR VISHWAKARMA 
#Aman Sharma
#Sumedh Prakash Pokhare """
        
        shiftfile = open('shift.txt','w')
        shiftfile.writelines([EngineerList])
        #time.sleep(2)
        sys.exit()
        continue
os.system(f"echo {Shift} >> ../log/log.txt")
print(f"Engineers in Shift : {Shift}")


IncRadio = str(IncRadio)
SrRadio = str(SrRadio)
SrUassigned = str(SrUassigned)
IncUnassigned = str(IncUnassigned)
TopTicket = str(TopTicket)
AssignToSelf = str(AssignToSelf)
HomeButton = str(HomeButton)
InnerIncRadio = str(InnerIncRadio)
InnerSrRadio = str(InnerSrRadio)
InnerUnassigned = str(InnerUnassigned)

opts = Options()
c = 0

while True:
    try:
        browser = webdriver.Chrome(options=opts)
        print("[*]Browser Instances Created.")
        break
    except KeyboardInterrupt:
        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
        os.system("echo ########################################################################### >> ../log/log.txt")
        sys.exit()
        break
    except:
        c = c+1
        print(f'[*]: Unable to create a browser instance... Retry({c})')
        #os.system("echo [*] Unable to create a browser instances >> log.txt")
        
        if c >= 3:
            os.system("echo [*]: Unable to create a browser instance. Hence execution stopped. >> ../log/log.txt")
            sys.exit()
            break
        #print(c)
        time.sleep(3)
        continue
    

##while True:
##    try:
##        #opts = webdriver.EdgeOptions()
##        browser = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
##        print("[*]Edge Browser Instances Created.")
##        break
##    except:
##        print('[*]: Unable to create a Edge browser instance')
##        os.system("echo [*] Unable to create a browser instances >> log.txt")
##        time.sleep(3)
##        continue

while True:
    try:
        try:
            browser.get('https://idp.larsentoubro.com/adfs/ls/?SAMLRequest=hVFNb8IwDP0rUe40SUGii6CIjcOQmIag7LDLlKYpRKRJFyeIn7%2BuDI1d2NH28%2FuwJ7NzY9BJedDOTjFLKJ7lExCNafk8hoPdqM%2BoIKAOZoH3gymO3nInQAO3olHAg%2BTb%2BcuKpwnlrXfBSWcwWi6m%2BENmrByNmRjWaTrOavVQVyOM3q6C3UYHBIhqaSEIG7oWTdmAsQFNC8o4zfhomGTj9B2j9Q%2F1o7aVtvv7PsoLCPhzUawH69dtgdGiS6KtCL30IYQWOCG6ahMjPCgbXCy9S6RriKhqIAYIRnMA5b83npyF2Ci%2FVf6kpdptVr8cxoaDMm2l4JjoWp%2BlcbHqiIhxe22JFMaUQh7x5bS8D%2Bxvbno%2FirhawPn%2Fgn0SyibkRim%2FVH9fmn8B&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=Hec6pBk7TGe097AB351I1zGOi4W2J280URtnx8kmaIoyTCX0qFdajTln2yhtz4ZSRoM%2FdnG0RaJ7W8w4EsHndVeOfTEWfvPGITPU8X%2BuMl9i4uxk2aXO8LBCTYUqoJdXJE6glQYHifEakCwq97CIk8VkbSAERBCjHjFI94%2Fz76lwxHrFIWNyENnATpOCwtcnfezZ0pjRIn3yvLVuxF2mC6kqbGMlyJBLzmNlJr5LH02u%2FQE%2FxnTKel3%2FgYTnx%2BEVskrzyKjALl0H1HoJBAwCPxsVrmwyK34If7qTKk0VqZ19hKK1LKzIPB787pTgnqObu1r9mry7lYQZFhhOBO4H%2FNG3hy2WddjL3B6g5EcgFZ%2BOvLAFehjz4I1h8mFFx6VQS19rwxeWlVM%2BpYk4uoq%2Fs2rUFej%2F9Pq4eUvBpwJelQhC1%2FYwVg4WTVoFm06ouPQVNnokKrjtiwYucDQojkfRFNNgTYfpacIEmqiJipLns9EsuyGgNsbcmG5wL1%2BDU%2FmymIScy27s8LLVwAdh%2BylvZjdsu0UiXIajWuaxLz31GwCb5AGWwdjMnLPDiA6Q9RrCK4nm4YBm28421dFcLFV4l9CAMTz8%2FRol%2FlEohJ3MDYqc0qmtQi1DzowAqlDK5vNRl0ajDHNjMGEBpeqJffD45C04fGWYVkkY1TKrEU7JyS4%3D')
            print("[*]URL Redirection Sucessful")
            
            
            browser.find_element("id","userNameInput").send_keys(username)
            browser.find_element("id","passwordInput").send_keys(psswd)
            browser.find_element("id", "submitButton").click()
            
            select = Select(browser.find_element(By.CLASS_NAME,"form-control"))
            select.select_by_value("3")
            
            print("[*]Logged In")
            break
        except KeyboardInterrupt:
            os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
            os.system("echo ########################################################################### >> ../log/log.txt")
            sys.exit()
        except:
            print("[-]Login error. Retrying...")
            os.system("echo [*] URL Not Opening or Login issue. Check Internet connection. >> ../log/log.txt")      
            continue
    except KeyboardInterrupt:
        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
        os.system("echo ########################################################################### >> ../log/log.txt")
        sys.exit()

if(len(Shift) != 1):
    print("### Multiple members detected - TRIGERRING THE THREAD ###")
    t1 = threading.Thread(target=Distribution, daemon=True, args=(username,psswd,SrRadio,SrAssigned,Tickets,TopTicket,Shift,HomeButton,)).start()

try:
    time.sleep(7)
except KeyboardInterrupt:
    os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
    os.system("echo ########################################################################### >> ../log/log.txt")
    sys.exit()
    
try:
    while True:
        try:
            time.sleep(1)
            b = browser.find_element(By.XPATH,SrRadio).click()
            print('Clicked on SR Radio')
            time.sleep(0.5)
            b = browser.find_element(By.XPATH,SrUassigned).click()
            print('Clicked on SR Unassigned Bucket.')
            print("-"*50)
            print("Initializing Ticket Assigning Loop.")
            print("-"*50)
        except KeyboardInterrupt:
            os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
            os.system("echo ########################################################################### >> ../log/log.txt")
            sys.exit()
            
        except:
            browser.refresh()
            print('[*]Unable to read radio and unassigned bucket refreshing browser.')
            time.sleep(3)
            continue
##        while True:
##            num = 0
##            try:
##                b = browser.find_element(By.XPATH,InnerSrRadio).click()
##                print("[*]Entered SR Section")
##                time.sleep(2)
##            except KeyboardInterrupt:
##                os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> log.txt")
##                os.system("echo ########################################################################### >> log.txt")
##                sys.exit()
##            except:
##                browser.refresh()
##                print("[InnerSrRadio]page refresh.")
##                time.sleep(5)
##                continue
##            try:
##                b = browser.find_element(By.XPATH,InnerUnassigned).click()
##                print("     [*]Entered SR Unassigned Bucket")
##            except KeyboardInterrupt:
##                os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> log.txt")
##                os.system("echo ########################################################################### >> log.txt")
##                sys.exit()
##            except:
##                browser.refresh()
##                print("[InnerUnassigned_SR]page refresh.")
##                time.sleep(5)
##                continue
        
        while True:
            time.sleep(3)
            try:
                print('      [*]Searching for tickets.')
                print("     [*]Selecting Top most SR")
                TicketID = browser.find_element(By.XPATH,TicketIdPath).text
                #print("*" * 50 )
                #print(Ticket_id)
                #print("*" * 50 )
                Tickets.append(TicketID)
                c = browser.find_element(By.XPATH,TopTicket).click()
                #print("[Sucess]Selected Top-Most SR Ticket.")
                time.sleep(2)
                while True:
                    try:
                        d = browser.find_element(By.XPATH,AssignToSelf).click()
                        print(f"    {SR_num}) SR Ticket assigned!")
                        SR_num = SR_num + 1
                        time.sleep(1)
                    except KeyboardInterrupt:
                        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                        os.system("echo ########################################################################### >> ../log/log.txt")
                        sys.exit()
                    except:
                            #num = 1
                            #while True:
                                #if(num == 3):
                                    #break
                            #browser.refresh()
                            #print("[AssignToSelf_SR]page refresh")
                        if (num == 10):
                            browser.refresh(3)
                            print("Browser refreshed")
                            time.sleep(3)
                            break
                        print("Waiting for the ticket to Load.")
                        num = num + 1
                        time.sleep(1)
                            #time.sleep(5)
                        continue
                            #num = 1
                            #continue
                        
                    try:
                            
                            #time.sleep(2)
                            #Alert = browser.switch_to.alert()
                            #Alert_text = Alert.getText()
                        alert = Alert(browser)
                        print("    [*] " + alert.text)
                        browser.switch_to.alert.accept()
                        print(f"    [*] Popup accepted")
                        time.sleep(2)
                        if (alert.text != "Ticket Forwarded successfully"):
                            Tickets.append(TicketID)
                            print(f'    [*] SR Ticket - {TicketID} Assigned!')
                            TopTicketIndex = TopTicketIndex + 1
                            break
                        Tickets = list(set(Tickets))
                        print(Tickets)
                        time.sleep(1)
                        num = 0
    ##                        print("#" * 50)
    ##                        print(t1 , ": " , type(t1))
    ##                        print("#" * 50)
    ##                        if t1 == 'Stopped':
    ##                            print("Starting a new thread.")
    ##                            t1 = threading.Thread(target=Distribution, daemon=True, args=(username,psswd,SrRadio,SrAssigned,Tickets,TopTicket,Shift,HomeButton,)).start()

                        break
                    except KeyboardInterrupt:
                        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                        os.system("echo ########################################################################### >> ../log/log.txt")
                        sys.exit()
                    except:
                        browser.refresh()
                        print("[popup_SR]page refresh")
                        time.sleep(3)
                        break
                continue
                #if (num == 120):
                    #break               
            except KeyboardInterrupt:
                os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                os.system("echo ########################################################################### >> ../log/log.txt")
                sys.exit()
            except:
                try:
                    print(f"Assigned tickets in this run {Tickets}")
                        #Tickets = []
                    print("         *All SR Assigned Redirecting to Incident Tickets*")
                    while True:
                        try:
                            browser.find_element(By.XPATH,HomeButton).click()
                            print('    [*]Clicked on HomeButton.')
                            time.sleep(2)
                            break
                        except:
                            print('    [*]HomeButton Error. Retrying')
                            continue
                    #break
                except:
                    browser.refresh()
                    print("[*ALL*_SR]page refresh")
                    continue
                #break
            
            TopTicketIndex = 1
            
        ##################################################################################################
                
            time.sleep(2)
            while True:
                num = 0
                try:
                    print("[*]Entering Incident section")
                    browser.find_element(By.XPATH,IncRadio).click()
                    time.sleep(2)
                except KeyboardInterrupt:
                    os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                    os.system("echo ########################################################################### >> ../log/log.txt")
                    sys.exit()
                except:
                    browser.refresh()
                    print("[IncRadio]page refresh.")
                    time.sleep(5)
                    continue
                    
                try:
                    b = browser.find_element(By.XPATH,IncUnassigned).click()
                    print("     [*]Entered Incident Unassigned Bucket")
                except KeyboardInterrupt:
                    os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                    os.system("echo ########################################################################### >> ../log/log.txt")
                    sys.exit()
                except:
                    browser.refresh()
                    print("[Unassigned]page refresh.")
                    time.sleep(5)
                    continue

                while True:
                    time.sleep(3)
                    try:
                        c = browser.find_element(By.XPATH,TopTicket).click()
                        print("         [*]Selected Top-Most Incident Ticket.")
                        time.sleep(2)
                        while True:
                            try:
                                d = browser.find_element(By.XPATH,AssignToSelf).click()
                                print(f"         {INC_num}) Incident Ticket assigned!")
                                INC_num = INC_num + 1
                                time.sleep(1)
                            except KeyboardInterrupt:
                                os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                                os.system("echo ########################################################################### >> ../log/log.txt")
                                sys.exit()
                            except:
                                #browser.refresh()
                                #print("[AssignToSelf_INC]page refresh")
                                #time.sleep(5)
                                #continue
                                #num = 1
                                #while True:
                                    #if(num == 3):
                                        #break
                                #browser.refresh()
                                #print("[AssignToSelf_SR]page refresh")
                                if (num == 10):
                                    browser2.refresh()
                                    print("[Dist][Done]Browser Refresh")
                                    time.sleep(3)
                                    break
                                print("Waiting for the ticket to Load.")
                                num = num + 1
                                time.sleep(1)
                                #time.sleep(5)
                                continue
                            try:           
                                alert = Alert(browser)
                                print("    [*] " + alert.text)
                                browser.switch_to.alert.accept()
                                print(f"    [*] Popup accepted")
                                num = 0
                                break
                            except KeyboardInterrupt:
                                os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                                os.system("echo ########################################################################### >> ../log/log.txt")
                                sys.exit()
                            except:
                                browser.refresh()
                                print("[popup_INC]page refresh")
                                time.sleep(3)
                                continue


                    except KeyboardInterrupt:
                        os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
                        os.system("echo ########################################################################### >> ../log/log.txt")
                        sys.exit()
                    except:
                        try:
                            print("         *All Incidents assigned Redirection to SR Tickets*")
                            print("-"*50)
                            time.sleep(1)
                            break
                        except:
                            browser.refresh()
                            continue
                    #break
                break
            
            #try:
            sleep = 1
            print(f"Sleeping for {sleep} seconds")
            time.sleep(sleep)
            break
        browser.find_element(By.XPATH,HomeButton).click()
        time.sleep(1)
        continue
except KeyboardInterrupt:
    #EnggName = UpdateEngineerName()
    print("Trying to log the keyinterrupt..")
    os.system(f"echo Logged out at {datetime.now().strftime('%b %d %Y %H:%M:%S')} >> ../log/log.txt")
    os.system("echo ########################################################################### >> ../log/log.txt")
    sys.exit()
    #os.system(f'{date} >> log.txt')
