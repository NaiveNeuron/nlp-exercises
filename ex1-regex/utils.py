import os
import pprint


def process_dir(data_path, process_file):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path, fname)
        f = open(path, 'r', encoding='ISO-8859-1')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list


def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path, 'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list


def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower())
                  for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower())
                 for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    # print 'Guesses (%d): ' % len(guess_set)
    # pp.pprint(guess_set)
    # print 'Gold (%d): ' % len(gold_set)
    # pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn)))


def evaluate(data_path, gold_path, process_file):
    guess_list = process_dir(data_path, process_file)
    gold_list = get_gold(gold_path)
    score(guess_list, gold_list)
