import sys
from argparse import ArgumentParser
i = None
m = None
l = None
mx = None
output = None
def gen_with_range():
    with open(output, 'a') as file:
        for n in range(l, mx + 1):
            for x in range(i, m + 1):
                buf = '%{}.0f\n'.format(n)%x
                buf = buf.replace(' ', '0')
                log('\rWriting word %s'%buf.rstrip())
                file.write(buf)
def gendefault():
    with open(output, 'a') as file:
        for n in range(i, m + 1):
            buf = '%{}.0f\n'.format(l)%n
            buf = buf.replace(' ', '0')
            log('\rWriting word %s'%buf.rstrip())
            file.write(buf)
def log(str):
    sys.stdout.write(str)
    sys.stdout.flush()
def get_parser():
    parser = ArgumentParser(prog='Gerador de senhas numéricas')
    parser.add_argument('-i', '--initial', required=True, dest='min', type=int, help='O valor inicial da senha numérica.')
    parser.add_argument('-m', '--max', required=True, dest='max', type=int, help='O valor máximo do número.')
    parser.add_argument('-l', '--length', required=True, type=int, dest='len', help='O tamanho mínimo da senha.')
    parser.add_argument('-mx', '--max-length', type=int, dest='maxlen', help='O tamanho máximo da senha.')
    parser.add_argument('-o', '--output', dest='out', help='O arquivo de saída da worlist')
    return parser
def main():
    global i, m, l, mx, output
    parser = get_parser()
    if not len(sys.argv[1:]):
        sys.exit(parser.print_help())
    args = parser.parse_args()
    i = args.min
    m = args.max
    l = args.len
    mx = args.maxlen
    output = args.out or 'wordlist.txt'
    if mx is None:
        gendefault()
    else:
        gen_with_range()
if __name__ == '__main__':
    main()