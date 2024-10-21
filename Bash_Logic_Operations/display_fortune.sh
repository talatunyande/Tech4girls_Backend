#!/bin/bash
# this script  is use fortune to generate a random message and pipes it in to cowsay
fortune
cowsay talking cow
fortune | cowsay -f dashing >fortune_cowsay.txt