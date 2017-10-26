# This script is designed to work with ubuntu 16.04 LTS

# ensure system is updated and has basic build tools
sudo apt-get update
sudo apt-get --assume-yes upgrade
sudo apt-get --assume-yes install tmux build-essential gcc g++ make binutils
sudo apt-get --assume-yes install software-properties-common
sudo apt-get install git zip

# install Anaconda for current user
mkdir downloads
cd downloads
wget "http://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh" -O "Anaconda3-5.0.0.1-Linux-x86_64.sh"
bash "Anaconda3-5.0.0.1-Linux-x86_64.sh" -b

echo "export PATH=\"$HOME/anaconda3/bin:\$PATH\"" >> ~/.bashrc
export PATH="$HOME/anaconda3/bin:$PATH"
source  ~/.bashrc
conda install -y bcolz
conda upgrade -y --all


# configure jupyter and prompt for password
jupyter notebook --generate-config --allow-root
jupass=`python -c "from notebook.auth import passwd; print(passwd())"`
echo "c.NotebookApp.password = u'"$jupass"'" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False" >> $HOME/.jupyter/jupyter_notebook_config.py

# clone the fast.ai course repo and prompt to start notebook
cd ~
#git clone https://github.com/fastai/courses.git
echo "\"jupyter notebook\" will start Jupyter on port 8888"
echo "If you get an error instead, try restarting your session so your $PATH is updated"
tmux
jupyter notebook --allow-root
