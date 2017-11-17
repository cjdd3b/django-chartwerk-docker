#!/bin/bash
echo 'Copying conf ...'
cp /code/config/nginx/prod/chartwerk.prod.conf /etc/nginx/conf.d/default.conf

echo 'Echoing conf'
cat /etc/nginx/conf.d/default.conf

echo 'Running nginx'
nginx -g 'daemon off;'