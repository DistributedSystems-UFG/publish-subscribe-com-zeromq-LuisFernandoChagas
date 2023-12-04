import zmq
from constPS import * #-

context = zmq.Context()
s1 = context.socket(zmq.SUB)          # create a subscriber socket
p1 = "tcp://"+ HOST1 +":"+ PORT        # how and where to communicate
s1.connect(p1)                         # connect to the server
s1.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

for i in range(5):  # Five iterations
	time = s.recv()   # receive a message
	print (bytes.decode(time))
