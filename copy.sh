#!/bin/bash

cp service/qbittorrent.service /etc/systemd/system

cp conf/GetLastEpisode.txt /etc/
cp conf/bashrc /home/pi/.bashrc
cp conf/ssmtp.conf /etc/ssmtp/ssmtp.conf
cp conf/smb.conf /etc/samba/
cp conf/qBittorrent.conf /home/pi/.config/qBittorrent/

cp exec/GetLastEpisode /usr/local/bin
cp exec/login.txt      /usr/local/bin
cp exec/organise	      /usr/local/bin
cp exec/resurrect_qbt  /usr/local/bin

chmod +x /usr/local/bin/*
