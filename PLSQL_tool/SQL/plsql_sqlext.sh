#!/bin/sh

TOOLDIR=/home/cloud-user

inputdir="."
outputdir="."
prefix=""

while getopts i:o:p: opt
do
    case $opt in
        i) inputdir=$OPTARG
            ;;
        o) outputdir=$OPTARG
            ;;
        p) prefix=$OPTARG
            ;;
    esac
done

for p in `find $inputdir -name "*.sql"`;
do
    dn=$(dirname "$p")
    fn=$(basename "$p")
    if [ ! -d $outputdir/$dn ]; then
        mkdir -p $outputdir/$dn
    fi
    echo "SQL extracting ... $p -> $outputdir/$dn/$prefix$fn"
    python3 $TOOLDIR/plsql_sqlext.py < $p > $outputdir/$dn/$prefix$fn
done

exit
