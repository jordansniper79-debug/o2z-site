import os

def process_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into parts
    # Add translation keys
    en_insert = """                learn_more: "Book Service Now",
                contact_now: "Contact Us Now",
                soon: "SOON ✨","""
    if "contact_now: " not in content:
        content = content.replace('learn_more: "Book Service Now",', en_insert)

    ar_insert = """                learn_more: "احجز الخدمة الان",
                contact_now: "تواصل معنا الان",
                soon: "قريباً ✨","""
    if "contact_now: " not in content:
        content = content.replace('learn_more: "احجز الخدمة الان",', ar_insert)

    # Process all cards
    cards = content.split('<div class="flex-none w-[320px] sm:w-[380px] px-3">')
    
    new_cards = [cards[0]]
    for i in range(1, len(cards)):
        card = cards[i]
        
        # It's a card. Let's find its base link.
        # Change href globally for all cards first
        card = card.replace('<a href="#" class="group', '<a href="https://w.me/962797979760" target="_blank" class="group')
        
        # Is it in capabilities?
        # A capability card has data-i18n="c1_t" ... "c9_t"
        is_cap = False
        for j in range(1, 10):
            if f'data-i18n="c{j}_t"' in card:
                is_cap = True
                break
        
        if is_cap:
            card = card.replace('data-i18n="learn_more"', 'data-i18n="contact_now"')
            
        # Is it Omnichannel (s1_t or c1_t)?
        if 'data-i18n="s1_t"' in card or 'data-i18n="c1_t"' in card:
            # Change link to not open whatsapp
            card = card.replace('href="https://w.me/962797979760" target="_blank"', 'href="javascript:void(0)"')
            card = card.replace('class="group perspective-1000', 'class="group perspective-1000 cursor-default')
            
            # Find the button span block and replace it
            # The button block starts with <span and has data-i18n="learn_more" or "contact_now" inside.
            # We can just replace the whole mt-auto span block.
            import re
            
            # The backface button looks like:
            # <span class="mt-auto relative z-10 inline-flex items-center px-8 py-3.5 rounded-full bg-primary/10 text-primary font-semibold hover:bg-primary hover:text-white transition-all duration-300 transform group-hover:scale-105 shadow-[0_0_15px_rgba(0,229,255,0.2)]">
            #     <span data-i18n="learn_more">Learn More</span>
            #     <span class="material-icons text-[18px] ml-2 rtl:mr-2 rtl:ml-0 rtl-flip">arrow_forward</span>
            # </span>
            
            # Let's use regex to replace it
            pattern = r'<span[^>]*class="mt-auto relative[^>]*>.*?</span>\s*<span[^>]*>.*?</span>\s*</span>'
            soon_button = '''<span class="mt-auto relative z-10 inline-flex items-center px-8 py-3.5 rounded-full bg-gradient-to-r from-primary/20 to-secondary/20 border border-primary/50 text-white font-bold shadow-[0_0_25px_rgba(0,229,255,0.5)] animate-pulse backdrop-blur-md overflow-hidden before:absolute before:inset-0 before:bg-white/20 before:-translate-x-full hover:before:animate-[shimmer_1.5s_infinite]">
                                    <span class="relative z-10" data-i18n="soon">SOON ✨</span>
                                </span>'''
            card = re.sub(pattern, soon_button, card, flags=re.DOTALL)
            
        new_cards.append(card)

    result = '<div class="flex-none w-[320px] sm:w-[380px] px-3">'.join(new_cards)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
        
    print("Done")

if __name__ == "__main__":
    process_html()
