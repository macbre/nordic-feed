#!/bin/bash
date
source env/bin/activate
make
git diff
git add docs/ && git commit -m 'Updating the Planet'
git push origin master

echo 'Done'
date
