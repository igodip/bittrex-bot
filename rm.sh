docker ps -a | grep bittrex | awk '{ print $1 }' | xargs docker rm -f
find . -name '*.pyc' | xargs rm -f
rm -Rf src/log/*.lo*
