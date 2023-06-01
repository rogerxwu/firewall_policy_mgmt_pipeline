import argparse




parser = argparse.ArgumentParser(description='Test')
parser.add_argument('-username')
parser.add_argument('-password')
args = parser.parse_args()


print(args.username)
print(args.password)
