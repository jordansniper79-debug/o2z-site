import sys

with open(r'c:\Users\abdal\o2z\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if '<div class="flex-none w-[320px] sm:w-[380px] px-3">' in line:
        # Collect this div
        j = i
        found_target = False
        block_end = i
        stack = []
        while j < len(lines):
            if '<div' in lines[j]: stack.append('div')
            if '</div' in lines[j]: stack.pop()
            
            if 'data-i18n="s5_t"' in lines[j] or 'data-i18n="s6_t"' in lines[j]:
                found_target = True
                
            if len(stack) == 0:
                block_end = j
                break
            j += 1
            
        if found_target:
            # We skip adding lines[i : block_end+1]
            i = block_end + 1
            continue

    new_lines.append(line)
    i += 1

with open(r'c:\Users\abdal\o2z\index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Removed s5 and s6 services.")
