# Work in Progress
This is an untested sketch and is not ready for production.

# Installation
### 1. Install Python
### 2. Install the Selenium Python wrapper

```bash
$ sudo pip install selenium
```

### 3. Install ChromeDriver
Download and install the [appropriate version of ChromeDriver for your OS](http://code.google.com/p/chromedriver/downloads/list)

### 4. Download test_am_in
```bash
$ git clone git@github.com:scimusmn/test_am_ind.git
```

### 5. Configure
If you need to change any of the configurations you can edit the browser.cfg file, but some elements are still hard coded into the browser.py file. So this config isn't that changeable yet.

### 6. Run chrome_kiosk
```bash
$ cd test_am_in
$ chmod +x browser.py
$ ./browser.py
```
