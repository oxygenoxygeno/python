def comments(filename):
    with open(filename) as f:
        for index, line in enumerate(f):
            if line.lstrip().startswith('#'):
                print('{}: {}'.format(index + 1, line.strip().lstrip('#')))


comments('bsoup_test.py')