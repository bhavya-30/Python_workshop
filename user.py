import time
import webbrowser
print("please enter something:")
#input is used to accept user data
x=input()
#delay of 5 sec
time.sleep(5)
#let's print number
print("user input is: ",x)
#checking data type
y=12
t1=type(y)
print(t1)
#let's search on google
webbrowser.open_new_tab("https://www.google.com/search?q="+x)