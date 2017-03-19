#encoding:utf-8
import sys
import muke_android_test
from com.android.monkeyrunner import MonkeyRunner ,MonkeyDevice ,MonkeyImage

device=MonkeyRunner.waitForConnection(3,'M9N7N15530002084')
device.startActivity('com.android.calculator2/com.android.calculator2.Calculator')
MonkeyRunner.sleep(2)
device.touch(200,1000,'DOWN-AND-UP')
MonkeyRunner.sleep(1)
device.touch(1000,1200,'DOWN-AND-UP')
MonkeyRunner.sleep(1)
device.touch(600,1200,'DOWN-AND-UP')
MonkeyRunner.sleep(1)
device.touch(1000,1800,'DOWN-AND-UP')
MonkeyRunner.sleep(2)
image=device.takeSnapshot()
image.writeToFile('./Downloas.png','png')
MonkeyRunner.sleep(2)
