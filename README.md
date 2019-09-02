# Semrush Reports
<p align="center">
  <img src="http://hugoakhtari.com/wp-content/uploads/2019/09/semrush_python_script.gif">
</p>


My first ever Python project. This script allows you to download up to 5 organic reports from Semrush without going through the API. 

### Prerequisites

You will need :
<li>Python 3
<li>Pip (normally directly downloaded with Python)
<li>Requirements.txt
<li>Chromedriver (for windows or mac)
<li>A Semrush account

### Installing

<li>Step 1 : Python 3

Get it from : https://www.python.org/downloads/

<li>Step 2 : Pip

Enter this code in your terminal

```
pip --version
```
If no errors, we're good. Otherwise install pip from : https://www.liquidweb.com/kb/install-pip-windows/

<li>Step 3 : Requirements.txt

Enter this code in your terminal

```
pip install -r requirements.txt
```
This is for installing all the script requirements 

<li>Step 4 : Selenium & Chromedriver

Go on chrome://settings/help and check your version.

Then go on http://chromedriver.chromium.org/downloads and download the right version (mac or windows)

Then move the <b>chromedriver</b> file to the <b>driver folder</b>

## Running the script

<li>Input your Semrush login + password

open <b>semrush_report.py</b> with any text editor and input your login and password into these 2 lines
```
# Input your SemRush Login here
semrush_mail ="XXXXXXXXX"
semrush_password ="XXXXXXXXXX"
```

<li>Launching the script

open the <b>terminal</b> and write
```
cd /yourfilepath/semrush_report
python semrush_report.py
```
First line is to go into the folder where <b>semrush_report.py</b> is located (copy paste your own path). Second one is to launch the script (on mac you will need to type python3)

<li>Using the script

You can enter up to 5 websites (if you don't want 5 websites, just type "none"). You will also have to choose among a database list (countries where the keyword and posiitions will be exported).

For example : 
```
Enter your website: amazon.fr
Enter second website, (if no website type : "None") : alibaba.com
Enter third website, (if no website type : "None") : aliexpress.com
Enter fourth website, (if no website type : "None") : none
Enter yout Data Base ( ['us', 'uk', 'br', 'ca', 'au', 'fr', 'de', 'it', 'nl', 'es', 'in', 'ru', 'jp', 'tr', 'dk', 'mx', 'ar', 'pl', 'be', 'ie', 'se', 'ch', 'fi', 'hu', 'no', 'il', 'sg', 'hk']) :fr
Ok let's go !
```
This will get the organic reports on the French database for these 3 websites.

### Get the results

To get the .xls files, just go into the <b>/excel/</b> file and they will be there.

<p align="center">
  <img src="https://hugoakhtari.com/wp-content/uploads/2019/09/excel_export.png">
</p>

## License

This project is licensed under the GPL v3 License - see the [LICENSE.md](LICENSE.md) file for details

## Wanna know more ? 

https://hugoakhtari.com/automatisation-python-semrush/
