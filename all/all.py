import argparse as argparse
from brazilcode import brazilcode
from graphics import graphics
from covid19 import covid19
def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-all', '--all', dest='all',
                        type=bool,
                        default=True,
                        help='''run all''')
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='6/11/20',
                        help='''date maps''')
    parser.add_argument('-dbr', '--datebr', dest='datebr',
                        type=str,
                        default='11/6',
                        help='''date maps''')
    parser.add_argument('-dys', '--days', dest='days',
                        type=int,
                        default=30,
                        help='''countries number ''')
    parser.add_argument('-w', '--weeks', dest='weeks',
                        type=int,
                        default=5,
                        help='''today ''')
    parser.add_argument('-nw', '--n_weeks', dest='n_weeks',
                        type=int,
                        default=14,
                        help='''number weeks ''')
    parser.add_argument('-nc', '--numcountries', dest='nc',
                        type=int,
                        default=6,
                        help='''countries number ''')
    parser.add_argument('-n', '--numstates', dest='n',
                        type=int,
                        default=10,
                        help='''states number ''')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    param = vars(args)
    if param['all'] == True:
        graphics(date=param['date'],nc=param['nc'])
        brazilcode(datebr=param['datebr'], days=param['days'], weeks=param['weeks'], n_weeks=param['n_weeks'], n=param['n'])
        covid19(date=param['date'],nc=param['nc'])
