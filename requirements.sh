#! /bin/bash

mkdir -p Files
req=([1]=wget [2]=theharvester [3]=python2.7 [4]=npm)

for i in "${req[@]}"
do

if type $i > /dev/null; then
    echo $i" is already installed "
else
    echo $i" is not installed .. "
    echo "Installing " $i
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install $i
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        sudo apt-get install --force-yes --yes $i
    fi
fi

done

sudo npm install phantomjs

echo "Ready To Go !!!"
