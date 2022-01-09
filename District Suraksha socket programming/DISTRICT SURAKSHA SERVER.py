import socket
import pandas as pd
import numpy as np
from _thread import *
df = pd.read_csv(r"problem.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
ThreadCount = 0
s.listen(10)
list1=[]
def threaded_client(est):
    while True:
        est.send(bytes("Enter Name : ", "utf-8"))
        Name = est.recv(1000).decode("utf-8")
        est.send(bytes("Enter Phone number:","utf-8"))
        Phone_No= est.recv(1000).decode("utf-8")
        Phone_No= int(Phone_No)
        est.send(bytes("Enter District : ", "utf-8"))
        District = est.recv(1000).decode("utf-8")
        est.send(bytes("Enter Pincode:","utf-8"))
        Pincode = est.recv(1000).decode("utf-8")
        Pincode= int(Pincode)
        est.send(bytes("Enter Region : ", "utf-8"))
        Area = est.recv(1000).decode("utf-8")
        est.send(bytes("Enter Problem : ", "utf-8"))
        Problem = est.recv(1000).decode("utf-8")
        list1 = [[Name,Phone_No,District,Pincode,Area,Problem]]
        df2 = pd.DataFrame(list1, columns=['Name','Phone_No','District','Pincode','Area','Problem'])
        df2.to_csv(r'problem.csv',mode='a',index=False,header=False)

         
    est.close()

    
    
while True:
    est, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (est, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))



