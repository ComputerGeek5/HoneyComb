mkdir -p /etc/honeycomb
mkdir -p /etc/honeycomb/logs/web
mkdir -p /etc/honeycomb/logs/ftp

chmod 777 /etc/honeycomb
chmod 777 /etc/honeycomb/logs/web
chmod 777 /etc/honeycomb/logs/ftp

cp -r web_bait /etc/honeycomb