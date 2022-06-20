with open('INPUT.TXT') as f_in:
    print(sum(1 for x in f_in.readlines() if x.strip().startswith('#')))