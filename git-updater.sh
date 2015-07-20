#! /bin/bash
DIR=$1
BRANCH=$2
git -C $DIR branch $BRANCH
git -C $DIR checkout $BRANCH
git -C $DIR pull origin $BRANCH
