#!/bin/sh

kubectl exec --namespace=$1 $2 -i -t -- sh -il
