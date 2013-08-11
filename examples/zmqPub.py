import zmq, time, json, random, argparse
from datetime import datetime

def main():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.connect(args.endpoint)
    r=random.Random()
    while True:
        a=datetime.now()
        val = dict(unit='J/K', value=r.random()*100, time=str(datetime.now()))
        pub.send_multipart(["status/World/Entropy", json.dumps(val)])
        print "Sending %s"%val
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage='zmqPub.py tcp://broker:10000')
    parser.add_argument('endpoint', action='store')
    args=parser.parse_args()
    main()
