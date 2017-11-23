#!/usr/bin/python 
#create inception
### todo
# add check slcli file
#######################################################################
#defs

import os

def yum_install ( pkg ):
   "install via yum"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def play_book ( pb ):
   "run playbook"
   book = "ansible-playbook " + pb
   os.system(book)
   return;

def pip ( pp ):
   "run playbook"
   pcom = "pip install " + pp
   os.system(pcom)
   return;

def install_galaxy ( galaxy ):
   "install galaxy repo"
   ig = "ansible-galaxy install " + galaxy
   os.system(ig)
   return;

def git ( url ):
   " using git"
   gt = "git clone " + url
   os.system(gt)
   return;

def move ( ori, dest ):
   " coping file "
   pw = "mv " + ori + " " + dest
   os.system(pw)
   return;

def cmd ( cmdx ):
   " run"
   os.system(cmdx)
   return;

def copy ( ori, dest ):
   " coping file "
   cpw = "cp -r " + ori + " " + dest
   os.system(cpw)
   return;
 ############
 
yum_install("epel-release")
yum_install("python-setuptools")
cmd("easy_install pip")
yum_install("ansible")
yum_install("git")
yum_install("pysphere")
git("https://github.com/jmbarros/jumper.git")
git("https://github.com/jmbarros/servers.git")
play_book("~/jumper/jumper.yml")
copy("~/jumper/inventory", "~/inventory")
install_galaxy("jmbarros.icp")