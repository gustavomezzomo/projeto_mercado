#!/bin/bash
export COMPOSE_PROJECT_NAME=projeto_mercado_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run projeto_mercado unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
