#using module for using ping
import os,time
print("enter the valid IP address: ")
target_ip=input()
print(os.system('ping  '+target_ip))

#testing modulus by listing function
'''for i in dir(os):
    if 'sys' in i:
        print(i)
        time.sleep(1)'''

