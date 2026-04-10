import re

CSS = """
/* --- O2Z Before/After Capabilities Section --- */
.o2z-wrap{background:transparent;padding:72px 36px;max-width:900px;margin:0 auto;position:relative;overflow:hidden}
.o2z-glow{position:absolute;top:-80px;left:50%;transform:translateX(-50%);width:500px;height:300px;background:radial-gradient(ellipse,rgba(0,200,180,.07) 0%,transparent 70%);pointer-events:none}
.o2z-label{font-size:11px;letter-spacing:3px;color:#00c8b4;text-transform:uppercase;text-align:center;margin-bottom:12px}
.o2z-title{font-size:28px;font-weight:700;color:#fff;text-align:center;margin-bottom:8px;line-height:1.4}
.o2z-title span{color:#00c8b4}
.o2z-sub{font-size:13px;color:rgba(255,255,255,.35);text-align:center;margin-bottom:52px}
.o2z-hero{display:flex;align-items:center;justify-content:center;gap:0;max-width:700px;margin:0 auto 40px}
.o2z-side{flex:1;padding:22px 20px;border-radius:14px}
.o2z-side-before{background:rgba(255,60,60,.06);border:1px solid rgba(255,60,60,.15);transition:opacity .6s ease,filter .6s ease}
.o2z-side-before.faded{opacity:.15;filter:blur(1px)}
.o2z-side-before h4{font-size:11px;color:rgba(255,100,100,.6);margin-bottom:12px;letter-spacing:1px;text-transform:uppercase}
.o2z-prob{font-size:12px;color:rgba(255,255,255,.28);margin-bottom:8px;display:flex;align-items:flex-start;gap:6px}
.o2z-prob::before{content:'✕';color:rgba(255,80,80,.4);font-size:10px;flex-shrink:0;margin-top:1px}
.o2z-prob-text{position:relative;display:inline-block}
.o2z-prob-text::after{content:'';position:absolute;left:0;top:50%;width:0%;height:2.5px;background:rgba(255,70,70,.8);transition:width .4s ease}
.o2z-prob-text.struck::after{width:100%}
.o2z-mid{width:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;flex-shrink:0}
.o2z-logo-circle{width:54px;height:54px;border-radius:50%;background:#00c8b4;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#080d1a}
.o2z-logo-circle.burst{animation:o2zBurst .6s ease forwards}
@keyframes o2zBurst{0%{box-shadow:0 0 0 0 rgba(0,200,180,.7)}50%{box-shadow:0 0 0 28px rgba(0,200,180,0)}100%{box-shadow:0 0 0 0 rgba(0,200,180,0)}}
.o2z-arr-icon{font-size:18px;color:#00c8b4;transition:transform .4s ease;display:inline-block}
html[dir="rtl"] .o2z-arr-icon{transform:scaleX(-1)}
.o2z-side-after{background:rgba(0,200,180,.05);border:1px solid rgba(0,200,180,.15);opacity:0;transition:opacity .6s ease,transform .6s ease}
html[dir="ltr"] .o2z-side-after{transform:translateX(12px)}
html[dir="rtl"] .o2z-side-after{transform:translateX(-12px)}
.o2z-side-after.revealed{opacity:1;transform:translateX(0)!important}
.o2z-side-after h4{font-size:11px;color:#00c8b4;margin-bottom:12px;letter-spacing:1px;text-transform:uppercase}
.o2z-sol{font-size:12px;color:rgba(255,255,255,.8);margin-bottom:8px;display:flex;gap:6px;align-items:flex-start;opacity:0;transform:translateY(6px);transition:opacity .3s ease,transform .3s ease}
.o2z-sol.show{opacity:1;transform:translateY(0)}
.o2z-sol::before{content:'✓';color:#00c8b4;font-size:11px;flex-shrink:0;font-weight:700;margin-top:1px}
.o2z-savings{max-width:700px;margin:0 auto 36px;background:rgba(0,200,180,.05);border:1px solid rgba(0,200,180,.12);border-radius:12px;padding:20px 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center;opacity:0;transform:translateY(10px);transition:opacity .5s ease,transform .5s ease}
.o2z-savings.show{opacity:1;transform:translateY(0)}
.o2z-sav-num{font-size:22px;font-weight:800;color:#00c8b4}
.o2z-sav-lbl{font-size:10px;color:rgba(255,255,255,.3);margin-top:3px;line-height:1.4}
.o2z-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;max-width:700px;margin:0 auto 40px;background:rgba(255,255,255,.04);border-radius:14px;overflow:hidden}
.o2z-card{background:#0d1322;padding:22px 18px;opacity:0;transform:translateY(8px);transition:background .3s,opacity .4s ease,transform .4s ease}
.o2z-card.show{opacity:1;transform:translateY(0)}
.o2z-card:hover{background:#111928}
.o2z-before-line{font-size:11px;color:rgba(255,255,255,.22);margin-bottom:6px;display:flex;gap:5px;align-items:flex-start}
.o2z-before-line::before{content:'✕';color:rgba(255,80,80,.35);font-size:9px;flex-shrink:0;margin-top:2px}
.o2z-before-line-text{position:relative;display:inline-block}
.o2z-before-line-text::after{content:'';position:absolute;left:0;top:50%;width:0%;height:2px;background:rgba(255,70,70,.7);transition:width .4s ease}
.o2z-before-line-text.struck::after{width:100%}
.o2z-after-line{font-size:13px;font-weight:600;color:#fff;line-height:1.4;margin-bottom:8px;display:flex;gap:5px;align-items:flex-start;opacity:0;transition:opacity .4s ease .2s}
.o2z-after-line.show{opacity:1}
.o2z-after-line::before{content:'✓';color:#00c8b4;flex-shrink:0;font-size:11px;margin-top:2px;font-weight:700}
.o2z-stag{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:rgba(0,200,180,.45)}
.o2z-divider{border:none;border-top:1px solid rgba(255,255,255,.05);max-width:700px;margin:0 auto 32px}
.o2z-cta{text-align:center}
.o2z-cta-t{font-size:19px;font-weight:700;color:#fff;margin-bottom:6px}
.o2z-cta-s{font-size:13px;color:rgba(255,255,255,.3);margin-bottom:22px}
.o2z-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.o2z-btn1{background:#00c8b4;color:#080d1a;border:none;padding:13px 30px;border-radius:50px;font-size:13px;font-weight:700;cursor:pointer;transition:opacity .2s}
.o2z-btn1:hover{opacity:.85}
.o2z-btn2{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.15);padding:13px 30px;border-radius:50px;font-size:13px;cursor:pointer;transition:border-color .2s}
.o2z-btn2:hover{border-color:rgba(255,255,255,.4)}
@media(max-width:600px){.o2z-hero{flex-direction:column}.o2z-mid{flex-direction:row;width:100%;justify-content:center}.o2z-cards{grid-template-columns:1fr 1fr}.o2z-savings{grid-template-columns:repeat(2,1fr)}}
/* --- End O2Z Capabilities --- */
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already injected
if '.o2z-wrap' in content:
    print("CSS already exists in index.html — nothing to do.")
else:
    # Find the LAST </style> tag and inject before it
    last_style_pos = content.rfind('</style>')
    if last_style_pos == -1:
        print("ERROR: Could not find </style> tag!")
    else:
        new_content = content[:last_style_pos] + CSS + content[last_style_pos:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ CSS injected successfully!")
        print(f"   File size: {len(new_content.splitlines())} lines")
