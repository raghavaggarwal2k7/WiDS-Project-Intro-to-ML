import os

if (os.system(f'python time.py > out.txt'))==0: # changed python3 to python becuase that is what is in my PATH
    if (os.system(f'diff -w out.txt expected_output.txt'))==0:
        print("Test case passed")
    else:
        print("Test case failed")
        print("Above shows the mismatches")
    
else:
    print("Check for syntax errors or any other errors")

os.system(f'rm out.txt')