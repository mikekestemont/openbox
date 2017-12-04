#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

class DataIterator(object):

    def __init__(self, settings):
        super(DataIterator, self).__init__()
        self.s = settings

    def __iter__(self):
        exp = self.s.data_dir + os.sep + '*.' + self.s.extension
        nb_yielded = 0
        for fn in glob.glob(exp):
            for line in open(fn, 'r'):
                line = line.strip()
                if line:
                    nb_yielded += 1
                    if self.s.max_words and nb_yielded > nb_yielded:
                        break
                    comp = line.strip()
                    if len(comp) == 3:
                        yield comp


class Vectorizer(object):

    def __init__(self, settings):
        super(Vectorizer, self).__init__()
        self.s = settings

    def fit(self):
        for line in DataIterator(self.s):
            print(line)

        return self.s








