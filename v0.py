# async era starts here 
import asyncio
import logging
import random
import os
from pyfiglet import figlet_format
from cfonts import render
from urllib.parse import unquote
from playwright.async_api import async_playwright
#from fake_useragent import UserAgent


#ua = UserAgent()
#user_agent = ua.random
#print("User-Agent being used:", user_agent)

# 🎨 Terminal colors
# config.py
COLORS = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
     'cyan': '\033[36m',
    'blue': '\033[1;34m',
    'reset': '\033[0m',
    'gold': '\x1b[38;5;220m',
    'bold': '\033[1m',
}

background_colors = {
    'black'     : '\033[40m',
    'red'       : '\033[41m',
    'green'     : '\033[42m',
    'yellow'    : '\033[43m',
    'blue'      : '\033[44m',
    'magenta'   : '\033[45m',
    'cyan'      : '\033[46m',
    'white'     : '\033[47m'
}

background_256 = {
    'bright_magenta' : '\033[48;5;201m',
    'bright_blue'    : '\033[48;5;117m',
    'bright_green'   : '\033[48;5;82m',
    'bright_yellow'  : '\033[48;5;226m',
    'bright_cyan'    : '\033[48;5;87m',
    'bright_red'     : '\033[08;5;196m',
    'gray'           : '\033[48;5;244m',
    'orange'         : '\033[48;5;208m',
    'purple'         : '\033[48;5;93m'
}

def lago():
    print(render("• RAYSIST •", colors=["red", "white"]))
def logo():
    print(render("• GAME OVER •", colors=["red", "white"]))

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(render("• RAYSIST •", colors=["red", "blue"]))
    print(COLORS['blue'] + "Instagram automation NC " + COLORS['reset'])
    print(COLORS['yellow'] + "Created by RAYSIST." + COLORS['reset'])
    print(COLORS['red'] + "RAYSIST NC TOOL" + COLORS['reset'])
    print(COLORS['green']+COLORS['bold']+ "also known as\033[0m  "+background_256["bright_red"]+"the RDP killer" + COLORS['reset'])  
    print(background_256['bright_cyan'] + "ASYNC version" + COLORS['reset'])
   # print(render("• RAYSIST •", colors=["red", "blue"]))

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


# Emoji bases
try:
    with open("ufo_bases.txt", "r", encoding="utf-8") as f:
        ufo_bases = [line.strip() for line in f if line.strip()]
except Exception:
    ufo_bases = [ " AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR ", "AMIL CHAMAAR "  
]
emoji_suffixes = ["💔", "😖", "🦋", "🤍", "🔥", "⁉️", "😞", "👾" ,"🤤", "😋", "😛", "👌", "☺️", "😝", "😕", "🙂", "🤛", "🤜", "🤚", "👋", "🫶", "🙌", "👐", "✍️", "🤟", "🤲", "🙏", "💅", "💅", "🩷", "🧡", "💛", "💚", "💔", "❤️", "🔥", "❤️", "🩹", "❣️", "💕", "💞", "💟", "💝", "💘", "💖", "💓", "💗", "💌", "💢", "💥", "💤", "💦", "💨", "❤️", "🧡", "❤️‍🔥", "☮️", "🌑", "🌘", "🌗", "🌖", "🌖", "🌕", "🌔", "🌓", "🌒", "🐯", "🐱", "🦁", "🐻‍❄️", "🐨", "🐼", "🐹", "🦝", "🐭", "🐰", "🐺", "🐻", "🐷", "🐽", "⚕️", "♾️", "🐗", "🦓", "🦓", "🦓", "🦄", "⚛️", "🐉", "🦖", "🦕", "🉑", "💮", "🪷", "🉐", "🐲", "🦎", "🆑", "🙈", "🙉", "🙊", "🚼", "🈲", "🅾️", "⛔", "🐴", "🛑", "📛", "❌", "⭕", "🚫", "🔇", "🔕", "🚭", "🚷", "❗", "📵", "🔞", "🚱", "🚳", "🚯", "❕", "❓", "❔", "‼️", "🫁", "🦁", "☢️", "〽️", "⚜️", "🔱", "🔆", "🔅", "☣️", "☄️", "🚸", "🔰", "♻️", "🈯", "💠", "🌛", "✳️", "🌍", " 🌏", "🌏", "➿", "🌫️", "🛃", "🌚", "🌜", "🌝", "⛰️", "🏔️", "☀️", "🌤️", "🌥️", "🌦️", "⛈️", "🌩️", "🌧️", "🪨", "🌀", "🌨️", "🏞️", "🌈", "🌪️", "☃️", "⚡", "⛄", "🌺", "🍂", "🌻", "🍀", "🪴", "🌴", "🌲", "🪵", "🌱", "💮", "🪷", "🥀", "🌹"] 
used_names = set()
success_count = 0
fail_count = 0
lock = asyncio.Lock()

