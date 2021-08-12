

# Press "Page Down" key for me in a period of time

When you're reading a pdf book, do you want somebody (some code) press page down for you in a period of time?
This code does, just give right permission to this code and make a symbolic link or just copy this code to /usr/bin
After that, measure the reading time of one page and run code with one parameter (that time).

for make link:
```bash
cd /usr/bin
sudo ln -s -T /path-to-file/press_pageDown.py press_pageDown
```

for use:
```bash
press_PageDown 16.12
```
or just:
```bash
press_PageDown 16
```
Note: after 2 minutes of using this code, i understood which this code is completely useless :)
bye ;)
