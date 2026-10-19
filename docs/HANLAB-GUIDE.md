# HanLab 网站使用说明

这份网站基于 [al-folio 官方仓库](https://github.com/alshedivat/al-folio)，使用其 v1 bootstrap 流程配置为英文实验室网站。
主题的布局、字体和交互由原版插件提供；日常更新主要编辑 Markdown、YAML 和 BibTeX 内容文件。

当前基础资料为 HanLab、湖南大学计算机学院、韩静教授、Healthcare / Audio & Non-audio、`jhan@hnu.edu.cn`。
2026-10-11 已根据公开一手资料补充负责人介绍和照片、学术主页、20 篇近年及代表性论文、3 个合作项目和 3 条动态。
2026-10-12 已按维护者提供的名单加入 3 位 2026 级博士生，并为首页和部分论文加入有来源的图片。
2026-10-19 首页解释 HanLab 的 Healthcare、Audio、Non-audio 含义并集中展示韩静教授简介；People 精简为照片占位、负责人简介和学生卡片。
来源和归属说明见 [公开资料来源](HANLAB-CONTENT-SOURCES.md)；论文包括韩老师在此前机构完成的工作。
更多成员照片和具体招生条件应在确认后添加。
项目概况见 [HanLab 项目说明](HANLAB-PROJECT.md)；仓库原有的 `README.md` 保持原内容。

## 打开预览

在当前电脑上，可以双击网站根目录的 `preview.cmd` 启动预览，再打开 <http://localhost:4000/al-folio/>。
保留启动的终端窗口，关闭终端后预览服务也会停止。这个启动文件会使用本次准备的本地运行环境；换电脑需要重新安装依赖。

Jekyll 源文件需要先构建；直接双击 Markdown 文件不会显示完整网站。准备好 Ruby / Bundler 和 Node.js 后，也可以在网站根目录运行：

```bash
bundle install
npm ci
bundle exec jekyll serve --host 127.0.0.1 --baseurl /al-folio
```

在浏览器打开 <http://localhost:4000/al-folio/>。终端需保持运行，按 `Ctrl+C` 停止。
本地预览命令会临时覆盖路径为 `/al-folio`，不会修改 `_config.yml` 中的正式 `/biubiu17` 配置。
完成 GitHub Pages 部署后的公网地址为 <https://biubiu17.github.io/biubiu17/>；本地预览可用不代表公网已经发布。
修改页面通常会自动重新构建，刷新浏览器即可；修改 `_config.yml` 后应重启预览服务。
完整环境说明见 [官方安装文档](INSTALL.md)，Windows 环境也可按其中的 WSL / Docker 方案配置。

## 内容在哪里修改

| 想修改的内容                   | 对应文件或目录                       |
| ------------------------------ | ------------------------------------ |
| 网站名称、简介、网址、基础开关 | `_config.yml`                        |
| 首页介绍及韩静教授简介         | `_pages/about.md`                    |
| 研究方向                       | `_pages/research.md`                 |
| 论文页面与筛选区域             | `_pages/publications.md`             |
| 论文数据                       | `_bibliography/papers.bib`           |
| 团队负责人、图片展示区         | `_pages/profiles.md`                 |
| 博士生卡片排列方式             | `_pages/people_doctoral_students.md` |
| 学生照片、身份和个人页         | `_pages/student_*.md`                |
| 新闻页面                       | `_pages/news.md`                     |
| 每条新闻                       | `_news/` 中的 Markdown 文件          |
| 项目详情                       | `_projects/` 中的 Markdown 文件      |
| 联系方式和招生联系说明         | `_pages/contact.md`                  |
| 页脚 / 首页社交链接            | `_data/socials.yml`                  |
| 图片                           | `assets/img/`                        |
| 论文缩略图                     | `assets/img/publication_preview/`    |
| 可公开下载的论文 PDF           | `assets/pdf/`                        |

Markdown 文件顶部两行 `---` 之间是配置，请保留缩进和冒号；正文可以直接写英文段落、标题、列表及链接。
新增页面通常使用 `nav: true` 和 `nav_order` 控制菜单显示与顺序。站内链接应使用 `relative_url`，例如：

```liquid
[Contact us]({{ '/contact/' | relative_url }})
```

这样本地 `/al-folio/` 和正式网站 `/biubiu17/` 的链接都能跟随 `baseurl` 工作。

## 添加团队成员

People 页面按 **Principal Investigator** 和 **Doctoral Students** 分组。博士生以可点击的头像卡片展示，姓名、照片和“View profile”均进入站内个人页。
韩静教授的详细介绍放在首页；People 仅展示姓名、职务和通往首页介绍的链接。
顶部图片展示区使用 `assets/img/people/gallery-*.svg` 占位图。以后把照片放入 `assets/img/people/`，再修改 `_pages/profiles.md` 中对应的图片路径和说明文字即可。手机上可左右滑动查看三张图片。

三位现有学生的个人页分别为：

| 学生   | 编辑文件                        | 站内路径               |
| ------ | ------------------------------- | ---------------------- |
| 冯浩玮 | `_pages/student_feng_haowei.md` | `/people/feng-haowei/` |
| 凌鹏   | `_pages/student_ling_peng.md`   | `/people/ling-peng/`   |
| 胡博涵 | `_pages/student_hu_bohan.md`    | `/people/hu-bohan/`    |

### 更换学生照片

将照片放进 `assets/img/people/`，然后修改对应个人页顶部的两项。例如胡博涵：

```yaml
portrait: /assets/img/people/hu-bohan.jpg
portrait_alt: 胡博涵
```

卡片和个人页共同读取这两项，只需修改一次。建议使用居中、接近正方形的照片；照片区域会裁切为正方形。当前没有收到学生照片，使用明确标示“Photo coming soon”的默认头像。

### 补充个人信息或新增学生

直接编辑个人页第二个 `---` 后面的正文，可以继续添加 `## Research interests`、`## Education`、`## Publications` 和个人联系链接。只填写已确认、愿意公开的信息。

新增学生时，复制一份 `_pages/student_*.md`，修改 `title`、唯一的 `permalink`、`cohort`、`member_order` 和照片。保留 `member_group: doctoral`，People 页面就会自动收录，按 `member_order` 排序。`nav: false` 让个人页不占用顶部导航。

学生个人页需要生成网页，因此不要加入 `_config.yml` 的 `exclude`。`people_doctoral_students.md` 是 People 页面读取的内容片段，继续保留在排除列表中。

## 用 DOI 添加论文

**al-folio 使用 `_bibliography/papers.bib` 管理论文**。这是 Jekyll Scholar 使用的 BibTeX 数据文件，和 Greene Lab Website Template 的 `sources.yaml` 是不同的机制。

本项目附带 `bin/import-doi.py`，只需要 Python 3，无需安装第三方包。它通过 DOI 的官方内容协商接口取得 BibTeX 元数据，支持 DOI 或 `https://doi.org/...` 链接。
接口与格式说明见 [Crossref 官方文档](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/)。

在网站根目录的 PowerShell 中运行，先把占位文字替换成自己的论文 DOI：

```powershell
py -3 bin/import-doi.py "这里替换成自己的论文DOI"
```

默认只预览，不改动文件。核对标题、作者、年份和刊物后，增加 `--write` 写入：

```powershell
py -3 bin/import-doi.py "这里替换成自己的论文DOI" --write
```

也可以传入完整 DOI 链接。重复 DOI 会跳过；若不同论文的引用键重名，可用 `--key Han2026Healthcare` 指定唯一引用键。
在 macOS / Linux 上将 `py -3` 换成 `python3`。

该工具不会替你判断论文是否属于实验室。导入后请检查作者拼写、大小写、会议 / 期刊名称和年份；服务不可达或记录不完整时，可以从出版社、Zotero 等导出 BibTeX，再粘贴到同一文件。
不要将本说明中的命令占位文字当作真实 DOI。

论文条目可以按需添加以下 al-folio 字段：

```bibtex
selected = {true},
pdf = {your-paper.pdf},
code = {https://github.com/YOUR_ACCOUNT/YOUR_PROJECT},
abstract = {Your abstract here},
```

将 PDF 放入 `assets/pdf/your-paper.pdf`。需要在首页展示精选论文时，还应在 `_pages/about.md` 设置 `selected_papers: true`。
字段需写在具体论文条目的花括号内，并与前后字段用逗号分隔；不要直接把上面的片段作为独立条目粘贴。
更多字段见 [官方定制文档](CUSTOMIZE.md)。

## 添加新闻与项目

在 `_news/` 新建 `announcement_001.md`，例如：

```markdown
---
layout: post
date: 2026-10-11 09:00:00+0800
inline: true
related_posts: false
---

Write a confirmed lab update here.
```

日期和正文请替换为真实信息。若首页关闭了新闻区，在 `_pages/about.md` 中将 `announcements.enabled` 改为 `true`。

在 `_projects/` 新建 `project_name.md` 可以保存完整项目介绍，例如：

```markdown
---
layout: page
title: Your project title
description: A short description of the project.
importance: 1
category: research
---

Write the project description here.
```

项目详情文件创建后，研究页面会自动显示项目列表；`importance` 数字越小，排列越靠前。
图片、代码仓库、论文链接请使用真实资料。

## 发布到 biubiu17 的 GitHub Pages

目标仓库为 [biubiu17/biubiu17](https://github.com/biubiu17/biubiu17)。它是项目网站，发布后的完整地址为 <https://biubiu17.github.io/biubiu17/>。
`_config.yml` 已为这个目标配置：

```yaml
url: https://biubiu17.github.io
baseurl: /biubiu17
```

源码准备完成后，仍需使用对该仓库有写入权限的 GitHub 账号推送并完成部署。以下步骤用于正式上线，不表示网站已发布：

操作顺序：

1. 登录拥有 `biubiu17/biubiu17` 写入权限的 GitHub 账号。
2. 将这份完整源代码放到该仓库的 `main` 分支，包括 `.github/workflows/deploy.yml`、`Gemfile`、配置和内容文件，并保留仓库原有的 `README.md`；不要上传本地缓存、`node_modules`、`vendor/bundle` 或 `_site`。
3. 在仓库 `Settings → Actions → General → Workflow permissions` 中允许 **Read and write permissions**。仓库启用 Actions 后，提交会触发 **Deploy site**；也可以在 Actions 页面手动运行它。
4. 等待 **Deploy site** 成功并生成 `gh-pages` 分支。
5. 在 `Settings → Pages` 中选择 **Deploy from a branch**，分支为 **gh-pages**，目录为 **/ (root)**。完整源代码保留在 `main`，发布文件由工作流生成。
6. 打开 <https://biubiu17.github.io/biubiu17/>，检查菜单、图片、论文和移动端显示。以后修改源文件并提交，工作流会重新构建发布。

此流程基于 al-folio 官方 `deploy.yml`。当前已明确填写正式地址，工作流会保留它。
如果工作流失败，在 Actions 中查看出错步骤；在构建成功前，网站不会完成更新。
官方细节见 [安装与部署文档](INSTALL.md#enabling-automatic-deployment)。

将来迁移到其他仓库时，可以手动修改 `url` 和 `baseurl`。
工作流还保留一个可选的自动地址功能：当 `url` 设为 `http://localhost:4000` 时，会根据目标仓库生成 GitHub Pages 地址；当前配置不使用这个回退功能。

## 日常更新并发布

当前电脑的网站源码在 `hanlab-al-folio`，工作分支为 `codex/hanlab-al-folio`。
在此目录审阅 `git diff` 后，可以把当前分支的新提交推送到 GitHub 的 `main`。
无需切换本地 `main`；本地旧 `main` 不是当前 HanLab 配置。

以下命令在 CMD 和 PowerShell 中都适用（先进入网站目录）：

```bash
git status
git diff
git add _config.yml _data/socials.yml _pages _bibliography _news _projects assets/img/jing-han.jpg docs/HANLAB-GUIDE.md docs/HANLAB-PROJECT.md docs/HANLAB-CONTENT-SOURCES.md docs/HANLAB-PUBLICATION-SOURCES.md
git commit -m "Add verified Jing Han profile, publications and projects"
git push origin HEAD:main
```

这是本次补充内容的明确文件清单；后续更新可按实际修改调整 `git add` 参数。
如果推送提示远程有新提交，不要加 `--force`；先同步、处理冲突再推送。
Actions 构建和 Pages 发布成功后，公网内容才会更新。本地预览中的新内容不代表已经上传。

## 更新后的检查

日常内容修改后，至少打开首页及改动的页面检查排版和链接。正式提交前可运行：

```bash
npm run lint:prettier
npm run lint:style-contract
bundle exec al-folio upgrade audit --no-fail
bundle exec jekyll build --baseurl /al-folio
```

最后一条用于验证当前本地预览子路径。正式部署由工作流使用 `_config.yml` 中的正式 `baseurl` 构建。
要单独验证正式 `/biubiu17/` 路径，可运行 `bundle exec jekyll build`。
后续优先通过内容和配置调整网站；保留 `Gemfile` 与 `_config.yml` 的插件对应关系，避免为了改正文而复制整套主题布局。
