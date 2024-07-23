from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--basic', help='Basic argument',
                    type=str, metavar='STRING')
args = parser.parse_args()
print(args.basic)

if args.basic is None:
    print('No argument provided')
else:
    print('Argument provided')
