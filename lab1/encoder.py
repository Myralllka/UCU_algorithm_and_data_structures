def enc(filename):
    newf = open('result.txt', 'w+', encoding='UTF-8')
    with open(filename) as ff:
        type_ = 'shell_sort'
        l = ['selection_sort', 'insertion_sort']
        for line in ff.readlines():
            if '*' in line:
                type_ = l.pop()
            line = line \
                .replace('[', '') \
                .replace(']', '') \
                .replace(',', '') \
                .replace('\'', '') \
                .replace('\n', '') \
                .split(' ')
            i = 1
            line1 = 'random'
            average_time = 0.0
            average_count = 0.0

            while True:
                if i == len(line):
                    break
                if line[i] in ['random', '1-3', 'backsorted', 'sorted']:
                    print(filename[4:].replace('e', '^'), line1, type_,
                          average_time /
                          10,
                          average_count / 10, sep=',')
                    average_time = .0
                    average_count = .0
                    line1 = line[i]
                    newf.write(str(line[i]) + '\n')
                    i += 1
                    continue
                else:
                    average_time += float(line[i])
                    i += 1
                    average_count += float(line[i])
                    i += 1
            print(filename[4:].replace('e', '^'), line1, type_, average_time
                  /10, average_count / 10, sep=',')

    newf.close()


for i in range(7, 21):
    fn = 'test2e{}'.format(i)
    enc(fn)
