# -*- coding: utf-8 -*-
import dicom
import os
import judge_dicoom_file
import argparse
import logging
import logging.handlers

#命令行输入参数
parser = argparse.ArgumentParser()
parser.add_argument('--qp_dir')
parser.add_argument('--save_dir')
args = parser.parse_args()
qp_dir = args.qp_dir
save_dir = args.save_dir
qp_dir = qp_dir.replace('\\', '\\\\')
save_dir = save_dir.replace('\\', '\\\\')

# qp_dir = 'F:\\LN_Scanner_Y\\IA'
# save_dir = 'F:\\LN_Scanner_Y\\IA_tuomin'

# qp_dir = 'D:\\dicom'
# save_dir = 'D:\\dicomtm'

print ('The path of patients dicom files is: %s \nThe path of dicom files after TM is: %s'%(qp_dir, save_dir))

#遍历某文件夹下及其子文件夹下的所有文件
file_lsit = []
dicom_list = []
for root,dirs,files in os.walk(qp_dir):
    for file in files:
        file_p = os.path.join(root, file)
        file_lsit.append(file_p)
        if judge_dicoom_file.is_dicom_file(file_p) == True:
            dicom_list.append(file_p)
dicom_num = len(dicom_list)
print('the number of dicom files are: '+str(dicom_num))
count = 0
#对dicom文件进行脱敏并保存
for one_dicom in dicom_list:
    patient_dataset = dicom.read_file(one_dicom, force=True)
    patient_dataset.PatientsName = 'NA'
    patient_dataset.InstitutionName = 'NA'
    path_1 = one_dicom[len(qp_dir):len(one_dicom)]
    save_dicom_file = os.path.join(save_dir+path_1)
    save_dicom_file_array = save_dicom_file.split('\\')
    save_dicom_path_array = save_dicom_file_array[0:len(save_dicom_file_array)-1]
    save_dicom_path = '\\'.join(save_dicom_path_array)
    if not os.path.exists(save_dicom_path):
        os.makedirs(save_dicom_path)
    save_dicom_file = os.path.join(save_dicom_path,os.path.basename(one_dicom))
    patient_dataset.save_as(save_dicom_file)
    print("file saved from %s to %s"%(one_dicom, save_dicom_file))
#检测
# files = os.listdir('D:\\dicomtm')
# print(files)
# for file in files:
#     file = 'D:\\dicomtm\\'+file
#     patient_dataset = dicom.read_file(file, force = True)
#     print(patient_dataset.PatientsName, patient_dataset.InstitutionName)