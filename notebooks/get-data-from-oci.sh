#!/bin/bash 

data_dir="/home/datascience/data"
mkdir ${data_dir} && cd ${data_dir} 

wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/x-h8WMZtbxt5X1hkych796-m5GuN_fg_HANhVw-S5IY/n/paasdevdatasc/b/oow-2018/o/data_speech_commands_v0.02.tar.gz

gunzip data_speech_commands_v0.02.tar.gz && tar -xvf data_speech_commands_v0.02.tar
