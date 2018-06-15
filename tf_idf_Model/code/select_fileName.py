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


def re_fileName():
    home_dir = os.environ["HOME"]
    input_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_tFiDf_byClass")
    renamed_file = os.path.join(home_dir, "file_id_result.txt")
    output_file = os.path.join(home_dir, "missing.txt")
    file_ls = os.listdir(input_dir)
    # file_ls = [unicode(tmp_file) for tmp_file in file_ls]
    renamed_file_set = []

    with codecs.open(renamed_file, "r", "utf-8") as fin:
        for line in fin:
            file_name = line.strip().split(" ")[0]
            print "rename_file:", file_name
            renamed_file_set.append(file_name)
    print "========" * 3
    with codecs.open(output_file, "w", "utf-8") as fout:
        for tmp_file in file_ls:
            print "my_dir_file:", tmp_file
            if tmp_file not in renamed_file_set:
                fout.write(tmp_file.strip() + "\n")


def main():
    print "start..."
    re_fileName()
    print "end..."

if __name__ == "__main__":
    main()