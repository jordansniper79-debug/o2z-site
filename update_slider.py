import sys
import re

with open('C:/Users/abdal/o2z/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for Marquee
css_pattern = r'(\.hide-scroll-bar::-webkit-scrollbar\s*\{\s*display:\s*none;\s*\})'
new_css = r"""\1

        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }
        @keyframes marquee-rtl {
            0% { transform: translateX(0%); }
            100% { transform: translateX(50%); }
        }
        .animate-marquee {
            display: flex;
            width: max-content;
            animation: marquee 30s linear infinite;
            will-change: transform;
        }
        html[dir="rtl"] .animate-marquee {
            animation: marquee-rtl 30s linear infinite;
        }
        .group-slider:hover .animate-marquee {
            animation-play-state: paused;
        }
        
        .animated-border {
            position: absolute;
            inset: 0;
            border-radius: inherit;
            padding: 1px;
            background: linear-gradient(135deg, rgba(0, 229, 255, 0.5), transparent 40%, transparent 60%, rgba(41, 98, 255, 0.5));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            opacity: 0.3;
            transition: opacity 0.5s ease;
        }
        .group:hover .animated-border {
            opacity: 1;
            background: linear-gradient(135deg, rgba(0, 229, 255, 0.8), rgba(41, 98, 255, 0.3) 50%, rgba(0, 229, 255, 0.8));
        }
        .icon-glow {
            position: absolute;
            inset: 0;
            background: inherit;
            filter: blur(15px);
            opacity: 0.6;
            transition: opacity 0.5s ease;
        }
        .group:hover .icon-glow {
            opacity: 1;
            filter: blur(25px);
        }
"""
html = re.sub(css_pattern, new_css, html)

# 2. Rebuild the Services Section with 12 items (6 duplicated for infinite scroll) and enhanced visuals
suite_pattern = re.compile(r'<!-- Section: Services -->.*?</section>', re.DOTALL)

cards_data = [
    {
        "icon": "hub", "id": "1", "color": "primary", "bg": "primary/15", "shadow": "rgba(0,229,255,0.2)"
    },
    {
        "icon": "campaign", "id": "2", "color": "secondary", "bg": "secondary/15", "shadow": "rgba(41,98,255,0.2)"
    },
    {
        "icon": "smart_toy", "id": "3", "color": "primary", "bg": "primary", "text_color": "background-dark", "shadow": "rgba(0,229,255,0.5)", "is_filled": True
    },
    {
        "icon": "insights", "id": "4", "color": "secondary", "bg": "secondary/15", "shadow": "rgba(41,98,255,0.2)"
    },
    {
        "icon": "rocket_launch", "id": "5", "color": "primary", "bg": "primary/15", "shadow": "rgba(0,229,255,0.2)"
    },
    {
        "icon": "auto_awesome", "id": "6", "color": "secondary", "bg": "secondary/15", "shadow": "rgba(41,98,255,0.2)"
    }
]

card_html_template = """
                <div class="flex-none w-[320px] sm:w-[380px] px-3">
                    <a href="#" class="group perspective-1000 h-[420px] block w-full">
                        <div class="flip-card-inner">
                            <!-- Front -->
                            <div class="flip-card-front glass-panel rounded-[2rem] flex flex-col justify-center items-center text-center bg-gradient-to-br from-surface-light via-slate-50 to-slate-100 dark:from-surface-dark dark:via-[#111827] dark:to-[#0B1120] shadow-[0_10px_40px_-15px_rgba(0,0,0,0.3)] p-8 relative overflow-hidden">
                                <div class="animated-border"></div>
                                <div class="absolute -top-24 -right-24 w-48 h-48 bg-{color}/10 rounded-full blur-3xl group-hover:bg-{color}/20 transition-colors duration-700"></div>
                                <div class="absolute -bottom-24 -left-24 w-48 h-48 bg-secondary/10 rounded-full blur-3xl group-hover:bg-secondary/20 transition-colors duration-700"></div>
                                
                                <div class="relative z-10 w-24 h-24 rounded-2xl {bg_class} flex items-center justify-center mb-8 text-{text_col} shadow-[0_0_20px_{shadow}] group-hover:-translate-y-2 transition-transform duration-500">
                                    <div class="icon-glow rounded-2xl"></div>
                                    <span class="material-icons text-6xl relative z-10 group-hover:scale-110 transition-transform duration-500">{icon}</span>
                                </div>
                                <h3 class="font-display text-3xl font-bold text-slate-900 dark:text-white relative z-10" data-i18n="s{id}_t">Title</h3>
                                <div class="mt-8 flex gap-1 items-center opacity-50 relative z-10">
                                    <span class="w-1.5 h-1.5 rounded-full bg-{color}"></span>
                                    <span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
                                    <span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
                                </div>
                            </div>
                            
                            <!-- Back -->
                            <div class="flip-card-back glass-panel rounded-[2rem] flex flex-col justify-center items-center text-center bg-slate-50 dark:bg-slate-900 shadow-[0_0_40px_{shadow}] p-8 relative overflow-hidden">
                                <div class="absolute inset-0 bg-gradient-to-t from-{color}/5 to-transparent pointer-events-none"></div>
                                <div class="animated-border opacity-50 group-hover:opacity-100"></div>
                                <h3 class="font-display text-2xl font-bold text-slate-900 dark:text-white mb-6 text-{color} relative z-10" data-i18n="s{id}_t">Title</h3>
                                <p class="text-base text-slate-600 dark:text-slate-300 font-medium leading-relaxed mb-8 relative z-10" data-i18n="s{id}_d">description.</p>
                                
                                <span class="mt-auto relative z-10 inline-flex items-center px-8 py-3.5 rounded-full bg-{color}/10 text-{color} font-semibold hover:bg-{color} hover:text-white transition-all duration-300 transform group-hover:scale-105 shadow-[0_0_15px_{shadow}]">
                                    <span data-i18n="learn_more">Learn More</span> 
                                    <span class="material-icons text-[18px] ml-2 rtl:mr-2 rtl:ml-0 rtl-flip">arrow_forward</span>
                                </span>
                            </div>
                        </div>
                    </a>
                </div>"""

generated_cards = []
for c in cards_data:
    bg_class = f"bg-{c['color']}" if c.get('is_filled') else f"bg-{c['bg']}"
    text_col = c.get('text_color', c['color'])
    card = card_html_template.format(
        icon=c['icon'], id=c['id'], color=c['color'], bg_class=bg_class, text_col=text_col, shadow=c['shadow']
    )
    generated_cards.append(card)

# Need 12 cards total for seamless marquee (2 repetitions of the 6 cards)
all_cards_html = "".join(generated_cards) * 2

new_suite = f"""<!-- Section: Services -->
<section class="py-24 relative z-10 overflow-hidden" id="suite" dir="ltr"> <!-- Marquee structure is easier locked to ltr for sliding, translating text via auto dir -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-20" dir="auto">
        <div class="text-center mb-20 relative">
            <h2 class="font-display text-5xl md:text-6xl font-bold text-slate-900 dark:text-white mb-6" data-i18n="suite_t">The O2Z Operating System</h2>
            <p class="text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto font-light" data-i18n="suite_sub">A unified architecture designed to seamlessly integrate every facet of your enterprise operations.</p>
        </div>
    </div>
    
    <div class="w-full relative mt-4 group-slider">
        <div class="animate-marquee items-center" dir="ltr">
{all_cards_html}
        </div>
        
        <div class="pointer-events-none absolute inset-y-0 left-0 w-16 md:w-32 bg-gradient-to-r from-background-light dark:from-background-dark to-transparent z-20"></div>
        <div class="pointer-events-none absolute inset-y-0 right-0 w-16 md:w-32 bg-gradient-to-l from-background-light dark:from-background-dark to-transparent z-20"></div>
    </div>
</section>"""

html = suite_pattern.sub(new_suite, html)

with open('C:/Users/abdal/o2z/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
