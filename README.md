# CleverClip

### Useful commands
    $ pyuic5 interface/new_main.ui > ui/main.py
    $ i686-w64-mingw32-gcc-win32
    $ c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) utils.cpp -o utils$(python3-config --extension-suffix)
    $ c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) utils.cpp -o utils$(python3-config --extension-suffix) `pkg-config --cflags --libs gtk+-3.0`

### Colors:

1. `#525252` - background color  ![#525252](https://via.placeholder.com/15/525252/525252.png)
2. `#414141` - hover  ![#414141](https://via.placeholder.com/15/414141/414141.png)
3. `#313131` - borders  ![#313131](https://via.placeholder.com/15/313131/313131.png)
4. `#08ffc8` - accent color  ![#08ffc8](https://via.placeholder.com/15/08ffc8/08ffc8.png)
5. `#1ee3cf` - more accent color  ![#1ee3cf](https://via.placeholder.com/15/1ee3cf/1ee3cf.png)
6. `#a39e9e` - light background  ![#a39e9e](https://via.placeholder.com/15/a39e9e/a39e9e.png)
7. `#1F6ED4` - blue (links for example)  ![#1F6ED4](https://via.placeholder.com/15/1F6ED4/1F6ED4.png)

![img.png](docs/sources/img.png)


### TODO

- [ ] make show_window and hide_window override
- [x] show content by clicking on middle mouse
  - [ ] copy some **(not all)** text from details window
- [ ] create orange shadow effect for current tab button
- [ ] context menus for unions:
  - [ ] image: save image, edit image
  - [ ] link: open in browser
  - [ ] files: open folder
  - [ ] all: pin, delete
- [ ] add pin function:
  - user can pin union and then, when user clicked on `pinned widgets` button, user see only pinned unions
  - pinned widgets saves to memory
- [x] create new design for application
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
