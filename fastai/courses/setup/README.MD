## List of files
| File                  | Purpose       |
| --------------------- | ------------- |
| `install-gpu.sh`      | Installs required software on an Ubuntu machine. Instructions available on the [wiki](http://wiki.fast.ai/index.php/Ubuntu_installation).|

## Setup Instructions



### Ubuntu
Download and run the `install-gpu.sh` script to install required software on an Ubuntu machine. More instructions available on the [wiki](http://wiki.fast.ai/index.php/Ubuntu_installation).

```
# configure jupyter and prompt for password
jupyter notebook --generate-config --allow-root
jupass=`python -c "from notebook.auth import passwd; print(passwd())"`
echo "c.NotebookApp.password = u'"$jupass"'" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False" >> $HOME/.jupyter/jupyter_notebook_config.py
```
