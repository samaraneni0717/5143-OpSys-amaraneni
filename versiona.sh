#!/bin/bash
#takes name of file as first argument
name_of_file=$1
newFile="$(date +%y-%m-%d)_name_of_file"
cp $name_of_file  $newFile
