# Fuzzy Search

Searches through one or more files for a string or its fuzzy match.

## Dependencies
* python3.6
* colorama
* nltk
* fuzzywuzzy


## Installation
* Create virtual environment
* `pip3 install -r requirements.txt`

Example usage:

Searching for a text in one files:
```
python3 python3 fuzzy_search.py -f example1.txt -t "Boon Heong badminton"
```

Searching for a text across multiple files:
```
python3 python3 fuzzy_search.py -f example1.txt example2.txt -t "Boon Heong badminton"
```

Printing only the best match:

```
python3 python3 fuzzy_search.py -f example1.txt example2.txt -t "Boon Heong badminton" -k 1
```