#!/bin/bash

DOWNLOAD_DIR="./databases"
mkdir -p $DOWNLOAD_DIR

function download {
  name=$(echo $1 |awk -F "/" '{print $NF}')
  echo "Downloading $name..."
  wget -q -O "$DOWNLOAD_DIR/$name" "$1" &
}

download "https://ftp.afrinic.net/pub/dbase/afrinic.db.gz"

download "https://ftp.apnic.net/pub/apnic/whois/apnic.db.inetnum.gz"
download "https://ftp.apnic.net/pub/apnic/whois/apnic.db.inet6num.gz"

download "https://ftp.apnic.net/apnic/whois/apnic.db.organisation.gz"

download "https://ftp.apnic.net/apnic/whois/apnic.db.aut-num.gz"

# it is a 'route' db
# download "https://ftp.arin.net/pub/rr/arin.db.gz"

# it doesn't contain any tangible to org info
# download "https://ftp.lacnic.net/lacnic/dbase/lacnic.db.gz" 

download "https://ftp.ripe.net/ripe/dbase/split/ripe.db.inetnum.gz"
download "https://ftp.ripe.net/ripe/dbase/split/ripe.db.inet6num.gz"

download "https://ftp.ripe.net/ripe/dbase/split/ripe.db.organisation.gz"

download "https://ftp.ripe.net/ripe/dbase/split/ripe.db.aut-num.gz"

wait
