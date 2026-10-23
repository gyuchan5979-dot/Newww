"""광명커튼 사이트 생성기 - 공통 설정과 HTML 틀.

이 폴더(_build)는 FTP에 올리지 않아도 됩니다.
`python3 _build/build.py` 를 실행하면 루트의 HTML · sitemap.xml · rss.xml · js/includes.js 가 다시 만들어집니다.
"""
import html
import json

DOMAIN = "gmcurtain.co.kr"          # ★ 도메인을 사면 여기만 바꾸고 다시 생성
SITE = "https://" + DOMAIN
BRAND = "광명커튼"
BRAND_EN = "GWANGMYEONG CURTAIN"
PHONE = "010-8353-5979"
VER = "202610241230"             # 캐시 갱신용 (사진 · CSS를 바꾸면 숫자 올리기)
TODAY = "2026-10-24"
BASE_LOCALITY = "광명시"

esc = html.escape


def v(path):
    """정적 파일 주소에 캐시 버전 붙이기"""
    return f"{path}?v={VER}"


def ld_script(obj):
    return ('    <script type="application/ld+json">\n'
            + json.dumps(obj, ensure_ascii=False, indent=4).replace("\n", "\n    ")
            + "\n    </script>\n")


def business_ld(name=None, url=SITE + "/", area=None, desc=None):
    obj = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": name or BRAND,
        "alternateName": BRAND_EN,
        "url": url,
        "image": SITE + "/" + v("images/og-image.jpg"),
        "logo": SITE + "/images/brand/logo-full.png",
        "telephone": PHONE,
        "legalName": "드리움커튼블라인드",
        "taxID": "210-42-66972",
        "founder": {"@type": "Person", "name": "조규찬"},
        "priceRange": "₩₩",
        "sameAs": ["https://pf.kakao.com/_PJixjX"],
        "description": desc or "광명 철산 · 하안 · 소하 · 광명뉴타운 · 광명역세권 커튼 · 블라인드 맞춤 제작과 시공. 광명을 중심으로 서울 서남권과 경기 곳곳을 방문해 무료로 실측합니다.",
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "KR",
            "addressRegion": "경기도",
            "addressLocality": BASE_LOCALITY,
        },
        "areaServed": area or [
            {"@type": "City", "name": "광명시"},
            {"@type": "City", "name": "시흥시"},
            {"@type": "City", "name": "안양시"},
            {"@type": "City", "name": "부천시"},
            {"@type": "AdministrativeArea", "name": "서울특별시"},
            {"@type": "AdministrativeArea", "name": "경기도"},
        ],
    }
    return obj


def breadcrumb_ld(crumbs):
    """crumbs: [(이름, 파일명 또는 '')]"""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": SITE + "/" + ("" if f in ("index.html", "") and i == 0 else f)}
            for i, (n, f) in enumerate(crumbs)
        ],
    }


def faq_ld(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }


def head(title, desc, keywords, path, og_image="images/og-image.jpg", og_type="website",
         lds=(), noindex=False, verify=False):
    url = SITE + "/" + ("" if path == "index.html" else path)
    t, d = esc(title), esc(desc)
    out = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO 메타태그 -->
    <title>{t}</title>
    <meta name="description" content="{d}">
    <meta name="keywords" content="{esc(keywords)}">
'''
    if noindex:
        out += '    <!-- 검색 제외 페이지 (시공사례 페이지는 _build/build.py 의 CASES 에 사례가 생기면 자동으로 해제됨) -->\n'
        out += '    <meta name="robots" content="noindex, follow">\n'
    out += f'''    <link rel="canonical" href="{url}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="{BRAND}">
    <meta property="og:locale" content="ko_KR">
    <meta property="og:title" content="{t}">
    <meta property="og:description" content="{d}">
    <meta property="og:image" content="{SITE}/{v(og_image)}">
    <meta property="og:url" content="{url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#22302B">
    <link rel="icon" href="{v('images/favicon.png')}" type="image/png">
    <link rel="apple-touch-icon" href="{v('images/brand/apple-touch-icon.png')}">
    <link rel="alternate" type="application/rss+xml" title="{BRAND} 매거진" href="{SITE}/rss.xml">
'''
    if verify:
        out += '''    <!-- 네이버 서치어드바이저 / 구글 서치콘솔 인증 메타태그는 여기에 붙여넣기 -->
    <!-- <meta name="naver-site-verification" content=""> -->
    <!-- <meta name="google-site-verification" content=""> -->
'''
    for obj in lds:
        out += ld_script(obj)
    out += f'''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Marcellus&family=Gowun+Batang:wght@400;700&display=swap">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
    <link rel="stylesheet" href="{v('css/reset.css')}">
    <link rel="stylesheet" href="{v('css/style.css')}">
    <script>document.documentElement.classList.add('js');</script>
</head>
<body>

    <!-- 공통 헤더 (includes.js가 채움) -->
    <div id="site-header"></div>

    <main>
'''
    return out


def foot():
    return f'''    </main>

    <!-- 하단 상담 섹션 (includes.js가 채움) -->
    <div id="site-cta"></div>

    <!-- 공통 푸터 (includes.js가 채움) -->
    <div id="site-footer"></div>

    <script src="{v('js/config.js')}"></script>
    <script src="{v('js/includes.js')}"></script>
    <script src="{v('js/main.js')}"></script>
</body>
</html>
'''


def page(path, title, desc, keywords, body, crumbs=None, **kw):
    lds = list(kw.pop("lds", ()))
    if crumbs:
        lds.append(breadcrumb_ld([("홈", "index.html")] + crumbs))
    return head(title, desc, keywords, path, lds=lds, **kw) + body + foot()


# ---------------------------------------------------------------
# 제품 (products.html 의 #앵커와 이미지 파일명)
# ---------------------------------------------------------------
PRODUCTS = {
    "linen":     {"name": "린넨 커튼",        "en": "LINEN",            "short": "거친 결 사이로 햇빛이 순하게 번지는 겉커튼"},
    "chiffon":   {"name": "쉬폰 커튼",        "en": "SHEER",            "short": "낮에도 커튼을 닫고 지낼 수 있게 해 주는 속커튼"},
    "blackout":  {"name": "암막 커튼",        "en": "BLACKOUT",         "short": "단지 조명과 새벽빛을 막아 주는 침실용"},
    "combi":     {"name": "콤비 블라인드",    "en": "COMBI",            "short": "망사와 원단을 겹쳐 밝기를 고르는 기본형"},
    "wood":      {"name": "우드 블라인드",    "en": "WOOD",             "short": "슬랫을 기울여 빛이 들어오는 각도를 바꾸는"},
    "honeycomb": {"name": "허니콤 블라인드",  "en": "HONEYCOMB",        "short": "벌집 공기층이 창가 찬 기운을 덜어 주는"},
    "roll":      {"name": "롤스크린",          "en": "ROLLER",           "short": "말아 올리면 창이 그대로 드러나는 한 장"},
    "motor":     {"name": "전동 커튼 · 블라인드", "en": "MOTOR",          "short": "고층 통창과 높은 창을 리모컨으로"},
}


def product_card(key, cls="product-card"):
    p = PRODUCTS[key]
    return (f'                <a href="products.html#{key}" class="{cls}">\n'
            f'                    <div class="product-img"><img src="{v("images/products/" + key + ".jpg")}" alt="{p["name"]} 시공 사진" loading="lazy"></div>\n'
            f'                    <h3>{p["name"]}</h3>\n'
            f'                    <p>{p["short"]}</p>\n'
            f'                </a>\n')
