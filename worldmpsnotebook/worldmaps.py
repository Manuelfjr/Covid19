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
#a = False
#if a==True:
#    import confirmedworldmaps as cwm
#    cwm.confirmedmps(run=True)
#if a==False:
#    import deathsworldmaps as dwm
#    dwm.deathsmps(run=True,bool=False)

if __name__ == '__main__':
    args = parse_arguments()
    if vars(args)['type'] == 'cwm':
        import confirmedworldmaps as cwm
        cwm.confirmedmps(**vars(args))
    else:
        if vars(args)['type'] == 'dwm':
            import deathsworldmaps as dwm
            dwm.deathsmps(**vars(args))
        else:
            if vars(args)['type'] == 'rwm':
                import recoveredworldmaps as rwm
                rwm.recoveredmps(**vars(args))
