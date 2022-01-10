## For ubuntu lts ##

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


# Conda set up 
arch_type=$(dpkg --print-architecture)
case $arch_type in
        amd64)
                wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
                ;;
        armhf)
                wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
                ;;
esac

chmod +x Miniconda3-latest*

bash Miniconda-latest* -b

## To recreate the python enviroment ##
# conda create --name bitcoin_backtest --file bitcoin_backtest.txt
# conda activate bitcoin_backtest
