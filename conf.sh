#!/bin/bash
mkdir /mnt/Seagate
echo "*  *    * * *   pi      /usr/bin/perl /usr/local/bin/GetLastEpisode" >> /etc/crontab
echo "/dev/sda1 /mnt/Seagate  ext4 defaults,noatime 0 1" >> /etc/fstab
