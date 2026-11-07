# Git & GitHub 学习笔记

> 记录于 2026-11-07，跟着 Codex 实操走完了从建仓库到发 PR 的完整流程。

## 一、日常核心循环（最常用，背下来）

```bash
git pull                              # 开工前：先拉最新
# ... 改代码 ...
git add .                             # 加入暂存区
git commit -m "这次改了什么"           # 提交
git push                              # 收工前：推上去
```

一句话：**改 → add → commit → push**，开工先 pull。

## 二、命令速查表

| 命令 | 作用 |
|---|---|
| `git init` | 在本地初始化一个新仓库 |
| `git clone 地址` | 把远端仓库拉到本地 |
| `git status` | 看当前状态（改了哪些、暂存了哪些） |
| `git diff` | 看具体改了什么内容 |
| `git add 文件` / `git add .` | 把改动加入暂存区 |
| `git commit -m "说明"` | 提交到本地 |
| `git push` | 推送到 GitHub |
| `git pull` | 从 GitHub 拉取最新 |
| `git fetch` | 只下载远端新提交，不合并 |
| `git log --oneline` | 看提交历史（简洁模式） |
| `git switch -c 分支名` | 新建并切换分支 |
| `git switch 分支名` | 切换分支 |
| `git merge 分支名` | 合并分支到当前分支 |
| `git branch -d 分支名` | 删除分支 |
| `git branch` | 看所有本地分支 |

> 旧写法对照：`git switch -c` = `git checkout -b`，`git switch` = `git checkout`。

## 三、关键概念（大白话）

- **仓库 repository**：一个项目的「存档文件夹」，GitHub 上就是一个个项目主页。
- **暂存区 stage**：`git add` 后、`git commit` 前的「待提交清单」。
- **提交 commit**：一个「快照」，记录某时刻文件的样子，有唯一编号（如 `ca42594`）。
- **分支 branch**：在主线上开一条「平行线」做实验，互不干扰，做完合并回主线。
- **合并 merge**：把分支的改动并入当前分支。`Fast-forward` 表示主线没分叉，直接快进。
- **PR（Pull Request）**：网页版的合并，多了「请求别人审核」这一步，本质是带编号的 merge。
- **快进 fast-forward**：合并时主线没有别的提交，直接前进，不产生额外合并提交。

## 四、新手常见坑

1. **建仓库勾了 README** → 本地 push 会冲突。新手建仓库保持「空仓库」，三个选项都不勾。
2. **`main` 和 `master` 不一致** → 用 `git branch -M main` 统一。
3. **`git status` 显示 up to date 却是旧的** → `status` 不主动问远端，先 `git pull` 或 `git fetch`。
4. **push 前忘了 pull** → 远端有别人新提交时 push 会被拒，先 `git pull` 再 `push`。
5. **`.gitignore` 忘了写** → 缓存、密钥、系统文件会被误传。每个项目都该有。

## 五、GitHub 协作全流程（PR）

```
fork / 建分支 → 改代码 → push 分支 → 网页发 PR
     → 审核 Files changed → Merge → 删分支 → 本地 pull 同步
```

对应今天实操：本地建 `add-usage-section` 分支 → 改 README → push → 网页发 PR #1 → 点 Merge → 本地 `git pull`。

## 六、本项目文件说明

- `README.md`：项目说明，别人打开仓库第一眼看到的。
- `hello.py`：可运行的示例代码。
- `.gitignore`：告诉 git 哪些文件不要上传（缓存、系统文件）。
- `git-notes.md`：就是这份笔记。
