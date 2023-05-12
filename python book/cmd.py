#!python3

filename = "mytextfile.txt"
print("The file you want to read is called : " + filename)

python3 myscript.pt –filename myfile.txt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', required=True,
                  help='The filename you would like to have in your application')options = parser.parse_args()
args = parser.parse_args()

print("The file you selected was : " + args.filename)

#D:\tmp\python\test>python example1.py --filename /home/student/textfile.txt
#The file you selected was : /home/student/textfile.txt
#python3 myscript.py -f /etc/config/config.cfg
#python3 myscript.py -f /etc/config/config.cfg