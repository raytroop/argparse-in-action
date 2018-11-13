import argparse

def parse_args(args):
    """ Parse the arguments.
    arguments:
        args: list or None
    """
    parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
    parser.add_argument("--backbone", default='resnet50', type=str,
                    help="which fold to train")
    parser.add_argument("--bz", default=8, type=int,
                    help="batch size")
    parser.add_argument('--train', dest='debug', action='store_false',
                            help='Train network | True by default')
    parser.add_argument('--debug', dest='debug', action='store_true',
                            help='Debug network | False by default')
    parser.set_defaults(debug=False)

    # args - List of strings to parse. The default is taken from sys.argv.
    return parser.parse_args(args=args)


def run(args=None):
    args = parse_args(args)

    # pass args to below code
    print('backbone : {}'.format(args.backbone))
    print('batch size : {}'.format(args.bz))
    if args.debug:
        print('debug phase')
    else:
        print('train phase')

if __name__ == '__main__':
    run()
