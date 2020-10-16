# Resolve the problem!!
import re

def run():
    with open('encoded.txt','r', encoding='utf-8') as f:
        txt = f.read()
        print(re.findall('[a-z]',txt))


if __name__ == '__main__':
    run()
