Instructions:
-------------
1.Get the ipaddress by typing the command 'ifconfig'.
2.Open the wired connection ipv4 setting and seelct manual.
3.Enter the following:
	address: ipaddress which you got from ifconfig
	subnet mask:255.255.255.0 (default C type subnet)
	Gateway:0.0.0.0
4.Then press save.
5.sudo gedit /etc/hosts
  add the ipaddress of raspberrypi/nuc/pc with a name
  example:192.168.100.24 sayanuc
6.Do these steps in the host(pc,nuc) and the client(pi) system both.
7.Now connect both through wire(ethernet).
8.Sometimes in pi,we need manually start ssh service.so enter the following command
	sudo service ssh restart
9.Now from the host(pc/nuc),enter into the rpi:
	sudo ssh pi@raspberry                        [pi-username  ,raspberry - ipname stored in etc/hosts file)
10. it will ask for password, enter the password of the raspberrypi user.

Refer: screen and ros multiple machine setup.pdf
-------------------------------------------------------------------------------------------------------

For passwordless entry:
----------------------
1)Open a terminal and type "ssh-keygen -t rsa".

2) The output will look something like below :

*)Just press Enter when asked "Enter file in which to save the key
(/home/username/.ssh/id_rsa):"

*)When asked "Enter passphrase (empty for no passphrase):" Press Enter
again. DONOT TYPE IN ANY PASSPHRASE!!

################################################################
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
#################################################################

3)Now copy the key to client from hosts for psswordless entry
 ssh-copy-id -i ~/.ssh/id_rsa.pub pi@raspberry          [pi-username  ,raspberry - ipname stored in etc/hosts file)

4)Now try ssh into the system.
	sudo ssh pi@raspberrypi

-----------------------------------------------------------------------------------------------

Running ROS on multiple machines:
---------------------------------
1.Install screen software in host machine
	sudo apt-get install screen

2.Test it by running the command 'screen'

3.Open the .bashrc file in the home directory of host and the client add the following lines

	export ROS_MASTER_URI = http://192.168.100.24:11311          #Note:[192.168.100.24 -Host ipaddress ; 11311-default]
	export ROS_IP=192.168.100.24                                 #Note:[192.168.100.24 -host ip address]

4.If you want to run some files in a particular workspace of the client through ssh all the time,it's better to source command in .bashrc
	ex: source /path_to_ws/devel/setup.bash
Note: add this command after the debian sourcing[source /opt/ros/[ros-version]/setup.bash] in the basrc and not before it.

5.Now you can launch a file of the client(rpi) from host/master(pc or nuc) through ssh directly or using the screen software.

Refer: screen and ros multiple machine setup.pdf

------------------------------------------------------------------------------------------------------------






