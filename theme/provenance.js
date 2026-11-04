// A Court for Agents: set the bracketed provenance tags small, and let a reader hide them.
// The tags stay in the text (search, print and the source keep them); this only marks each
// one with <span class="prov"> so the stylesheet can mute it. No network; the one remembered
// preference is optional and survives its absence.
(function () {
  var TAG = /seq|CHARTER|SPEC|BRIEF|LAW\.md|REPORT|REVIEW|RUNBOOK|status\.py|value\.py|count_kernel|jack score|transcripts\/|data\/|tools\/|kernel2?\/|judge\/|log@|@[0-9a-f]{7}|enforcement|as transcript|agent-court#|PR #|issue|claude\//;
  var LEAD = /^\[(A\d+\.\d|§\d|lines? \d|same invocation|the same|chapters? \d|`)/;
  // Find the next top-level bracket pair in el's direct text children, starting at (i, off).
  function next(kids, i, off) {
    for (; i < kids.length; i++, off = 0) {
      var a = kids[i];
      if (a.nodeType !== 3) continue;
      var open = a.data.indexOf('[', off);
      if (open < 0) continue;
      while (open >= 0) {
        var depth = 0;
        for (var j = i; j < kids.length; j++) {
          var n = kids[j];
          if (n.nodeType !== 3) continue;
          var s = n.data;
          for (var k = (j === i ? open : 0); k < s.length; k++) {
            if (s[k] === '[') depth++;
            else if (s[k] === ']' && --depth === 0) return { a: a, open: open, b: n, close: k, i: i };
          }
        }
        open = a.data.indexOf('[', open + 1);  // unclosed, as in an interval [0, 1): try the next one
      }
    }
    return null;
  }
  function wrapIn(el) {
    var kids = Array.prototype.slice.call(el.childNodes), i = 0, off = 0, hit;
    while ((hit = next(kids, i, off))) {
      var r = document.createRange();
      r.setStart(hit.a, hit.open); r.setEnd(hit.b, hit.close + 1);
      var txt = r.toString();
      var lead = '[' + (hit.a.data.length === hit.open + 1 && hit.a.nextSibling && hit.a.nextSibling.nodeName === 'CODE' ? '`' : hit.a.data.slice(hit.open + 1, hit.open + 20));
      var nested = txt.indexOf('[', 1) >= 0 && !/^\[(seq|CHARTER|SPEC|BRIEF|LAW|REPORT|`)/.test(lead + txt.slice(1, 10));
      if ((TAG.test(txt) || LEAD.test(lead)) && !nested && !/^\[[^\]]*\|/.test(txt)) {
        var span = document.createElement('span');
        span.className = 'prov';
        if (hit.open > 0 && hit.a.data[hit.open - 1] === ' ') r.setStart(hit.a, hit.open - 1);  // hide the space before it too
        try {
          r.surroundContents(span);
          kids = Array.prototype.slice.call(el.childNodes);
          i = kids.indexOf(span) + 1; off = 0; continue;
        } catch (e) { /* range crossed an element boundary: leave it as it is */ }
      }
      i = hit.i; off = hit.open + 1;  // not a tag: look again from the next character
    }
  }
  function apply() {
    var main = document.querySelector('main');
    if (!main) return;
    main.querySelectorAll('p, li, td, em').forEach(wrapIn);
    var hidden = false;
    try { hidden = localStorage.getItem('acfa-hide-tags') === '1'; } catch (e) {}
    document.documentElement.classList.toggle('hide-prov', hidden);
    var bar = document.querySelector('.right-buttons');
    if (!bar || document.getElementById('prov-toggle')) return;
    var b = document.createElement('button');
    b.id = 'prov-toggle'; b.className = 'icon-button'; b.type = 'button';
    b.title = 'Show or hide the provenance tags';
    b.setAttribute('aria-pressed', String(hidden));
    b.textContent = hidden ? '[show sources]' : '[hide sources]';
    b.addEventListener('click', function () {
      var h = !document.documentElement.classList.contains('hide-prov');
      document.documentElement.classList.toggle('hide-prov', h);
      b.textContent = h ? '[show sources]' : '[hide sources]';
      b.setAttribute('aria-pressed', String(h));
      try { localStorage.setItem('acfa-hide-tags', h ? '1' : '0'); } catch (e) {}
    });
    bar.insertBefore(b, bar.firstChild);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply); else apply();
})();
