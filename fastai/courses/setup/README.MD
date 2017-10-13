## List of files
| File                  | Purpose       |
| --------------------- | ------------- |
| `aws-alias.sh`        | Command aliases that make AWS server management easier. |
| `instal-gpu-azure.sh` | Installs required software on an Azure Ubuntu server. Instructions available on the [wiki](http://wiki.fast.ai/index.php/Azure_install). |
| `install-gpu.sh`      | Installs required software on an Ubuntu machine. Instructions available on the [wiki](http://wiki.fast.ai/index.php/Ubuntu_installation). |
| `setup_instance.sh`   | Sets up an AWS environment for use in the course including a server that has the required software installed. This script is used by `setup_p2.sh` or `setup_t2.sh`. You probably don't need to call it by itself. |
| `setup_p2.sh` and `setup_t2.sh` | Configure environment variables for use in `setup_instance.sh`. These files call `setup_instance.sh`, which does the actual work of setting up the AWS instance. |

## Setup Instructions



### Ubuntu
Download and run the `install-gpu.sh` script to install required software on an Ubuntu machine. More instructions available on the [wiki](http://wiki.fast.ai/index.php/Ubuntu_installation).
