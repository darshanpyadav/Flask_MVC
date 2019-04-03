from app import create_app
import argparse

parser = argparse.ArgumentParser(description="Run this file to start the server")
parser.add_argument("-p", "--port", help="set the port")
parser.add_argument("-e", "--env", help="set the run environment")

args = parser.parse_args()

port = args.port if args.port else 8000
env = args.env if args.env else "development"

# initiate app
app = create_app(env)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
