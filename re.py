from pprint import pprint
import re

def read_result():
    file = open('result_counters.txt', 'r')
    result = {}
    host = ''
    command = ''
    for line in file:
        # line = line.split("|")
        if (re.search(r'^\[\/\]$', line) or 
        re.search(r'.*# $', line) or    
        re.search(r'^ \w', line) or     
        re.search(r'^ $', line) or      
        len(line)==1
        ):
            ''
        else:
            match = re.search(r':.*# ', line)
            if match:
                host = match[0]
                command = line[match.end():-1]
            if result.get(host, 'хуй') == 'хуй' and host != '':
                result.update({host:{command:''}})
            elif result.get(host, 'хуй') != 'хуй' and result[host].get(command, 'хуй') == 'хуй':
                result[host].update({command:''})
            elif command != '' and host != '':
                result[host][command] = result[host][command] + line
    final_result = {}
    for w in result:
        # pprint(w)
        final_result.update({str(w):{}})
        for line in result.get(w).items():
            match = re.search(r'^\s+\^', line[1])
            LSP0 = re.search(r'(LSP)', line[0])
            LSP1 = re.finditer(r'(LSP[A-Za-z0-9 :_-]+\n[A-Za-z :]+)\d+([A-Za-z :]+)\d+', line[1])
            if match or line[1] == '':
                ''
            elif LSP0 and LSP1:
                kk = ''
                for each in LSP1:
                    kk = kk + each[0] + '\n'
                final_result[w].update({line[0]:kk})
            else:
                final_result[w].update({line[0]:line[1]})

    for w in final_result:
        pprint(w)
        for z in final_result.get(w).items():
            print(z[0])
            print(z[1])
    return final_result

k = read_result()