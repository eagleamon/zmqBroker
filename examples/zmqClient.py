import zmq, argparse

def main():
	ctx = zmq.Context()

	client = ctx.socket(zmq.SUB)
	client.setsockopt(zmq.SUBSCRIBE, '')
	client.connect(args.endpoint)

	print "Starting ..."
	while True:
		topic, msg = client.recv_multipart()
		print topic, msg

if __name__ == "__main__":
	parser = argparse.ArgumentParser(usage='zmqClient.py tcp://broker:10001')
	parser.add_argument('endpoint', action='store')
	args = parser.parse_args()
	main()
