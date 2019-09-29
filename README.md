# FBM-Parse

This is a small project to experiment with quantifying facebook data. I downloaded my messenger data from Facebook, which allows for JSON export, and ran it through a custom python script.

The script allows for counting messages with a single participant or a group of participants, and will export the result into an .xls file, which can be read by excel.

# How to use
You need python installed on your machine.
Download your facebook data from facebook. You only need the messenger part for this program. 
Once downloaded, put them anywhere on your machine, copy down the filepath to message_1.json in any of the conversation folders.
Use any terminal and run "py countmessages_g.py". Afterwards you need to input the relative filepath to message_1.json.
The data will be exported to stats_xls.xls which will be placed in the same folder as countmessages_g.py.
