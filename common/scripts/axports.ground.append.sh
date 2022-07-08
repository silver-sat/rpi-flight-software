
. config.sh

# motify /etc/ax25/axports
sed -e '/^serial/d' /etc/ax25/axports > /tmp/axports
wget -q -O - "$BASEURL/common/data/axports.satellite.append.txt" >> /tmp/axports
sudo mv -f /tmp/axports /etc/ax25/axports
sudo chown root.root /etc/ax25/axports
