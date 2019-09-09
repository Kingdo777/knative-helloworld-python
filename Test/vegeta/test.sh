#!/usr/bin/env bash
rate=$1
duration=$2

if [[ -z ${rate} ]]; then
    rate="1"
fi

if [[ -z ${duration} ]]; then
    duration="120s"
    else
    duration="$2s"
fi
echo "GET http://helloworld-python.default.example.com" | vegeta attack -name=1qps -rate=${rate} -duration=${duration} > results.${rate}qps.${duration}.bin
cat results.${rate}qps.${duration}.bin | vegeta plot > plot.${rate}qps.${duration}.html
sudo cp plot.${rate}qps.${duration}.html /var/www/html
echo "http://www.kingdo.xyz/plot.${rate}qps.${duration}.html"