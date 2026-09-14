# 魏泽 / Ze Wei 学术主页 v2

柔和粉色主题，包含中英文首页、完整论文页、可打印简历、照片和本地字体。网站已经生成，无需安装 Node.js、Python 或任何软件即可查看、上传。


## v2 更新内容

本版保留粉色风格，精修首页研究定位和代表论文简介，更新 IEEE Communications Letters 投稿记录，整理学术服务与活动，暂时隐藏待本人确认的 ORCID 入口。未确认的项目与奖项细节见 `CONTENT-NOTES.md`。

如果已经上传 v1：将本包解压后的文件上传到同一仓库根目录，覆盖同名文件即可，无需重建仓库或重新设置 Pages。发布完成后可按 Ctrl+F5 刷新页面。

## 先在电脑上查看

1. 将压缩包完整解压到一个文件夹。
2. 双击 `index.html` 查看英文首页。
3. 点击右上角“中文”，或直接打开 `zh/index.html` 查看中文首页。
4. 点击“学术成果 / Publications”使用论文分类、检索及引用功能。
5. 点击“个人简历 / View CV”，再点“打印 / 另存为 PDF”。在浏览器打印对话框中选择“另存为 PDF”，可关闭浏览器自动添加的页眉页脚。

请先解压，再打开网页；直接在压缩包内打开 HTML 可能丢失样式和照片。

## 在你的 GitHub 账号下发布

可以创建独立仓库来存放魏泽的主页。建议仓库名：`ze-wei`。

1. 登录你的 GitHub 账号，右上角点击 **+ → New repository**。
2. Repository name 填写 `ze-wei`，选择 **Public**。可以勾选 **Add a README file**，然后点击 **Create repository**。
3. 进入新仓库，选择 **Add file → Upload files**。
4. 把解压后的网页文件和文件夹上传到仓库根目录，点击 **Commit changes**。根目录必须直接包含 `index.html`，不要把外层文件夹整个套在根目录下，也不要只上传 ZIP。
5. 打开仓库 **Settings → Pages**。
6. 在 **Build and deployment** 中，将 Source 设为 **Deploy from a branch**。
7. Branch 选择 **main**，目录选择 **/ (root)**，点击 **Save**。
8. 等待发布完成后，Pages 页面会显示网站地址。可以到 **Actions** 查看部署进度。

如果账号仍为 `Leon1995-ai`，且新仓库名为 `ze-wei`，发布成功后的英文主页地址是：

[https://Leon1995-ai.github.io/ze-wei/](https://Leon1995-ai.github.io/ze-wei/)

中文主页地址是：

[https://Leon1995-ai.github.io/ze-wei/zh/](https://Leon1995-ai.github.io/ze-wei/zh/)

这两个地址是按推荐仓库名说明的未来发布地址，本交付包尚未上传到 GitHub。仓库名改变时，地址中的 `ze-wei` 相应改变。

所有网页资源采用相对路径，适合 GitHub Pages 的项目子目录。

GitHub 官方说明：[配置 GitHub Pages 发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 文件用途

| 文件 | 用途 |
| --- | --- |
| `index.html` | 英文首页 |
| `publications.html` | 英文论文页 |
| `cv.html` | 英文可打印简历 |
| `zh/` | 对应的三个中文页面 |
| `style.css` | 粉色主题与手机适配样式 |
| `site.js` | 导航、论文筛选、检索、复制引用与打印 |
| `assets/` | 照片、图标和本地字体；请完整上传 |
| `content.json` | 中英文内容数据 |
| `build.py` | 可选的网页重新生成脚本 |
| `CONTENT-NOTES.md` | 内容来源、已修正信息和待核对事项 |

## 后续更新

通常只需修改 `content.json`，再在当前目录运行 `python3 build.py`（Windows 也可用 `py build.py`），即可同步生成六个页面，然后上传更新的文件。

这个脚本只依赖 Python 标准库。日常浏览和首次上传完全不需要运行它。不要仅修改数据文件而遗漏重新生成 HTML；网页显示的是已生成的 HTML。

如直接手动修改 HTML，请同时更新相应语言页面，后续重新运行脚本会覆盖这些直接修改。

## 检查范围

交付前检查了六个页面的内部路径、锚点、资源文件、论文状态数量及 JavaScript 语法，并用 DOM 功能检查验证导航、分类、检索、论文定位与复制引用逻辑。尚未在浏览器中逐屏完成桌面和手机视觉验收；浏览器打印后的 PDF 分页也需以实际打印预览为准。