# Inputs
banner()
session_id = input("Session ID: ").strip() or unquote('______')
dm_url = input("Group chat URL: ").strip() or 'https://www.instagram.com/direct/t/832560749198761/'
try:
    task_count = int(input("Number of async tasks: ").strip())
except:
    task_count = 5

def generate_name():  
        base = random.choice(ufo_bases)
        emoji = random.choice(emoji_suffixes)
        name = f"{base}_{emoji}"
        return name

async def rename_loop(context):
    global success_count, fail_count
    page = await context.new_page()
    try:
        await page.goto(dm_url, wait_until='domcontentloaded', timeout=600000)
        gear = page.locator('svg[aria-label="Conversation information"]')
        await gear.wait_for(timeout=160000)
        await gear.click()
        await asyncio.sleep(1)
    except Exception as e:
        logging.error(f"Page init failed: {e}")
        return

    change_btn = page.locator('div[aria-label="Change group name"][role="button"]')
    group_input = page.locator('input[aria-label="Group name"][name="change-group-name"]')
    save_btn = page.locator('div[role="button"]:has-text("Save")')

    while True:
        try:
            name = generate_name()
            await change_btn.click()
            await group_input.click(click_count=3)
            await group_input.fill(name)

            disabled = await save_btn.get_attribute("aria-disabled")
            if disabled == "true":
                async with lock:
                    fail_count += 1
                continue

            await save_btn.click()
            async with lock:
                success_count += 1

            await asyncio.sleep(0.05)

        except Exception:
            async with lock:
                fail_count += 1
            await asyncio.sleep(0.1)

async def live_stats():
    while True:
        async with lock:
            
            #print(f"\033[1;33mSession ID: {session_id}\033[0m")
            print(f"\033[1;34mDM URL: {dm_url}\033[0m")
            print(f"\033[1;35mTasks: {task_count}\033[0m")
            print(f"\033[1;36mUsed Names: {len(used_names)}\033[0m")
            print(f"\033[1;37mTotal Attempts: {success_count + fail_count}\033[0m")
            print(f"\033[42m✅ Success: {success_count}\033[0m  \033[41m❌ Failed: {fail_count}\033[0m", end="\r")
        await asyncio.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'])

        context = await browser.new_context(
           # user_agent=user_agent,
            locale="en-US",
            extra_http_headers={"Referer": "https://www.instagram.com/"},
            viewport=None
        )
        await context.add_cookies([{
            "name": "sessionid",
            "value": session_id,
            "domain": ".instagram.com",
            "path": "/",
            "httpOnly": True,
            "secure": True,
            "sameSite": "None"
        }])

        tasks = [asyncio.create_task(rename_loop(context)) for _ in range(task_count)]
        tasks.append(asyncio.create_task(live_stats()))

        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            print("\n👋 Done.")
            logo()
        finally:
            await browser.close()

if __name__ == "__main__":
    
    asyncio.run(main())

input()