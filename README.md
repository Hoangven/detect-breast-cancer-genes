# Detect Breast Cancer Genes
A simple Python script to detect and report breast cancer-associated genes and their aliases.

# How it works
* Provided with a file containing 8159 known human cancer genes, the script searches for breast cancer related terms in the gene description with a regular expression.
* Matching genes and aliases are returned to the console.
* Aliases for genes and number of alias occurrences are plotted.

To use a custom file, make sure it matches the tab-separated format of the file included to this repository.

# Getting started
### Running in an environment
It's recommended to run the script in a contained Conda environment to ensure the installation of all dependencies, the required steps are listed below:

#### Install Miniconda
`$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`

`$ bash Miniconda3-latest-Linux-x86_64.sh`
#### Create and activate the environment
`$ conda env create --name {environment-name} --file environment.yml`

`$ source activate {environment-name}`
#### Run the script
`$ python detect_breast_cancer_genes.py`

`$ source deactivate`

### Running stand-alone
Alternatively, to run the script as a stand-alone, make sure the following dependencies are included:
* Python version 3
* Pip
* Matplotlib

# Examples
**1 - Console output returns breast cancer-associated genes and their aliases.**

![Console output](https://user-images.githubusercontent.com/24732704/41819408-62bb9f3e-77c0-11e8-83ac-3eaee91ebef1.png)

**2 - Chart plots number of aliases per breast cancer-associated gene.**

![1st chart](https://user-images.githubusercontent.com/24732704/41819286-26b2cdd4-77be-11e8-84c5-efa358e119d0.png)

**3 - Chart plots number of occurrences of aliases.**

![2nd chart](https://user-images.githubusercontent.com/24732704/41819287-26cb28f2-77be-11e8-919d-4e6e55dcf19f.png)
