

> 更新服务器代码到本地

```
git fetch origin master //从远程的origin仓库的master分支下载代码到本地的origin master

$ git log -p master.. origin/master //比较本地的仓库和远程参考的区别

$ git merge origin/master
```


> 提交代码到服务器


```
git add .

git commit -m "commit"

git push -u origin master
```


```
execute the md document
pip install https://github.com/mli/notedown/tarball/master

pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable execute_time/ExecuteTime

#jupyter notebook --allow-root
jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager' --allow-root
```


https://community.cloud.databricks.com/login.html?user=raidery%40gmail.com
