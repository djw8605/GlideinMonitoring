#!/bin/sh
#. /opt/condor-7.4.3/condor.sh
cd /home/swanson/dweitzel/sites_rrd

output=`condor_status -format '%s\n' 'GLIDEIN_ResourceName' -const 'IS_MONITOR_VM =!= TRUE' | sort | uniq -c`
IFS=$'\n'
declare -a sitedata
for line in $output; do
sitedata=(`echo $line | tr " " "\n"`)
slots=${sitedata[0]}
site=${sitedata[1]}

# Set the rrd's to 0
for file in `ls *.rrd`; do
rrdupdate $file -t slots N:0
done

if [ -e $site.rrd ]; then
  rrdupdate $site.rrd -t slots N:$slots
else
  rrdtool create $site.rrd --step 60 \
  DS:slots:GAUGE:120:0:100000 \
  RRA:AVERAGE:0.5:1:900 \
  RRA:AVERAGE:0.5:5:288 \
  RRA:AVERAGE:0.5:30:336

  rrdupdate $site.rrd -t slots N:$slots
fi
buildstring="DEF:$site=$site.rrd:slots:AVERAGE"
rrdtool graph graph.png -a PNG --title "Glideins Running" $buildstring
#buildstring="DEF:$site=$site.rrd:slots:AVERAGE $buildstring"

done
# Build the graph
#rrdtool graph graph.png -a PNG --title "Glideins Running" $buildstring

cp *.rrd /var/www/html/sites
chmod 644 /var/www/html/sites/*.rrd

