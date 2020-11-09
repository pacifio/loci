# LOCI

LOCI means Lines Of Codes Indicator . A simple python script that will show you how many lines you've written inside your code project !

```bash
git clone https://github.com/pacifio/loci.git
cd loci
```
Now add loci to the path

Now in your project use loci
```bash
cd YOUR_PROJECT
loci.py LANG
```

Suported languages

* html
* css
* javascript
* typescript
* python
* dart
* c
* c++

You can add custom languages . The configuration file lives under ```~/.loci.json```

The configuration for your language is set like this

```json
"LANGUAGE_NAME": {
  "extension": "LANGUAGE_EXTENSION",
  "ids": ["LANGUAGE_ID"]
}
```

Example configuration for ```dart```:
```json
"dart": {
  "extension": ".dart",
  "ids": ["dart", "flutter", ".dart"]
}
```

here the ids are how loci identifies differet languages . For dart

```bash
loci.py dart
```
and
```bash
loci.py flutter
```

both of these commands are the same . These are ids . You can add more languages in the main configuration file which lives at ```~/.loci.json```
