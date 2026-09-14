(() => {
  'use strict';
  const zh = document.documentElement.lang === 'zh-CN';
  const menu = document.getElementById('menuButton');
  const nav = document.getElementById('mobileNav');
  function toggleMenu(open) {
    if (!menu || !nav) return;
    nav.hidden = !open;
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', zh ? (open ? '关闭导航' : '打开导航') : (open ? 'Close navigation' : 'Open navigation'));
  }
  if (menu && nav) {
    menu.addEventListener('click', () => toggleMenu(nav.hidden));
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => toggleMenu(false)));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !nav.hidden) {
        toggleMenu(false);
        menu.focus();
      }
    });
    window.matchMedia('(min-width: 801px)').addEventListener('change', event => {
      if (event.matches) toggleMenu(false);
    });
  }

  const filters = [...document.querySelectorAll('.filter')];
  const papers = [...document.querySelectorAll('.publication')];
  const search = document.getElementById('publicationSearch');
  const results = document.getElementById('resultsStatus');
  const empty = document.getElementById('emptyState');
  let activeFilter = 'published';
  const labels = zh ? { published:'篇已发表论文', journal:'篇期刊论文', conference:'篇会议论文', accepted:'篇已接收论文', submitted:'篇已投稿件' } : { published:'published papers', journal:'journal articles', conference:'conference papers', accepted:'accepted papers', submitted:'submitted manuscripts' };
  const normalized = value => value.normalize('NFKC').toLocaleLowerCase().trim();
  const searchable = new Map(papers.map(paper => [paper, normalized(paper.textContent)]));
  function applyFilter(key = activeFilter) {
    activeFilter = key;
    const tokens = normalized(search ? search.value : '').split(/\s+/).filter(Boolean);
    let visible = 0;
    filters.forEach(button => {
      const current = button.dataset.filter === key;
      button.classList.toggle('active', current);
      button.setAttribute('aria-pressed', String(current));
    });
    papers.forEach(paper => {
      const categoryMatches = key === 'journal' || key === 'conference'
        ? paper.dataset.status === 'published' && paper.dataset.kind === key
        : paper.dataset.status === key;
      const queryMatches = tokens.every(token => searchable.get(paper).includes(token));
      paper.hidden = !(categoryMatches && queryMatches);
      if (!paper.hidden) visible += 1;
    });
    if (results) results.textContent = `${visible} ${labels[key]}` + (tokens.length ? (zh ? '（检索结果）' : ' matching your search') : '');
    if (empty) empty.hidden = visible !== 0;
  }
  filters.forEach(button => button.addEventListener('click', () => applyFilter(button.dataset.filter)));
  if (search) search.addEventListener('input', () => applyFilter());
  function revealPaper() {
    const id = window.location.hash.slice(1);
    if (!id.startsWith('paper-')) return;
    const paper = document.getElementById(id);
    if (!paper || !paper.classList.contains('publication')) return;
    if (search) search.value = '';
    applyFilter(paper.dataset.status);
    requestAnimationFrame(() => paper.scrollIntoView({ block:'start' }));
  }
  if (filters.length) {
    applyFilter();
    revealPaper();
    window.addEventListener('hashchange', revealPaper);
  }

  document.querySelectorAll('.copy-citation').forEach(button => {
    const original = button.innerHTML;
    button.addEventListener('click', async () => {
      const text = button.parentElement.querySelector('.citation-text').textContent;
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(text);
        } else {
          const input = document.createElement('textarea');
          input.value = text;
          input.setAttribute('readonly', '');
          input.style.cssText = 'position:fixed;left:0;top:0;width:1px;height:1px;opacity:0';
          document.body.appendChild(input);
          input.select();
          let copied = false;
          try { copied = document.execCommand('copy'); }
          finally { input.remove(); button.focus(); }
          if (!copied) throw new Error('Clipboard unavailable');
        }
        button.textContent = zh ? '已复制' : 'Copied';
      } catch {
        button.textContent = zh ? '请选中上方文字复制' : 'Select the citation above to copy';
      }
      button.setAttribute('aria-live','polite');
      setTimeout(() => { button.innerHTML = original; }, 2500);
    });
  });
  document.querySelectorAll('.print-button').forEach(button => {
    button.addEventListener('click', () => window.print());
  });
})();
