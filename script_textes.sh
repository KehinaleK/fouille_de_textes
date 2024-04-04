#!/bin/bash
# bash script_textes.sh test.txt

FILE_PATH_IN=$1

if [ $# -ne 1 ] # verifier si le script a un argument
then
	echo "ce programme demande un argument: le chemin vers le fichier contenant les URLS, exemple : text.txt"
	exit
fi


N=1
while read -r line;
do
    curl -s -L ${line} > "aspirations/url_${N}.html"
    lynx -dump -nolist ${line} > "dumps-text/dump_${N}.txt"
    N=$((N + 1))

done < "${FILE_PATH_IN}"