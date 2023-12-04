import zmq, time
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(3)                    # wait every 5 seconds
	msg = str.encode("Publisher_2 - time " + time.asctime())
	s.send(msg) # publish the current time
