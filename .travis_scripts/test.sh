#! /bin/sh
set -e
packages="DisplayAdapter GameEngine ProjectConway"

for package in $packages
do 
    echo "Testing pachage: $package"
    cd $package
    make test
    cd ..
done
