## rpmbuild usage examples

### SPECS

- `SPECS/cello.spec`  source code compile
- `SPECS/s3test.spec` package binary
- `SPECS/openresty-x86_64.spec` comple openresty



### Usage

```bash
rpmbuild -bb SPECS/cello.spec
```

Output directory is **RPMS**.


### test
#### list files
```bash
rpm2cpio xxx.rpm | cpio -t
```
