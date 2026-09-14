"""Build the bilingual static website. Python 3 standard library only.
Edit content.json, then run: python3 build.py
"""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parent
D = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
E = lambda s: escape(str(s), quote=True)

PATHS = {
 'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
 'external':'<path d="M7 17 17 7M7 7h10v10"/>',
 'mail':'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 7 8 6 8-6"/>',
 'menu':'<path d="M4 7h16M4 12h16M4 17h16"/>',
 'pin':'<path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 0 1 14 0Z"/><circle cx="12" cy="10" r="2.5"/>',
 'intelligence':'<rect x="6" y="6" width="12" height="12" rx="3"/><path d="M9 2v4m6-4v4M9 18v4m6-4v4M2 9h4m-4 6h4m12-6h4m-4 6h4"/><path d="M10 10h4v4h-4z"/>',
 'sustainability':'<path d="M19 4C9 3 4 7 4 13a7 7 0 0 0 7 7c6 0 9-6 8-16Z"/><path d="M5 20 16 8m-6 7h5m-5 0v-5"/>',
 'networks':'<circle cx="12" cy="12" r="3"/><circle cx="4" cy="4" r="2"/><circle cx="20" cy="4" r="2"/><circle cx="4" cy="20" r="2"/><circle cx="20" cy="20" r="2"/><path d="m6 6 4 4m4 0 4-4M6 18l4-4m4 0 4 4"/>',
 'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
 'print':'<path d="M7 8V3h10v5M7 16H4V9h16v7h-3M7 13h10v8H7z"/>',
 'copy':'<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M15 8V3H3v13h5"/>',
}
def icon(name):
    return f'<svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PATHS[name]}</svg>'

