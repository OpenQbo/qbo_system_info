#!/usr/bin/env python

import sys
import ConfigParser
import commands
import os
import roslib; roslib.load_manifest('qbo_system_info')
import rospy
from qbo_system_info.srv import AskInfo


def handle_service(req):
    config=ConfigParser.ConfigParser()

    path = roslib.packages.get_pkg_dir("qbo_system_info")
    config.readfp(open(path+"/config/main.conf"))
    allsections=config.sections()
    for i in allsections:
	if req.command==config.get(i,"input"):
		execparams=config.get(i, "command")
		result=commands.getoutput(execparams)
		return result
    return "Error, input not exist"

def init_server():
    rospy.init_node('pluginsystem')
    s = rospy.Service('/pluginsystem', AskInfo, handle_service)
    rospy.spin()

if __name__ == "__main__":
    init_server()

