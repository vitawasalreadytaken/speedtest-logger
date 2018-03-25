speedtest-logger
================

Run https://github.com/sivel/speedtest-cli periodically and append the results to a CSV file.

.. code:: bash

	docker run \
		--rm \
		--name speedtest-logger \
		--volume "$(pwd)/output:/output" \
		--net=host \
		vitasmid/speedtest-logger /output/speedtest-log.csv 300
