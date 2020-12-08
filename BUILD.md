# Build Furry Games Index website from source

Tested operating systems:

- macOS Catalina
- Ubuntu 20.04
- Windows 10

You need Python 3.7 or later. (If you are using CPython, 3.6 is also acceptable)

## Install dependencies

```
pip3 install --user pyyaml jinja2 requests Pillow
```

Currently, a patched python-markdown2 (added [image filter supporting](https://github.com/FurryGamesIndex/python-markdown2/commit/51cab36062baa4a46a7a414c7c95bcbd161a1049)) is required to build FGI website.

```
pip3 install --user git+https://github.com/FurryGamesIndex/python-markdown2
```

(Optional) For Chinese Converting, you need

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

## Build offline snapshot editiom

```
./scripts/build-offline-version.sh <output_path>
```

> On Windows, you should use [MSYS2](https://www.msys2.org)
> 
> This requires a good internet connection.

## Build FGI-next (FGI with experimental patches)

FGI-next requires a `git` command and FGI source tree MUST be in a cleaning git workspace.

```
./scripts/fix-mtime.sh
./scripts/build-next.sh init origin
./scripts/build-next.sh build <output_path>
```

> On Windows, you should use [MSYS2](https://www.msys2.org)
>
> If FGI git remote name is not "origin", please use `./scripts/build-next.sh init <your remote name>` instead.
>
> The script cannot clean up the git workspace after patching when the build fails, you need to clean it up manually. It can be automatically cleaned up when building successfully.

## More Options

see `./generate.py -h`
