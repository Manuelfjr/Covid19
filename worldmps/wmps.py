import argparse as argparse
import sys as sys

modules = 'argparse'.split(' ')

install, k = [], 0
for i in modules:
    if (i in sys.modules ) == False:
        install.append(i)
        print(install[k])
        k+=1

if len(install) >= 1:
    print('----------------------------------------------------------')
    for i in range(len(install)):
        print('Suggestion :' + '\n' + 'pip install {}'.format(install[i]))
        print()
    sys.exit()

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--run', dest='run',
                        type=bool,
                        default=True,
                        help='''run maps''')
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='20/6/20',
                        help='''date maps''')
    parser.add_argument('-f', '--folder', dest='folder',
                        type=str,
                        default='dataworld',
                        help='''folder name''')
    parser.add_argument('-t', '--type', dest='type',
                        type=str,
                        default='cwm',
                        help='''type (confirmed,deaths,recovered) ''')
    parser.add_argument('-a', '--all', dest='all',
                        type=bool,
                        default=False,
                        help='''boolean value''')
    return parser.parse_args()

def wmps(parse_arguments):
    if parse_arguments['all'] == True:
        from cwm import cwm
        from dwm import dwm
        from rwm import rwm
        cwm(**parse_arguments)
        dwm(**parse_arguments)
        rwm(**parse_arguments)
    elif parse_arguments['all'] == False:
        if parse_arguments['type'] == 'cwm':
            from cwm import cwm
            cwm(**parse_arguments)
        else:
            if parse_arguments['type'] == 'dwm':
                from dwm import dwm
                dwm(**parse_arguments)
            else:
                if parse_arguments['type'] == 'rwm':
                    import rwm as rwm
                    rwm.rwm(**parse_arguments)

if __name__ == '__main__':
    args = parse_arguments()
    wmps(vars(args))
