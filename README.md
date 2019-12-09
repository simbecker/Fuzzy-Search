# Fuzzy Search

Searches through one or more files for a string or its fuzzy match, making use of the fuzzwuzzy library.

## Dependencies
* python3.6
* colorama
* nltk
* fuzzywuzzy


## Installation
* Create virtual environment
* `pip3 install -r requirements.txt`

### Arguments
* -f: one or more files
* -t: the string to be searched
* -k (optional): show the k best results. Default is 5

Example usage:

Searching for a text in one file:
```
python3 fuzzy_search.py -f example1.txt -t "Boon Heong badminton"
```

Searching for a text across multiple files:
```
python3 fuzzy_search.py -f example1.txt example2.txt -t "Boon Heong badminton"
```

Printing only the best match:
```
python3 fuzzy_search.py -f example1.txt example2.txt -t "Boon Heong badminton" -k 1
```
