import ujson

FILE_NAME = "unsent.jsonl"

def save(reading):
    with open(FILE_NAME, "a") as f:
        f.write(ujson.dumps(reading) + "\n")

def load_all():
    try:
        with open(FILE_NAME, "r") as f:
            return f.readlines()
    except:
        return []

def overwrite(lines):
    with open(FILE_NAME, "w") as f:
        for line in lines:
            f.write(line)
