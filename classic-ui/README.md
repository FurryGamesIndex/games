# Classic UI archives for FGI

FGI can change the page theme through the `uimod` plugin.
The UI used in the history of FGI is packaged in a format recognized by `uimod` plugin and stored in the `classic-ui` subdirectory.

The history of FGI UI generations:

+ pioneer: the 1th Gen UI (classic-ui/pioneer)
+ peafowl: current UI

While classic-ui may be used to build optional UI, they lack maintenance and therefore may not be built with the latest FGI.
Their quality is not guaranteed and they should only used for historical archiving.

For example, if you want to render FGI with the `pioneer` UI, run

```
./generate.py --plugin uimod,mod=classic-ui/pioneer <output path>
```
