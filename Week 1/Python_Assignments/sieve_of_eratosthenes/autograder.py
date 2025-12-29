import os

with open('testcases.txt','r',encoding='utf-8') as f:
    
    for line in f:
        num = int(line)
        os.system(f'wsl timeout 1s python.exe sieve_of_eratosthenes.py {num} > out.txt') # using the timeout from wsl as windows doesnt have a similar command natively
        f1 = open(f'out.txt','r',encoding='utf-8')
        f2 = open(f'expected_outputs/{num}.txt','r',encoding='utf-8')
        if f1.readlines() == f2.readlines():
            print(f'Testcase {num} Passed')
        else:
            print(f'Testcase {num} Failed or Time Limit Exceeded')
        # wsl doesnt have permission to remove files on windows apparently, so reomved the file removed statement
