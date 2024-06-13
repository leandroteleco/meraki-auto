# Meraki-Auto

Lightweight Flask-based web application that allows you to upload files with information to configure networks based on Cisco Meraki infrastructure through the Meraki Dashboard API.

Currently it is only capable of uploading firewall rules in a policy group of a given network. This is one of the typical configurations that takes a long time to configure through the dashboard graphical interface, so it will save time for the network engineer who operates a Meraki network on a daily basis.

More features could be added in the future.

## Steps to install and use the application on Windows ##

### Step 1: Generate API Key in Meraki Dashboard ###

The first step to be able to interact with the Meraki Dashboard is to enable access through its API, and to do so we must generate an API KEY.

For this step, you can follow the instructions from the Meraki website here: https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API

It is important that you save the API KEY because we will need to use it later to configure the Meraki-Auto application.

### Step 2: Install the latest version of Python ###

Meraki-Auto uses Python 3.12.3, so you need to install at least that version on Windows. It will probably also work with later versions of Python 3.12.x.

In any case, you can install version 3.12.3 with this installer (for amd64 or 64-bit systems): https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

It is important that during the installation you check the option to add to the Windows path: "Add python.exe to PATH".

If you already had a previous version of Python installed, it is recommended to uninstall it before installing version 3.12 of Python.

### Step 3: Install Git for Windows ###

In order to download the necessary files from Meraki-Auto and easily update the application in the future, we will need to install Git on Windows (for amd64 or 64-bit systems): https://github.com/git-for-windows/git/releases/download/v2.45.2.windows.1/Git-2.45.2-64-bit.exe

When the installer asks which editor to use for effect, you can choose Notepad if you don't have another editor listed.

### Step 4: Download the Meraki-Auto application files ###

Choose a folder where Meraki-Auto and its files will be downloaded, for example, the desktop is recommended.

From the chosen folder (the desktop), access it, and from the context menu that will appear when you right-click, you can choose "Open Git Bash here".

A console (CLI) will open, enter the following command:
git clone https://github.com/leandroteleco/meraki-auto

A folder called "meraki-auto" will be created in which all the necessary files will have been downloaded.

We can close the console.

### Step 5: Activate the virtual environment in python ###

Open the meraki-auto folder and open the git console again (right click and choose "Open Git Bash here"). The console will open.

In the console we will write "pip install virtualenv", this will install the python virtual environments module.

When the installation is finished, we will write in the console "python -m venv venv". With this we will create a python virtual environment.

Next, we will write the following code "source venv\Scripts\activate", this will activate the python virtualization environment.

### Step 6: Meraki-Auto Initial Setup ###

Enter the command "pip install -r requirements.txt" in the console, this will install all the dependencies (Python modules and libraries) necessary to run the program. This step may take several minutes, please be patient.

When you're done, open the .env file located in the "meraki-auto" folder using notepad or any other text editor. In that file, you'll need to replace the text "YOUR_API_KEY" with the API KEY you obtained in step 1 from the Meraki Dashboard.

If you have more than 1 organization in your account, you'll need to change the text "YOUR_ORG_ID" to your organization's ID.

If you are going to run the application on a PC that uses a corporate proxy such as Zscaler, you will need to obtain the certificate from your proxy. Also in that case you should set USE_PROXY to 1, and in PROXY_CERTIFICATE_FILE you should indicate the full path to the certificate you downloaded, similar to this: C:\\certfolder\\certfile.cer

Save the changes and close the .env file.

### Step 7: Running the Meraki-Auto application ###

In the console we will write "py main.py", this will run the Flask web server on our system on port 5000.

To access the application, we will open a web browser such as Firefox or Chrome, accessing the following url: http://127.0.0.1:5000/

Enjoy!


