#!/bin/bash

mkdir /etc/honeycomb
mkdir /etc/honeycomb/logs
cp -r web /etc/honeycomb
cp app.conf /etc/honeycomb/
chmod 777 /etc/honeycomb
chmod 777 /etc/honeycomb/logs
chmod 777 /etc/honeycomb/web