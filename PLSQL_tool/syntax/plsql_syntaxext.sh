#!/bin/sh

#
# usage: plsql_syntaxext.sh -i (inputdir) -o (outputfile)
#
# 説明:  (inputdir)にある *.sql を入力して、非互換構文チェックの結果を出力する。
#        出力先は (outputfile)
#        -o オプション省略時は syntax_check.txt とする。
#
# 備考:  python3 環境を必要とする。
#

TOOLDIR=/home/cloud-user

inputdir="."
outputfile="syntax_check.txt"

while getopts i:o: opt
do
    case $opt in
        i) inputdir=$OPTARG
            ;;
        o) outputfile=$OPTARG
            ;;
    esac
done

if [ -e $outputfile ]; then
    mv $outputfile $outputfile.old
fi

for p in `find $inputdir -name "*.sql"`;
do
    echo "PL/SQL syntax check ... $p"
    python3 $TOOLDIR/plsql_syntaxext.py $p >> $outputfile
done

exit