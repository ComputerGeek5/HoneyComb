#!/bin/bash
#TODO: Make this environment-agnostic as well in the future

mkdir -p /etc/honeycomb
mkdir -p /etc/honeycomb/logs/web
mkdir -p /etc/honeycomb/logs/ftp
mkdir -p /etc/honeycomb/logs/telnet

chmod 777 /etc/honeycomb
chmod 777 /etc/honeycomb/logs/web
chmod 777 /etc/honeycomb/logs/ftp
chmod 777 /etc/honeycomb/logs/telnet

cp -r web_bait /etc/honeycomb