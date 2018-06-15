# -*- coding:UTF-8 -*-
"""
Filename:
Function:
Author:
Create:
"""
import os
import jieba
import codecs
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def load_classNameId_2_dict():
    dict_classNameId = {}
    home_dir = os.environ["HOME"]
    classId_file = os.path.join(home_dir, "hackAtHon/data/classNameId.txt")

    with codecs.open(classId_file, "r", "utf-8") as fin:
        for line in fin:
            arr = line.strip().split(" ")
            if len(arr) == 2:
                classId = arr[0].strip()
                className = arr[1].strip()
                if className not in dict_classNameId:
                    dict_classNameId[className] = classId
    return dict_classNameId


def load_stopWords_2_set(stop_words_file):
    stop_words_set = set()
    with codecs.open(stop_words_file, "r", "utf-8") as fin:
        for line in fin:
            stop_words_set.add(line.strip())
    return stop_words_set


def split_file_by_class(input_file):
    home_dir = os.environ["HOME"]
    input_file = os.path.join(home_dir, "hackAtHon/data", input_file)
    output_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_byClass")
    dict_content_by_class = {}

    # print "load class info 2 dict..."
    # dict_classNameId = load_classNameId_2_dict()

    print "load file 2 dict..."
    with codecs.open(input_file, "r", "utf-8") as fin:
        for line in fin:
            # print line
            arr = line.strip().split("|")
            if len(arr) < 4:
                continue
            class_name = arr[3].strip()
            text = ",".join(arr[1:])
            if class_name in dict_content_by_class:
                # if class_name in dict_classNameId:
                dict_content_by_class[class_name].append(text)
            else:
                # if class_name in dict_classNameId:
                    dict_content_by_class[class_name] = [text]

    print "write content 2 file by class..."
    for tmp_class, tmp_text_ls in dict_content_by_class.iteritems():
        output_file = os.path.join(output_dir, "splitFile_byClass_%s" % tmp_class.strip().replace("/", "-").replace("【", "[").replace("】", "]").replace("（", "(").replace("）", ")"))
        with codecs.open(output_file, "w", "utf-8") as fout:
            for tmp_text in tmp_text_ls:
                fout.write(tmp_text.strip() + "\n")


def get_fen_ci_result(stop_words_file, user_dict_path=None):
    import re
    home_dir = os.environ["HOME"]
    input_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_byClass")
    file_list = os.listdir(input_dir)

    stop_words_set = load_stopWords_2_set(stop_words_file)
    for tmp_file in file_list:
        input_file = os.path.join(input_dir, tmp_file)
        output_file = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_fenCi_byClass", tmp_file)
        print input_file
        result = []
        with codecs.open(input_file, "r", "utf-8") as fin, codecs.open(output_file, "w", "utf-8") as fout:
            for line in fin:
                text = line.strip()
             #   text = ",".join(text.split("|")[1:])
                text = text.replace(" ", "")
                fenci_result = jieba.cut(text)
                fenci_result = list(set(fenci_result) - set(stop_words_set))
                fenci_result = [tmp_word.strip() for tmp_word in fenci_result if tmp_word.strip() != ""]

                result.extend(fenci_result)
                result = {}.fromkeys(result).keys()
            result_str = " ".join(result)
            result_str = re.sub(r'\d', "", result_str)
            fout.write(result_str.strip() + "\n")


def get_tf_idf_result():
    home_dir = os.environ["HOME"]
    input_dir = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_fenCi_byClass")
    file_list = os.listdir(input_dir)

    record_file_name = []
    data_fenci = []
    for tmp_file in file_list:
        input_file = os.path.join(input_dir, tmp_file)
        print input_file

        record_file_name.append(tmp_file)
        with codecs.open(input_file, "r", "utf-8") as fin:
            for line in fin:
                data_fenci.append(line.strip())

    vectorizer = CountVectorizer()
    termFreq_matrix = vectorizer.fit_transform(data_fenci)
    word_bag = vectorizer.get_feature_names()
    vc_vocabulary = vectorizer.vocabulary_
    #freWord = termFreq_matrix.toarray().sum(axis=0)
   # print len(freWord)
    print len(word_bag)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(termFreq_matrix)
    weight = tfidf.toarray()

    for tmp_ind in xrange(len(record_file_name)):
        tmp_output_file = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_tFiDf_byClass", ("tmp_" + record_file_name[tmp_ind]))
        with codecs.open(tmp_output_file, "w", "utf-8") as fout:
            for j in xrange(len(word_bag)):
                fout.write(word_bag[j] + " " + str(vc_vocabulary[word_bag[j]]) + " " + str(weight[tmp_ind][j]) + "\n")

        output_file = os.path.join(home_dir, "hackAtHon/data/classes/splitFile_tFiDf_byClass", record_file_name[tmp_ind])
        cmd = "sort -k 2nr %s > %s" % (tmp_output_file, output_file)
        print "Execute cmd:\n", cmd
        os.system(cmd)

        cmd = "rm %s" % tmp_output_file
        print "Execute cmd:\n", cmd
        os.system(cmd)


def main():
   # # 按照班级分文件
   # input_file = "merged_data"
   # print "start..."
   # split_file_by_class(input_file)
   # print "end..."

   # # 分词
   # home_dir = os.environ["HOME"]
   # stop_words_file = os.path.join(home_dir, "hackAtHon/code", "stopword.dic")
   # print "start..."
   # get_fen_ci_result(stop_words_file)
   # print "end..."

    # tfidf
    print "start..."
    get_tf_idf_result()
    print "end..."

if __name__ == "__main__":
    main()
