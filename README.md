# Clone

```
git clone https://github.com/bhrte/can-utils-systemd.git
```

# Build

```
rpmbuild -D '_topdir %(echo $PWD)' -ba SPECS/can-utils-systemd.spec
```
