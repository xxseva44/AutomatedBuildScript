#!/bin/bash

#Fint the rom
Rom=$(<temp/BuildConfR.txt)
  echo "$Rom"

#Find the device
DeviceVar=$(<temp/BuildConfD.txt)
  echo "$DeviceVar"

#Find the build type
BuildType=$(<temp/BuildConfB.txt)
  echo "$BuildType"

AndroidVersion=$(<temp/BuildConfA.txt)
  echo "$AndroidVersion"

Thread=$(<temp/BuildConfT.txt)
  echo "$Thread"

lunch ${Rom}_$DeviceVar
echo "lunch ${Rom}_$DeviceVar"
