# -*- coding:UTF-8 -*-
"""
Filename:
Function:
Author:
Create:
"""
import os
import codecs

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def load_tfidf_file_2_dict(input_file):
    dict_tfidf = {}
    with codecs.open(input_file, "r", "utf-8") as fin:
        for line in fin:
            arr = line.strip().split(" ")
            if len(arr) == 3:
                fenci_iterm = arr[0].strip()
                tfidf = arr[-1].strip()
                dict_tfidf[fenci_iterm] = tfidf
    return dict_tfidf


def combine_fenci_and_tfidf_2_file():
    home_dir = os.environ["HOME"]
    fenci_file_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_fenCi_byClass")
    tfidf_file_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_tFiDf_byClass")
    output_file_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_fenci_tFiDf_byClass")

    fenCi_file_ls = os.listdir(fenci_file_dir)
    tfidf_file_ls = os.listdir(tfidf_file_dir)
    for tmp_file in fenCi_file_ls:  # 分词文件列表
        if tmp_file in tfidf_file_ls:
            tfidf_file = os.path.join(tfidf_file_dir, tmp_file)
            dict_tfidf = load_tfidf_file_2_dict(tfidf_file)
            with codecs.open(os.path.join(fenci_file_dir, tmp_file), "r", "utf-8") as fin, codecs.open(os.path.join(output_file_dir, tmp_file), "w", "utf-8") as fout:
                for line in fin:
                    arr = line.strip().split(" ")
                    for tmp in arr:
                        if tmp in dict_tfidf:
                            fout.write(tmp + " " + dict_tfidf[tmp] + "\n")


def main():
    print "start..."
    combine_fenci_and_tfidf_2_file()
    print "end..."

if __name__ == "__main__":
    main()