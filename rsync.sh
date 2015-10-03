#!/bin/bash

rsync -rav -e ssh --exclude='__pycache__' --exclude='.git' --exclude='*.pyc' --exclude='*.swp' ../sneak-streaming/ $1:/root/sneak-streaming/
