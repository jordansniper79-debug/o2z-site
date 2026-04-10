import re

NEW_SECTION = '''<section class="py-24 relative z-10 overflow-hidden" id="capabilities">
  <div class="o2z-wrap">
    <div class="o2z-glow"></div>

    <div class="o2z-label" data-i18n="cap_ba_label">ماذا يتغير معنا</div>
    <div class="o2z-title">
      <span data-i18n="cap_ba_title_before">قبل O2Z</span> —
      <span data-i18n="cap_ba_title_after" style="color:#00c8b4">وبعدها</span>
    </div>
    <div class="o2z-sub" data-i18n="cap_ba_sub">تحول حقيقي يشعر به عملك من أول يوم تعمل معنا</div>

    <div class="o2z-hero">
      <div class="o2z-side o2z-side-before" id="o2z-sideBefore">
        <h4 data-i18n="cap_ba_before_title">قبل O2Z</h4>
        <div class="o2z-prob"><span class="o2z-prob-text" id="o2z-p1" data-i18n="cap_ba_p1">عملاء بلا رد خارج الدوام</span></div>
        <div class="o2z-prob"><span class="o2z-prob-text" id="o2z-p2" data-i18n="cap_ba_p2">فريقك يكرر نفس العمل يومياً</span></div>
        <div class="o2z-prob"><span class="o2z-prob-text" id="o2z-p3" data-i18n="cap_ba_p3">قرارات مبنية على تخمين</span></div>
        <div class="o2z-prob"><span class="o2z-prob-text" id="o2z-p4" data-i18n="cap_ba_p4">أنظمة منفصلة وفوضى</span></div>
      </div>

      <div class="o2z-mid">
        <div class="o2z-logo-circle" id="o2z-logo">O2Z</div>
        <span class="o2z-arr-icon">&#8594;</span>
      </div>

      <div class="o2z-side o2z-side-after" id="o2z-sideAfter">
        <h4 data-i18n="cap_ba_after_title">مع O2Z</h4>
        <div class="o2z-sol" id="o2z-s1" data-i18n="cap_ba_s1">ردود فورية على مدار الساعة</div>
        <div class="o2z-sol" id="o2z-s2" data-i18n="cap_ba_s2">فريقك يبتكر بدل ما يكرر</div>
        <div class="o2z-sol" id="o2z-s3" data-i18n="cap_ba_s3">أرقام حقيقية تقود كل قرار</div>
        <div class="o2z-sol" id="o2z-s4" data-i18n="cap_ba_s4">منظومة واحدة متكاملة وهادئة</div>
      </div>
    </div>

    <div class="o2z-savings" id="o2z-savingsBar">
      <div><div class="o2z-sav-num" data-i18n="cap_stat1_num">-60%</div><div class="o2z-sav-lbl" data-i18n="cap_stat1_lbl">تكاليف تشغيلية</div></div>
      <div><div class="o2z-sav-num" data-i18n="cap_stat2_num">3x</div><div class="o2z-sav-lbl" data-i18n="cap_stat2_lbl">سرعة خدمة العملاء</div></div>
      <div><div class="o2z-sav-num" data-i18n="cap_stat3_num">+90%</div><div class="o2z-sav-lbl" data-i18n="cap_stat3_lbl">معدل قراءة رسائلك</div></div>
      <div><div class="o2z-sav-num" data-i18n="cap_stat4_num">24/7</div><div class="o2z-sav-lbl" data-i18n="cap_stat4_lbl">عمل بلا توقف</div></div>
    </div>

    <div class="o2z-cards">
      <div class="o2z-card" id="o2z-c0">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl0" data-i18n="cap_c1_before">ردود متأخرة تُضيّع الفرص</span></div>
        <div class="o2z-after-line" id="o2z-al0" data-i18n="cap_c1_after">عميلك يُجاب فوراً في أي وقت</div>
        <div class="o2z-stag">AI Chatbot</div>
      </div>
      <div class="o2z-card" id="o2z-c1">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl1" data-i18n="cap_c2_before">رسائل تُرسل ولا تُقرأ</span></div>
        <div class="o2z-after-line" id="o2z-al1" data-i18n="cap_c2_after">عروضك تصل وتُقرأ وتُحوَّل</div>
        <div class="o2z-stag">WhatsApp Marketing</div>
      </div>
      <div class="o2z-card" id="o2z-c2">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl2" data-i18n="cap_c3_before">مهام يدوية تستنزف وقتك</span></div>
        <div class="o2z-after-line" id="o2z-al2" data-i18n="cap_c3_after">عملياتك تسير وحدها بهدوء</div>
        <div class="o2z-stag">Automation</div>
      </div>
      <div class="o2z-card" id="o2z-c3">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl3" data-i18n="cap_c4_before">أنظمة منفصلة وبيانات ضائعة</span></div>
        <div class="o2z-after-line" id="o2z-al3" data-i18n="cap_c4_after">كل شيء متصل ومتزامن دائماً</div>
        <div class="o2z-stag">System Integration</div>
      </div>
      <div class="o2z-card" id="o2z-c4">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl4" data-i18n="cap_c5_before">قرارات على التخمين</span></div>
        <div class="o2z-after-line" id="o2z-al4" data-i18n="cap_c5_after">أرقام حقيقية تقود كل قرار</div>
        <div class="o2z-stag">Data &amp; Analytics</div>
      </div>
      <div class="o2z-card" id="o2z-c5">
        <div class="o2z-before-line"><span class="o2z-before-line-text" id="o2z-bl5" data-i18n="cap_c6_before">مهام تستنزف وقتك يومياً</span></div>
        <div class="o2z-after-line" id="o2z-al5" data-i18n="cap_c6_after">وكيل ذكي ينجزها باستقلالية</div>
        <div class="o2z-stag">AI Agents</div>
      </div>
    </div>

    <hr class="o2z-divider">
    <div class="o2z-cta">
      <div class="o2z-cta-t" data-i18n="cap_cta_t">جاهز تشوف الفرق بنفسك؟</div>
      <div class="o2z-cta-s" data-i18n="cap_cta_s">15 دقيقة كافية — ونريك كيف يتحول عملك</div>
      <div class="o2z-btns">
        <button class="o2z-btn1" data-i18n="cap_btn1">ابدأ رحلتك معنا</button>
        <button class="o2z-btn2" data-i18n="cap_btn2">تعرف على خدماتنا</button>
      </div>
    </div>
  </div>
</section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the old capabilities section and replace it
pattern = r'<section[^>]*id="capabilities"[^>]*>.*?</section>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find id='capabilities' section!")
else:
    old = match.group(0)
    print(f"Found old section: {len(old.splitlines())} lines (lines {content[:match.start()].count(chr(10))+1} to {content[:match.end()].count(chr(10))+1})")
    new_content = content[:match.start()] + NEW_SECTION + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Section replaced successfully!")
    print(f"   New file: {len(new_content.splitlines())} lines")
