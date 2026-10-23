"""받은 시공 사진(_build/photos-src/gm-XX.jpg)을 사이트용으로 자르고 줄여서 images/ 에 저장.

실행: python3 _build/photos.py
- 원본은 위치 정보(EXIF)를 지운 상태로 photos-src 에 보관
- 남의 상호 · 전화번호 · 모니터 화면처럼 보이면 안 되는 곳은 흐리게 처리
- 드리움 · 결앤빛 · 런던커튼 사진과 겹치지 않는지 비교해서 확인함 (README 참고)
"""
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_build", "photos-src")
OUT = os.path.join(ROOT, "images")

# 흐림 처리할 영역 (원본 좌표)
BLUR = {
    "01": [(1770, 430, 2016, 870),    # 달력 (다른 업체 상호 · 전화번호)
           (1610, 980, 1860, 1300)],  # 모니터 화면
    "18": [(1600, 630, 1805, 895),    # 화이트보드 손글씨
           (515, 935, 700, 1130),     # 모니터 화면
           (90, 1050, 940, 1300)],    # 책상 위 서류 · 달력
    "32": [(1280, 940, 2016, 1160),   # 창밖 상가 간판
           (290, 940, 530, 1160)],
    "39": [(1500, 730, 1760, 830),    # 창밖 간판
           (1250, 950, 1400, 1040),   # 창밖 간판
           (1220, 1035, 1460, 1275)], # 쇼핑백 글씨 · 사진
    "40": [(1140, 1010, 1390, 1260)], # 쇼핑백 글씨 · 사진
    "42": [(540, 715, 900, 785)],     # 창밖 건물 이름
}


# 결앤빛 네이버 블로그에 이미 쓴 사진 → 같은 사진으로 보이지 않게 편집
# mirror: 좌우 반전 / crop: (가로 기준점, 세로 기준점, 남길 비율) / tone: (밝기, 따뜻함)
EDIT = {
    "21": dict(mirror=True, crop=(0.25, 0.4, 0.86), tone=(1.04, 1.04)),
    "22": dict(mirror=True, crop=(0.5, 0.2, 0.84), tone=(1.03, 0.97)),
    "23": dict(mirror=True, crop=(0.5, 0.3, 0.85), tone=(1.05, 1.03)),
    "24": dict(mirror=True, crop=(0.3, 0.25, 0.86), tone=(1.04, 1.05)),
    "25": dict(mirror=True, crop=(0.4, 0.6, 0.85), tone=(1.03, 0.97)),
    "26": dict(mirror=True, crop=(0.6, 0.5, 0.84), tone=(1.04, 1.03)),
    "27": dict(mirror=True, crop=(0.35, 0.35, 0.85), tone=(0.98, 0.96)),
    "28": dict(mirror=True, crop=(0.45, 0.25, 0.86), tone=(1.04, 1.04)),
    # 결앤빛 시공사례에 쓴 사진
    "36": dict(mirror=True, crop=(0.4, 0.5, 0.85), tone=(1.04, 1.04)),
    "43": dict(mirror=True, crop=(0.6, 0.35, 0.86), tone=(1.03, 1.03)),
    "44": dict(mirror=True, crop=(0.35, 0.4, 0.85), tone=(1.04, 0.97)),
}


def edit(im, mirror=False, crop=None, tone=None):
    if crop:
        fx, fy, k = crop
        w, h = round(im.width * k), round(im.height * k)
        x0, y0 = round((im.width - w) * fx), round((im.height - h) * fy)
        im = im.crop((x0, y0, x0 + w, y0 + h))
    if mirror:
        im = ImageOps.mirror(im)
    if tone:
        bright, warm = tone
        im = ImageEnhance.Brightness(im).enhance(bright)
        r, g, b = im.split()
        r = r.point(lambda v: min(255, round(v * warm)))
        b = b.point(lambda v: min(255, round(v / warm)))
        im = Image.merge("RGB", (r, g, b))
    return im


