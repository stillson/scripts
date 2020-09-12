#!/bin/sh

while true ; do
    kubectl get -w -A events
done
