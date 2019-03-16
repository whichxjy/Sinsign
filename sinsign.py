# -*- coding: utf-8 -*-

import argparse
import random
import collections

START = "Y2Cf4cho7EZpsY8kWU8Gl2TkOhuRH3wPKJYgPEPV"
END = "z328j9c8C1ChB3DKuCxTy1HrBEj1kU3fPN29JIsD"

def main():
    parser = argparse.ArgumentParser('Text generator')
    parser.add_argument('-f', '--file', type=str, help='File name of training text')
    parser.add_argument('-l', '--length', type=int, default=4, help='Number of sentences to return')
    args = parser.parse_args()

    model = train_model(args.file)
    for sentence in generate(model, args.length):
        sentence[0] = sentence[0].capitalize()
        for word in sentence:
            print(word, end=' ')
        print()

def train_model(filename):
    """Construct the model"""
    model = collections.defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.lower().split()
            for i, word in enumerate(line):
                if i == len(line) - 1:
                    model[END] += [word]
                else:
                    if i == 0:
                        model[START] += [word]
                    model[word] += [line[i + 1]]
    return model

def generate(model, length):
    """Generate sentences"""
    for i in range(length):
        generated = []
        words = []
        while True:
            if not generated:
                words = model[START]
            elif generated[-1] in model[END]:
                break
            else:
                words = model[generated[-1]]
            generated.append(random.choice(words))
        yield generated

if __name__ == "__main__":
    main()
