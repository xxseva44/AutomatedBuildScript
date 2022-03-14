import subprocess
import os

def TextBreak ():
	print("#############################")

def Rom_Check ():
	Rom = input("What rom are you building")


def Working_DirCheck ():
	subprocess.call(['pwd'])
	DirCon = input("is this the correct directory? Y/N \n")
	if DirCon == "Y":
		print("Directory set")
	elif DirCon == "N":
		TextBreak()
		DirSelect()
	else:
		print("Please choose a valid option!!!")
		Working_DirCheck()


def DirSelect ():
	Dir = input("Please enter the working directory \n")
	TextBreak()
	os.chdir(Dir)
	print (f"{Dir} is now selected!")



def Android_VersionCheck ():
	AndroidVersion = int(input("What android version is being built? Ex. 10,11,12 \n"))
	if AndroidVersion > 11:
		os.system('. build/envsetup.sh')
	elif AndroidVersion <= 11:
		os.system('source build/envsetup.sh')
	else:
		print ("Please choose a valid option!")
		TextBreak()
		Android_VersionCheck()
	fi


def Ccache_Config ():
	CcacheCon = input("Enable ccache? Y/N")
	if CcacheCon == "Y":
		subprocess.call(['export USE_CCACHE=1'])
		CcacheSpace = input("How much space would you like too allocate in gigabytes? Ex. 50")
		subprocess.call(['ccache -M {CcacheSpace}G'])
	elif CcacheCon == "N":
		subprocess.call(['export USE_CCACHE=0'])
		fi


def DeviceVariant_BuildConfig ():
	DeviceVar = input("What device/variant would you like to build? \n")
	print(f"Building android {AndroidVersion} for {DeviceVar}")
	if AndroidVersion <= 11:
		subprocess.call(['lunch {Rom}_{DeviceVar}'])
	elif AndroidVersion > 12:
		subprocess.call(['lunch {Rom}_{DeviceVar}-{BuildType}'])
	print(f"lunch {Rom}_{DeviceVar}")


def Build_Type ():
	print("What build would you like to make? \n")
	BuildType = input("Options: user|userdebug|eng")


def Start_Build ():
	print("Starting Build")
	if AndroidVersion <= 11:
		 subprocess.call(['bsubprocess.callch {Rom}_{DeviceVar}-{BuildType}'])
		 print(f"{Rom}_{DeviceVar}-{BuildType}")
	elif AndroidVersion > 12:
		subprocess.call(['make $rom -j$nproc'])
		print("Starting build, please wait...")


print("########################")
print("#Automated Build Script#")
print("#By:   XXSEVA44@XDA    #")
print("########################")
Working_DirCheck()
Rom_Check()
Android_VersionCheck()
Ccache_Config()
Build_Type()
DeviceVariant_BuildConfig()
Start_Build()
