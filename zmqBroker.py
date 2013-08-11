import zmq, argparse

def main():
	ctx = zmq.Context()

	frontend = ctx.socket(zmq.SUB)
	frontend.bind("tcp://*:%d" % args.sub_port)

	backend = ctx.socket(zmq.PUB)
	backend.bind("tcp://*:%d" % args.pub_port)

	frontend.setsockopt(zmq.SUBSCRIBE, '')

	try:
		zmq.device(zmq.FORWARDER, frontend, backend)
	except KeyboardInterrupt:
		# When all is said..
		frontend.close()
		backend.close()
		ctx.term()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Simple broker like solution based on ZMQ')
	parser.add_argument('-sp', help='sub_port', dest='sub_port', default=10000, type=int)
	parser.add_argument('-pp', help='pub_port', dest='pub_port', default=10001, type=int)
	args = parser.parse_args()
	main()