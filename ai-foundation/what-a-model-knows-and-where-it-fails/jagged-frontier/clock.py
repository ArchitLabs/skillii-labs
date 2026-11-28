# Draws an analog clock as a PNG image, in memory, with nothing but Python's standard library.
import math
import struct
import zlib

SIZE = 400  # pixels across and down


def draw_clock(hour, minute):
    """PNG bytes of a black-on-white clock showing hour:minute. Nothing is saved to disk."""
    px = bytearray(b"\xff" * SIZE * SIZE)  # one grey byte per pixel, all white
    c = SIZE / 2

    def dot(x, y, r):  # a filled black disc
        for yy in range(int(y - r), int(y + r) + 1):
            for xx in range(int(x - r), int(x + r) + 1):
                if (xx - x) ** 2 + (yy - y) ** 2 <= r * r:
                    px[yy * SIZE + xx] = 0

    def stroke(turn, r0, r1, width):  # a line out from the centre; turn 0 points at 12, 0.25 at 3
        a = 2 * math.pi * turn
        for i in range(121):
            r = r0 + (r1 - r0) * i / 120
            dot(c + r * math.sin(a), c - r * math.cos(a), width)

    for i in range(720):  # the rim
        dot(c + 185 * math.cos(i * math.pi / 360), c + 185 * math.sin(i * math.pi / 360), 3)
    for k in range(60):  # a short tick for each minute, a long thick one for each hour
        stroke(k / 60, 160 if k % 5 == 0 else 172, 180, 3.5 if k % 5 == 0 else 1.5)
    stroke(0, 140, 180, 6)  # a heavier mark at 12, so the face has a top
    stroke((hour % 12 + minute / 60) / 12, 0, 95, 7)  # hour hand: short and thick
    stroke(minute / 60, 0, 150, 3)  # minute hand: long and thin
    rows = b"".join(b"\x00" + px[y * SIZE:(y + 1) * SIZE] for y in range(SIZE))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 0, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))


def chunk(kind, data):  # a PNG chunk: length, type, data, checksum
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
