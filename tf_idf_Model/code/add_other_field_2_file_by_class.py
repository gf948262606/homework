# -*- coding:UTF-8 -*-
"""
Filename:
Function:
Author:
Create:
"""
import os
import codecs


def load_field_2_dict(input_file):
    dict_field = {}
    with codecs.open(input_file, "r", "utf-8") as fin:
        for line in fin:
            arr = line.strip().split("|")
            if len(arr) == 3:
                classId = arr[0].strip()
                fieldName = arr[1].strip()
                fieldValue = arr[2].strip()
                if classId not in dict_field:
                    dict_field[classId] = [(fieldName, fieldValue)]
                else:
                    dict_field[classId].append((fieldName, fieldValue))
    return dict_field


def add_field_2_file(dict_field):
    home_dir = os.environ["HOME"]
    input_dir = os.path.join(home_dir, "hackAtHon/data/classes/renamedFile_fenci_tFiDf_byClass")
    file_ls = os.listdir(input_dir)

    for tmp_file in file_ls:
        if tmp_file in dict_field:
            file_path = os.path.join(input_dir, tmp_file)
            with codecs.open(file_path, "a", "utf-8") as fout:
                for tmp_field in dict_field[tmp_file]:
                    fout.write(tmp_field[0] + " " + tmp_field[1] + "\n")


def add_other_field_2_file_by_class():
    home_dir = os.environ["HOME"]
    other_fields_file_dir = os.path.join(home_dir, "hackAtHon/data/classes/other_fileds")

    # city_result_file = os.path.join(other_fields_file_dir, "city_result")
    # dict_city_result = load_field_2_dict(city_result_file)
    #
    # degree_result_file = os.path.join(other_fields_file_dir, "degree_result")
    # dict_degree_result = load_field_2_dict(degree_result_file)
    #
    # province_result_file = os.path.join(other_fields_file_dir, "province_result")
    # dict_province_result = load_field_2_dict(province_result_file)
    #
    # sex_result_file = os.path.join(other_fields_file_dir, "sex_result")
    # dict_sex_result = load_field_2_dict(sex_result_file)
    #
    # time_result_file = os.path.join(other_fields_file_dir, "time_result")
    # dict_time_result = load_field_2_dict(time_result_file)

    all_other_field_file = os.path.join(other_fields_file_dir, "all_other_field")
    dict_all_other_field = load_field_2_dict(all_other_field_file)
    #print len(dict_all_other_field)
    add_field_2_file(dict_all_other_field)


def main():
    print "start..."
    add_other_field_2_file_by_class()
    print "end..."

if __name__ == "__main__":
    main()
