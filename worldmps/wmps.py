import argparse as argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--run', dest='run',
                        type=bool,
                        default=True,
                        help='''run maps''')
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='6/10/20',
                        help='''date maps''')
    parser.add_argument('-b', '--bool', dest='bool',
                        type=bool,
                        default=False,
                        help='''boolean value''')
    parser.add_argument('-f', '--folder', dest='folder',
                        type=str,
                        default='dataworldr',
                        help='''folder name''')
    parser.add_argument('-n', '--filename', dest='filename',
                        type=str,
                        default='confirmed.csv',
                        help='''file name ''')
    parser.add_argument('-t', '--type', dest='type',
                        type=str,
                        default='cwm',
                        help='''type (confirmed,deaths,recovered) ''')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    if vars(args)['type'] == 'cwm':
        from cwm import cwm
        cwm(**vars(args))
    else:
        if vars(args)['type'] == 'dwm':
            from dwm import dwm
            dwm(**vars(args))
        else:
            if vars(args)['type'] == 'rwm':
                from rwm import rwm
                rwm(**vars(args))
