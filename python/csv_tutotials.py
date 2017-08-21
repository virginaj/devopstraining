#!/usr/bin/python

import csv

csv_file = "N4xFilterTier1.csv"

def read_using_csv_module(input_file):
    with open(input_file) as csvfile:
        sp = csv.reader(csvfile, delimiter = ',')
        for row in sp:
            print(row)

def read_simple(input_file):
    with open(input_file) as csvfile:
        lines = csvfile.readlines()
        for line in lines:
            print(line.strip().split(','))

def write_simple(input_file,output_file):
    with open(input_file) as csvfile:
        lines = csvfile.readlines()
        for line in lines:
            print(line.strip().split(','))

    with open(output_file,'w') as csvfile:
        sp = csv.writer(csvfile, delimiter=',')
        for line in lines:
            sp.writerow(line.strip().split(','))

def read_modify_write(csv_file,'output.csv','Running'):
    with open(input_file) as csvfile:
        lines = csvfile.readlines()

    index=lines[0].find('Running')
    running = []
    for line in lines[1:]:
        running.append(float(line[index])*100)

    with open(output_file,'w') as csvfile:
        sp = csv.writer(csvfile, delimiter=',')
        for line in lines:
            sp.writerow(line.strip().split(','))

if __name__ == '__main__':
    #read_using_csv_module(csv_file)
    write_simple(csv_file,'output.csv')
    read_modify_write(csv_file,'output.csv','Running')