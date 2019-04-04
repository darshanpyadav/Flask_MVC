import argparse

parser = argparse.ArgumentParser(description="Just display the SB_HOST and MOUNT_HOST")
required = parser.add_argument_group('required arguments')
required.add_argument("--SB_PATH", help="SB path", required=True)
required.add_argument("--HOST", help="Mount host", required=True)
required.add_argument("--GEO", help="Geo on which the tool was invoked", required=True)

args = parser.parse_args()

print("hello world!")

