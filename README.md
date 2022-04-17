# CleverClip

### Useful commands
    $ pyuic5 interface/main.ui > ui/main.py
    $ i686-w64-mingw32-gcc-win32
    $ c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) utils.cpp -o utils$(python3-config --extension-suffix)
    $ c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) utils.cpp -o utils$(python3-config --extension-suffix) `pkg-config --cflags --libs gtk+-3.0`

### Colors:

1. `#525252` - background color
2. `#414141` - hover
3. `#313131` - borders
4. `#08ffc8` - accent color
5. `#1ee3cf` - more accent color
6. `#a39e9e` - light background
6. `#1F6ED4` - blue (links for example)

![img.png](docs/sources/img.png)


### TODO

- [ ] change ui framework
- [ ] context menus for unions:
  - [ ] image: save image, edit image
  - [ ] link: open in browser
  - [ ] files: open folder
  - [ ] all: pin, delete
- [ ] add pin function:
  - user can pin union and then, when user clicked on `pinned widgets` button, user see only pinned unions
  - pinned widgets saves to memory
- [ ] create new design for application
- [ ] add possibility to resize window
- [ ] add settings of different functions
  - [ ] save all unions
    - [ ] save for `...` days
    - [ ] save only text/images/links/files
  - [ ] save only pinned unions
  - [ ] change theme of the application
  - [ ] change accent color
  - [ ] add smart tab: copied from application, copied from site...
- [ ] add tray icon of the application
- [ ] add function of changing tabs order
- [ ] add or remove some tabs
- [ ] open window when click on icon
