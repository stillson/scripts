#!/bin/sh

while [ 1 ] ; do
    date
    az acr login --name sifivedev
    sleep 600
done
