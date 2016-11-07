# az playground frontend
FROM kyma/docker-nginx
COPY src/ /var/www
CMD sed 's/PLAYGROUND_INSTANCE_URL/'$PLAYGROUND_INSTANCE_URL'/' -i /var/www/play/index.html; \
    sed 's/PLAYGROUND_API_ROOT_ENDPOINT/'$PLAYGROUND_API_ROOT_ENDPOINT'/' -i /var/www/assets/js/main.js; \
    sed 's/PLAYGROUND_API_ROOT_ENDPOINT_PORT/'$PLAYGROUND_API_ROOT_ENDPOINT_PORT'/' -i /var/www/assets/js/main.js; \
    'nginx'
