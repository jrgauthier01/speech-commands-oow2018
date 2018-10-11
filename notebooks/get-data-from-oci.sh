#!/bin/bash 

data_dir="/home/datascience/data"
mkdir ${data_dir} && cd ${data_dir} 

wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/e3lkFK77z6pIRodYctsVOv82b4ZwpOAT0hoN9PcIboA/n/paasdevdatasc/b/oow-2018/o/data_speech_commands_v0.02.tar.gz 

gunzip data_speech_commands_v0.02.tar.gz && tar -xvf data_speech_commands_v0.02.tar