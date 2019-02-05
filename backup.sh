#!/bin/sh

#
# mv backup
#
#

dirname=$1
date=$(date +%y%m%d)

if [ -z $dirname ] ; then
    echo "please input backup directory or file"
    exit
fi

if [ -f $dirname.bk ] || [ -d $dirname.bk ] ; then
    echo "remove:$dirname"
    rm -rf $dirname.bk
fi

mv $dirname bk${date}.$dirname




