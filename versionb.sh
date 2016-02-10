#!/bin/bash
name_of_file=$1

basename="${name_of_file##*/}"
extension="${name_of_file##*.}"

copyFile="${basename%.*}_$(date +%y-%m-%d).$extension"
cp $name_of_file $copyFile

