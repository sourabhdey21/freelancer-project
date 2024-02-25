#!/bin/bash
set -e

dir_name="hiring-test-$(whoami)"
mkdir -p $dir_name

git format-patch --stdout $(git rev-list --max-parents=0 HEAD)..HEAD > ${dir_name}/git-changes.patch
kubectl describe deployments -A > ${dir_name}/kubectl-deployments.txt
kubectl describe pods -A > ${dir_name}/kubectl-pods.txt
curl -sG http://localhost/api/v1/query --data-urlencode "query=bitcoin_price" > ${dir_name}/prometheus-bitcoin-metric.json
curl -sG http://localhost/api/v1/query --data-urlencode "query=node_boot_time_seconds" > ${dir_name}/prometheus-random-metric.json

tar -czf ${dir_name}.tar.gz $dir_name
rm -rf $dir_name

echo 'Thank you for completing our hiring test!'
echo
echo "Please send us your results: ${dir_name}.tar.gz"
