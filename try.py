from scapy.all import *

myip = '172.16.44.5'
dst = '172.16.44.1'
payload = Raw('172.16.44.5')

ip = IP(src = '172.16.44.5',dst = '172.16.44.1')

SYN1 = TCP(dport = 13337, flags = "S",seq = 1234)
for i in range(1000):
    SYNACK = sr1(ip/SYN1)
    my_ack = SYNACK.seq +1
    print(my_ack-1,hex(my_ack-1))
    ACK = TCP(flags = 'A',seq = 1235, ack = my_ack ,dport = 13337 )
    send(ip/ACK/payload)






