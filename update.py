import sys
import re

with open('C:/Users/abdal/o2z/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace CSS
css_pattern = re.compile(r'(\s*\.node-pulse\s*\{[^}]+\}\s*@keyframes pulse-ring\s*\{.*?\100%\s*\{[^}]+\}\s*\})', re.DOTALL)
new_css = r"""\1
        .perspective-1000 { perspective: 1000px; }
        .transform-style-3d { transform-style: preserve-3d; }
        .backface-hidden { backface-visibility: hidden; }
        .flip-card-inner { transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); transform-style: preserve-3d; }
        .group:hover .flip-card-inner { transform: rotateY(180deg); }
        html[dir="rtl"] .group:hover .flip-card-inner { transform: rotateY(-180deg); }
        .flip-card-front, .flip-card-back { backface-visibility: hidden; position: absolute; top:0; left:0; width:100%; height:100%; padding: 2rem; }
        .flip-card-back { transform: rotateY(180deg); }
        html[dir="rtl"] .flip-card-back { transform: rotateY(-180deg); }"""
html = css_pattern.sub(new_css, html)

# 2. Replace Suite Section mapping
suite_pattern = re.compile(r'<!-- Section: Suite -->.*?</section>', re.DOTALL)
new_suite = """<!-- Section: Services -->
<section class="py-24 relative z-10" id="suite" dir="auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="font-display text-4xl md:text-5xl font-bold text-slate-900 dark:text-white mb-4" data-i18n="suite_t">The O2Z Operating System</h2>
            <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl mx-auto" data-i18n="suite_sub">A unified architecture designed to seamlessly integrate every facet of your enterprise operations.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-slate-200 dark:border-slate-700 shadow-xl"><div class="w-16 h-16 rounded-xl bg-primary/10 flex items-center justify-center mb-6 text-primary"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">hub</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s1_t">Omnichannel</h3></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-primary/30 shadow-[0_0_30px_rgba(0,229,255,0.15)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-primary" data-i18n="s1_t">Omnichannel</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s1_d">description.</p><span class="inline-flex items-center text-primary text-sm font-semibold hover:text-primary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>
            
            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-slate-200 dark:border-slate-700 shadow-xl"><div class="w-16 h-16 rounded-xl bg-secondary/10 flex items-center justify-center mb-6 text-secondary"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">campaign</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s2_t">WhatsApp</h3></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-secondary/30 shadow-[0_0_30px_rgba(41,98,255,0.15)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-secondary" data-i18n="s2_t">WhatsApp</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s2_d">description.</p><span class="inline-flex items-center text-secondary text-sm font-semibold hover:text-secondary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>

            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-primary/30 relative overflow-hidden shadow-xl"><div class="absolute inset-0 bg-primary/5"></div><div class="relative z-10 flex flex-col items-center"><div class="w-16 h-16 rounded-xl bg-primary flex items-center justify-center mb-6 shadow-[0_0_15px_rgba(0,229,255,0.5)] text-background-dark"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">smart_toy</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s3_t">AI Chatbots</h3></div></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-primary/50 shadow-[0_0_30px_rgba(0,229,255,0.25)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-primary" data-i18n="s3_t">AI Chatbots</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s3_d">description.</p><span class="inline-flex items-center text-primary text-sm font-semibold hover:text-primary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>

            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-slate-200 dark:border-slate-700 shadow-xl"><div class="w-16 h-16 rounded-xl bg-secondary/10 flex items-center justify-center mb-6 text-secondary"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">insights</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s4_t">Ads</h3></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-secondary/30 shadow-[0_0_30px_rgba(41,98,255,0.15)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-secondary" data-i18n="s4_t">Ads</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s4_d">description.</p><span class="inline-flex items-center text-secondary text-sm font-semibold hover:text-secondary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>

            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-slate-200 dark:border-slate-700 shadow-xl"><div class="w-16 h-16 rounded-xl bg-primary/10 flex items-center justify-center mb-6 text-primary"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">rocket_launch</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s5_t">Viral</h3></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-primary/30 shadow-[0_0_30px_rgba(0,229,255,0.15)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-primary" data-i18n="s5_t">Viral</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s5_d">description.</p><span class="inline-flex items-center text-primary text-sm font-semibold hover:text-primary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>

            <a href="#" class="group perspective-1000 h-80 block w-full"><div class="flip-card-inner w-full h-full relative z-10">
                <div class="flip-card-front glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-gradient-to-b from-surface-light to-slate-50 dark:from-surface-dark dark:to-slate-800/50 border-t border-slate-200 dark:border-slate-700 shadow-xl"><div class="w-16 h-16 rounded-xl bg-secondary/10 flex items-center justify-center mb-6 text-secondary"><span class="material-icons text-4xl group-hover:scale-110 transition-transform">auto_awesome</span></div><h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white" data-i18n="s6_t">AI Design</h3></div>
                <div class="flip-card-back glass-panel rounded-2xl flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-800 border-2 border-secondary/30 shadow-[0_0_30px_rgba(41,98,255,0.15)]"><h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-4 text-secondary" data-i18n="s6_t">AI Design</h3><p class="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-6" data-i18n="s6_d">description.</p><span class="inline-flex items-center text-secondary text-sm font-semibold hover:text-secondary/70 transition-colors"><span data-i18n="learn_more">Learn</span> <span class="material-icons text-sm ml-1 rtl:mr-1 rtl:ml-0 rtl-flip">arrow_forward</span></span></div>
            </div></a>
        </div>
    </div>
</section>

<!-- Section: Clients -->
<section class="py-20 bg-white dark:bg-background-dark border-t border-slate-200 dark:border-slate-800 relative z-10" id="clients" dir="auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h3 class="font-display text-2xl font-bold text-slate-500 dark:text-slate-400 mb-10 tracking-widest uppercase" data-i18n="clients_t">Trusted By Industry Leaders</h3>
        <div class="flex flex-wrap justify-center items-center gap-8 md:gap-20 opacity-60 hover:opacity-100 transition-opacity duration-500">
            <div class="flex items-center gap-2 text-2xl font-bold font-display text-slate-800 dark:text-slate-300">
                <span class="material-icons text-primary rounded-lg p-2 bg-primary/10">corporate_fare</span>
                BrandCorp
            </div>
            <div class="flex items-center gap-2 text-2xl font-bold font-display text-slate-800 dark:text-slate-300">
                <span class="material-icons text-secondary rounded-lg p-2 bg-secondary/10">memory</span>
                TechVision AI
            </div>
            <div class="flex items-center gap-2 text-2xl font-bold font-display text-slate-800 dark:text-slate-300">
                <span class="material-icons text-primary rounded-lg p-2 bg-primary/10">language</span>
                GlobalReach
            </div>
            <div class="flex items-center gap-2 text-2xl font-bold font-display text-slate-800 dark:text-slate-300">
                <span class="material-icons text-secondary rounded-lg p-2 bg-secondary/10">trending_up</span>
                Nexus Growth
            </div>
        </div>
    </div>
</section>"""
html = suite_pattern.sub(new_suite, html)

# 3. Replace EN Translations safely
en_dict = """            s1_t: "Omnichannel Communications",
            s1_d: "A unified platform connecting all your customer touchpoints into a single intelligent dashboard.",
            s2_t: "WhatsApp & Marketing Automation",
            s2_d: "Launch massive marketing campaigns and automate WhatsApp interactions with precision.",
            s3_t: "AI Auto-Reply Chatbots",
            s3_d: "Intelligent bots answering customers instantly across WhatsApp, Facebook, and Instagram.",
            s4_t: "Ads Optimization & Consulting",
            s4_d: "Expert marketing consulting to lower your CPA and maximize your ROI across ad networks.",
            s5_t: "Viral Marketing Services",
            s5_d: "Strategic campaigns engineered for explosive viral growth and intensive market penetration.",
            s6_t: "AI Design & Video Editing",
            s6_d: "Generate captivating visuals and professional montages driven by advanced generative AI.",
            clients_t: "Trusted By Industry Leaders",
            learn_more: "Explore Details","""

ar_dict = """            s1_t: "قنوات التواصل الموحدة (OmniChannel)",
            s1_d: "منصة تواصل موحدة تجمع كافة نقاط اتصال عملائك في لوحة تحكم واحدة وذكية.",
            s2_t: "أتمتة الواتسآب والحملات التسويقية",
            s2_d: "إطلاق حملات تسويقية ضخمة وأتمتة تفاعلات الواتساب بدقة متناهية.",
            s3_t: "ردود آلية بالذكاء الاصطناعي",
            s3_d: "رد فوري على العملاء عبر الواتساب، فيسبوك، انستجرام وجميع منصات التواصل.",
            s4_t: "استشارات وتحسين الإعلانات",
            s4_d: "استشارات لتطوير الحملات الممولة وتقليل التكلفة مع مضاعفة العائد المادي.",
            s5_t: "خدمات الانتشار الواسع والمكثف",
            s5_d: "خطط تسويقية مخصصة لتحقيق انتشار سريع وأكبر وصول لخدماتك.",
            s6_t: "تصميم ومونتاج بالذكاء الاصطناعي",
            s6_d: "إنشاء تصاميم احترافية وفيديوهات مونتاج إبداعية وحصرية بالاعتماد على أدوات الذكاء الاصطناعي.",
            clients_t: "عملاؤنا وشركاء النجاح",
            learn_more: "تفاصيل الخدمة","""

s1_en = html.find('s1_t: "O2Z Connect",')
s_end_en = html.find('cap_t:', s1_en)
if s1_en != -1 and s_end_en != -1:
    html = html[:s1_en] + en_dict + '\n            ' + html[s_end_en:]

s1_ar = html.find('s1_t: "O2Z Connect",', s_end_en if s_end_en != -1 else 0)
s_end_ar = html.find('cap_t:', s1_ar)
if s1_ar != -1 and s_end_ar != -1:
    html = html[:s1_ar] + ar_dict + '\n            ' + html[s_end_ar:]

with open('C:/Users/abdal/o2z/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
