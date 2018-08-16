Prerequisites
Ensure that you have more than 2GB RAM. In the case of not having enough memory, you could use swap to extend the RAM capacity. Just follow the tutorial here to create swap.

Step 1: Install dependencies
Installing Julia requires some dependencies such as gcc, g++, etc. To simplify the process, log in as root and install all the dependencies.

apt install gcc
apt install make
apt install g++
apt install python
apt install gfortran
apt install perl
apt install m4
apt install patch
apt install cmake
apt install pkg-config
Step 2: Download Julia and install
The whole process here does not require root privilege to install Julia. Start your terminal and get the source code of Julia from Github

git clone git://github.com/JuliaLang/julia.git
All the source code will be in the folder named julia. Switch to this folder.

cd julia
Checkout the latest version of Julia.

git checkout v0.6.0
Build Julia from source.

make -j 2
The -j option indicates how many threads for building Julia. The more the better. It should be set equal to the number of cores of the server.

The building process is quite long.

Step 3: Verify Julia
Inside the folder julia, we can find an executable file named julia.

Type ./julia --version in the command prompt and the output should look like this.

julia version 0.6.0
There are two ways to use Julia, The first one is via its REPL. Just type in ./julia to access the REPL. The second one is by saving the running code under a file with extension .jl and run this file with ./julia <nameOfFile.jl>.

For convenience, you can create an alias to access julia anywhere in your server
