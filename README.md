# Petty Tools

For the regrettable moments.

## Followback Checker

This command line tool tells you who you follow that doesn't follow you back. Unlike other followback checker tools made for the same purpose, this one is fully privacy-respecting, not requiring you to log into your Instagram account with a third party library. However, it'll take a bit of extra work on your part.

### How to export your list of followers and following

In your web browser on a desktop, log into Instagram. Go to your profile and click the gear icon in the top right. Click "Settings and Privacy", and then find and click the box labeled "Meta Accounts Center". Once in your Accounts Center, click "Your information and permissions" in the sidebar on the left. Click "[Download your information](https://accountscenter.instagram.com/info_and_permissions/dyi/)".

In the overlay that pops up, click "Download or transfer information". Select "some of your information", and scroll down to the "Connections" section. All you need is "Followers and following". Check that box and press next. Select "Download to device", **set the date range to "all time"**, hit "save", and hit "create files".

The download should be ready in a few minutes. Click "download" on the most recent request, and extract the contents of the .zip file. The two pages you will need, `followers_1.html` and `following.html`, will be located in the folder, under `connections/followers_and_following`.

### How to use the script

Drag and drop `followers_1.html` and `following.html` into the same folder as the Python file. Run the Python script on the command line using `python3 followback-checker.py`.
