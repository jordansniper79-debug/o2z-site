import re
import io

# Read both files
with io.open('c:/Users/abdal/Downloads/o2z_capabilities_FINAL.html', 'r', encoding='utf-8') as f:
    ref_content = f.read()

with io.open('c:/Users/abdal/o2z/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Extract CSS
css_start = ref_content.find("/* ══ ① CSS ══ */")
if css_start == -1: css_start = ref_content.find("/* ══════════════════════════════════════════════")
css_end = ref_content.find("</style>", css_start)
css_block = ref_content[css_start:css_end].strip()

# Inject CSS into index.html
index_content = index_content.replace('    </style>\n</head>', f'\n{css_block}\n    </style>\n</head>')

# 2. Extract New Capabilities HTML
html_start = ref_content.find('<section class="py-24 relative z-10 overflow-hidden" id="capabilities">')
html_end = ref_content.find('</section>', html_start) + len('</section>')
new_html_block = ref_content[html_start:html_end]

# Find Old Capabilities HTML in index.html
old_html_start = index_content.find('<section class="py-24 bg-slate-50 dark:bg-slate-900/50 relative overflow-hidden" id="capabilities"')
old_html_end = index_content.find('</section>', old_html_start) + len('</section>')
old_html_block = index_content[old_html_start:old_html_end]

# Replace HTML
index_content = index_content.replace(old_html_block, new_html_block)

# 3. Add Translations
en_keys = """cap_ba_label: "What Changes With Us",
cap_ba_title_before: "Before O2Z",
cap_ba_title_after: "After O2Z",
cap_ba_sub: "A real transformation your business feels from day one",
cap_ba_before_title: "Before O2Z",
cap_ba_after_title: "With O2Z",
cap_ba_p1: "Customers left unanswered after hours",
cap_ba_p2: "Your team repeats the same tasks daily",
cap_ba_p3: "Decisions based on guesswork",
cap_ba_p4: "Disconnected systems and chaos",
cap_ba_s1: "Instant responses around the clock",
cap_ba_s2: "Your team innovates instead of repeating",
cap_ba_s3: "Real numbers driving every decision",
cap_ba_s4: "One unified, seamless ecosystem",
cap_stat1_num: "-60%",
cap_stat1_lbl: "Operational costs",
cap_stat2_num: "3x",
cap_stat2_lbl: "Customer service speed",
cap_stat3_num: "+90%",
cap_stat3_lbl: "Message open rate",
cap_stat4_num: "24/7",
cap_stat4_lbl: "Non-stop operation",
cap_c1_before: "Slow replies lose opportunities",
cap_c1_after: "Customers answered instantly, anytime",
cap_c2_before: "Messages sent but never read",
cap_c2_after: "Your offers land, get read, convert",
cap_c3_before: "Manual tasks drain your time",
cap_c3_after: "Your operations run smoothly on autopilot",
cap_c4_before: "Disconnected systems, lost data",
cap_c4_after: "Everything connected and synced always",
cap_c5_before: "Decisions based on guesswork",
cap_c5_after: "Real numbers guide every decision",
cap_c6_before: "Repetitive tasks drain you daily",
cap_c6_after: "An AI agent handles them autonomously",
cap_cta_t: "Ready to see the difference yourself?",
cap_cta_s: "15 minutes is all it takes — we'll show you how your business transforms",
cap_btn1: "Start Your Journey",
cap_btn2: "Explore Our Services","""

ar_keys = """cap_ba_label: "ماذا يتغير معنا",
cap_ba_title_before: "قبل O2Z",
cap_ba_title_after: "وبعدها",
cap_ba_sub: "تحول حقيقي يشعر به عملك من أول يوم تعمل معنا",
cap_ba_before_title: "قبل O2Z",
cap_ba_after_title: "مع O2Z",
cap_ba_p1: "عملاء بلا رد خارج الدوام",
cap_ba_p2: "فريقك يكرر نفس العمل يومياً",
cap_ba_p3: "قرارات مبنية على تخمين",
cap_ba_p4: "أنظمة منفصلة وفوضى",
cap_ba_s1: "ردود فورية على مدار الساعة",
cap_ba_s2: "فريقك يبتكر بدل ما يكرر",
cap_ba_s3: "أرقام حقيقية تقود كل قرار",
cap_ba_s4: "منظومة واحدة متكاملة وهادئة",
cap_stat1_num: "-60%",
cap_stat1_lbl: "تكاليف تشغيلية",
cap_stat2_num: "3x",
cap_stat2_lbl: "سرعة خدمة العملاء",
cap_stat3_num: "+90%",
cap_stat3_lbl: "معدل قراءة رسائلك",
cap_stat4_num: "24/7",
cap_stat4_lbl: "عمل بلا توقف",
cap_c1_before: "ردود متأخرة تُضيّع الفرص",
cap_c1_after: "عميلك يُجاب فوراً في أي وقت",
cap_c2_before: "رسائل تُرسل ولا تُقرأ",
cap_c2_after: "عروضك تصل وتُقرأ وتُحوَّل",
cap_c3_before: "مهام يدوية تستنزف وقتك",
cap_c3_after: "عملياتك تسير وحدها بهدوء",
cap_c4_before: "أنظمة منفصلة وبيانات ضائعة",
cap_c4_after: "كل شيء متصل ومتزامن دائماً",
cap_c5_before: "قرارات على التخمين",
cap_c5_after: "أرقام حقيقية تقود كل قرار",
cap_c6_before: "مهام تستنزف وقتك يومياً",
cap_c6_after: "وكيل ذكي ينجزها باستقلالية",
cap_cta_t: "جاهز تشوف الفرق بنفسك؟",
cap_cta_s: "15 دقيقة كافية — ونريك كيف يتحول عملك",
cap_btn1: "ابدأ رحلتك معنا",
cap_btn2: "تعرف على خدماتنا","""

# Inject en keys
en_match = re.search(r'("en": \{[\s\S]*?)(sys_op:\s*"Operational"\s*)\}', index_content)
if en_match:
    index_content = index_content[:en_match.start(2)] + en_match.group(2) + ",\n                " + en_keys.replace("\n", "\n                ") + "\n            }" + index_content[en_match.end():]

# Inject ar keys
ar_match = re.search(r'("ar": \{[\s\S]*?)(sys_op:\s*"يعمل بكفاءة"\s*)\}', index_content)
if ar_match:
    index_content = index_content[:ar_match.start(2)] + ar_match.group(2) + ",\n                " + ar_keys.replace("\n", "\n                ") + "\n            }" + index_content[ar_match.end():]

# 4. Add Animation Function
anim_func = """
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
    ['o2z-p1','o2z-p2','o2z-p3','o2z-p4'].forEach((id, i) => {
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.classList.add('struck');
      }, i * 120);
    });
  }, 300);

  setTimeout(() => {
    if (before) before.classList.add('faded');
    if (logo)   logo.classList.add('burst');
  }, 1000);

  setTimeout(() => {
    if (after) after.classList.add('revealed');
    ['o2z-s1','o2z-s2','o2z-s3','o2z-s4'].forEach((id, i) => {
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.classList.add('show');
      }, i * 120);
    });
  }, 1300);

  setTimeout(() => {
    if (savings) savings.classList.add('show');
  }, 1800);

  setTimeout(() => {
    [0,1,2,3,4,5].forEach(i => {
      setTimeout(() => {
        const card = document.getElementById('o2z-c'+i);
        const bl   = document.getElementById('o2z-bl'+i);
        const al   = document.getElementById('o2z-al'+i);
        if (card) card.classList.add('show');
        if (bl)   bl.classList.add('struck');
        setTimeout(() => { if (al) al.classList.add('show'); }, 300);
      }, i * 120);
    });
  }, 2200);
}
"""
# Inject animation function before toggleLanguage()
index_content = index_content.replace('function toggleLanguage() {', f'{anim_func}\n        function toggleLanguage() {{')

# 5. Run Animation On Load
load_listener = """document.addEventListener("DOMContentLoaded", () => {"""
index_content = index_content.replace(load_listener, f"window.addEventListener('load', () => {{ setTimeout(o2zRunAnim, 500); }});\n        {load_listener}")

# 6. Run Animation on Language Toggle
# Inject at the end of toggleLanguage()
toggle_match = re.search(r'(function toggleLanguage\(\) \{[\s\S]*?    \})', index_content)
if toggle_match:
    original_toggle = toggle_match.group(1)
    new_toggle = original_toggle[:-1] + "    setTimeout(o2zRunAnim, 600);\n        }"
    index_content = index_content.replace(original_toggle, new_toggle)

with io.open('c:/Users/abdal/o2z/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Update completed successfully!")
