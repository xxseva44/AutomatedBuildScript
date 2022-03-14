import subprocess
import os

def TextBreak ():
	print("#############################")
	print("#############################")

def Rom_Check ():
	global Rom
	Rom = input("What rom are you building \n")


def Thread_Check():
	global Thread
	Thread = input("How many threads does your cpu have?")


def Working_DirCheck ():
	subprocess.call(['pwd'])
	DirCon = input("is this the correct directory? Y/N \n")
	if DirCon == "Y":
		print("Directory set")
	elif DirCon == "N":
		DirSelect()
	else:
		print("Please choose a valid option!!!")
		Working_DirCheck()


def DirSelect ():
	os.chdir("/home")
	subprocess.call(['pwd'])
	Dir = input("Please enter the working directory \n")
	os.chdir(Dir)
	print (f"{Dir} is now selected!")



def Android_VersionCheck ():
	global AndroidVersion
	AndroidVersion = int(input("What android version is being built? Ex. 10,11,12 \n"))
	if AndroidVersion > 11:
		os.system(". build/envsetup.sh")
	elif AndroidVersion <= 11:
		os.system("source build/envsetup.sh")
	else:
		print ("Please choose a valid option!")
		Android_VersionCheck()


def Ccache_Config ():
	CcacheCon = input("Enable ccache? Y/N \n")
	if CcacheCon == "Y":
		os.system("export USE_CCACHE=1")
		CcacheSpace = input("How much space would you like too allocate in gigabytes? Ex. 50G \n")
		os.system("ccache -M" + CcacheSpace)
	elif CcacheCon == "N":
		subprocess.run('export USE_CCACHE=0')


def DeviceVariant_BuildConfig ():
	global DeviceVar
	DeviceVar = input("What device/variant would you like to build? \n")
	print(f"Building android {AndroidVersion} for {DeviceVar}")
	if AndroidVersion <= 11:
		os.system("lunch " + Rom + "_" + DeviceVar)
	elif AndroidVersion > 12:
		os.system("lunch " + Rom + "_" + DeviceVar + "-" + BuildType)
	print(f"lunch {Rom}_{DeviceVar}")


def Build_Type ():
	print("What build would you like to make?")
	global BuildType
	BuildType = input("Options: user|userdebug|eng \n")


def Start_Build ():
	print("Starting Build")
	if AndroidVersion <= 11:
		os.system("brunch " + Rom + "_" + DeviceVar + "-" + BuildType)
		print(f"{Rom}_{DeviceVar}-{BuildType}")
	elif AndroidVersion > 12:
		os.system("make " + Rom + "-j" + Thread)
		print("Starting build, please wait...")


print("########################")
print("#Automated Build Script#")
print("#By:   XXSEVA44@XDA    #")
print("########################")
TextBreak()
Working_DirCheck()
TextBreak()
Rom_Check()
TextBreak()
Android_VersionCheck()
TextBreak()
Ccache_Config()
TextBreak()
Build_Type()
TextBreak()
DeviceVariant_BuildConfig()
TextBreak()
Start_Build()
TextBreak()
TextBreak()
