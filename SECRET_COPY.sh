#!/bin/sh

# $1 -> secret
# $2 -> from namespace
# $3 -> to namespace
# usage:
# SECRET_COPY.sh <secret> <lives in ns> <copy to ns>
set -ex

kubectl get secret ${1} --namespace=${2} --export -o yaml | kubectl apply --namespace=${3} -f -

