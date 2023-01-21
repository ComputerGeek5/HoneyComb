mkdir -p /etc/honeycomb
mkdir -p /etc/honeycomb/logs
mkdir -p /etc/honeycomb/logs/web

chmod 777 /etc/honeycomb
chmod 777 /etc/honeycomb/logs
chmod 777 /etc/honeycomb/logs/web

cp -r web_bait /etc/honeycomb