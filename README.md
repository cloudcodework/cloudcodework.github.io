# algorithm-design-implementation-case.github.io

## Notes

### 每次打开新的Gitpod之后如何 push _site to gh-pages branch

一行：初始化

```bash
rm -rf _site &&\
mkdir -p _site/ &&\
git clone -b gh-pages `git config remote.origin.url` _site &&\
git config pull.rebase false
```

一行：push

```bash
cd _site &&\
git config pull.rebase false &&\
rm -f README.md &&\
git add -A &&\
git commit -a -m "update" &&\
git push ;\
cd ..
```

> [https://stackoverflow.com/a/35798092/4295046](https://stackoverflow.com/a/35798092/4295046)

### 如何更新内容

1. 修改 `_data/cases.csv`
2. 执行 `python create_cases.py`
