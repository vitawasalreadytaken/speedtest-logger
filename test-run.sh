#!/bin/bash

cd ${0%/*}

docker build -t vitasmid/speedtest-logger .

docker run \
	--rm \
	--name speedtest-logger \
	--volume "$(pwd)/output:/output" \
	--net=host \
	vitasmid/speedtest-logger /output/speedtest-log.csv 300
