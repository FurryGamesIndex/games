# Build Furry Games Index website from source

Tested operating systems:

- macOS Catalina
- Ubuntu 20.04
- Windows 10

You need Python 3.7 or later. (If you are using CPython, 3.6 is also acceptable)

## Install dependencies

```
pip3 install --user pyyaml jinja2 requests Pillow beautifulsoup4
```

Currently, a [patched python-markdown2](https://github.com/FurryGamesIndex/python-markdown2) (added many features needed for FGI) is required to build FGI website.

```
pip3 install --user git+https://github.com/FurryGamesIndex/python-markdown2
```

(Optional) For Chinese Converting, you need

```
pip3 install --user OpenCC
```

## Build website

(Optional) If you have modified zh-xx files, run it to generate other variants (for example, zh-cn => zh-tw, etc)

```
./zhconv.py
```

Do a general build

```
./generate.py <output_path>
```

## Build options

### Webp images

#### Convert images to webp and remove original image

```
./generate.py --images-to-webp
```

#### Convert webp format and make it as a candition for browsers (double format will be provided)

```
./generate.py --images-candidate-webp
```

### Add workaround hacks to make it runable on local `file://` in modern browsers

Modern browsers block file requests from `file://` scheme. This will cause some functions in standard builds to not work properly.

FGI can inject some hacks to make builds available in `file://` scheme. Tested on Chrome and Firefox.

This will waste space and affect performance. Do not enable this option on a version designed to be published online.

> For Chrome/Chromium, you can run browser like the `google-chrome --allow-file-access-from-files` to disable this browser security mechanism.
>
> For Firefox, you can disable this browser security mechanism by `security.fileuri.strict_origin_policy` in `about:config`.

```
./generate.py --file-uri-workaround
```

### Plugins

Use `--plugin name[,options]` argument to load plugin.

For example, the `steam-cdn-unite` plugin will unite all steam CDN URIs:

```
./generate.py --plugin steam-cdn-unite
```

You can pass plugin specified options to them. format is `key=value`, multiple options joined with `,`. For example:

```
./generate.py --plugin steam-cdn-unite,cdn=akamai,verbose=1
```

You can load multiple plugins, for example:

```
./generate.py --images-candidate-webp --plugin steam-cdn-unite,verbose=yes --plugin webp-converter-stub
```

### More Options

see `./generate.py -h`

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

