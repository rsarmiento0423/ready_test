lint:
	find ./libs -type f -name "*.py" | xargs pylint

clean_up:
	@echo "Removing old files!"
	rm *.html *.xml || true
	rm *.png || true

decrypt_staging:
	export KMS_KEY=projects/onec-stage/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-staging-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/stage.enc.json > ./data/stage.json
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/accounts.enc.json > ./data/accounts.json

decrypt_prod:
	export KMS_KEY=projects/onec-prod/locations/global/keyRings/sops-prod-keyring/cryptoKeys/sops-prod-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/prod.enc.json > ./data/prod.json

chrome_prod_parallel:
	pabot -i Demo --logtitle Ready_Chrome_Prod --reporttitle Ready_Chrome_Prod -l ready_prod_chrome_log.html -r ready_prod_chrome_report.html -o ready_prod_chrome_output.xml --variable BROWSER:chrome --variable URL:https://app.oneconcern.com/#/ --variable ENVFILE:prod.json --pythonpath ./libs/pages tests/

ff_prod_parallel:
	pabot -i Smoke --logtitle Ready_Firefox_Prod --reporttitle Ready_Firefox_Prod -l ready_prod_firefox_log.html -r ready_prod_firefox_report.html -o ready_prod_firefox_output.xml --variable BROWSER:firefox --variable URL:https://app.oneconcern.com/#/ --variable ENVFILE:prod.json --pythonpath ./libs/pages tests/

edge_prod_parallel:
	pabot -i Smoke --logtitle Ready_Edge_Prod --reporttitle Ready_Edge_Prod -l ready_prod_edge_log.html -r ready_prod_edge_report.html -o ready_prod_edge_output.xml --variable BROWSER:edge --variable URL:https://app.oneconcern.com/#/ --variable ENVFILE:prod.json --pythonpath ./libs/pages tests/

chrome_staging_parallel:
	pabot -i Smoke -i Staging --logtitle Ready_Chrome_Staging --reporttitle Ready_Chrome_Staging -l ready_staging_chrome_log.html -r ready_staging_chrome_report.html -o ready_staging_chrome_output.xml --variable BROWSER:chrome --variable URL:https://app.staging.onec.co/#/ --variable ENVFILE:stage.json --pythonpath ./libs/pages tests/

chrome_staging_sanity:
	pabot -i Sanity --logtitle Ready_Chrome_Staging_Sanity --reporttitle Ready_Chrome_Staging_Sanity -l ready_staging_chrome_sanity_log.html -r ready_staging_chrome_sanity_report.html -o ready_staging_chrome_sanity_output.xml --variable BROWSER:chrome --variable URL:https://app.staging.onec.co/#/ --variable ENVFILE:stage.json --pythonpath ./libs/pages tests/

chrome_prod_sanity:
	pabot -i Sanity --logtitle Ready_Chrome_Prod_Sanity --reporttitle Ready_Chrome_Prod_Sanity -l ready_prod_chrome_sanity_log.html -r ready_prod_chrome_sanity_report.html -o ready_prod_chrome_sanity_output.xml --variable BROWSER:chrome --variable URL:https://app.oneconcern.com/#/ --variable ENVFILE:prod.json --pythonpath ./libs/pages tests/

ff_staging_parallel:
	pabot -i Smoke --logtitle Ready_Firefox_Staging --reporttitle Ready_Firefox_Staging -l ready_staging_firefox_log.html -r ready_staging_firefox_report.html -o ready_staging_firefox_output.xml --variable BROWSER:firefox --variable URL:https://app.staging.onec.co/#/ --variable ENVFILE:stage.json --pythonpath ./libs/pages tests/

edge_staging_parallel:
	pabot -i Smoke --logtitle Ready_Edge_Staging --reporttitle Ready_Edge_Staging -l ready_staging_edge_log.html -r ready_staging_edge_report.html -o ready_staging_edge_output.xml --variable BROWSER:edge --variable URL:https://app.staging.onec.co/#/ --variable ENVFILE:stage.json --pythonpath ./libs/pages tests/

api_staging:
	robot --logtitle Ready_API_Tests --reporttitle Ready_API_Tests -l ready_api_tests_log.html -r ready_api_tests_report.html -o ready_api_tests_output.xml --pythonpath ./libs/api -i API tests/
