#!/bin/bash
cd "$( dirname "$0" )"
java -Xmx1024M -Xms1024M -XX:MaxPermSize=256M -Dfile.encoding=UTF-8 -jar spigot.jar