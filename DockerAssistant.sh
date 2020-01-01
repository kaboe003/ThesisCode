sudo apt-get install apt-transport-https ca-certificates software-properties-common -y
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker pi
sudo curl https://download.docker.com/linux/raspbian/gpg
vim /etc/apt/sources.list
deb https://download.docker.com/linux/raspbian/ stretch stable
sudo apt-get update
sudo apt-get upgrade
systemctl start docker.service
docker info