def load(n):
    im = Image.open(os.path.join(SRC, f"gm-{n}.jpg")).convert("RGB")
    for box in BLUR.get(n, []):
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(18)), box[:2])
    if n in EDIT:
        im = edit(im, **EDIT[n])
    return im


def fit(im, aspect, box=None, focus=(0.5, 0.5)):
    """box 안에서 aspect(가로/세로) 비율로 가장 크게 자르기. focus 는 잘라낼 때 기준점"""
    x0, y0, x1, y1 = box or (0, 0, im.width, im.height)
    w, h = x1 - x0, y1 - y0
    if w / h > aspect:
        nw = round(h * aspect)
        x0 += round((w - nw) * focus[0]); x1 = x0 + nw
    else:
        nh = round(w / aspect)
        y0 += round((h - nh) * focus[1]); y1 = y0 + nh
    return im.crop((x0, y0, x1, y1))


def save(im, rel, size, quality=80):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im = im.resize(size, Image.LANCZOS)
    q = quality
    while True:
        im.save(path, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(path) <= 300_000 or q <= 60:
            break
        q -= 5


# 시공사례: 사례 번호 → [(원본 번호, focus)]  (첫 번째가 대표 사진)
CASE_PHOTOS = {
    "01": [("11", (0.5, 0.5)), ("10", (0.5, 0.5))],   # 거실 간접조명 커튼박스 · 아이보리 겉커튼 + 쉬폰
    "02": [("02", (0.5, 0.5))],                       # 거실 웨이브 겉커튼
    "03": [("04", (0.5, 0.5))],                       # 침실 암막 웨이브
    "04": [("05", (0.5, 0.5))],                       # 방 코너 창 그레이 겉커튼 + 쉬폰
    "05": [("09", (0.5, 0.5))],                       # 거실 화이트 쉬폰 (핀치)
    "06": [("07", (0.5, 0.5))],                       # 거실 쉬폰 (피아노 · 책장)
    "07": [("12", (0.5, 0.5))],                       # 공부방 쉬폰
    "08": [("16", (0.5, 0.5))],                       # 거실 콤비 블라인드
    "09": [("14", (0.5, 0.5))],                       # 주택 내닫이창 콤비
    "10": [("08", (0.5, 0.5))],                       # 사무실 콤비 블라인드
    "11": [("13", (0.5, 0.5))],                       # 침실 알루미늄 블라인드
    "12": [("15", (0.5, 0.35))],                      # 주방 알루미늄 블라인드 (세로 사진)
    "13": [("03", (0.5, 0.5))],                       # 복층 커튼월 롤스크린
    "14": [("01", (0.5, 0.5))],                       # 사무실 코너 롤스크린
    "15": [("06", (0.5, 0.5))],                       # 쉬폰 웨이브 클로즈업
    "16": [("23", (0.5, 0.5)), ("24", (0.5, 0.5))],   # 부천 거실 블루그레이 겉커튼 + 쉬폰
    "17": [("25", (0.5, 0.4)), ("26", (0.5, 0.5))],   # 부천 베란다 허니콤
    "18": [("27", (0.5, 0.45))],                      # 부천 도트 줄무늬 쉬폰
    "19": [("21", (0.5, 0.5)), ("22", (0.5, 0.4))],   # 마포 거실 웨이브 겉커튼 + 자석 타이백
    "20": [("28", (0.5, 0.5))],                       # 구로 거실 화이트 쉬폰
    "21": [("18", (0.5, 0.5))],                       # 고층 서재 콤비
    "22": [("19", (0.5, 0.5))],                       # 사무실 우드 블라인드
    "23": [("20", (0.5, 0.5))],                       # 거실 화이트 쉬폰 (천장형 에어컨)
    "24": [("30", (0.5, 0.5))],                       # 방 쉬폰 + 그레이 겉커튼
    "25": [("32", (0.5, 0.5))],                       # 사무실 콤비 (도로 쪽 창)
    "26": [("17", (0.5, 0.5))],                       # 쉬폰 사이로 드는 햇빛
    "27": [("29", (0.5, 0.5))],                       # 바닥 가까이 맞춘 쉬폰 기장
    "28": [("33", (0.5, 0.5))],                       # 안방 웨이브 겉커튼 (가운데 창)
    "29": [("35", (0.5, 0.5)), ("34", (0.5, 0.5))],   # 운동방 화이트 쉬폰
    "30": [("36", (0.5, 0.5))],                       # 거실 넓은 창 쉬폰
    "31": [("37", (0.5, 0.5))],                       # 거실 쉬폰 + 옆 창 알루미늄
    "32": [("38", (0.5, 0.5))],                       # 코너 거실 쉬폰 두 면
    "33": [("39", (0.5, 0.5)), ("40", (0.5, 0.5))],   # 상가 사무실 화이트 콤비 4칸
    "34": [("41", (0.5, 0.5))],                       # 거실 통창 알루미늄 블라인드
    "35": [("42", (0.5, 0.5)), ("43", (0.5, 0.5))],   # 방 롤스크린 2분할
    "36": [("44", (0.5, 0.5))],                       # 거실 쉬폰 (베란다 문)
    "37": [("45", (0.5, 0.5))],                       # 우드 블라인드 결
    "38": [("46", (0.5, 0.5))],                       # 작은 방 아이보리 롤스크린
    "39": [("47", (0.5, 0.45))],                      # 사무실 높은 창 다크우드
    "40": [("48", (0.5, 0.5))],                       # 휴게 공간 린넨 롤스크린
}

# 메인 슬라이드 · 페이지 배경 (원본 번호, focus)
HERO = {
    "hero-01": ("11", (0.5, 0.55)), "hero-02": ("04", (0.5, 0.5)), "hero-03": ("16", (0.5, 0.5)),
    "hero-gallery": ("07", (0.5, 0.4)), "hero-products": ("06", (0.5, 0.5)), "hero-areas": ("09", (0.5, 0.45)),
    "hero-blog": ("12", (0.5, 0.4)), "hero-about": ("10", (0.5, 0.5)), "hero-faq": ("05", (0.5, 0.4)),
    "hero-inquiry": ("02", (0.5, 0.4)), "hero-cta": ("03", (0.5, 0.5)),
}

# 제품 사진 (세로 3:4). 사진이 없는 제품은 자리표시 그대로 둠
PRODUCT = {
    "linen": ("02", (0.45, 0.5)), "chiffon": ("06", (0.55, 0.5)), "blackout": ("04", (0.7, 0.5)),
    "combi": ("16", (0.6, 0.5)), "roll": ("03", (0.5, 0.5)),
    "wood": ("19", (0.15, 0.5)), "honeycomb": ("25", (0.5, 0.4)),
}

ABOUT = {"about-01": ("10", (0.35, 0.5)), "about-02": ("14", (0.5, 0.5))}


if __name__ == "__main__":
    cache = {}

    def src(n):
        if n not in cache:
            cache[n] = load(n)
        return cache[n]

    for no, photos in CASE_PHOTOS.items():
        for k, (n, focus) in enumerate(photos):
            name = f"cases/case-{no}.jpg" if k == 0 else f"cases/case-{no}-{k + 1}.jpg"
            im = src(n)
            if im.height > im.width:      # 세로 사진은 세로 그대로
                save(fit(im, 3 / 4, focus=focus), name, (1200, 1600))
            else:
                save(fit(im, 4 / 3, focus=focus), name, (1600, 1200))
    for name, (n, focus) in HERO.items():
        save(fit(src(n), 16 / 9, focus=focus), f"hero/{name}.jpg", (1920, 1080), quality=78)
    for name, (n, focus) in PRODUCT.items():
        save(fit(src(n), 3 / 4, focus=focus), f"products/{name}.jpg", (900, 1200))
    for name, (n, focus) in ABOUT.items():
        save(fit(src(n), 4 / 5, focus=focus), f"about/{name}.jpg", (1000, 1250))
    print("photos written")
