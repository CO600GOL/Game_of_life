#! /bin/sh

packages="DisplayAdapter GameEngine ProjectConway"

for package in $packages
do
    echo "Building package: $package"
    cd $package
    make setup
    cd ..
done
