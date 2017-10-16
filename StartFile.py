import math

import MaxModule
x = MaxModule.tinyfunction(2)

print("Hello")

ivar = [1,3,5]


print("Hello, World")

x = [3,2]
print(x)

str(3.2)

mytuple = (3,4)
mylist = [1,"2",mytuple]
print(mylist)

print(mylist==[1,'2',(3,4)])

y = "Meaning of Life, Universe, and Everthing"
x = 42
print(y,x)

len(y)

help(round)
#dir() tells you what you have in record

for miles in range(10,70,10):
        km= miles * 1.609
        print("%d miles --> %3.2f kilometers" % (miles,km))

mylist = ['spam','lovely','spam','glorious','spam']
set(mylist)

zed = "lower case spring"
zed.upper()

shopping_list = ['eggs','bacon','spam']
shopping_list.append('butter')

countdown = 10
while countdown:
        print countdown,
        countdown -= 1
print ("blastoff")

user_input = input("Enter an Integer: ")
try:
        number = int(user_input)
        print("You entered",number)
except ValueError:
        print("Integers please")

def myfunction(x):
        y=x**x
        print(x, "raised to the power ",x," is ",y)
        return y

class SayMyName:
        def __init__(self,myname):
                self.myname=myname
        def say(self):
                print("Hello, my name is",self.myname)

name1 = SayMyName("Aahz")


import sys
import urllib
import urllib.parse
import html.parser
from cStringIO import StringIO

def log_stdout(msg):
        """Print Message to Screen"""
        print(msg)

def get_pag(url,log):
        """Retrieve URL and return contents"""
        try:
                page=urllib.urlopen(url)
        except urllib.URLError
                log("Error Retrieving"+url)
        return('')
        body=page.read()
        page.close()
        return(body)

class Spider:

        """
        The heart of this program, finds all links within a website

        run() contains the main loop
        process_page() retrieves each page and finds the links

        """
        def __init__(self,startURL, log=None):
                #This method sets initial values
                self.URLs = set()
                self.URLs.add(startURL)
                self.include = startURL
                self._links_to_process = [startURL]
                if log is None:
                        self.log =log_stdout
                else:
                     self.log = log

                def run(self):
                        #Process list of URLs one at a time
                        while self._links_to_process:
                                url = self._links_to_process.pop()
                                self.log("Retrieving:"+url)
                                self.process_page(url)


if __name__ == '__main__':
        #This code runs if started from command line
        startURL = sys.argv[1]
        spider = Spider(startURL)
        spider.run()
        for URL in sorted(spider.URLs):
                print(URL)


##Execute from command line - /Users/Max/startfile.py(1)<module>() (1) - first line of program.
# Press s for step. Press p for see values

### debugger
print("This function makes a list")
def makelist():
    a = []
    for i in range(1,20):
        a.append(i)
        print("appending", i,":",a)


print("%2s %5s %12s" % ('x','x**2','x**x'))
print("="*21)
for x in range(1,6):
    print("%2s %5s %12s" % (x,x**2,x**x))


for n in range(1,6):
    nn = str(n**2)
    nnn = str(n**n)
    print(n, nn.rjust(4), nnn.rjust(6))

import locale
x = locale.getdefaultlocale()
print(x)
