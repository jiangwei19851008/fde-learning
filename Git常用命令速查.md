# Git 常用命令速查

> 面向用过 SVN、正在转 Git 的同学。每条命令后面标注了对应的 SVN 操作。

---

## 一、初始化 / 克隆（一次性操作）

```bash
git init                          # 当前目录建成 Git 仓库
git clone https://xxx.git         # 从远程复制整个仓库到本地（≈ svn checkout）
git clone https://xxx.git mydir   # 克隆并重命名目录
git remote add origin https://xxx.git   # 首次关联远程仓库
git remote -v                     # 查看当前关联的远程地址
```

---

## 二、日常三步曲（90% 时间就在这三条）

```bash
git status                        # 看当前状态：改了哪些文件（≈ svn status）
git add .                         # 把所有改动加入暂存区
git commit -m "说明这次改了什么"    # 拍快照提交到本地（≈ svn commit，但不连服务器）
```

> **关键区别**：`git commit` 只提交到**本地**，服务器还看不到。要同步上去必须再 `git push`。

---

## 三、和远程同步

```bash
git push                          # 把本地 commit 推到远程（≈ svn commit）
git pull                          # 拉取远程最新并自动合并（≈ svn update）
git fetch                         # 只拉取不合并（先看看别人改了啥）
```

---

## 四、查看历史

```bash
git log                           # 完整提交历史
git log --oneline                 # 一行一条，简洁版（最常用）
git log --oneline --graph         # 带分支图形的历史
git diff                          # 看还没 add 的改动
git diff --staged                 # 看已经 add 的改动
git show <commit-id>              # 看某次提交具体改了什么
```

---

## 五、撤销 / 回退（改坏了怎么办）

```bash
git restore 文件名                 # 丢弃某个文件的未提交改动（改动直接没了）
git reset HEAD 文件名              # 把文件从暂存区撤出（add 错了用这个）
git reset --soft HEAD~1           # 撤销上一次 commit，但保留改动
git reset --hard HEAD~1           # 撤销上一次 commit 且丢弃改动（危险！）
git revert <commit-id>            # 生成一个新 commit 来抵消某次提交（安全，团队推荐）
```

---

## 六、分支

```bash
git branch                        # 列出本地分支
git branch -a                     # 列出本地 + 远程所有分支
git switch -c 新分支名             # 新建并切换过去（≈ svn copy 但瞬间完成）
git switch 分支名                  # 切换到已有分支
git merge 其他分支                  # 把其他分支合并进当前分支
git branch -d 分支名               # 删除已合并的分支
```

---

## 七、忽略文件（重要）

新建 `.gitignore` 文件，写上不想提交的内容：

```
__pycache__/
*.pyc
.vscode/
*.log
jx_bidding.csv
```

---

## 八、最常用的 8 条（背下来就够用）

```bash
git status                  # 我改了啥
git add .                   # 全加进去
git commit -m "说明"         # 拍快照
git push                    # 传上远程
git pull                    # 拉最新
git log --oneline           # 看历史
git diff                    # 看具体改动
git restore 文件             # 后悔了，丢弃改动
```

---

## SVN 对照表

| 动作 | SVN | Git |
|------|-----|-----|
| 拿到代码 | `svn checkout` | `git clone` |
| 看改了啥 | `svn status` | `git status` |
| 提交 | `svn commit`（直接上服务器） | `git add` + `git commit`（本地）+ `git push`（上远程） |
| 更新 | `svn update` | `git pull` |
| 回到老版本 | `svn update -r 1234` | `git checkout <commit-id>` |
| 开分支 | `svn copy URL/branches/xxx`（慢，服务器真复制） | `git switch -c xxx`（瞬间，只是指针） |

---

## 概念速记

```
Git      = 工具（装在你电脑上的 git.exe）
GitHub   = 服务（网站，存放远程仓库）
Gitee    = 国内版 GitHub，速度更快
SVN      = 集中式版本管理（必须连服务器）
Git      = 分布式版本管理（每个人都有一份完整仓库，断网也能干活）
```

---

## 备注

- 第一次提交前要配置身份（只需一次）：
  ```bash
  git config --global user.name "你的名字"
  git config --global user.email "你的邮箱"
  ```
- 检查是否配置成功：`git config --list`
