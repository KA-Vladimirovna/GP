from sklearn.svm import OneClassSVM
import itertools
import glob
import re

def read_src(src):
    with open(src, 'r', encoding='utf-8') as r:
        src = r.readlines()
    return src

def get_features(src):
    def avg_line_len(src):
        avg_line_len = sum(len(line) for line in src) / len(src)
        return avg_line_len

    def func_to_len(src):
        tokens = [line.split(' ') for line in src]
        tokens = list(itertools.chain.from_iterable(tokens))
        src_text = ' '.join(src)
        func_to_len = src_text.count('def')/len(tokens)
        return func_to_len

    def comm_to_len(src):
        tokens = [line.split(' ') for line in src]
        tokens = list(itertools.chain.from_iterable(tokens))
        src_text = ' '.join(src)
        comms = len([re.search('#', src_text)])
        comm_to_len = comms/len(tokens)
        return comm_to_len

    features = {'avg_line_len': avg_line_len(src),
                'func_to_len': func_to_len(src),
                'comm_to_len': comm_to_len(src),
                }

    return features


def main():
    versus = []
    srcs = glob.glob('D:/Scripts/oneclass/ex/*.py')
    for src in srcs:
        src = read_src(src)
        features = get_features(src)
        versus.append(features)

    vs_values = [list(vs.values()) for vs in versus]
    for vec in zip(vs_values):
        vec = [[i] for i in list(vec)]
        clf = OneClassSVM(gamma='auto').fit(vec)
        print('vecs: ', clf.predict(vec))
        print('scores: ', clf.score_samples(vec))

if __name__ == '__main__':
    main()
