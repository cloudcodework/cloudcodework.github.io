# algorithm-design-implementation-case.github.io

## Notes

### 每次打开新的Gitpod之后如何 push _site to gh-pages branch

[publish.sh](publish.sh)

```bash
bash publish.sh
```

> [https://stackoverflow.com/a/35798092/4295046](https://stackoverflow.com/a/35798092/4295046)

### 如何更新内容

1. 修改 `_data/cases.csv`
2. 执行 `python create_cases.py`

### 如何上传PPT

1. PPT文件命名为 ch_<chapter_id>.pptx, 如 ch_1.pptx
2. 上传到/downloads/ppt/目录下
3. 添加元数据，分别编辑 /data/cases.csv 和 /data/ppt_list.csv
4. 注意：/data/cases.csv 中ppt_url列，路径开头要加上 `/`，绝对路径
5. 注意：/data/ppt_list.csv中的url字段，开头要加 `/`，绝对路径

### Dev参考

- Liquid [https://shopify.dev/api/liquid](https://shopify.dev/api/liquid)
- Jekyll [https://jekyllrb.com/docs/](https://jekyllrb.com/docs/)
