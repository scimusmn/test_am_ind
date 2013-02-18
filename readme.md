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

### 4. Download chrome_kiosk
```bash
$ git clone git://github.com/scimusmn/chrome-kiosk.git
```

### 5. Configure
```bash
$ cp browser.cfg.default browser.cfg
```
Edit the browser.cfg file and define your values.

### 6. Run chrome_kiosk
```bash
$ cd chrome_kiosk
$ python chrome_kiosk
```
