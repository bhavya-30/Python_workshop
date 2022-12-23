'''only for receiver 
s.bind((target_ip,target_port))
while 3>2:
data=s.recvfrom(100)
print(data)
'''
'''seperating data by reciver side
actual_data=data[0]
sender_add=data[1]
comman_msg="got it"
new_common_msg=common_msg.encode()
s.sendto(new_commom_msg,sender_add)
'''
#lets implement logging 
# f=open(sender_addr[0]+'.text','w+')
#data decode
# data_newrec=actual_data.decode()
#  f.write(data_newrec)
#f.close