def tr(en, zh, lang): return zh if lang == 'zh' else en
def local(value, lang): return value[lang]
def xlink(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{E(url)}" target="_blank" rel="noopener noreferrer">{label}{icon("external")}</a>'

def header(lang, page):
    home = 'index.html'
    links = [(home+'#research',tr('Research','研究方向',lang)),('publications.html',tr('Publications','学术成果',lang)),(home+'#experience',tr('Experience','学术经历',lang)),(home+'#contact',tr('Contact','联系',lang))]
    nav = ''.join(f'<a href="{u}"'+(' aria-current="page"' if page=='publications' and u=='publications.html' else '')+f'>{t}</a>' for u,t in links)
    other = ('../' if lang=='zh' else 'zh/') + page + '.html'
    return f'''<a class="skip-link" href="#main">{tr('Skip to content','跳至正文',lang)}</a>
<header class="site-header"><div class="shell header-inner">
<a class="brand" href="index.html" aria-label="{tr('Ze Wei home','魏泽的学术主页',lang)}"><span class="monogram" aria-hidden="true">zw<span>·</span></span><span>Ze Wei <span class="brand-cn">魏泽</span></span></a>
<nav class="desktop-nav" aria-label="{tr('Main navigation','主导航',lang)}">{nav}</nav>
<div class="header-actions"><a class="language-link" href="{other}" lang="{tr('zh-CN','en',lang)}" hreflang="{tr('zh-CN','en',lang)}">{tr('中文','EN',lang)}</a><button class="menu-button" id="menuButton" type="button" aria-expanded="false" aria-controls="mobileNav" aria-label="{tr('Open navigation','打开导航',lang)}">{icon('menu')}</button></div>
</div><nav class="mobile-nav shell" id="mobileNav" hidden aria-label="{tr('Mobile navigation','移动导航',lang)}">{nav}</nav></header>'''

def footer(lang):
    return f'''<footer class="site-footer shell"><p>© 2026 {E(D['name'][lang])}<span class="footer-dot">·</span>{E(D['university'][lang])}</p><div><a href="cv.html">{tr('Curriculum vitae','个人简历',lang)}</a><a href="#top">{tr('Back to top ↑','返回顶部 ↑',lang)}</a></div></footer>'''

def document(body, lang, page, title, desc):
    base = '../' if lang=='zh' else ''
    alternate = ('../' if lang=='zh' else 'zh/')+page+'.html'
    return f'''<!doctype html>
<html lang="{tr('en','zh-CN',lang)}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#a33461"><title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:locale" content="{tr('en_US','zh_CN',lang)}"><link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"><link rel="alternate" hreflang="{tr('zh-CN','en',lang)}" href="{alternate}"><link rel="stylesheet" href="{base}style.css"><script src="{base}site.js" defer></script><noscript><style>@media(max-width:800px){{.mobile-nav[hidden]{{display:block!important}}}}.menu-button,.copy-citation,.print-button{{display:none!important}}</style></noscript></head>
<body id="top" class="page-{page}">{header(lang,page)}<main id="main">{body}</main>{footer(lang)}</body></html>'''

def section_head(kicker, title, note='', link=''):
    return f'<div class="section-heading"><div><p class="eyebrow">{kicker}</p><h2>{title}</h2>{f"<p class=section-note>{note}</p>" if note else ""}</div>{link}</div>'

def photo(lang, base):
    return f'''<div class="portrait-stage"><div class="portrait-orbit orbit-one" aria-hidden="true"></div><div class="portrait-orbit orbit-two" aria-hidden="true"></div><span class="orbit-dot dot-one" aria-hidden="true"></span><span class="orbit-dot dot-two" aria-hidden="true"></span><div class="portrait-card"><div class="portrait-topline"><span>ZE WEI</span><span aria-hidden="true">✳</span></div><img src="{base}assets/profile.jpg" alt="{tr('Portrait of Ze Wei','魏泽的个人照片',lang)}" width="275" height="367" fetchpriority="high"><div class="portrait-caption"><span>{tr('Wireless networks<br>& edge intelligence','无线网络<br>与边缘智能',lang)}</span>{icon('external')}</div></div><div class="portrait-note">{icon('pin')}<span>{E(D['location'][lang])}</span></div></div>'''

def authors_html(authors):
    return E(authors).replace('Z. Wei*','<strong>Z. Wei<sup>*</sup></strong>').replace('Z. Wei,','<strong>Z. Wei</strong>,').replace('Z. Wei.','<strong>Z. Wei</strong>.').replace('and Z. Wei','and <strong>Z. Wei</strong>')

def selected_paper(p,lang,i):
    venue = 'IEEE IoT Journal' if p['venue']=='IEEE Internet of Things Journal' else p['venue']
    url = 'https://doi.org/'+p['doi'] if p['doi'] else p['url']
    return f'''<article class="selected-paper"><div class="paper-side"><span class="small-index">0{i}</span><span class="venue-name">{venue}</span><span class="paper-year">{p['year']}</span></div><div class="paper-main"><span class="topic-label">{E(p['tag'][lang])}</span><h3><a href="publications.html#paper-{p['id']}">{E(p['title'])}</a></h3><p class="authors">{authors_html(p['authors'])}</p><p class="paper-summary">{E(p['summary'][lang])}</p><div class="selected-links">{xlink(url,tr('Read paper','论文链接',lang))}<a class="quiet-link" href="publications.html#paper-{p['id']}">{tr('Citation','引用信息',lang)} {icon('arrow')}</a></div></div></article>'''

def research_cards(lang):
    items=[]
    for i,r in enumerate(D['research'],1):
        tags=''.join(f'<span>{E(t)}</span>' for t in r['tags'][lang])
        items.append(f'''<article class="research-card research-{i}"><div class="research-top"><span class="research-icon">{icon(r['key'])}</span><span class="small-index">0{i}</span></div><p class="eyebrow">{E(r['label'][lang])}</p><h3>{E(r['title'][lang])}</h3><p class="research-text">{E(r['text'][lang])}</p><div class="research-tags">{tags}</div></article>''')
    return '<div class="research-grid">'+''.join(items)+'</div>'

def experience(lang):
    employment=f'''<div class="timeline-item"><div class="timeline-date">{tr('Jun. 2026 — Present','2026.06 — 至今',lang)}</div><div><span class="mini-label">{tr('ACADEMIC APPOINTMENT','学术任职',lang)}</span><h3>{E(D['university'][lang])}</h3><p>{E(D['role'][lang])} · {E(D['school'][lang])}</p></div></div>'''
    rows=[employment]
    for edu in D['education']:
        rows.append(f'''<div class="timeline-item"><div class="timeline-date">{E(edu['period'][lang])}</div><div><span class="mini-label">{E(edu['degree'][lang])}</span><h3>{E(edu['institution'][lang])}</h3>{f'<p>{E(edu["note"][lang])}</p>' if edu['note'][lang] else ''}</div></div>''')
    return '<div class="timeline">'+''.join(rows)+'</div>'

def home(lang):
    base='../' if lang=='zh' else ''
    chips=''.join(f'<span>{E(x)}</span>' for x in D['methods'][lang])
    about=''.join(f'<p>{E(x)}</p>' for x in D['about'][lang])
    selected=''.join(selected_paper(next(p for p in D['papers'] if p['id']==id),lang,i) for i,id in enumerate(D['selected'],1))
    project=D['project']
    awards=''.join(f'<li>{E(x[lang])}</li>' for x in D['awards'])
    services=''.join(f'<li>{E(x[lang])}</li>' for x in D['services'])
    body=f'''<section class="hero shell" aria-labelledby="hero-name"><div class="hero-copy"><p class="eyebrow hero-eyebrow"><span class="rose-dot" aria-hidden="true"></span>{tr('ACADEMIC HOMEPAGE','个人学术主页',lang)}</p><h1 id="hero-name">{E(D['name'][lang])}<span class="name-secondary">{tr('魏泽','Ze Wei',lang)}</span></h1><p class="hero-role">{E(D['role'][lang])} <span>·</span> {E(D['university'][lang])}</p><p class="hero-school">{E(D['school'][lang])}</p><h2 class="hero-statement">{D['hero'][lang]}</h2><p class="hero-intro">{E(D['intro'][lang])}</p><div class="hero-buttons"><a class="button button-primary" href="#publications">{tr('Explore my work','查看研究成果',lang)}{icon('arrow')}</a><a class="button button-light" href="cv.html">{tr('View CV','个人简历',lang)}{icon('external')}</a></div><div class="profile-links"><a href="mailto:{E(D['email'])}">{icon('mail')}Email</a>{xlink('https://orcid.org/'+D['orcid'],'ORCID','profile-link')}</div></div>{photo(lang,base)}</section>
<section id="about" class="about-section shell section"><div><p class="eyebrow">{tr('01 / ABOUT','01 / 关于我',lang)}</p><h2>{tr('A little<br>about me.','关于我的<br>研究。',lang)}</h2></div><div class="about-copy">{about}<div class="method-chips" aria-label="{tr('Research methods','研究方法',lang)}">{chips}</div></div></section>
<section id="research" class="research-section section"><div class="shell">{section_head(tr('02 / RESEARCH','02 / 研究方向',lang),tr('Research interests','研究兴趣',lang),tr('Intelligent decisions. Resource-aware systems.','关注智能决策与资源受限系统。',lang))}{research_cards(lang)}</div></section>
<section id="publications" class="section shell">{section_head(tr('03 / SELECTED WORK','03 / 代表成果',lang),tr('Selected publications','代表论文',lang),link=f'<a class="text-link" href="publications.html">{tr("All publications","全部学术成果",lang)}{icon("arrow")}</a>')}<div class="selected-list">{selected}</div></section>
<section id="experience" class="section experience-section"><div class="shell experience-grid"><div><p class="eyebrow">{tr('04 / EXPERIENCE','04 / 学术经历',lang)}</p><h2>{tr('Academic<br>journey','学术<br>经历',lang)}</h2><p class="experience-intro">{tr('From automation and biomedical engineering to wireless networks and edge intelligence.','从自动化、生物医学工程，到无线网络与边缘智能。',lang)}</p></div>{experience(lang)}</div></section>
<section id="activities" class="section shell">{section_head(tr('05 / ACADEMIC LIFE','05 / 科研与学术活动',lang),tr('Research & community','科研与学术活动',lang))}<article class="project-card"><div><span class="mini-label">{E(project['funder'][lang])}</span><h3>{E(project['title'][lang])}</h3><p>{E(project['role'][lang])}</p></div><div class="grant-number"><span>NSFC</span><strong>{E(project['number'])}</strong></div></article><div class="activity-grid"><article><h3>{tr('Honors & experience','荣誉与实践',lang)}</h3><ul class="clean-list">{awards}</ul><p class="subtle-note">{E(D['award_note'][lang])}</p></article><article><h3>{tr('Academic service','学术服务',lang)}</h3><ul class="clean-list">{services}</ul><p class="subtle-note">{E(D['skills'][lang])}</p></article></div></section>
<section id="contact" class="contact-section"><div class="shell contact-inner"><div><p class="eyebrow">{tr('GET IN TOUCH','学术联系',lang)}</p><h2>{tr('Let’s connect.','欢迎交流。',lang)}</h2><p>{tr('For research correspondence and academic exchange.','有关研究工作与学术交流，欢迎通过邮箱联系。',lang)}</p></div><div class="contact-details"><a class="contact-email" href="mailto:{E(D['email'])}">{E(D['email'])}{icon('external')}</a><p>{E(D['school'][lang])} · {E(D['university'][lang])}<br>{E(D['location'][lang])}</p></div></div></section>'''
    return document(body,lang,'index',tr('Ze Wei | Edge Intelligence & Sustainable Networks','魏泽 | 边缘智能与可持续网络',lang),D['intro'][lang])

def citation(p):
    end=f"{p['venue']}"
    if p['details']: end+=', '+p['details']
    if p['year']: end+=', '+str(p['year'])
    if p['status']!='published': end+=' ('+p['status']+')'
    return p['authors'].rstrip('.')+'. “'+p['title']+'.” '+end+'.'+(' https://doi.org/'+p['doi'] if p['doi'] else '')

def publication_item(p,lang):
    title = p['title_zh'] if lang=='zh' and p['title_zh'] else p['title']
    tag = tr('Conference','会议论文',lang) if p['kind']=='conference' else tr('Journal article','期刊论文',lang)
    status = {'published':tr('Published','已发表',lang),'accepted':tr('Accepted','已接收',lang),'submitted':tr('Submitted','已投稿',lang)}[p['status']]
    if p['early']: tag=tr('Earlier work · Biomedical engineering','早期研究 · 生物医学工程',lang)
    subtitle = ''
    if p['title_zh'] and lang=='en': subtitle='<p class="original-title" lang="zh-CN">'+E(p['title_zh'])+'</p>'
    detail=f"{p['venue']}"+(f" · {p['details']}" if p['details'] else '')
    if p['status']=='submitted': detail=tr('Submitted to ','投稿至 ',lang)+detail
    url = 'https://doi.org/'+p['doi'] if p['doi'] else p['url']
    link = xlink(url,tr('Paper / DOI','论文链接',lang),'paper-link') if url else ''
    if not url and p['status']=='published':
        link=xlink('https://scholar.google.com/scholar?q='+quote('"'+(p['title_zh'] or p['title'])+'"'),tr('Find paper','检索论文',lang),'paper-link')
    if p['status']=='published': cite=f'''<details class="citation"><summary>{tr('Cite','引用',lang)}</summary><div><p class="citation-text">{E(citation(p))}</p><button class="copy-citation" type="button">{icon('copy')}{tr('Copy citation','复制引用',lang)}</button></div></details>'''
    else: cite=''
    status_class = 'status-submitted' if p['status']=='submitted' else 'status-accepted' if p['status']=='accepted' else ''
    return f'''<article class="publication" id="paper-{p['id']}" data-status="{p['status']}" data-kind="{p['kind']}" {'hidden' if p['status']!='published' else ''}><div class="publication-meta"><span>{p['year'] or '—'}</span><span class="publication-status {status_class}">{status}</span></div><div class="publication-body"><div class="publication-tags">{tag}{' · '+tr('In Chinese','中文论文',lang) if p['title_zh'] else ''}</div><h2>{E(title)}</h2>{subtitle}<p class="authors">{authors_html(p['authors'])}</p><p class="publication-venue">{E(detail)}</p><div class="publication-actions">{link}{cite}</div></div></article>'''

def publication_page(lang):
    filters=[('published',tr('Published','已发表',lang)),('journal',tr('Journals','期刊论文',lang)),('conference',tr('Conferences','会议论文',lang)),('accepted',tr('Accepted','已接收',lang)),('submitted',tr('Submitted','已投稿',lang))]
    counts={key:sum((p['status']=='published' and p['kind']==key) if key in ['journal','conference'] else p['status']==key for p in D['papers']) for key,_ in filters}
    buttons=''.join(f'<button class="filter{" active" if key=="published" else ""}" type="button" data-filter="{key}" aria-pressed="{"true" if key=="published" else "false"}">{label}<span>{counts[key]}</span></button>' for key,label in filters)
    ordered=sorted(D['papers'],key=lambda p:({'published':0,'accepted':1,'submitted':2}[p['status']],-(p['year'] or 0)))
    pubs=''.join(publication_item(p,lang) for p in ordered)
    body=f'''<section class="shell publications-head"><a class="breadcrumb" href="index.html">← {tr('Home','首页',lang)}</a><p class="eyebrow">{tr('RESEARCH OUTPUT','学术成果',lang)}</p><h1>{tr('Publications','论文与研究成果',lang)}</h1><p class="page-intro">{tr('Research in edge computing, sustainable wireless networks, and distributed intelligence.','边缘计算、可持续无线网络与分布式智能领域的研究成果。',lang)}</p><p class="publication-note">{tr('Accepted and submitted manuscripts are listed separately. * Corresponding author.','已接收论文与已投稿件单独列示。* 表示通讯作者。',lang)}</p></section><section class="shell publications-content" aria-label="{tr('Publication list','论文列表',lang)}"><div class="publication-toolbar"><div class="filters" role="group" aria-label="{tr('Filter publications','筛选论文',lang)}">{buttons}</div><label class="search-box">{icon('search')}<input id="publicationSearch" type="search" placeholder="{tr('Search title, author, year…','检索标题、作者、年份…',lang)}" aria-label="{tr('Search publications','检索论文',lang)}"></label></div><p class="results-status" id="resultsStatus" role="status" aria-live="polite">{tr(str(counts['published'])+' published papers',str(counts['published'])+' 篇已发表论文',lang)}</p><div id="publicationList">{pubs}</div><p class="empty-state" id="emptyState" hidden>{tr('No matching publications. Try another keyword or category.','没有匹配的论文，请尝试其他关键词或分类。',lang)}</p><noscript><style>.publication[hidden]{{display:grid!important}}.publication-toolbar,.results-status{{display:none!important}}</style><p>{tr('All publication statuses are shown below.','以下展示所有状态的论文记录。',lang)}</p></noscript></section>'''
    return document(body,lang,'publications',tr('Publications | Ze Wei','学术成果 | 魏泽',lang),tr('Publications and manuscripts by Ze Wei.','魏泽的已发表论文、已接收论文与已投稿件。',lang))

def cv_page(lang):
    about=''.join(f'<p>{E(p)}</p>' for p in D['about'][lang][:2])
    research=''.join(f'<li>{E(r["title"][lang])}</li>' for r in D['research'])
    sections=[]
    for status,title in [('published',tr('Published papers','已发表论文',lang)),('accepted',tr('Accepted papers','已接收论文',lang)),('submitted',tr('Submitted manuscripts','已投稿件',lang))]:
        items=''.join(f'<li>{E(citation(p))}</li>' for p in sorted(D['papers'],key=lambda p:-(p['year'] or 0)) if p['status']==status)
        sections.append(f'<section class="cv-section"><h2>{title}</h2><ol>{items}</ol></section>')
    edus=''.join(f'<li><strong>{E(e["institution"][lang])}</strong> · {E(e["degree"][lang])}<br>{E(e["period"][lang])}. {E(e["note"][lang])}</li>' for e in D['education'])
    awards=''.join(f'<li>{E(x[lang])}</li>' for x in D['awards'])
    services=''.join(f'<li>{E(x[lang])}</li>' for x in D['services'])
    project=D['project']
    body=f'''<div class="shell cv-toolbar"><a class="breadcrumb" href="index.html">← {tr('Home','首页',lang)}</a><button class="button button-primary print-button" type="button">{icon('print')}{tr('Print / save PDF','打印 / 另存为 PDF',lang)}</button></div><article class="cv-sheet shell"><header class="cv-header"><p class="eyebrow">CURRICULUM VITAE</p><h1>{E(D['name'][lang])} <span>{tr('魏泽','Ze Wei',lang)}</span></h1><p>{E(D['role'][lang])} · {E(D['school'][lang])} · {E(D['university'][lang])}</p><p><a href="mailto:{E(D['email'])}">{E(D['email'])}</a> · ORCID: {E(D['orcid'])}</p></header><section class="cv-section"><h2>{tr('Research profile','研究简介',lang)}</h2>{about}<ul>{research}</ul></section><section class="cv-section"><h2>{tr('Academic appointment','学术任职',lang)}</h2><p><strong>{E(D['university'][lang])}</strong> · {E(D['role'][lang])}, {E(D['school'][lang])}<br>{tr('Jun. 2026 — Present','2026.06 — 至今',lang)} · {E(D['location'][lang])}</p></section><section class="cv-section"><h2>{tr('Education','教育经历',lang)}</h2><ul>{edus}</ul></section>{''.join(sections)}<p class="publication-note">{tr('* Corresponding author.','* 表示通讯作者。',lang)}</p><section class="cv-section"><h2>{tr('Research project','科研项目',lang)}</h2><p><strong>{E(project['funder'][lang])} · {E(project['number'])}</strong><br>{E(project['title'][lang])}<br>{E(project['role'][lang])}</p></section><section class="cv-section"><h2>{tr('Honors & experience','荣誉与实践',lang)}</h2><ul>{awards}</ul><p>{E(D['award_note'][lang])}</p></section><section class="cv-section"><h2>{tr('Academic service & skills','学术服务与技能',lang)}</h2><ul>{services}</ul><p>{E(D['skills'][lang])}</p></section><p class="cv-update">{tr('Updated: September 2026','更新于 2026 年 9 月',lang)}</p></article>'''
    return document(body,lang,'cv',tr('Curriculum Vitae | Ze Wei','个人简历 | 魏泽',lang),tr('Academic curriculum vitae of Ze Wei.','魏泽的学术简历。',lang))

if __name__ == '__main__':
    for lang in ['en','zh']:
        out=ROOT/('zh' if lang=='zh' else '')
        out.mkdir(exist_ok=True)
        for name,render in [('index',home),('publications',publication_page),('cv',cv_page)]:
            (out/(name+'.html')).write_text(render(lang),encoding='utf-8')
    print('Built 6 static pages.')
