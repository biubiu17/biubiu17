# HanLab

HanLab at Hunan University, led by Professor Jing Han (韩静).
Research: healthcare, audio and non-audio. Contact: jhan@hnu.edu.cn.

本项目直接使用官方 **al-folio v1**，保留原版布局、字体、导航、深色模式和论文排版。

- [中文使用说明](HANLAB-GUIDE.md)
- [公开内容来源与待补资料](HANLAB-CONTENT-SOURCES.md)
- [官方安装与部署说明](INSTALL.md)
- [使用的 bootstrap 技能](../.agents/skills/al-folio-bootstrap/SKILL.md)

## 本地预览

在此电脑上双击 `preview.cmd`，在浏览器访问 `http://localhost:4000/al-folio/`。首次构建后再打开网页；关闭命令窗口即可停止服务。

源文件是 Markdown / YAML / BibTeX，需要 Jekyll 构建，不能直接双击源文件预览。

## 发布

发布目标已配置为 `biubiu17/biubiu17`，正式网址为 `https://biubiu17.github.io/biubiu17/`。
推送后，`Deploy site` 工作流会构建 `gh-pages` 分支；仓库需要先完成 GitHub Pages 设置。
在仓库 Settings → Pages 中选择 Deploy from a branch → gh-pages → / (root)。如使用自定义域名，按中文说明修改发布配置。

## 来源

来自 [alshedivat/al-folio](https://github.com/alshedivat/al-folio)，官方源版本 `c479d7e815907076abd0932166ff1af47038de92`（2026-10-11 获取）。
通过 GitHub 官方源文件下载并逐文件校验 Git blob SHA；没有引入示例媒体。
模板遵循 MIT License，见 [LICENSE](../LICENSE)。未创建主题布局、组件或 CSS 的本地覆盖。
