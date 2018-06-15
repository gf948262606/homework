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


def rename_file():
    home_dir = os.environ["HOME"]
    fileNameId = os.path.join(home_dir, "hackAtHon/data/classes/file_id_result.txt")
    input_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_fenci_tFiDf_byClass")
    output_dir = os.path.join(home_dir, "hackAtHon/data/classes/renamedFile_fenci_tFiDf_byClass")
    file_ls = os.listdir(input_dir)

    dict_NameId = {}
    with codecs.open(fileNameId, "r", "utf-8") as fin:
        for line in fin:
            arr = line.strip().split(" ")
            name = "".join(arr[:-1]).strip()
            class_id = arr[-1].strip()
            dict_NameId[name] = class_id
   # for tmp_name, tmp_id in dict_NameId.iteritems():
   #     print tmp_name, tmp_id
    for tmp_file in file_ls:
        if unicode(tmp_file) in dict_NameId:
            input_file = os.path.join(input_dir, unicode(tmp_file))
            output_file = os.path.join(output_dir, dict_NameId[unicode(tmp_file)])

            cmd = 'cp %s %s' % (input_file, output_file)
            print "Execute cmd:\n", cmd
            os.system(cmd)


def main():
    print "start..."
    rename_file()
    print "end..."
    
if __name__ == "__main__":
    main()
