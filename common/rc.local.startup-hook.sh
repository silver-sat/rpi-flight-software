# modify /etc/rc.local
sed -e '/^fi$/,/^exit 0$/d' /etc/rc.local > /tmp/rc.local
echo "fi" >> /tmp/rc.local
wget -q -O - 'https://raw.githubusercontent.com/silver-sat/rpi-flight-software/master/common/rc.local.insert.sh' >> /tmp/rc.local
echo "exit 0" >> /tmp/rc.local
sudo mv -f /tmp/rc.local /etc/rc.local
sudo chown root.root /etc/rc.local
sudo chmod +x /etc/rc.local
