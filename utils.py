debug_enabled = False  # updated from config later

def set_debug(value):
    global debug_enabled
    debug_enabled = value


def debug(msg):
    if debug_enabled:
        print("[DEBUG]", msg)
