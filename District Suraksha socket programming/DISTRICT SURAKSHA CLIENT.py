import socket
import pandas as pd
import numpy as np
df = pd.read_csv(r"problem.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
Name = input(s.recv(1000).decode("utf-8"))
s.send(Name.encode("utf-8"))
Phone_No = int(input(s.recv(1000).decode("utf-8")))
s.send(str(Phone_No).encode("utf-8"))
District= str(input(s.recv(1000).decode("utf-8")))
s.send(District.encode("utf-8"))
Pincode = int(input(s.recv(1000).decode("utf-8")))
s.send(str(Pincode).encode("utf-8"))
Area = str(input(s.recv(1000).decode("utf-8")))
s.send(Area.encode("utf-8"))
Problem = str(input(s.recv(1000).decode("utf-8")))
s.send(Problem.encode("utf-8"))
print(Name)
print(Phone_No)
print("Thanks for registering your problems....")
s.close()

