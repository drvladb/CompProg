import subprocess
import sys

f = open("input.txt", "r")
inputs = f.read().split("\n---\n")
f.close()

for i, testcase in enumerate(inputs):
    command = [sys.executable, 'solution.py']
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate(input=testcase.encode())[0]
    print(output.decode())
