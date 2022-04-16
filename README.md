# linux_bufer

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