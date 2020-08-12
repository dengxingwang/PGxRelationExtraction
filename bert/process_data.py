f_w = open("C:\lab_work\梅雨\\test.tsv",'w',encoding='utf-8')
with open("C:\lab_work\梅雨\\example.test",'r',encoding='utf-8') as f:
    for line in f.readlines():
        if not line.split():
            continue

        token = line.split()[0]
        flag = line.split()[1]
        flag = flag[0]
        f_w.write(token + '\t' + flag)
        f_w.write("\n")


