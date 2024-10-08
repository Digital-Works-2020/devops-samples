#Write a shell script to get the file names of all text files without extension in the current directory

#!/bin/bash

#Loop through file in current directory
for file in *.txt; do
    #Check for File extension
    if [[ -e $file ]]; then
       #Use Parameter Expansion. % Removes Suffix. .* Means everything after last dot
       echo "${file%.*}"
    fi
done
