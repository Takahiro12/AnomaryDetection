git init
git commit --allow-empty -m "Initial Commit"
git branch develop
git checkout develop
pipenv --python 3

pipenv install ~~
pipenv run python ./ch2/example1.py
pipenv run python ./ch2/example2.py
