> 提交代码到服务器


```
git add .

git commit -m "commit"

git push -u origin master
```


> 更新服务器代码到本地

```
git fetch origin master //从远程的origin仓库的master分支下载代码到本地的origin master

$ git log -p master.. origin/master //比较本地的仓库和远程参考的区别

$ git merge origin/master
```
