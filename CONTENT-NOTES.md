# 内容来源与维护说明

版本：v2 · 内容精修版。整理时间：2026-09-14。

## 基础资料

姓名、任职、教育、导师、邮箱、照片、研究项目、荣誉和学术服务来自用户提供的魏泽英文简历 PDF。研究介绍和研究方向说明是在该简历范围内整理的中英文主页文案，未添加招生信息、团队身份或量化研究成果。

研究方向保留简历的三个主轴：

1. Edge Computing & Edge Intelligence / 边缘计算与边缘智能。
2. Green Edge Computing & Sustainable Networks / 绿色边缘计算与可持续网络。
3. Integrated Space–Air–Ground–Sea Networks / 空天地海一体化网络。

正文使用邮箱作为联系入口。可打印简历为重新整理的网页版本，未将原始 PDF 中的手机号、投稿编号和分区/影响因子直接公开。

## 论文状态

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| 已发表 | 13 | 12 篇期刊论文、1 篇会议论文；包含硕士阶段的 3 篇研究成果 |
| 已接收 | 1 | 按原简历保留 Accepted，未虚填年份和卷期 |
| 已投稿 | 5 | 按原简历保留 Submitted，与已发表成果分开 |

发表状态以本次提供的简历及用户在会话中明确的后续更新为依据，未通过投稿系统核查。潮汐能海岛物联网的 Survivability-Oriented 稿件已根据此前明确的改投信息更新为 IEEE Communications Letters，状态仍为 Submitted，不展示投稿编号。

## 核对后的主要英文论文链接

| 论文简称 | 链接 |
| --- | --- |
| Green MEC / Island IoT | https://doi.org/10.1109/JIOT.2024.3459098 |
| Contribution-aware clustered FL | https://doi.org/10.1109/JIOT.2025.3635589 |
| Energy anxiety / Maritime IoT | https://doi.org/10.1109/TNSM.2026.3655385 |
| Digital twin / Hierarchical FL | https://doi.org/10.1016/j.comcom.2025.108410 |
| DRL / Green maritime MEC | https://doi.org/10.3390/electronics12244967 |
| ICCC Workshops 2023 | https://doi.org/10.1109/ICCCWorkshops57813.2023.10233832 |
| Traffic grooming / Optical networks | https://ieeexplore.ieee.org/document/10935616/ |
| Spectrum defragmentation | https://doi.org/10.1016/j.yofte.2024.103838 |

DOI 通过 Crossref 的出版商提交元数据核对，结合期刊网页。IEEE 部分元数据仍采用 Early Access 年份，因此正式卷期年份与 DOI 中的年份可能不同；主页使用简历所列的正式卷期。未批量下载或再分发论文全文。

未确认正式文章网址的五篇已发表中文论文保留明确标注的“检索论文 / Find paper”入口。没有用猜测的 DOI 或不相关的文章替代。

## 对原简历的两处作者信息修正

1. **Electronics 2023**：原简历列出 Z. Wei、R. He、C. Song；[期刊官网](https://www.mdpi.com/2079-9292/12/24/4967)列出 Ze Wei、Rongxi He、Yunuo Li、Chengzhi Song。主页已补充 **Y. Li**，顺序以官网为准。
2. **Computer Communications 2026**：原简历第三、四作者顺序为 C. Song、X. Chen；[Crossref 出版商元数据](https://api.crossref.org/works/10.1016/j.comcom.2025.108410)为 Xiaojing Chen、Chengzhi Song。主页按元数据排列，并补充正式卷号 **248**。

此前收集的 ORCID [0009-0006-3838-3790](https://orcid.org/0009-0006-3838-3790) 来自 [Island IoT 论文的 Crossref 作者记录](https://api.crossref.org/works/10.1109/JIOT.2024.3459098)。它尚未由本人确认为当前主账号，因此 v2 已隐藏所有公开页面中的 ORCID 入口和号码；数据文件保留来源记录。确认后，修改 `content.json` 中的 `orcid` 并把 `show_orcid` 设为 `true`，重新生成页面即可恢复。

## 中文表述

部分中文题名依据公开检索记录补充；未确认正式英文题名的中文论文沿用用户简历的英文表述。英文项目名与荣誉来自简历，中文名称为对应译写；如有正式中文立项名称或获奖证书名称，以原件为准。

## 设计与技术

采用浅粉、玫瑰色、暖白和深梅色，首页为个人介绍、研究方向、代表论文、学术经历、项目/荣誉/服务和联系方式。未使用大型框架、在线字体或分析追踪脚本。Inter 字体采用随包提供的 OFL 许可证。

本版照片直接提取自简历，原图为 275 × 367 像素，未做 AI 人像重绘。以后可以用清晰度更高的原始照片替换 `assets/profile.jpg`。


## v2 的具体调整

- 首页先介绍边缘智能、绿色边缘计算与通信—计算—能量协同；空天地海一体化网络在 About 和 Research 中作为进一步研究背景展开。
- 三个研究方向标题保持原样；第一、三项说明作小幅调整，明确已有工作的重点与进一步探索的范围。
- 三篇代表论文保持原选择，简介改为研究问题与处理思路的简要介绍。部分出版商摘要页面访问受限，本轮只依据已确认题名、书目信息和用户简历的研究范围改写，未新增具体算法步骤、定量结果或最优性结论。
- 审稿工作列入“学术服务”，会议报告单列为“学术活动”。软件工具介绍仅保留在简历，归入“研究方法与工具”。
- 六个中英文页面同步生成，粉色配色、样式文件、照片和字体保持不变。

## 仍待原始材料补全的信息

项目的正式中文名称、清华论坛奖项全称，以及机器人大赛获奖年份和具体赛项，目前没有取得立项书或证书作为核对依据。此版保留所提供简历中的信息与对应译写，未猜测补齐。以后取得材料时可在 `content.json` 中更新，无需重做页面。
