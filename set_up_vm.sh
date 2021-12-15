# For ubuntu lts

sudo apt-get update; sudo apt-get upgrade -y

sudo apt install gnome-tweak-tool
sudo apt install git
sudo apt install vim 
sudo apt-get install cifs-utils

mkdir /mnt/external_hdd
echo "//192.168.0.171/share /mnt/external_hdd cifs guest,uid=1000,nobrl,iocharset=utf8  0  0" >> /etc/fstab
sudo mount /mnt/external_hdd
ln -s  /mnt/external_hdd ~/hdd

gnome-tweak-tool
