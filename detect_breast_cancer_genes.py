'''
AUTHOR: Koen Rademaker
FILE: detect_breast_cancer_genes.py
VERSION: 0.1
DATE: 10/feb/2018
FUNCTION: Detect human genes and aliases associated with breast cancer from the complete list of human cancer genes (n = 8159)
'''
import matplotlib.pyplot as plt
import re

# Terms can be expanded to widen search
regular_expression_terms = ['breast cancer', 'breast carcinoma', 'ductal carcinoma']
# File has to be ordered by columns 'Symbol', 'Description', 'Chromosome', 'Aliases'
file_location = 'human_cancer_genes.txt'

# Loads and processes list of human cancer genes from .txt file, returns instance data as dictionary
def read_file(file_location):
    try:
        data_file = open(file_location, 'rt')
        data_file_lines = data_file.readlines()
        data_dictionary = {}
        for instance in data_file_lines:
            instance = instance.strip()
            if instance != 'Symbol\tDescription\tChromosome\tAliases':
                line = instance.split('\t')
                try:
                    instance_symbol = line[0]
                    instance_description = line[1]
                    instance_chromosome = line[2]
                    instance_alias = line[3]
                    data_dictionary.update({instance_symbol:[instance_description,instance_chromosome,instance_alias]})
                except IndexError:
                    instance_alias = None
                    data_dictionary.update({instance_symbol:[instance_description,instance_chromosome,instance_alias]})
        return data_dictionary
    except FileNotFoundError:
        print('ERROR: FILE NOT FOUND, CHECK THE FILE LOCATION')

# Searches human cancer genes for matches with breast cancer terms, returns symbol and aliases for matching genes as dictionary   
def search(data_dictionary):
    result_dictionary = {}
    for instance_symbol in data_dictionary.keys():
        instance_values = data_dictionary.get(instance_symbol)
        instance_description = str.lower(instance_values[0])
        for re_term in regular_expression_terms:
            re_search = re.search(re_term, instance_description)
            if(re_search != None):
                instance_alias = instance_values[2]
                result_dictionary.update({instance_symbol:instance_alias})
    return result_dictionary

# Prints aliases for all genes matching breast cancer terms
def generate_output(result_dictionary):
    print('----------OUTPUT OF BREAST CANCER GENES----------')
    for instance_symbol in result_dictionary.keys():
        print('Gene:\t',instance_symbol,'\nAliases:',result_dictionary.get(instance_symbol),'\n')
    print('-------------------------------------------------')
   
# Gathers data, visualizes the number of aliases for breast cancer genes and the number of occurrences per alias in pie charts.
def visualize(result_dictionary):
    chart_1_labels = []
    chart_1_values = []
    for instance_symbol in result_dictionary.keys():
        if isinstance(result_dictionary.get(instance_symbol),str):
            number_of_aliases = len(result_dictionary.get(instance_symbol).split(','))
            chart_1_labels.append(instance_symbol)
            chart_1_values.append(number_of_aliases)
    fig1, ax1 = plt.subplots(figsize=(6,6))
    ax1.pie(chart_1_values, labels=chart_1_labels, autopct=make_autopct(chart_1_values), startangle=90)
    ax1.axis('equal')
    plt.title('Figure 1 - Number of aliases for breast cancer-associated genes', y=1.1)
    fig1.savefig('Figure 1.svg', bbox_inches='tight')
    
    chart_2_labels = []
    chart_2_values = []
    for instance_symbol in result_dictionary.keys():
        if isinstance(result_dictionary.get(instance_symbol),str):
            number_of_aliases = str(len(result_dictionary.get(instance_symbol).split(',')))
            if number_of_aliases not in chart_2_labels:
                chart_2_labels.append(number_of_aliases)
        if result_dictionary.get(instance_symbol) is None:
            if '0' not in chart_2_labels:
                chart_2_labels.append('0')
    chart_2_labels.sort(key=int)
    for label in chart_2_labels:
        count = 0
        for instance_symbol in result_dictionary.keys():
            if label is not 'None':
                if isinstance(result_dictionary.get(instance_symbol),str):
                    number_of_aliases = str(len(result_dictionary.get(instance_symbol).split(',')))
                    if number_of_aliases == label:
                        count += 1
            if label is '0':
                if result_dictionary.get(instance_symbol) is None:
                    count += 1
        chart_2_values.append(count)
    chart_2_labels = [label+' aliases' for label in chart_2_labels]
    fig2, ax2 = plt.subplots(figsize=(6,6))
    ax2.pie(chart_2_values, labels=chart_2_labels, autopct=make_autopct(chart_2_values), startangle=90)
    ax2.axis('equal')
    plt.title('Figure 2 - Number of occurrences of aliases for breast cancer-associated genes', y=1.1)
    fig2.savefig('Figure 2.svg', bbox_inches='tight')
    
# Generates text to visualize inside a pie chart
def make_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v}'.format(v=val)
    return autopct

# Runs all functions, handle exceptions when necessary
def main():
    human_cancer_genes = read_file(file_location)
    try:
        human_breast_cancer_genes = search(human_cancer_genes)
        generate_output(human_breast_cancer_genes)
        visualize(human_breast_cancer_genes)
    except AttributeError:
        print('ERROR: SEARCHING FILE FAILED, CHECK THE FILE LOCATION')
        
main()
