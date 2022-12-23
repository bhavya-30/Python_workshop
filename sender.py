#sending data to another IP ADDRESS
import socket
#creating UDP socket method  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            #ip type v4,protocol type UDP
target_ip="172.16.27.146"
target_port=8182
'''only for receiver 
s.bind((target_ip,target_port))
while 3>2:
data=s.recvfrom(100)
print(data)
'''
print("enter msg to send: ")
msg=input()
new_msg=msg.encode()
#let's send data 
s.sendto(new_msg,(target_ip,target_port))


'''seperating data by reciver side
actual_data=data[0]
sender_add=data[1]
comman_msg="got it"
new_common_msg=common_msg.encode()
s.sendto(new_commom_msg,sender_add)
'''
print("waiting for responce")
my_responce=s.recvfrom(50)
print(my_responce)