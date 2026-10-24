"""광명커튼 로고 · 파비콘 · 공유 이미지 생성.

아치형 창 안에 떠오르는 해(광명 = 밝은 빛) + 양옆으로 묶인 커튼.
실행: python3 _build/logo.py [글꼴 폴더]
  글꼴 폴더에 GowunBatang-Bold.ttf, Marcellus-Regular.ttf 가 있으면 그 글꼴로 글자를 씁니다.
  (Google Fonts 에서 무료로 받을 수 있음. 없으면 시스템 글꼴 사용)
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "fonts")
INK = (34, 48, 43)
PAPER = (247, 244, 236)
AMBER = (224, 164, 88)


def font(name, size, fallback="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"):
    p = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(p if os.path.exists(p) else fallback, size)


def mark(size, bg=True):
    """정사각 아이콘 (크게 그려서 줄이면 선이 매끄러움)"""
    S = 1024
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if bg:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=220, fill=INK)
    line = PAPER
    w = 34
    # 아치형 창틀
    l, r, top, bottom = 250, 774, 200, 820
    cx = (l + r) // 2
    rad = (r - l) // 2
    d.arc([l, top, r, top + 2 * rad], 180, 360, fill=line, width=w)
    d.line([(l + w // 2 - 1, top + rad), (l + w // 2 - 1, bottom)], fill=line, width=w)
    d.line([(r - w // 2, top + rad), (r - w // 2, bottom)], fill=line, width=w)
    d.line([(l - 40, bottom), (r + 40, bottom)], fill=line, width=w)
    # 떠오르는 해
    sun_y, sun_r = 690, 105
    d.pieslice([cx - sun_r, sun_y - sun_r, cx + sun_r, sun_y + sun_r], 180, 360, fill=AMBER)
    import math
    for ang in (200, 235, 270, 305, 340):
        a = math.radians(ang)
        x1, y1 = cx + math.cos(a) * (sun_r + 40), sun_y + math.sin(a) * (sun_r + 40)
        x2, y2 = cx + math.cos(a) * (sun_r + 105), sun_y + math.sin(a) * (sun_r + 105)
        d.line([(x1, y1), (x2, y2)], fill=AMBER, width=26)
    d.line([(l + 60, sun_y + 4), (r - 60, sun_y + 4)], fill=AMBER, width=14)
    # 양옆으로 묶인 커튼 자락 (위는 넓게, 끈 묶은 곳에서 좁게, 아래로 다시 퍼짐)
    y0, tie, y1 = top + 150, 600, bottom - w // 2

    def width(y):
        if y <= tie:
            t = (y - y0) / (tie - y0)
            return 120 - 92 * (t ** 1.6)
        t = (y - tie) / (y1 - tie)
        return 28 + 62 * (t ** 0.7)

    for side in (-1, 1):
        edge = l + w if side < 0 else r - w
        ys = range(y0, y1 + 1, 4)
        inner = [(edge - side * width(y), y) for y in ys]
        poly = [(edge, y0)] + inner + [(edge, y1)]
        d.polygon(poly, fill=line)
        d.line([(edge - side * 34, tie), (edge - side * 4, tie)], fill=AMBER, width=16)
    return img.resize((size, size), Image.LANCZOS)


def save(img, rel, fmt="PNG", **kw):
    path = os.path.join(ROOT, "images", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, fmt, **kw)


def logo_full():
    """세로형 전체 로고 (구조화 데이터 · 공유 이미지용)"""
    W, H = 900, 900
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m = mark(420, bg=False)
    img.alpha_composite(m, ((W - 420) // 2, 60))
    d = ImageDraw.Draw(img)
    ko = font("GowunBatang-Bold.ttf", 120)
    en = font("Marcellus-Regular.ttf", 40, "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf")
    t = "광명커튼"
    d.text(((W - d.textlength(t, font=ko)) / 2, 520), t, font=ko, fill=PAPER)
    e = "G W A N G M Y E O N G   C U R T A I N"
    d.text(((W - d.textlength(e, font=en)) / 2, 700), e, font=en, fill=AMBER)
    return img


def product_tile(title, sub, size=(900, 1200)):
    """실제 사진이 아직 없는 제품 칸을 채우는 브랜드 이미지 (로고 + 제품명)"""
    W, H = size
    img = Image.new("RGB", size, INK)
    d = ImageDraw.Draw(img)
    for y in range(H):   # 위는 조금 밝게
        t = y / H
        c = tuple(int(INK[k] + (12 if k else 8) * (1 - t)) for k in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # 커튼 주름 느낌의 세로 줄
    for x in range(60, W, 70):
        d.line([(x, 0), (x, H)], fill=(40, 56, 50), width=2)
    m = mark(360, bg=False)
    img.paste(m, ((W - 360) // 2, 260), m)
    ko = font("GowunBatang-Bold.ttf", 64)
    small = font("GowunBatang-Bold.ttf", 30)
    en = font("Marcellus-Regular.ttf", 30, "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf")
    d.line([((W - 80) // 2, 690), ((W + 80) // 2, 690)], fill=AMBER, width=3)
    d.text(((W - d.textlength(title, font=ko)) / 2, 730), title, font=ko, fill=PAPER)
    d.text(((W - d.textlength(sub, font=small)) / 2, 840), sub, font=small, fill=(196, 190, 176))
    e = "G W A N G M Y E O N G   C U R T A I N"
    d.text(((W - d.textlength(e, font=en)) / 2, H - 120), e, font=en, fill=AMBER)
    return img


if __name__ == "__main__":
    icon = mark(512)
    save(icon, "brand/logo-icon.png")
    save(mark(92, bg=True), "brand/logo-icon-sm.png")
    save(mark(180), "brand/apple-touch-icon.png")
    save(mark(64), "favicon.png")
    full = logo_full()
    bgfull = Image.new("RGBA", full.size, INK + (255,))
    bgfull.alpha_composite(full)
    save(bgfull.convert("RGB"), "brand/logo-full.png")
    og = Image.new("RGB", (1200, 630), INK)
    f2 = full.copy()
    f2.thumbnail((560, 560), Image.LANCZOS)
    og.paste(f2, ((1200 - f2.width) // 2, (630 - f2.height) // 2), f2)
    save(og, "og-image.jpg", "JPEG", quality=90)
    # 실제 사진이 생기면 photos.py 의 PRODUCT 에 넣으면 그 사진으로 덮어씀
    save(product_tile("전동 커튼 · 블라인드", "리모컨 하나로 여닫는 높은 창 · 넓은 통창"), "products/motor.jpg", "JPEG", quality=88)
    print("logo images written")
