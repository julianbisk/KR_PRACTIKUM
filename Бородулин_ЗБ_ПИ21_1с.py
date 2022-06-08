def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n-1))


def filter_even(numbers):
    return list(filter(lambda x: (x % 2 == 0), numbers))


def square(li):
    return list(map(lambda x: x ** 2, li))


def bin_search(li, element):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = li[mid]
        if guess == element:
            return mid
        elif guess > element: 
            high = mid - 1
        else:
            low = mid + 1
    return None 


def is_palindrome(string):
    string1 = ''
    string = string.lower()
    wrong_symbols = [',', '.', '-', ' ', '?', '!', '_', "'"]
    for symbol in wrong_symbols:
        string = string.replace(symbol, '')
    print(string)
    for i in range(len(string) - 1, -1, -1):
        string1 += string[i]
    if string == string1:
        return 'YES'
    else:
        return 'NO'


def calculate(path2file):
    file = open(path2file, "r")

    line = file.readline()
    string = ""

    while line:
        if (len(string) != 0):
            string += ","
        
        value = line.split("    ").replace("\n", "")

        if value[0] == '+':
            string += str(int(value[1]) + int(value[2]))
        elif value[0] == '-':
            string += str(int(value[1]) - int(value[2]))
        elif value[0] == '*':
            string += str(int(value[1]) * int(value[2]))
        elif value[0] == '//':
            string += str(int(value[1]) // int(value[2]))
        elif value[0] == '%':
            string += str(int(value[1]) % int(value[2]))
        elif value[0] == '**':
            string += str(int(value[1]) ** int(value[2]))
        
        line = file.readline()

    return string


def substring_slice(path2file_1,path2file_2):
    file1 = open(path2file_1, "r")
    file2 = open(path2file_2, "r")

    line1 = file1.readline()
    line2 = file2.readline()
    string = ""

    while line1:
        if (len(string) != 0):
            string += " "

        s = line2.replace("\n", "").split(" ")

        string += line1[int(s[0]):int(s[1])+1]

        line1 = file1.readline()
        line2 = file2.readline()

    return string


import json
import re

def decode_ch(srting_of_elements):
    periodic_table = json.load(open('periodic_table.json'))
    string = ""
    sliced = re.findall('[A-Z][a-z]*', srting_of_elements)

    for s in sliced:
        string += periodic_table[s]

    return string


class Student:

    def __init__(self,
                 name,
                 surname,):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = [3, 4, 5]

    def greeting(self):
        print(f"Hello, I am Student")

    def mean_grade(self):
        sum = 0
        for g in self.grades:
            sum += g
        return sum/len(self.grades)

    def is_otlichnik(self):
        sr = self.mean_grade()
        if (sr >= 4.5):
            return "YES"
        else:
            return "NO"
    
    def __add__(self,
                  other):
        return self.name + 'is friend with ' + other.name

    def __str__(self):
        return self.fullname



class MyError(Exception):
  def __init__(self, msg):
    self.msg = msg