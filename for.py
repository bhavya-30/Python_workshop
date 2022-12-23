import time
import webbrowser
print("please enter something to search on google:")
#input is used to accept user data
x=input()
mylist=x.split()

#delay of 5 sec
time.sleep(1)
for i in mylist:
#let's print number
        print("user input is: ",i)
        #let's search on google
        webbrowser.open_new_tab("https://www.google.com/search?q="+i)