#!/bin/bash

#Compile
for file in ./*.ui
do
	echo Compiling $file
	pyside6-uic $file > ../gui/$file
done

#Rename
for file in ../gui/*.ui
do
	mv "$file" "${file%.ui}.py"
done
