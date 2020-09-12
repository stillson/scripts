#!/bin/sh

openssl enc -chacha -a -md sha1 -in $1 -out $1.enc
