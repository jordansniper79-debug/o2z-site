JS_INJECT = """
    // ── O2Z Capabilities Animation ──────────────────────
    function o2zRunAnim() {
      ['o2z-p1','o2z-p2','o2z-p3','o2z-p4'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.remove('struck');
      });
      ['o2z-s1','o2z-s2','o2z-s3','o2z-s4'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.remove('show');
      });
      const before  = document.getElementById('o2z-sideBefore');
      const after   = document.getElementById('o2z-sideAfter');
      const logo    = document.getElementById('o2z-logo');
      const savings = document.getElementById('o2z-savingsBar');
      if (before)  before.classList.remove('faded');
      if (after)   after.classList.remove('revealed');
      if (logo)    logo.classList.remove('burst');
      if (savings) savings.classList.remove('show');
      [0,1,2,3,4,5].forEach(i => {
        const card = document.getElementById('o2z-c'+i);
        const bl   = document.getElementById('o2z-bl'+i);
        const al   = document.getElementById('o2z-al'+i);
        if (card) card.classList.remove('show');
        if (bl)   bl.classList.remove('struck');
        if (al)   al.classList.remove('show');
      });
      setTimeout(() => {
        ['o2z-p1','o2z-p2','o2z-p3','o2z-p4'].forEach((id,i) => {
          setTimeout(() => { const el=document.getElementById(id); if(el) el.classList.add('struck'); }, i*120);
        });
      }, 300);
      setTimeout(() => {
        if (before) before.classList.add('faded');
        if (logo)   logo.classList.add('burst');
      }, 1000);
      setTimeout(() => {
        if (after) after.classList.add('revealed');
        ['o2z-s1','o2z-s2','o2z-s3','o2z-s4'].forEach((id,i) => {
          setTimeout(() => { const el=document.getElementById(id); if(el) el.classList.add('show'); }, i*120);
        });
      }, 1300);
      setTimeout(() => { if(savings) savings.classList.add('show'); }, 1800);
      setTimeout(() => {
        [0,1,2,3,4,5].forEach(i => {
          setTimeout(() => {
            const card=document.getElementById('o2z-c'+i);
            const bl=document.getElementById('o2z-bl'+i);
            const al=document.getElementById('o2z-al'+i);
            if(card) card.classList.add('show');
            if(bl)   bl.classList.add('struck');
            setTimeout(() => { if(al) al.classList.add('show'); }, 300);
          }, i*120);
        });
      }, 2200);
    }
    window.addEventListener('load', () => { setTimeout(o2zRunAnim, 500); });
    // ── End O2Z Animation ────────────────────────────────
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check already injected
if 'o2zRunAnim' in content:
    print("o2zRunAnim already exists — nothing to do.")
else:
    # Inject before closing </script> of the last script tag
    pos = content.rfind('</script>')
    if pos == -1:
        print("ERROR: No </script> found!")
    else:
        new_content = content[:pos] + JS_INJECT + content[pos:]

        # Also wire into toggleLanguage
        if 'setTimeout(o2zRunAnim' not in new_content:
            new_content = new_content.replace(
                'function toggleLanguage() {',
                'function toggleLanguage() {\n'
            )
            # Add call at end of toggleLanguage
            # Find the closing } of toggleLanguage by looking for setTimeout(o2zRunAnim trigger point
            toggle_pos = new_content.find('function toggleLanguage()')
            if toggle_pos != -1:
                # find the next standalone } after toggleLanguage body
                search_from = toggle_pos + len('function toggleLanguage()')
                depth = 0
                i = search_from
                while i < len(new_content):
                    if new_content[i] == '{':
                        depth += 1
                    elif new_content[i] == '}':
                        depth -= 1
                        if depth == 0:
                            new_content = new_content[:i] + '\n        setTimeout(o2zRunAnim, 600);\n    ' + new_content[i:]
                            break
                    i += 1

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ o2zRunAnim injected and wired successfully!")
        print(f"   File: {len(new_content.splitlines())} lines")
