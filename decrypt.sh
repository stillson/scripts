#!/bin/sh

openssl enc -d -chacha -a -md sha1 -in $1.enc -out $1.dec
