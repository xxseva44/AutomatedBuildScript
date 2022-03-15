#!/bin/bash

#Find the rom
FindRom() {
Rom=$(<BSAddons/temp/BuildConfR.txt)
  echo "$Rom"
}

#Find the device
FindDevice() {
DeviceVar=$(<BSAddons/temp/BuildConfD.txt)
  echo "$DeviceVar"
}

#Find the build type
FindBuildType() {
BuildType=$(<BSAddons/temp/BuildConfB.txt)
  echo "$BuildType"
}

#Find android Android version
FindAndroidVersion() {
AndroidVersion=$(<BSAddons/temp/BuildConfA.txt)
  echo "$AndroidVersion"
}

Start_Build () {
  if [[ $AndroidVersion -le 11 ]]; then
  	echo "brunch ${Rom}_$DeviceVar-$BuildType"
    echo brunch ${Rom}_$DeviceVar-$BuildType

	elif [[ $AndroidVersion -gt 11 ]]; then
  	echo "make $Rom -j$(nproc)"
    make $Rom -j$(nproc)
  fi
}

FindRom
FindDevice
FindBuildType
FindAndroidVersion

cd -
pwd

Start_Build
