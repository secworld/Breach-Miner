#! /bin/bash

mkdir -p Files
declare -A req=([1]=wget [2]=theharvester [3]=python2.7 [4]=npm)

for i in "${req[@]}"
do
INSTALLED=$(dpkg -s $i | grep installed)
if [ "$INSTALLED" != "" ]; then
    echo $i" is already installed "
else
    echo $i" is not installed .. "
    echo "Installing " $i
    sudo apt-get install --force-yes --yes $i
    exit
fi

done

sudo npm install phantomjs

echo "Ready To Go !!!"
