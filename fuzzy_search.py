from colorama import init, deinit, Fore
import nltk
from fuzzywuzzy import fuzz
import argparse
from collections import defaultdict


def preprocess(filepath):
    with open(filepath, "r") as f:
        raw_text = f.read()
    raw_sentences = nltk.sent_tokenize(raw_text)
    sentences = []
    for sent in raw_sentences:
        sentences.append({
            "file": filepath,
            "text": sent
        })
    return sentences


def colorful_output(target, sentences):
    target_words = set(target.split())
    file2sentence = defaultdict(list)

    for sent in sentences:
        file2sentence[sent["file"]].append(sent)

    for filename in file2sentence:
        print(filename)
        print()
        for i, sent in enumerate(file2sentence[filename]):
            print(str(i + 1) + ")", end='', flush=True)
            for word in sent["text"].split():
                if word in target_words:
                    print(" " + Fore.RED + word, end='', flush=True)
                else:
                    print(" " + word, end='', flush=True)
            print()
        print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, nargs='+')
    parser.add_argument('-k', type=int, default=5)
    parser.add_argument('-t', type=str)
    args = parser.parse_args()

    print(f"Searching for '{args.t}'...\n")

    target_sentence = args.t
    sentences = []
    for filepath in args.f:
        sentences.extend(preprocess(filepath))

    for sent in sentences:
        sent["ratio"] = fuzz.token_set_ratio(target_sentence, sent["text"])

    sorted_sentences = sorted(sentences, key=lambda s: -s["ratio"])[:args.k]
    colorful_output(target_sentence, sorted_sentences)

if __name__ == "__main__":
    init(autoreset=True)
    main()
    deinit()
