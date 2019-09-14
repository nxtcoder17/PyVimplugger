import os
from pathlib import Path
import threading
import subprocess
from ColorPython import pprint
import time

PLUGIN_HOME = Path(os.environ['HOME']).joinpath (".vim/pack/plugins")
# PLUGIN_HOME = Path(os.environ['HOME']).joinpath (".config/nvim/pack/plugins")

START = PLUGIN_HOME.joinpath ("./start")
OPT = PLUGIN_HOME.joinpath ("./opt")

CONFIG_FILE = Path(os.environ['HOME']).joinpath ("./.vimplugger")

def makedirs (dir):
    try:
        os.makedirs (dir)
    except FileExistsError:
        pass
makedirs (PLUGIN_HOME)
makedirs (START)
makedirs (OPT)

plugins = []
for line in open(CONFIG_FILE):
    line = line.split('#', 1)[0].strip()
    if line:
        plugins.append (line)

# print (plugins)

def plugin_dir (x):
    if x.lower() == 'start':
        return START
    elif x.lower() == 'opt':
        return OPT
    return None

def cloner (url, dir):
    try:
        process = subprocess.run (f"git clone {url} {dir}".split(), capture_output=True)
        process.check_returncode()
    except subprocess.CalledProcessError as e:
        print ("ERROR: ", e)

def puller (url, dir):
    try:
        process = subprocess.run ("git pull".split(), cwd = dir, capture_output=True)
    except subprocess.CalledProcessError as e:
        print (" update ERROR");

def progress(msg, cond_thread):
    symbols = ('|   ', '\\   ', '|   ', '/   ')
    count = 0
    print("[" + pprint ("green", "bold", msg.split()[0]) + "] " + pprint("yellow", "bold", msg.split()[1]), end=' ')
    start = time.time()
    while cond_thread.is_alive():
        print(symbols[count], end='\b\b\b\b')
        if time.time() - start > 0.1:
            count += 1
            start = time.time()
        count = count % len(symbols)
    print(pprint("purple", 'bold', 'Done'))

for plugin in plugins:
    url, dir = plugin.split(' ')
    name = url.split('/')[-1]
    dir = plugin_dir (dir)
    # print (name)
    # print (set ([x.stem for x in dir.iterdir()]))
    if dir is not None:
        if name not in set([x.stem for x in dir.iterdir()]):
            #### Make a git clone for plugin
            thread = threading.Thread (target = cloner, args=(url, dir.joinpath(name)))
            thread.start()
            bar = threading.Thread (target = progress, args = (f"cloning {name}", thread))
            bar.start()
        else:
            #### Make a git pull for plugin
            thread = threading.Thread (target = puller, args=(url, dir.joinpath(name)))
            thread.start()
            bar = threading.Thread (target = progress, args = (f"pulling {name}", thread))
            bar.start()
        while (bar.is_alive()):
            pass
    else:
        print ("[ERROR]: There is an error in your vimplugger configuration......")
