# Build Furry Games Index website from source

Tested operating systems:

- macOS Catalina
- Ubuntu 20.04
- Windows 10 (Partially available)

You need Python 3.7 or later. (If you are using CPython, 3.6 is also acceptable)

## Install dependencies

```
pip3 install --user pyyaml jinja2 requests Pillow
```

Currently, a patched python-markdown2 (added [image filter supporting](https://github.com/FurryGamesIndex/python-markdown2/commit/51cab36062baa4a46a7a414c7c95bcbd161a1049)) is required to build FGI website.

```
pip3 install --user git+https://github.com/FurryGamesIndex/python-markdown2
```

(Optional) For Chinese Converting, you need (Seems not working on Windows due to encoding problem)

```
pip3 install --user OpenCC
```

## Build website

(Optional) If you have changed zh-cn files, run it to generate zh-tw files

```
./zhconv.py
```

Do a general build

```
./generate.py <output_path>
```

## Build offline snapshot version (Not working on Windows)

```
./scripts/build-offline-version.sh <output_path>
```

## More Options

see `./generate.py -h`
