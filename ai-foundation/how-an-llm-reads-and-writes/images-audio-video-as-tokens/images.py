# One blank picture at four sizes: how many tokens does Claude count for each?
import base64, math, struct, zlib

import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
SIZES = [(200, 200), (1000, 1000), (1920, 1080), (3840, 2160)]


def blank_png(width, height):
    """A plain white PNG picture, made in memory: no file is read or written."""
    rows = (b"\x00" + b"\xff" * width) * height
    header = struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0)
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    body = chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b"")
    return b"\x89PNG\r\n\x1a\n" + body


def tokens(content):
    message = [{"role": "user", "content": content}]
    return client.messages.count_tokens(model=MODEL, messages=message).input_tokens


question = {"type": "text", "text": "What is in this picture?"}
text_only = tokens([question])
print(f"text only: {text_only} tokens")
print(f"{'size':<11}{'28px patches':>13}{'with image':>12}{'image tokens':>14}")
for width, height in SIZES:
    data = base64.b64encode(blank_png(width, height)).decode()
    image = {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": data}}
    with_image = tokens([image, question])
    patches = math.ceil(width / 28) * math.ceil(height / 28)
    size = f"{width}x{height}"
    print(f"{size:<11}{patches:>13}{with_image:>12}{with_image - text_only:>14}")
