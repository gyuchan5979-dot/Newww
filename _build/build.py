"""광명커튼 사이트 생성.

실행: python3 _build/build.py   (저장소 루트 또는 어디서든)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (SITE, DOMAIN, BRAND, BRAND_EN, PHONE, TODAY, VER, PRODUCTS, esc, v,
                    page, business_ld, faq_ld, product_card)
from areas_data import AREAS, GROUPS, OTHER_AREAS, BY_SLUG as AREA
from posts_data import POSTS, BY_SLUG as POST
from photos import PRODUCT as _PHOTO_PRODUCT

PHOTO_PRODUCTS = set(_PHOTO_PRODUCT)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
written = []


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    written.append(path)


def area_file(a):
    return f"area-{a['slug']}.html"


def date_dot(d):
    return d.replace("-", ".")


# ---------------------------------------------------------------
# 시공사례 — 실제 시공 사진이 생기면 여기에 추가하세요.
# 사진: images/cases/case-01.jpg (대표), case-01-2.jpg (두 번째) … / 권장 1600×1200
# 형식 (cat: curtain / blind / motor / commercial, 여러 개면 띄어쓰기):
#   dict(no="01", cat="curtain", space="광명 철산 · 34평 거실", product="겉커튼 + 쉬폰",
#        spec="베이지 린넨 겉커튼 + 화이트 쉬폰 (이중 레일)", photos=1,
#        title="사례 제목", text="시공 내용 설명",
#        points=["포인트 1", "포인트 2", "포인트 3"]),
# 지역 · 평수를 space 에 적으면 지역 검색에 크게 도움이 됩니다.
# 사례가 하나라도 생기면 메인에 사례 영역이 나타나고 시공사례 페이지가 검색에 노출됩니다.
# ---------------------------------------------------------------
CASES = [
    dict(no="01", cat="curtain", space="거실", product="겉커튼 + 쉬폰", spec="아이보리 겉커튼 + 화이트 쉬폰 (간접조명 커튼박스 · 이중 레일)", photos=2,
         title="간접조명 아래 아이보리 겉커튼과 화이트 쉬폰",
         text="천장 커튼박스에 간접조명이 들어간 거실에 아이보리 겉커튼과 화이트 쉬폰을 이중 레일로 달았습니다. 낮에는 겉커튼을 양옆으로 모아 두고 쉬폰만 닫아 빛을 부드럽게 들이고, 밤에는 겉커튼까지 닫으면 조명이 주름을 따라 은은하게 번집니다. 두 사진은 같은 집 거실입니다.",
         points=["간접조명과 겹치지 않도록 커튼박스 안쪽에 레일 배치", "겉커튼을 벽 끝까지 모아 열었을 때 창이 넓게 드러나게", "바닥에 살짝 닿는 기장으로 주름 끝을 정돈"],
         captions=["겉커튼은 열고 쉬폰만 닫았을 때", "겉커튼까지 닫았을 때"]),
    dict(no="02", cat="curtain", space="거실", product="겉커튼", spec="라이트그레이 결 원단 겉커튼 (웨이브 주름 · 천장 레일)", photos=1,
         title="천장형 에어컨 아래 라이트그레이 웨이브 커튼",
         text="천장형 에어컨이 있는 거실 창에 결이 살아 있는 라이트그레이 겉커튼을 웨이브 주름으로 달았습니다. 천장 바로 아래에서 시작해 바닥까지 떨어지도록 맞춰 층고가 높아 보이고, 물결처럼 일정한 주름이 벽 한 면을 차분하게 채웁니다.",
         points=["천장형 에어컨과 겹치지 않는 레일 위치", "S자 웨이브 레일로 주름 간격을 고르게", "옆 출입문과 간섭이 없도록 레일 길이 조절"]),
    dict(no="03", cat="curtain", space="침실", product="암막 커튼", spec="그레이베이지 암막 커튼 (웨이브 주름 · 천장 레일)", photos=1,
         title="빛을 막아 주는 침실 그레이베이지 암막 커튼",
         text="침대 옆 큰 창에 그레이베이지 암막 커튼을 웨이브 주름으로 달았습니다. 낮에도 커튼을 닫으면 방이 차분하게 어두워져 쉬기 좋고, 두께감 있는 원단이 일정한 주름을 만들어 침실이 정돈돼 보입니다.",
         points=["천장 바로 아래에 레일을 달아 위쪽 빛샘 줄이기", "창보다 넓게 레일을 빼서 옆으로 새는 빛 줄이기", "바닥 가까이 맞춘 기장"]),
    dict(no="04", cat="curtain", space="방", product="겉커튼 + 쉬폰", spec="그레이 겉커튼 + 화이트 쉬폰 (코너 창 두 곳 · 이중 레일)", photos=1,
         title="두 면에 창이 난 방, 그레이 겉커튼과 화이트 쉬폰",
         text="벽 두 면에 창이 하나씩 있는 방에 창마다 그레이 겉커튼과 화이트 쉬폰을 이중 레일로 달았습니다. 쉬폰만 닫아도 바깥 풍경이 은은하게 비치면서 시선은 흐려지고, 겉커튼을 닫으면 방이 아늑해집니다. 창 아래 공간을 쓸 수 있도록 창틀 조금 아래까지 오는 기장으로 맞췄습니다.",
         points=["창마다 따로 재서 두 창의 높이와 길이를 맞춤", "창 아래 공간을 살린 짧은 기장", "겉커튼과 쉬폰을 따로 여닫는 이중 레일"]),
    dict(no="05", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (핀치 주름 · 커튼박스)", photos=1,
         title="TV 맞은편 거실 창을 채운 화이트 쉬폰",
         text="TV가 걸린 벽 맞은편 거실 창에 화이트 쉬폰을 나비(핀치) 주름으로 달았습니다. 낮에 쉬폰을 닫아 두면 화면에 비치는 햇빛이 줄고, 거실이 하얀 빛으로 고르게 밝아집니다.",
         points=["커튼박스 양 끝까지 채운 레일", "두 장이 가운데서 겹치도록 넉넉한 폭", "바닥에서 살짝 띄운 기장으로 청소가 편하게"]),
    dict(no="06", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (핀치 주름 · 넓은 창)", photos=1,
         title="피아노와 책장이 있는 거실의 넓은 창, 화이트 쉬폰",
         text="피아노와 낮은 책장이 놓인 거실의 넓은 창에 화이트 쉬폰을 달았습니다. 창틀 모양이 쉬폰 너머로 은은하게 비치고, 햇빛이 주름 사이로 걸러져 책장 위까지 부드럽게 퍼집니다.",
         points=["가구 뒤로도 여닫기 편하도록 넉넉한 주름 배수", "천장 몰딩 아래 레일", "넓은 창을 한 번에 덮는 폭"]),
    dict(no="07", cat="curtain", space="공부방", product="쉬폰 커튼", spec="화이트 쉬폰 (천장 레일)", photos=1,
         title="책상 앞 눈부심을 덜어 준 공부방 화이트 쉬폰",
         text="책상이 창 옆에 놓인 공부방에 화이트 쉬폰을 천장 레일로 달았습니다. 쉬폰을 닫으면 강한 햇빛이 부드럽게 퍼져 책상 위가 눈부시지 않고, 방은 밝게 유지됩니다.",
         points=["천장 레일로 창 위 벽까지 덮어 높아 보이게", "벽 끝에서 끝까지 이어지는 폭", "가볍고 세탁이 쉬운 쉬폰 원단"]),
    dict(no="08", cat="blind", space="거실", product="콤비 블라인드", spec="그레이 콤비 블라인드 (2분할 · 커튼박스)", photos=1,
         title="고층 거실 통창에 단 그레이 콤비 블라인드",
         text="바깥 풍경이 트인 고층 거실 창에 그레이 콤비 블라인드를 두 개로 나눠 달았습니다. 망사 부분을 맞추면 바깥이 비치고, 원단을 겹치면 시선과 햇빛을 함께 가려 줍니다. 차분한 그레이가 원목 바닥과도 잘 어울립니다.",
         points=["넓은 창은 두 개로 나눠 조작이 가볍게", "커튼박스 안에 깔끔하게 설치", "바닥 가까이 내려오는 길이"]),
    dict(no="09", cat="blind", space="주택", product="콤비 블라인드", spec="화이트 콤비 블라인드 (내닫이창 3면)", photos=1,
         title="세 면으로 꺾인 내닫이창에 맞춘 화이트 콤비",
         text="원목 창틀이 있는 주택의 내닫이창(밖으로 튀어나온 창) 세 면에 화이트 콤비 블라인드를 하나씩 맞춰 달았습니다. 면마다 폭과 높이가 달라 따로 재서 제작했고, 각 창을 따로 올리고 내릴 수 있습니다. 오래 쓰던 커튼과 봉을 떼어 내고 블라인드로 바꾼 교체 시공입니다.",
         points=["창마다 따로 실측해 세 개를 각각 제작", "창틀 안쪽에 맞춰 원목 틀을 가리지 않게", "기존 커튼 · 커튼봉 철거 후 교체"]),
    dict(no="10", cat="blind commercial", space="사무실", product="콤비 블라인드", spec="그레이 콤비 블라인드 (긴 창 · 여러 칸)", photos=1,
         title="길게 이어진 사무실 창의 그레이 콤비 블라인드",
         text="창대가 길게 이어진 사무실 벽에 그레이 콤비 블라인드를 여러 칸으로 나눠 달았습니다. 오후 햇빛이 비스듬히 들어와도 줄무늬 원단이 한 번 걸러 주고, 앉은 자리 앞 칸만 따로 내릴 수 있습니다.",
         points=["창틀 칸에 맞춰 여러 개로 나눠 제작", "자리마다 필요한 칸만 조절", "사무실에 어울리는 차분한 그레이"]),
    dict(no="11", cat="blind", space="침실", product="알루미늄 블라인드", spec="화이트 알루미늄 블라인드 (2분할)", photos=1,
         title="몰딩 아래 딱 맞춘 안방 알루미늄 블라인드 두 장",
         text="가로로 긴 안방 창 위 몰딩 바로 아래에 알루미늄 블라인드 두 장을 나란히 달았습니다. 슬랫이 얇아 닫아 두어도 방이 답답해 보이지 않고, 막대를 돌려 각도만 바꾸면 아침 빛을 위쪽으로 돌려 보낼 수 있습니다.",
         points=["몰딩 선에 맞춰 수평을 잡은 설치", "왼쪽 · 오른쪽을 따로 올리고 내리기", "벽지 톤과 맞춘 밝은 슬랫"]),
    dict(no="12", cat="blind", space="주방", product="알루미늄 블라인드", spec="화이트 알루미늄 블라인드 (싱크대 앞 창)", photos=1,
         title="싱크대 앞 창에 맞춘 알루미늄 블라인드",
         text="싱크대 앞 창에 화이트 알루미늄 블라인드를 창틀 안쪽에 맞춰 달았습니다. 물기와 습기에 강한 알루미늄이라 주방에 잘 맞고, 슬랫을 살짝 열면 바깥 하늘은 보이면서 시선은 가려집니다.",
         points=["창틀 안쪽에 딱 맞춘 치수", "물기에 강한 알루미늄 슬랫", "슬랫 각도로 빛과 시선 조절"]),
    dict(no="13", cat="blind commercial", space="복층 공간", product="롤스크린", spec="그레이 롤스크린 (커튼월 통창 · 칸마다 개별)", photos=1,
         title="층고 높은 복층 공간의 커튼월 칸마다 롤스크린",
         text="천장이 높은 복층 공간의 커튼월 통창에 칸마다 그레이 롤스크린을 달았습니다. 창틀 칸 크기가 제각각이라 하나씩 재서 만들었고, 위아래 칸을 따로 내릴 수 있어 필요한 만큼만 빛을 가릴 수 있습니다.",
         points=["창틀 칸마다 따로 실측 · 제작", "위 칸과 아래 칸을 따로 조절", "손이 닿지 않는 위 칸도 체인을 당겨 여닫기"]),
    dict(no="14", cat="blind commercial", space="사무실", product="롤스크린", spec="아이보리 롤스크린 (코너 창 · 체인 조작)", photos=1,
         title="코너 창이 있는 사무실 아이보리 롤스크린",
         text="두 면이 창으로 된 사무실 코너에 아이보리 롤스크린을 창마다 달았습니다. 내리면 햇빛이 부드럽게 걸러져 모니터 눈부심이 줄고, 올리면 창이 깔끔하게 드러납니다.",
         points=["천장 몰딩에 맞춘 설치 높이", "창마다 따로 올리고 내리는 체인 조작", "사무실에 어울리는 밝은 아이보리"]),
    dict(no="15", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (웨이브 주름)", photos=1,
         title="웨이브 주름으로 단 화이트 쉬폰, 가까이에서 본 결",
         text="거실 창에 화이트 쉬폰을 웨이브 주름으로 달았습니다. 가까이에서 보면 얇은 원단 너머로 창틀이 은은하게 비치고, 전용 레일 덕분에 주름 간격이 처음부터 끝까지 고르게 유지됩니다.",
         points=["웨이브 전용 레일로 고른 주름 간격", "빛이 고르게 퍼지는 얇은 원단", "천장 레일로 깔끔한 윗선"]),
    dict(no="16", cat="curtain", space="부천 · 거실", product="겉커튼 + 쉬폰", spec="블루그레이 겉커튼 + 린넨 쉬폰 (이중 레일 · 끈 고정)", photos=2,
         title="부천 거실, 블루그레이 겉커튼과 린넨 쉬폰",
         text="거실 창 양 끝에 블루그레이 겉커튼을 모아 두고, 가운데는 결이 보이는 린넨 쉬폰으로 채웠습니다. 쉬폰을 끈으로 묶어 베란다 문 쪽을 열어 두면 드나들기 편하고, 풀어 두면 난간 그림자가 원단 위로 은은하게 비칩니다. 두 사진은 같은 거실입니다.",
         points=["겉커튼은 양 끝에, 쉬폰은 가운데에 오도록 이중 레일 배치", "베란다 문 앞 쉬폰은 끈으로 묶어 출입이 편하게", "푸른 기가 도는 겉커튼으로 하얀 거실에 포인트"],
         captions=["거실 창 전체", "가까이에서 본 겉커튼과 쉬폰"]),
    dict(no="17", cat="blind", space="부천 · 베란다", product="허니콤 블라인드", spec="베이지 허니콤 블라인드 (꺾인 창 세 면 · 창틀 안쪽)", photos=2,
         title="꺾인 베란다 창 세 면에 하나씩 맞춘 허니콤 블라인드",
         text="베란다의 꺾인 창 세 면에 베이지 허니콤 블라인드를 창틀 안쪽에 맞춰 하나씩 달았습니다. 벌집 모양 원단이 햇빛을 은은하게 퍼뜨리고, 원단 속 공기층이 창가의 찬 기운과 열기를 함께 덜어 줍니다.",
         points=["면마다 폭이 달라 창 하나씩 따로 실측", "창틀 안쪽에 딱 맞춰 옆으로 새는 빛 줄이기", "햇빛이 강한 베란다에 단열을 더하는 원단"],
         captions=["세 면 전체", "가까이에서 본 원단 결"]),
    dict(no="18", cat="curtain", space="부천 · 거실", product="쉬폰 커튼", spec="도트 줄무늬 쉬폰 (핀치 주름)", photos=1,
         title="해 질 녘 빛이 스미는 도트 줄무늬 쉬폰",
         text="가는 세로줄과 작은 도트가 들어간 쉬폰을 달았습니다. 해가 낮게 들어오는 시간이면 무늬 사이로 빛이 반짝이고, 바깥 풍경은 흐릿하게 남아 창가가 한층 따뜻해 보입니다.",
         points=["무늬가 세로로 곧게 떨어지도록 주름 간격 맞춤", "강한 햇빛도 부드럽게 퍼뜨리는 얇은 원단", "흰 창틀과 어울리는 아이보리 톤"]),
    dict(no="19", cat="curtain", space="서울 마포 · 거실", product="겉커튼", spec="라이트그레이 겉커튼 (웨이브 주름 · 자석 타이백)", photos=2,
         title="마포 거실, 웨이브 겉커튼을 자석 타이백으로",
         text="거실 벽 한 면을 채우는 라이트그레이 겉커튼을 웨이브 주름으로 달고, 가운데 창 앞은 자석 타이백으로 묶어 바깥 나무가 보이게 했습니다. 끈을 풀면 벽 전체가 한 장의 패브릭으로 이어집니다.",
         points=["벽 끝에서 끝까지 이어지는 천장 레일", "자석 타이백으로 쉽게 묶고 풀기", "바닥에 살짝 닿는 기장으로 물결 끝을 정돈"],
         captions=["타이백으로 가운데를 연 모습", "자석 타이백 가까이"]),
    dict(no="20", cat="curtain", space="서울 구로 · 거실", product="쉬폰 커튼", spec="화이트 쉬폰 (나비 주름 · 넓은 창)", photos=1,
         title="구로 거실, 넓은 창을 한 번에 덮은 화이트 쉬폰",
         text="스탠드 에어컨 옆까지 이어지는 넓은 거실 창에 화이트 쉬폰을 나비 주름으로 달았습니다. 오후 햇빛이 쉬폰을 지나며 부드러워져, 바닥과 소파 쪽까지 은은하게 밝아집니다.",
         points=["창 폭보다 넉넉한 레일로 가장자리 빛샘 줄이기", "촘촘한 나비 주름으로 넓은 창도 풍성하게", "바닥에서 살짝 띄운 기장"]),
    dict(no="21", cat="blind commercial", space="서재 · 업무 공간", product="콤비 블라인드", spec="웜그레이 콤비 블라인드 (높은 창 · 천장 설치)", photos=1,
         title="고층 서재의 높은 창에 단 웜그레이 콤비",
         text="천장 가까이까지 올라가는 고층 서재 창에 웜그레이 콤비 블라인드를 통으로 달았습니다. 망사 부분을 맞추면 도시 풍경이 그대로 보이고, 겹치면 책상 위로 떨어지는 햇빛을 덜어 줍니다.",
         points=["천장 바로 아래 설치로 창 전체를 덮기", "책상 앞 눈부심을 줄이는 밝기 조절", "대리석 벽과 어울리는 웜그레이"]),
    dict(no="22", cat="blind commercial", space="사무실", product="우드 블라인드", spec="그레이우드 블라인드 (창틀 안쪽 · 2분할)", photos=1,
         title="새로 꾸민 사무실 창 두 곳의 우드 블라인드",
         text="새로 단장한 사무실의 두 창에 그레이 톤 우드 블라인드를 창틀 안쪽으로 맞춰 달았습니다. 슬랫 각도를 바꾸면 바닥에 줄무늬 빛이 길게 들어오고, 닫으면 공간이 차분하게 정돈됩니다.",
         points=["창틀 안쪽 치수에 맞춘 제작", "넓은 창은 두 개로 나눠 조작이 가볍게", "흰 벽 · 원목 걸레받이와 어울리는 그레이우드"]),
    dict(no="23", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (나비 주름 · 몰딩 아래 레일)", photos=1,
         title="천장형 에어컨 아래 몰딩 선에 맞춘 화이트 쉬폰",
         text="천장형 에어컨이 있는 거실에서 몰딩 바로 아래에 레일을 달고 화이트 쉬폰을 걸었습니다. 몰딩 선과 커튼 윗선이 나란히 이어져 깔끔하고, 낮에는 거실 전체가 하얗게 밝아집니다.",
         points=["몰딩 선에 맞춘 레일 높이", "에어컨과 간섭 없는 위치", "창 양옆 벽까지 덮는 폭"]),
    dict(no="24", cat="curtain", space="방", product="겉커튼 + 쉬폰", spec="웜그레이 겉커튼 + 화이트 쉬폰 (이중 레일)", photos=1,
         title="작은 방 창을 채운 웜그레이 겉커튼과 화이트 쉬폰",
         text="수납장이 놓인 작은 방 창에 화이트 쉬폰과 웜그레이 겉커튼을 이중 레일로 달았습니다. 쉬폰만 닫아도 방이 환하고, 겉커튼을 펼치면 밤에 바깥 불빛을 가려 줍니다.",
         points=["가구 위치를 피해 겉커튼이 모이는 방향 정하기", "바닥까지 내려오는 쉬폰 기장", "벽지 톤에 맞춘 웜그레이"]),
    dict(no="25", cat="blind commercial", space="사무실", product="콤비 블라인드", spec="그레이 콤비 블라인드 (도로 쪽 창 · 3분할)", photos=1,
         title="도로 쪽 사무실 창, 세 칸으로 나눈 그레이 콤비",
         text="도로를 마주한 사무실 창에 그레이 콤비 블라인드를 세 칸으로 나눠 달았습니다. 망사 부분으로 하늘과 나무는 보이게 두고, 아래쪽은 원단을 겹쳐 길 건너 시선을 가릴 수 있습니다.",
         points=["창틀 칸에 맞춘 세 칸 구성", "아래 창 손잡이와 부딪히지 않는 길이", "사무 공간에 어울리는 그레이"]),
    dict(no="26", cat="curtain", space="방", product="쉬폰 커튼", spec="화이트 쉬폰 (웨이브 주름)", photos=1,
         title="오후 빛이 번지는 방 안의 화이트 쉬폰",
         text="방 창에 화이트 쉬폰을 웨이브 주름으로 달았습니다. 오후 햇빛이 창틀 모양대로 쉬폰 위에 비치고, 방 안은 눈부시지 않게 밝아집니다.",
         points=["창보다 넓게 단 레일", "물결 모양으로 고르게 떨어지는 주름", "햇빛을 부드럽게 퍼뜨리는 얇은 원단"]),
    dict(no="27", cat="curtain", space="거실", product="쉬폰 커튼", spec="린넨 쉬폰 (바닥 가까이 맞춘 기장)", photos=1,
         title="바닥 바로 위에서 멈춘 린넨 쉬폰의 끝선",
         text="바닥에서 낮게 바라본 린넨 쉬폰입니다. 주름 끝이 바닥에 닿을 듯 말 듯한 높이에서 고르게 멈춰 있어, 청소기를 돌리기 편하면서도 커튼이 짧아 보이지 않습니다.",
         points=["창 여러 곳을 재서 기장 오차 줄이기", "바닥 레일과 겹치지 않는 높이", "결이 보이는 린넨 쉬폰 원단"]),
    dict(no="28", cat="curtain", space="안방", product="겉커튼", spec="웜그레이 겉커튼 (웨이브 주름 · 벽면 전체 천장 레일)", photos=1,
         title="벽 한쪽 끝에서 끝까지, 안방 웜그레이 웨이브 커튼",
         text="가운데에 창이 하나 난 넓은 안방 벽에 웜그레이 겉커튼을 벽 끝에서 끝까지 이어 달았습니다. 커튼을 양쪽으로 모아 두면 창 하나만 액자처럼 남고, 닫으면 벽 전체가 부드러운 천으로 덮여 방이 아늑해집니다.",
         points=["벽 폭 전체를 쓰는 천장 레일", "창 위치와 상관없이 고른 웨이브 주름", "짙은 원목 바닥과 어울리는 웜그레이"]),
    dict(no="29", cat="curtain", space="운동방", product="쉬폰 커튼", spec="화이트 쉬폰 (나비 주름 · 넓은 창)", photos=2,
         title="실내 자전거를 둔 방, 햇살을 걸러 주는 화이트 쉬폰",
         text="운동 기구와 화분을 둔 방의 넓은 창에 화이트 쉬폰을 나비 주름으로 달았습니다. 쉬폰 너머로 방범창 무늬가 그림자처럼 비치고, 운동하는 동안 햇빛이 직접 닿지 않아 눈이 편합니다.",
         points=["벽 끝까지 덮는 넉넉한 폭", "바닥에 살짝 닿는 기장", "빛은 들이고 시선은 흐리는 얇은 원단"],
         captions=["방 전체", "가까이에서 본 주름과 빛"]),
    dict(no="30", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (나비 주름 · 거실 창 전체)", photos=1,
         title="TV 옆 거실 창 전체를 감싼 화이트 쉬폰",
         text="스탠드 에어컨과 TV 사이 거실 창 전체에 화이트 쉬폰을 달았습니다. 창틀 가로대 그림자가 원단 위로 은은하게 비치고, 거실은 낮에도 차분한 밝기를 유지합니다.",
         points=["에어컨 앞을 피해 열고 닫기 편한 레일 길이", "고른 나비 주름", "바닥 가까이 맞춘 기장"]),
    dict(no="31", cat="curtain blind", space="거실", product="쉬폰 + 알루미늄 블라인드", spec="화이트 쉬폰 (베란다 창) + 화이트 알루미늄 블라인드 (옆 창)", photos=1,
         title="한 거실 두 창, 쉬폰과 알루미늄 블라인드를 함께",
         text="베란다 쪽 큰 창에는 화이트 쉬폰을, 옆 벽의 가로로 긴 창에는 화이트 알루미늄 블라인드를 달았습니다. 창마다 쓰임에 맞춰 제품을 나누면서 색은 같은 화이트로 맞춰 거실이 한 덩어리로 정돈돼 보입니다.",
         points=["베란다 창은 드나들기 편한 커튼으로", "가구가 붙는 옆 창은 짧은 블라인드로", "두 제품 모두 화이트로 통일"]),
    dict(no="32", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 린넨 쉬폰 (코너 거실 두 면 · 천장 레일)", photos=1,
         title="두 면에 창이 난 코너 거실, 이어지는 린넨 쉬폰",
         text="창이 두 벽에 걸쳐 있는 코너형 거실에 린넨 쉬폰을 면마다 천장 레일로 달았습니다. 두 면의 높이와 주름 간격을 맞춰 한 장처럼 이어 보이고, 베란다 난간 무늬가 원단 너머로 흐릿하게 비칩니다.",
         points=["두 면의 레일 높이를 똑같이 맞춤", "천장형 에어컨 아래로 지나가는 레일", "결이 보이는 린넨 쉬폰"]),
    dict(no="33", cat="blind commercial", space="상가 사무실", product="콤비 블라인드", spec="화이트 콤비 블라인드 (창대 위 4칸)", photos=2,
         title="상가 건물 사무실 창대 위, 네 칸으로 나눈 화이트 콤비",
         text="창대가 길게 이어진 상가 사무실 창에 화이트 콤비 블라인드를 네 칸으로 나눠 달았습니다. 칸마다 높이를 따로 맞출 수 있어 아래 여닫이창 쪽만 올려 환기하기 좋고, 모두 내리면 길 건너 간판 불빛까지 부드럽게 가려집니다.",
         points=["창틀 칸에 맞춘 4칸 구성", "아래 여닫이창을 열 수 있게 칸별 조절", "밝은 화이트로 실내를 환하게"],
         captions=["일부 칸을 올렸을 때", "모두 내렸을 때"]),
    dict(no="34", cat="blind", space="거실", product="알루미늄 블라인드", spec="화이트 알루미늄 블라인드 (거실 통창 · 여러 장)", photos=1,
         title="거실 통창을 여러 장으로 나눈 화이트 알루미늄 블라인드",
         text="천장 우물 아래 거실 통창에 화이트 알루미늄 블라인드를 여러 장으로 나눠 달았습니다. 커튼 대신 얇은 슬랫을 쓰니 거실이 한결 정돈돼 보이고, 각도만 바꿔 빛과 시선을 조절할 수 있습니다. 옆방 창도 같은 제품으로 맞췄습니다.",
         points=["바닥 가까이까지 내려오는 긴 길이", "넓은 창은 여러 장으로 나눠 조작이 가볍게", "옆방 창까지 같은 제품으로 통일"]),
    dict(no="35", cat="blind", space="방", product="롤스크린", spec="화이트 롤스크린 (2분할 · 창 위 설치)", photos=2,
         title="파우더룸 창 두 칸에 단 화이트 롤스크린",
         text="화장대가 있는 방의 가로로 긴 창에 화이트 롤스크린을 두 칸으로 나눠 달았습니다. 올리면 창밖 산과 동네 풍경이 그대로 보이고, 내리면 빛이 부드럽게 퍼져 방이 하얗게 밝아집니다.",
         points=["창 위 벽에 달아 창틀을 모두 덮기", "두 칸으로 나눠 따로 조절", "흰 가구와 어울리는 화이트 원단"],
         captions=["반쯤 올렸을 때", "모두 내렸을 때"]),
    dict(no="36", cat="curtain", space="거실", product="쉬폰 커튼", spec="화이트 쉬폰 (나비 주름 · 베란다 문)", photos=1,
         title="베란다 문 쪽만 열어 둔 거실 화이트 쉬폰",
         text="베란다로 나가는 문이 있는 거실 창에 화이트 쉬폰을 달았습니다. 문 쪽만 살짝 열어 두면 바깥 산이 보이고, 닫으면 거실이 하얀 빛으로 고르게 채워집니다.",
         points=["문 쪽에서 나뉘도록 커튼 두 장 배치", "몰딩 아래 레일로 윗선 정리", "바닥에 닿을 듯한 기장"]),
    dict(no="37", cat="blind commercial", space="사무실", product="우드 블라인드", spec="내추럴 우드 블라인드 (슬랫 클로즈업)", photos=1,
         title="빛 사이로 보이는 내추럴 우드 블라인드의 결",
         text="사무실 창에 단 내추럴 톤 우드 블라인드를 아래에서 올려다봤습니다. 슬랫을 조금 열면 하늘빛이 줄무늬로 들어오고, 나뭇결이 살아 있어 사무 공간에도 따뜻한 느낌을 더합니다.",
         points=["넓은 슬랫으로 빛의 양을 크게 조절", "나뭇결이 살아 있는 내추럴 톤", "천장 아래 바로 붙인 설치"]),
    dict(no="38", cat="blind", space="방", product="롤스크린", spec="아이보리 롤스크린 (창틀 위 설치)", photos=1,
         title="작은 방 창을 한 장으로 덮은 아이보리 롤스크린",
         text="작은 방 창에 아이보리 롤스크린 한 장을 창틀보다 조금 넓게 달았습니다. 내리면 창이 벽처럼 정돈되고, 옆으로 새는 빛이 적어 방이 차분해집니다.",
         points=["창보다 넓게 달아 빛샘 줄이기", "몰딩 아래 설치로 깔끔한 윗선", "벽 색과 어울리는 아이보리"]),
    dict(no="39", cat="blind commercial", space="사무실", product="우드 블라인드", spec="다크우드 블라인드 (높은 창 · 창틀 안쪽)", photos=1,
         title="짙은 벽에 맞춘 사무실 높은 창 다크우드 블라인드",
         text="짙은 색 벽으로 꾸민 사무실의 높은 창에 다크우드 블라인드를 창틀 안쪽으로 맞춰 달았습니다. 벽과 블라인드 색이 이어져 공간이 묵직하게 정리되고, 슬랫 각도로 빛을 조절합니다.",
         points=["창틀 안쪽 치수에 딱 맞춘 제작", "높은 창도 아래에서 줄로 조작", "벽 색과 이어지는 다크우드"]),
    dict(no="40", cat="blind commercial", space="휴게 공간", product="롤스크린", spec="린넨 질감 롤스크린 (베란다 창 · 2분할)", photos=1,
         title="휴게 공간 베란다 창의 린넨 질감 롤스크린",
         text="안마의자와 테이블을 둔 휴게 공간의 베란다 창에 린넨 질감 롤스크린을 두 칸으로 달았습니다. 바깥이 은은하게 비쳐 답답하지 않고, 천장형 에어컨 아래로 깔끔하게 들어갑니다.",
         points=["천장형 에어컨과 간섭 없는 설치 위치", "두 칸으로 나눠 따로 조절", "은은하게 비치는 린넨 질감 원단"]),
]

CASE = {c["no"]: c for c in CASES}


def case_card(c, cls="case-card", extra=""):
    return f'''                <a href="case-{c["no"]}.html" class="{cls}{extra}" data-cat="{c["cat"]}">
                    <div class="case-img">
                        <img src="{v(f'images/cases/case-{c["no"]}.jpg')}" alt="{c["space"]} {c["product"]} 시공 사진" loading="lazy">
                        <span class="case-badge">{c["product"]}</span>
                    </div>
                    <div class="case-info">
                        <span class="case-loc">{c["space"]} · {c["product"]}</span>
                        <h3>{c["title"]}</h3>
                    </div>
                </a>
'''


def post_card(p):
    return f'''                <a href="{p["slug"]}.html" class="post-card">
                    <div class="post-img"><img src="{v('images/products/' + p['img'] + '.jpg')}" alt="{esc(p["title"])}" loading="lazy"></div>
                    <span class="post-cat">{p["cat"]}</span>
                    <h3>{p["title"]}</h3>
                    <p>{p["desc"]}</p>
                    <span class="post-date">{date_dot(TODAY)}</span>
                </a>
'''


def faq_items(pairs, indent="                "):
    out = ""
    for q, a in pairs:
        out += (f'{indent}<details class="faq-item">\n'
                f'{indent}    <summary>{q}</summary>\n'
                f'{indent}    <div class="answer"><p>{a}</p></div>\n'
                f'{indent}</details>\n')
    return out


def other_areas_html(cls="area-plain"):
    rows = "".join(f"                <p><strong>{g}</strong> · {names}</p>\n" for g, names in OTHER_AREAS)
    return f'''            <div class="{cls}">
                <h2>그 밖의 방문 지역</h2>
{rows}                <p>위 지역도 일정을 맞춰 원단 샘플을 들고 방문합니다. 거리에 따라 방문 날짜를 묶어서 잡을 수 있어요.</p>
            </div>
'''


# ---------------------------------------------------------------
# 메인
# ---------------------------------------------------------------
HOME_FAQ = [
    ("실측하러 와 주시는 데 비용이 드나요?",
     "광명 안은 출장비 · 상담비 · 실측비가 모두 없습니다. 구로 · 금천 · 시흥 · 안양 · 부천처럼 가까운 지역도 마찬가지예요. 견적만 받아 보고 결정하셔도 괜찮습니다."),
    ("광명커튼은 어느 동네에 있나요?",
     "경기 광명시에서 운영합니다. 철산 · 하안 · 소하 · 광명동 · 일직동 · 학온동 어디든 차로 금방이라 실측 날짜를 맞추기 쉽고, 달고 난 뒤 손볼 일이 생겨도 빨리 들를 수 있어요."),
    ("재고 나서 설치까지 며칠 걸리나요?",
     "맞춤 제작이라 실측 뒤 보통 일주일 안팎이 걸립니다. 입주 · 이사 날짜가 정해져 있으면 상담 때 먼저 말씀해 주세요. 그 날짜를 기준으로 거꾸로 일정을 잡습니다."),
    ("뉴타운 사전점검 날 실측이 되나요?",
     "됩니다. 사전점검 날 재 두면 입주일에 맞춰 바로 달 수 있어서 가장 권하는 방법이에요. 단지마다 외부 업체 동행 규정이 달라 미리 확인해 드립니다."),
]


def build_index():
    local = ["gwangmyeong", "cheolsan", "haan", "soha", "newtown", "iljik", "hakon",
             "guro", "geumcheon", "siheung", "anyang", "bucheon"]
    sub = {"gwangmyeong": "광명시 전 지역", "cheolsan": "철산역 · 재건축 단지", "haan": "하안주공 · 교체",
           "soha": "소하택지 · 구름산", "newtown": "광명동 · 입주 준비", "iljik": "KTX역세권 · 통창",
           "hakon": "노온사 · 가학 · 옥길", "guro": "개봉 · 고척", "geumcheon": "독산 · 가산",
           "siheung": "목감 · 은계", "anyang": "석수 · 박달", "bucheon": "옥길 · 범박"}
    local_map = "".join(
        f'                    <a href="{area_file(AREA[s])}"{" class=\"is-home\"" if AREA[s].get("base") else ""}><strong>{AREA[s]["name"]}</strong><small>{sub[s]}</small></a>\n'
        for s in local)

    quick = ""
    for g, label in GROUPS:
        links = " ".join(f'<a href="{area_file(a)}">{a["name"]}</a>' for a in AREAS if a["group"] == g)
        quick += f'                <div><h3>{label}</h3><p>{links}</p></div>\n'
    for g, names in OTHER_AREAS[:2]:
        quick += f'                <div><h3>{g} 방문</h3><p>{names.replace(" · ", " ")}</p></div>\n'

    cases = ""
    if CASES:
        picks = [CASE[n] for n in ("01", "03", "08", "13", "02")]
        cards = "".join(case_card(c, extra=(" wide reveal" if i == 0 else " reveal")) for i, c in enumerate(picks))
        cases = f'''    <!-- ===== 시공사례 ===== -->
    <section class="section">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">WORKS</p>
                    <h2 class="section-title">시공 사례</h2>
                    <p class="section-sub">광명커튼이 직접 재고 직접 단 현장입니다.</p>
                </div>
                <a href="gallery.html" class="link-more">전체 사례 보기 →</a>
            </div>
            <div class="case-grid">
{cards}            </div>
        </div>
    </section>

'''

    body = f'''    <!-- ===== 메인 히어로: 배경 사진은 js/includes.js 의 HOME_HERO_SLIDES 에서 관리 ===== -->
    <section class="hero" data-hero="home">
        <p class="hero-badge" aria-hidden="true">GWANGMYEONG · CURTAIN &amp; BLIND</p>
        <div class="container hero-content">
            <p class="hero-eyebrow">GWANGMYEONG CURTAIN</p>
            <h1><span class="hero-kicker">광명 커튼 · 블라인드 맞춤 시공</span>우리 동네 창은<br>우리 동네에서 잽니다</h1>
            <p class="hero-sub">철산 · 하안 · 소하 · 광명뉴타운 · 광명역까지, 광명에 사는 사람이 직접 찾아갑니다.<br>원단 샘플을 들고 가는 무료 방문 실측, 서울 · 경기도 방문해요.</p>
            <div class="hero-buttons">
                <a href="inquiry.html" class="btn btn-light">무료 방문 견적 <span class="arrow">→</span></a>
                <a href="area-gwangmyeong.html" class="btn btn-outline-white">광명 시공 안내</a>
            </div>
        </div>
    </section>

    <!-- ===== 약속 띠 ===== -->
    <section class="promise">
        <div class="promise-grid">
            <div class="promise-item"><span class="num">01</span><strong>광명 출장비 없음</strong><p>실측 · 상담 · 견적 모두 무료</p></div>
            <div class="promise-item"><span class="num">02</span><strong>재는 사람이 답니다</strong><p>상담부터 설치까지 한 사람이</p></div>
            <div class="promise-item"><span class="num">03</span><strong>샘플은 우리 집 창가에서</strong><p>원단을 실제 빛에 대 보고 결정</p></div>
            <div class="promise-item"><span class="num">04</span><strong>가까우니까 A/S도 빨리</strong><p>광명 안이면 그날 들르기도</p></div>
        </div>
    </section>

    <!-- ===== 광명 동네 (지역 검색 강화: 동네별 페이지로 바로 연결) ===== -->
    <section class="section bg-ink">
        <div class="container local-band">
            <div class="reveal">
                <p class="section-tag">GWANGMYEONG</p>
                <h2>광명에 살면서<br>광명의 창을 다룹니다</h2>
                <p>광명커튼은 경기 광명시에서 운영하는 커튼 · 블라인드 집입니다. 철산과 하안의 주공 단지, 소하택지, 새 아파트가 들어서는 광명뉴타운, 고층 통창이 많은 광명역세권, 주택이 많은 학온동까지 동네마다 창의 사정이 다르다는 걸 매일 다니며 봅니다.</p>
                <p>광명과 붙어 있는 구로 · 금천 · 시흥 · 안양 · 부천도 같은 동선으로 다니고, 그 밖의 서울 · 경기 지역도 일정을 맞춰 방문해요.</p>
                <a href="area-gwangmyeong.html" class="btn btn-brass">광명 시공 안내 <span class="arrow">→</span></a>
            </div>
            <nav class="local-map reveal d1" aria-label="광명과 가까운 시공 지역">
{local_map}            </nav>
        </div>
    </section>

{cases}    <!-- ===== 제품 컬렉션 ===== -->
    <section class="section">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">COLLECTION</p>
                    <h2 class="section-title">어떤 창에 무엇을 달까</h2>
                    <p class="section-sub">옆으로 넘기며 8가지 제품을 살펴보세요.</p>
                </div>
                <a href="products.html" class="link-more">제품 전체 보기 →</a>
            </div>
            <div class="product-rail reveal">
{"".join(product_card(k) for k in PRODUCTS)}            </div>
        </div>
    </section>

    <!-- ===== 브랜드 이야기 ===== -->
    <section class="section bg-paper">
        <div class="container split">
            <div class="split-img reveal"><img src="{v('images/about/about-01.jpg')}" alt="간접조명 커튼박스에 단 아이보리 겉커튼 시공 사진" loading="lazy"></div>
            <div class="split-text reveal d1">
                <p class="section-tag">WHY US</p>
                <h2>멀리 있는 큰 업체보다<br>가까이 있는 한 사람</h2>
                <p>커튼은 달고 나서부터가 시작입니다. 몇 달 뒤 레일이 뻑뻑해지거나 블라인드 줄이 꼬였을 때, 전화 한 통에 금방 와 줄 수 있는 사람이 있으면 마음이 편하죠.</p>
                <p>광명커튼은 광명에 살면서 광명 현장을 직접 다닙니다. 상담한 사람이 창을 재고, 그 사람이 직접 달고, A/S도 같은 사람이 갑니다. <strong>말이 중간에서 바뀌지 않도록</strong> 처음부터 끝까지 한 사람이 맡아요.</p>
                <a href="about.html" class="btn btn-outline">광명커튼 이야기 <span class="arrow">→</span></a>
            </div>
        </div>
    </section>

    <!-- ===== 진행 과정 ===== -->
    <section class="section">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">PROCESS</p>
                    <h2 class="section-title">문의부터 설치까지 네 단계</h2>
                </div>
            </div>
            <div class="process-list reveal">
                <div class="process-item"><span class="step">STEP 01</span><h3>문의</h3><p>전화나 카카오톡, 온라인 신청서로 연락 주세요. 창 사진을 같이 보내 주시면 대략적인 구성을 먼저 알려드려요.</p></div>
                <div class="process-item"><span class="step">STEP 02</span><h3>방문 실측</h3><p>원단 샘플을 챙겨 방문해 창마다 세 군데씩 재고, 빛이 드는 방향을 보며 함께 고릅니다.</p></div>
                <div class="process-item"><span class="step">STEP 03</span><h3>제작</h3><p>고른 원단과 잰 치수로 맞춤 제작합니다. 입주 · 이사 날짜에 맞춰 일정을 잡아요.</p></div>
                <div class="process-item"><span class="step">STEP 04</span><h3>설치와 A/S</h3><p>직접 달고 여닫아 보며 마무리합니다. 쓰다가 불편한 점이 생기면 언제든 연락 주세요.</p></div>
            </div>
        </div>
    </section>

    <!-- ===== 시공 지역 바로가기 (검색엔진이 지역 페이지를 찾을 수 있도록 HTML 링크로 둠) ===== -->
    <section class="section bg-sand">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">SERVICE AREA</p>
                    <h2 class="section-title">광명 중심, 서울 · 경기 방문</h2>
                    <p class="section-sub">동네 이름을 누르면 그 동네 안내를 볼 수 있어요.</p>
                </div>
                <a href="areas.html" class="link-more">시공 지역 전체 →</a>
            </div>
            <div class="area-quick reveal">
{quick}            </div>
        </div>
    </section>

    <!-- ===== 고객 후기 =====
         후기가 생기면 아래 review-empty 를 지우고 이 형식으로 추가하세요. (실제 후기만 올려 주세요)
         <div class="review-grid">
             <div class="review-card">
                 <p class="stars" aria-label="별점 5점">★★★★★</p>
                 <p class="quote">"후기 내용"</p>
                 <p class="meta">김OO 고객님 · 광명 철산동 · 암막커튼</p>
             </div>
         </div>
    -->
    <section class="section">
        <div class="container">
            <div class="section-head center reveal">
                <p class="section-tag">REVIEW</p>
                <h2 class="section-title">고객 후기</h2>
            </div>
            <div class="review-empty reveal">
                <p>광명커튼은 새로 문을 연 집입니다.<br>시공받으신 분들이 남겨 주시는 후기를 이곳에 차례로 소개할게요.</p>
                <div class="btn-row">
                    <a href="#" class="btn btn-outline" data-link="naver">네이버 리뷰 보기</a>
                    <a href="#" class="btn btn-kakao">카카오톡으로 문의하기</a>
                    <a href="inquiry.html" class="btn btn-primary">무료 견적 신청</a>
                </div>
            </div>
        </div>
    </section>

    <!-- ===== FAQ 미리보기 ===== -->
    <section class="section bg-paper">
        <div class="container-narrow">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">FAQ</p>
                    <h2 class="section-title">자주 받는 질문</h2>
                </div>
                <a href="faq.html" class="link-more">질문 더 보기 →</a>
            </div>
            <div class="faq-list reveal">
{faq_items(HOME_FAQ)}            </div>
        </div>
    </section>

    <!-- ===== 매거진 ===== -->
    <section class="section">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">MAGAZINE</p>
                    <h2 class="section-title">고르기 전에 읽어 보세요</h2>
                </div>
                <a href="blog.html" class="link-more">매거진 전체 →</a>
            </div>
            <div class="post-grid reveal">
{post_card(POST["blog-1-newtown-move-in"])}{post_card(POST["blog-2-old-apt-replace"])}{post_card(POST["blog-9-choose-gwangmyeong"])}            </div>
        </div>
    </section>
'''
    title = "광명커튼 | 광명 커튼 · 블라인드 맞춤 시공 · 철산 하안 소하 광명뉴타운 무료 실측"
    desc = "광명에 사는 사람이 직접 재고 다는 광명커튼. 철산동 · 하안동 · 소하동 · 광명뉴타운 · 광명역세권 · 학온동 커튼 · 블라인드 무료 방문 실측, 서울 · 경기 방문. 암막 · 린넨 · 쉬폰 커튼, 콤비 · 우드 · 허니콤 블라인드, 전동커튼."
    kw = "광명커튼, 광명 커튼, 광명 블라인드, 광명시 커튼, 철산 커튼, 하안동 커튼, 소하동 커튼, 광명뉴타운 커튼, 광명역 커튼, 광명 커튼 시공, 광명 블라인드 시공, 광명 암막커튼, 광명 콤비블라인드, 광명 전동커튼"
    lds = [business_ld(), {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND,
                           "alternateName": BRAND_EN, "url": SITE + "/"}]
    write("index.html", page("index.html", title, desc, kw, body, lds=lds, verify=True))


# ---------------------------------------------------------------
# 시공사례 목록 + 상세
# ---------------------------------------------------------------
def build_gallery():
    if CASES:
        cards = "".join(case_card(c, extra=" reveal") for c in CASES)
        inner = f'''            <div class="filter-bar" role="group" aria-label="사례 분류">
                <button class="filter-btn is-active" data-filter="all">전체</button>
                <button class="filter-btn" data-filter="curtain">커튼</button>
                <button class="filter-btn" data-filter="blind">블라인드</button>
                <button class="filter-btn" data-filter="motor">전동</button>
                <button class="filter-btn" data-filter="commercial">매장 · 사무실</button>
            </div>
            <div class="case-grid is-even">
{cards}            </div>
'''
    else:
        inner = f'''            <div class="review-empty">
                <p>광명커튼은 새로 문을 열어 시공 사례를 하나씩 모으고 있습니다.<br>직접 시공한 현장 사진만 올릴 예정이에요. 그동안은 제품 안내에서 종류별 특징을 먼저 살펴보세요.</p>
                <div class="btn-row">
                    <a href="products.html" class="btn btn-outline">제품 안내 보기</a>
                    <a href="inquiry.html" class="btn btn-primary">무료 견적 신청</a>
                </div>
            </div>
            <div class="pick-grid mt-48">
{"".join(product_card(k) for k in ["chiffon", "blackout", "combi"])}            </div>
'''
    body = f'''    <section class="page-hero" data-hero="gallery">
        <div class="container">
            <h1>시공 사례</h1>
            <p class="lead">광명커튼이 직접 재고 직접 단 현장을 모았습니다.</p>
        </div>
    </section>

    <!-- 사례 추가는 _build/build.py 의 CASES 에 한 덩어리 추가 후 build.py 실행 (README 참고) -->
    <section class="section">
        <div class="container">
{inner}        </div>
    </section>
'''
    write("gallery.html", page("gallery.html", "커튼 · 블라인드 시공사례 | 광명 철산 · 하안 · 소하 | 광명커튼",
                               "광명커튼이 직접 시공한 커튼 · 블라인드 현장. 광명 철산 · 하안 · 소하 · 광명뉴타운 · 광명역세권 거실 커튼, 안방 암막, 콤비 · 우드 · 허니콤 블라인드 사례를 공간별로 확인하세요.",
                               "광명 커튼 시공사례, 광명 블라인드 시공사례, 철산 커튼, 하안동 커튼, 거실 커튼 사례, 암막커튼 시공, 콤비블라인드 시공",
                               body, crumbs=[("시공사례", "gallery.html")], noindex=not CASES))

    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        pts = "".join(f"                    <li>{p}</li>\n" for p in c["points"])
        caps = c.get("captions") or ["시공 후 전체"] + [f"시공 사진 {k + 2}" for k in range(c["photos"] - 1)]
        figs = "".join(
            f'                    <figure><img src="{v("images/cases/case-" + c["no"] + ("" if k == 0 else f"-{k + 1}") + ".jpg")}" alt="{c["space"]} {c["product"]} 시공 사진 - {caps[k]}" loading="lazy"><figcaption>{caps[k]}</figcaption></figure>\n'
            for k in range(c["photos"]))
        single = " is-single" if c["photos"] == 1 else " is-pair"
        body = f'''    <section class="page-hero" data-hero="case" data-hero-img="{v(f'images/cases/case-{c["no"]}.jpg')}" data-crumb="{c["space"]} {c["product"]}">
        <div class="container">
            <h1>{c["title"]}</h1>
            <div class="tag-row">
                <span class="tag">{c["space"]}</span>
                <span class="tag">{c["product"]}</span>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container-narrow">
            <dl class="case-spec">
                <div><dt>공간</dt><dd>{c["space"]}</dd></div>
                <div><dt>제품</dt><dd>{c["spec"]}</dd></div>
                <div><dt>사진</dt><dd>시공 현장 {c["photos"]}장</dd></div>
                <div><dt>상담</dt><dd>무료 방문 실측</dd></div>
            </dl>

            <article class="prose">
                <h2>시공 내용</h2>
                <p>{c["text"]}</p>

                <div class="case-photos{single}">
{figs}                </div>

                <h3>시공 포인트</h3>
                <ul>
{pts}                </ul>

                <div class="note-box">
                    <strong>이 구성이 마음에 든다면</strong>
                    상담 때 사례 번호(case-{c["no"]})를 알려 주세요. 우리 집 창 크기에 맞춰 같은 구성을 제안해 드립니다.
                    <a href="inquiry.html">무료 방문 견적 신청</a>
                </div>
            </article>

            <nav class="pager" aria-label="다른 사례">
                <a href="gallery.html"><small>←</small><strong>사례 목록</strong></a><a href="case-{nxt["no"]}.html"><small>다음 사례 →</small><strong>{nxt["title"]}</strong></a>
            </nav>
        </div>
    </section>
'''
        kind = "블라인드" if "blind" in c["cat"] else "커튼"
        write(f"case-{c['no']}.html", page(
            f"case-{c['no']}.html", f"{c['space']} {c['product']} 시공사례 - {c['title']} | 광명커튼",
            f"{c['space']} {c['spec']} 시공 사례. {c['text'][:70]}…",
            f"{c['space']} {c['product']}, {c['product']} 시공, {kind} 시공사례, 광명 {kind}",
            body, crumbs=[("시공사례", "gallery.html"), (c["title"], f"case-{c['no']}.html")],
            og_image=f"images/cases/case-{c['no']}.jpg", og_type="article"))


# ---------------------------------------------------------------
# 제품
# ---------------------------------------------------------------
PRODUCT_DETAIL = {
    "linen": ("굵은 실로 짠 린넨은 햇빛이 결 사이로 한 번 걸러져 들어옵니다. 같은 베이지라도 린넨으로 하면 빛이 닿았을 때 따뜻한 기운이 돌아, 거실 겉커튼으로 가장 많이 권하는 원단이에요. 자연 섬유가 섞인 원단은 걸어 두면 조금 늘어나서 기장을 맞출 때 그만큼 계산합니다.",
              [("이런 집에", "거실 분위기를 부드럽게 바꾸고 싶은 집"), ("잘 맞는 곳", "거실, 안방, 남향 창"), ("같이 쓰면", "쉬폰 속커튼, 웨이브 주름"), ("관리", "원단마다 물세탁 · 드라이 여부가 달라 상담 때 안내")], "blog-4-curtain-length.html"),
    "chiffon": ("얇게 비치는 쉬폰은 낮에 커튼을 닫고도 집이 어두워지지 않게 해 줍니다. 앞 동과 마주 보는 거실이나 1 · 2층 저층 집에서 특히 쓸모가 커요. 고층 통창에서는 바깥 풍경을 흐릿하게 남겨 두는 역할을 합니다.",
                [("이런 집에", "앞 동 시선이 신경 쓰이는 집, 저층"), ("잘 맞는 곳", "거실, 이중 커튼의 속커튼, 통창"), ("같이 쓰면", "린넨 · 암막 겉커튼"), ("관리", "가벼워서 세탁기 울 코스로 관리 가능한 원단이 많음")], "blog-12-curtain-care.html"),
    "blackout": ("단지 가로등과 새벽빛을 막아 잠자는 방을 어둡게 만들어 줍니다. 원단보다 중요한 건 빛이 새는 틈을 줄이는 설치라서, 레일을 창보다 넓게 달고 기장은 바닥 가까이 맞춥니다.",
                 [("이런 집에", "동향 침실, 단지 조명이 밝은 집, 교대 근무"), ("잘 맞는 곳", "안방, 아이방, 홈시어터"), ("같이 쓰면", "쉬폰(이중 레일), 암막 롤스크린"), ("관리", "코팅 암막은 건조기 사용을 피하기")], "blog-5-blackout-guide.html"),
    "combi": ("망사와 막힌 원단이 줄무늬로 번갈아 있어 줄 하나로 밝기를 바꿉니다. 깔끔하고 가격 부담이 적어 새 아파트 입주 때 방 전체를 콤비로 맞추는 경우가 많아요.",
              [("이런 집에", "입주 때 방을 한 번에 정리하고 싶은 집"), ("잘 맞는 곳", "방, 거실, 사무실"), ("같이 쓰면", "거실 린넨 커튼과 레이어드"), ("관리", "먼지떨이나 청소기 브러시로 간단히")], "blog-6-blind-compare.html"),
    "wood": ("나무 슬랫의 각도를 돌려 빛이 들어오는 방향을 바꿀 수 있습니다. 위로 기울이면 빛이 천장으로 튕겨 방은 밝고 눈부심은 줄어서, 책상이나 TV가 창 가까이 있는 방에 잘 맞아요.",
             [("이런 집에", "공부방 · 재택근무 방, 원목 가구가 많은 집"), ("잘 맞는 곳", "서재, 아이 공부방, 거실, 카페"), ("같이 쓰면", "양옆 장식용 커튼"), ("관리", "마른 천으로 닦기, 물기 많은 곳은 피하기")], "blog-6-blind-compare.html"),
    "honeycomb": ("단면이 벌집 모양이라 원단 속에 공기층이 생깁니다. 겨울에 창가 찬 기운이 신경 쓰이는 방에 좋고, 위아래로 따로 여닫을 수 있어 아래만 가리고 위로 하늘을 볼 수도 있어요.",
                  [("이런 집에", "산 쪽 창, 겨울에 창가가 추운 집"), ("잘 맞는 곳", "침실, 베란다 창, 북향 방"), ("같이 쓰면", "겉커튼(겨울 단열 보강)"), ("관리", "찬바람 드라이기로 칸 속 먼지 털기")], "blog-11-winter-window.html"),
    "roll": ("원단 한 장을 말아 올리는 구조라 올렸을 때 창이 가장 깨끗하게 드러납니다. 비치는 선스크린, 빛을 막는 암막, 일반 원단 중에서 골라 쓰임을 정해요.",
             [("이런 집에", "깔끔한 창을 좋아하는 집, 원룸 · 오피스텔"), ("잘 맞는 곳", "주방, 아이방, 드레스룸, 사무실"), ("같이 쓰면", "암막 커튼(두 겹 암막)"), ("관리", "끝까지 내린 상태로 청소기")], "blog-8-no-drill.html"),
    "motor": ("손이 닿지 않는 높은 창이나 폭이 넓은 통창을 리모컨 · 벽 스위치 · 휴대폰으로 여닫습니다. 예약을 걸어 아침에 자동으로 열리게 할 수도 있어요. 커튼박스 근처에 전원이 있어야 해서, 공사 계획이 있다면 먼저 상담해 주세요.",
              [("이런 집에", "고층 통창, 복층, 높은 창이 있는 주택"), ("잘 맞는 곳", "광명역세권 주상복합, 학온동 주택"), ("같이 쓰면", "린넨 웨이브 커튼, 롤스크린"), ("관리", "모터 · 레일 점검은 A/S로")], "blog-3-highrise-window.html"),
}


def build_products():
    nav = "".join(f'                <a href="#{k}" class="filter-btn">{p["name"]}</a>\n' for k, p in PRODUCTS.items())
    blocks = ""
    for k, p in PRODUCTS.items():
        text, specs, link = PRODUCT_DETAIL[k]
        dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in specs)
        blocks += f'''            <article class="product-block" id="{k}">
                <div class="split-img"><img src="{v('images/products/' + k + '.jpg')}" alt="{p["name"]}" loading="lazy"></div>
                <div>
                    <h2>{p["name"]}</h2>
                    <span class="en">{p["en"]}</span>
                    <p class="prose">{text}</p>
                    <dl class="spec-list">
                        {dl}
                    </dl>
                    <a href="{link}" class="btn btn-outline">관련 글 읽기 <span class="arrow">→</span></a>
                </div>
            </article>
'''
    body = f'''    <section class="page-hero" data-hero="products">
        <div class="container">
            <h1>제품 안내</h1>
            <p class="lead">같은 창이라도 무엇을 다느냐에 따라 하루의 빛이 달라집니다.<br>광명커튼이 시공하는 8가지 제품을 비교해 보세요.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <nav class="product-nav" aria-label="제품 바로가기">
{nav}            </nav>
{blocks}        </div>
    </section>
'''
    write("products.html", page("products.html", "커튼 · 블라인드 종류 | 암막 · 린넨 · 쉬폰 · 콤비 · 우드 · 허니콤 | 광명커튼",
                                "광명커튼이 시공하는 린넨 커튼, 쉬폰 커튼, 암막 커튼, 콤비 블라인드, 우드 블라인드, 허니콤 블라인드, 롤스크린, 전동 커튼의 특징과 어울리는 집을 비교해 보세요.",
                                "커튼 종류, 블라인드 종류, 린넨커튼, 쉬폰커튼, 암막커튼, 콤비블라인드, 우드블라인드, 허니콤블라인드, 롤스크린, 전동커튼, 광명 블라인드",
                                body, crumbs=[("제품", "products.html")]))


# ---------------------------------------------------------------
# 지역 목록 + 지역 상세
# ---------------------------------------------------------------
def build_areas():
    groups = ""
    for g, label in GROUPS:
        items = ""
        for a in AREAS:
            if a["group"] != g:
                continue
            cls = ' class="is-base"' if a.get("base") else ""
            small = "광명 전체 안내 →" if a.get("base") else f'{len(a["dongs"])}개 동네 →'
            items += f'                <a href="{area_file(a)}"{cls}>{a["name"]}<small>{small}</small></a>\n'
        extra = " is-home" if g == "gwangmyeong" else ""
        groups += f'            <h2 class="area-group-title">{label}</h2>\n            <div class="area-index{extra}">\n{items}            </div>\n'
    body = f'''    <section class="page-hero" data-hero="areas">
        <div class="container">
            <h1>시공 지역</h1>
            <p class="lead">광명시 전 지역과 광명에 붙은 서울 서남권 · 경기 도시를 중심으로, 서울 · 경기 · 인천 어디든 방문합니다.<br>동네를 누르면 그 동네 안내를 볼 수 있어요.</p>
        </div>
    </section>

    <!-- 지역 페이지 추가는 _build/areas_data.py 에 한 덩어리 추가 후 build.py 실행 (README 참고) -->
    <section class="section">
        <div class="container">
{groups}{other_areas_html()}            <div class="home-base">
                <p><strong>목록에 없는 동네도 연락 주세요.</strong> 일정만 맞으면 원단 샘플을 챙겨 찾아갑니다.</p>
                <a href="inquiry.html">무료 방문 견적 신청 →</a>
            </div>
        </div>
    </section>
'''
    write("areas.html", page("areas.html", "시공 지역 | 광명 철산 · 하안 · 소하 · 광명뉴타운 · 광명역 · 서울 경기 방문 | 광명커튼",
                             "광명커튼 시공 지역. 광명 철산동 · 하안동 · 소하동 · 광명동 뉴타운 · 일직동 광명역세권 · 학온동, 인접한 구로 · 금천 · 영등포 · 양천 · 강서 · 관악 · 시흥 · 안양 · 부천과 서울 · 경기 · 인천 커튼 · 블라인드 방문 실측.",
                             "광명 커튼, 광명 블라인드, 철산 커튼, 하안동 커튼, 소하동 커튼, 광명뉴타운 커튼, 광명역 커튼, 구로 커튼, 금천 커튼, 시흥 커튼, 안양 커튼, 부천 커튼",
                             body, crumbs=[("시공지역", "areas.html")]))

    for idx, a in enumerate(AREAS):
        build_area(a, idx)


LEADS = [
    "광명에서 출발해 {full}까지 직접 찾아갑니다. 원단 샘플을 챙겨 가 창가에서 비교해 드려요. 실측 · 견적 무료.",
    "{full}의 아파트 · 빌라 · 사무실, 창마다 직접 재서 맞춤으로 만듭니다. 방문 실측은 무료예요.",
    "광명과 맞닿은 {full}은 광명 현장과 같은 날 묶어서 방문합니다. 출장비 없이 무료 실측.",
]


LOCAL_LEADS = [
    "광명에 사는 사람이 {full} 창을 직접 재고 직접 답니다. 광명 안은 출장비 없이 무료 실측.",
    "{full}은 광명커튼에서 금방입니다. 원단 샘플을 챙겨 가 우리 집 빛 아래에서 골라 보세요.",
    "같은 광명이라 실측 날짜도, 달고 난 뒤 A/S도 빠릅니다. {full} 방문 실측 무료.",
    "{full}의 아파트 · 주택, 창마다 따로 재서 맞춤으로 만듭니다. 상담과 견적은 무료예요.",
]


def build_area(a, idx):
    f = area_file(a)
    name, full = a["name"], a["full"]
    plain = name.replace(" · ", "·")
    d1 = a["dongs"][0].split(" ")[-1]
    d2 = (a["dongs"][1] if len(a["dongs"]) > 1 else a["dongs"][0]).split(" ")[-1]
    if a["group"] == "gwangmyeong":
        title, desc, kw = a["title"], a["desc"], a["kw"]
        lead = LOCAL_LEADS[idx % len(LOCAL_LEADS)].format(full=full)
    else:
        short = name.split(" · ")[0]
        title = f"{short} 커튼 · 블라인드 | {d1} · {d2} 방문 실측 · 광명에서 가까운 광명커튼"
        dong_txt = ", ".join(a["dongs"][:5])
        desc = (f"{short} 커튼 · 블라인드 맞춤 시공. {dong_txt} 등 {full} 무료 방문 실측. "
                f"바로 옆 광명에서 출발하는 광명커튼이 원단 샘플을 들고 찾아갑니다.")
        kws = []
        for n in name.split(" · "):
            kws += [f"{n} 커튼", f"{n} 블라인드", f"{n} 커튼 시공", f"{n} 암막커튼"]
        kws += [f"{d.split(' ')[-1]} 커튼" for d in a["dongs"][:4]]
        kw = ", ".join(dict.fromkeys(kws))
        lead = LEADS[idx % len(LEADS)].format(full=full)

    strong = set(a.get("strong", []))
    dongs = "".join(f'                <li{" class=\"is-strong\"" if d in strong else ""}>{d}</li>\n' for d in a["dongs"])
    paras = "".join(f"                <p>{p}</p>\n" for p in a["paras"])
    picks_li = "".join(f'                    <li><a href="products.html#{k}">{PRODUCTS[k]["name"]}</a> — {PRODUCTS[k]["short"]}</li>\n' for k in a["picks"])
    reads = " · ".join(f'<a href="{s}.html">{POST[s]["title"].split(" — ")[0]}</a>' for s in a["posts"])
    pick_cards = "".join(product_card(k) for k in a["picks"])
    nearby = "".join(f'                <a href="{area_file(AREA[s])}">{AREA[s]["name"]}</a>\n' for s in a["nearby"])
    # 대표 사진: 실제 사진이 있는 제품 중 첫 번째 (photos.py 의 PRODUCT 에 있는 제품)
    img = next((k for k in a["picks"] if k in PHOTO_PRODUCTS), "chiffon")

    faq_html, lds = "", [business_ld(name=f"{BRAND} - {full}", url=f"{SITE}/{f}",
                                     area={"@type": "Place", "name": full},
                                     desc=f"{full} 커튼 · 블라인드 맞춤 제작과 시공, 무료 방문 실측")]
    if a.get("faq"):
        faq_html = f'''    <section class="section">
        <div class="container-narrow">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">LOCAL FAQ</p>
                    <h2 class="section-title">{plain}에서 자주 받는 질문</h2>
                </div>
            </div>
            <div class="faq-list reveal">
{faq_items(a["faq"])}            </div>
        </div>
    </section>
'''
        lds.append(faq_ld(a["faq"]))

    if a.get("base"):
        base_box = '''            <div class="home-base">
                <p><strong>광명커튼은 광명에서 운영합니다.</strong> 광명시 어느 동이든 출장비 없이 방문해요.</p>
                <a href="inquiry.html">무료 방문 견적 신청 →</a>
            </div>
'''
    elif a["group"] == "gwangmyeong":
        base_box = f'''            <div class="home-base">
                <p><strong>같은 광명이라 가깝습니다.</strong> {full}은 실측 날짜를 맞추기 쉽고, 달고 난 뒤 A/S도 빨리 들를 수 있어요.</p>
                <a href="area-gwangmyeong.html">광명 전체 안내 →</a>
            </div>
'''
    else:
        base_box = f'''            <div class="home-base">
                <p><strong>광명커튼은 바로 옆 광명에서 출발합니다.</strong> {full} 실측도 출장비를 받지 않아요.</p>
                <a href="area-gwangmyeong.html">광명 시공 안내 →</a>
            </div>
'''

    body = f'''    <section class="page-hero" data-hero="area" data-crumb="{plain}">
        <div class="container">
            <h1>{full}<br>커튼 · 블라인드 맞춤 시공</h1>
            <p class="lead">{lead}</p>
            <div class="hero-buttons">
                <a href="inquiry.html" class="btn btn-light">{plain} 방문 견적 신청 <span class="arrow">→</span></a>
                <a href="tel:{PHONE}" class="btn btn-outline-white">전화 상담</a>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container split">
            <div class="split-img reveal"><img src="{v('images/products/' + img + '.jpg')}" alt="{full} {PRODUCTS[img]['name']}" loading="lazy"></div>
            <div class="split-text prose reveal d1">
                <p class="section-tag">LOCAL NOTE</p>
                <h2>{a["h2"]}</h2>
{paras}                <h3>{plain}에서 많이 찾는 제품</h3>
                <ul>
{picks_li}                </ul>
                <p>읽어 보면 좋은 글: {reads}</p>
            </div>
        </div>
    </section>

{faq_html}    <section class="section bg-sand">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">COVERAGE</p>
                    <h2 class="section-title">{plain} 방문 동네</h2>
                    <p class="section-sub">목록에 없더라도 {full} 안이라면 찾아갑니다.</p>
                </div>
            </div>
            <ul class="dong-list">
{dongs}            </ul>
{base_box}        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">PRODUCTS</p>
                    <h2 class="section-title">{plain} 추천 구성</h2>
                </div>
                <a href="products.html" class="link-more">제품 전체 보기 →</a>
            </div>
            <div class="pick-grid reveal">
{pick_cards}            </div>
        </div>
    </section>

    <section class="section bg-paper">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">NEARBY</p>
                    <h2 class="section-title">가까운 시공 지역</h2>
                </div>
                <a href="areas.html" class="link-more">시공 지역 전체 →</a>
            </div>
            <nav class="nearby-links" aria-label="가까운 시공 지역">
{nearby}            </nav>
        </div>
    </section>
'''
    write(f, page(f, title, desc, kw, body, crumbs=[("시공지역", "areas.html"), (plain, f)],
                  og_image=f"images/products/{img}.jpg", lds=lds))


# ---------------------------------------------------------------
# 매거진
# ---------------------------------------------------------------
def build_blog():
    cards = "".join(post_card(p) for p in POSTS)
    body = f'''    <section class="page-hero" data-hero="blog">
        <div class="container">
            <h1>매거진</h1>
            <p class="lead">커튼 · 블라인드를 고르기 전에 알아 두면 덜 헤매는 이야기.<br>광명 현장을 다니며 자주 받은 질문을 글로 정리했습니다.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="post-grid">
{cards}            </div>
        </div>
    </section>
'''
    write("blog.html", page("blog.html", "매거진 | 입주 커튼 준비 · 구축 아파트 교체 · 암막 · 블라인드 비교 | 광명커튼",
                            "광명뉴타운 입주 커튼 준비, 하안 · 철산 구축 아파트 커튼 교체, 고층 통창 커튼, 커튼 길이, 암막 커튼, 블라인드 비교, 견적서 보는 법까지. 광명커튼이 현장에서 정리한 커튼 · 블라인드 가이드.",
                            "커튼 고르는 법, 블라인드 고르는 법, 입주 커튼, 커튼 교체, 커튼 길이, 암막커튼, 블라인드 종류, 커튼 견적, 광명 커튼",
                            body, crumbs=[("매거진", "blog.html")]))

    for i, p in enumerate(POSTS):
        others = [POSTS[(i + k) % len(POSTS)] for k in (1, 2, 3)]
        more = "".join(post_card(o) for o in others)
        body = f'''    <section class="page-hero is-short" data-hero="post" data-hero-img="{v('images/products/' + p['img'] + '.jpg')}" data-crumb="{p["cat"]}">
        <div class="container">
            <h1>{p["title"]}</h1>
            <div class="tag-row"><span class="tag">{p["cat"]}</span><span class="tag">{date_dot(TODAY)}</span></div>
        </div>
    </section>

    <section class="section">
        <article class="container-narrow prose">
{p["body"].strip(chr(10))}
        </article>
    </section>

    <section class="section bg-paper">
        <div class="container">
            <div class="section-head">
                <div>
                    <p class="section-tag">MORE</p>
                    <h2 class="section-title">이어서 읽기</h2>
                </div>
            </div>
            <div class="post-grid">
{more}            </div>
        </div>
    </section>
'''
        ld = {
            "@context": "https://schema.org", "@type": "Article",
            "headline": p["title"], "description": p["desc"],
            "image": f"{SITE}/{v('images/products/' + p['img'] + '.jpg')}",
            "datePublished": TODAY, "dateModified": TODAY,
            "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": BRAND,
                          "logo": {"@type": "ImageObject", "url": f"{SITE}/images/brand/logo-full.png"}},
            "mainEntityOfPage": f"{SITE}/{p['slug']}.html",
        }
        write(f"{p['slug']}.html", page(f"{p['slug']}.html", f"{p['title']} | 광명커튼", p["desc"], p["kw"], body,
                                        crumbs=[("매거진", "blog.html"), (p["title"], f"{p['slug']}.html")],
                                        og_image=f"images/products/{p['img']}.jpg", og_type="article", lds=[ld]))


# ---------------------------------------------------------------
# 브랜드 · FAQ · 문의 · 완료
# ---------------------------------------------------------------
def build_about():
    body = f'''    <section class="page-hero" data-hero="about">
        <div class="container">
            <h1>우리 동네 창은<br>우리 동네에서 잽니다</h1>
            <p class="lead">광명커튼은 광명에 사는 사람이 운영하는 커튼 · 블라인드 맞춤 시공 집입니다.</p>
        </div>
    </section>

    <!-- 브랜드 소개 문구는 초안입니다. 대표님 이야기(경력, 시작한 계기 등)를 넣으면 더 좋아요. -->
    <section class="section">
        <div class="container split">
            <div class="split-img reveal"><img src="{v('images/about/about-01.jpg')}" alt="거실 아이보리 겉커튼과 쉬폰 시공 사진" loading="lazy"></div>
            <div class="split-text reveal d1">
                <p class="section-tag">OUR STORY</p>
                <h2>이름에 동네를<br>걸었습니다</h2>
                <p>가게 이름을 '광명커튼'으로 지은 건 이 동네에서 오래 일하겠다는 뜻입니다. 이름에 동네를 걸면 대충 할 수가 없어요. 오늘 단 집 앞을 내일도 지나다니니까요.</p>
                <p>광명은 하안 · 철산의 오래된 단지부터 뉴타운 새 아파트, 광명역 고층 통창, 학온동 주택까지 한 도시 안에 집의 모양이 다양합니다. 그 차이를 매일 다니며 보고 있기 때문에, 처음 보는 창이라도 어떤 구성이 맞을지 금방 떠올릴 수 있어요.</p>
            </div>
        </div>
    </section>

    <section class="section bg-sand">
        <div class="container">
            <div class="section-head reveal">
                <div>
                    <p class="section-tag">PROMISE</p>
                    <h2 class="section-title">광명커튼의 네 가지 원칙</h2>
                </div>
            </div>
            <div class="process-list reveal">
                <div class="process-item"><span class="step">01</span><h3>한 사람이 끝까지</h3><p>상담한 사람이 재고, 그 사람이 달고, A/S도 같은 사람이 갑니다. 말이 중간에서 바뀌지 않아요.</p></div>
                <div class="process-item"><span class="step">02</span><h3>샘플은 창가로</h3><p>원단을 들고 가 실제 창에 대 봅니다. 매장 조명 아래 색과 우리 집 빛 아래 색은 다르니까요.</p></div>
                <div class="process-item"><span class="step">03</span><h3>견적은 항목별로</h3><p>원단 · 레일 · 시공비를 나눠 적어 드립니다. 다른 곳과 비교해 보셔도 괜찮아요.</p></div>
                <div class="process-item"><span class="step">04</span><h3>안 해도 되는 건 말씀드립니다</h3><p>쓸 수 있는 레일은 그대로 두고, 모든 창에 비싼 제품을 권하지 않습니다.</p></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container split reverse">
            <div class="split-img reveal"><img src="{v('images/about/about-02.jpg')}" alt="주택 내닫이창 화이트 콤비 블라인드 시공 사진" loading="lazy"></div>
            <div class="split-text reveal d1">
                <p class="section-tag">SERVICE AREA</p>
                <h2>광명을 중심으로<br>서울 · 경기까지</h2>
                <p>광명시 전 지역(광명동 · 철산동 · 하안동 · 소하동 · 일직동 · 학온동)을 기본으로, 바로 붙은 구로 · 금천 · 영등포 · 양천 · 강서 · 관악 · 시흥 · 안양 · 부천을 같은 동선으로 다닙니다. 그 밖의 서울 · 경기 · 인천 지역도 일정을 맞춰 방문해요.</p>
                <a href="areas.html" class="btn btn-outline">시공 지역 보기 <span class="arrow">→</span></a>
            </div>
        </div>
    </section>
'''
    write("about.html", page("about.html", "광명커튼 소개 | 광명에 사는 사람이 하는 커튼 · 블라인드 맞춤 시공",
                             "광명커튼은 광명에 사는 사람이 직접 재고 직접 다는 커튼 · 블라인드 맞춤 시공 집입니다. 상담부터 A/S까지 한 사람이 맡고, 원단 샘플을 들고 광명 · 서울 · 경기를 방문합니다.",
                             "광명커튼, 광명 커튼 업체, 광명 블라인드 업체, 광명 커튼 가게, 철산 커튼, 하안동 커튼",
                             body, crumbs=[("브랜드", "about.html")], lds=[business_ld(url=SITE + "/about.html")]))


FAQ_GROUPS = [
    ("상담 · 실측", [
        ("방문 실측과 견적에 비용이 드나요?", "광명시 전 지역과 가까운 서울 서남권 · 경기 지역은 출장비 없이 원단 샘플을 들고 방문해 실측하고 견적을 드립니다."),
        ("견적만 받고 계약하지 않아도 되나요?", "네, 괜찮습니다. 견적서를 받아 보시고 다른 곳과 비교하신 뒤 천천히 정하셔도 돼요."),
        ("방문 전에 사진으로 대략적인 견적을 알 수 있나요?", "창 사진과 대강의 가로 · 세로를 카카오톡으로 보내 주시면 추천 구성과 예상 금액을 먼저 알려드립니다. 정확한 금액은 실측 뒤에 정해져요."),
        ("평일 저녁이나 주말에도 와 주시나요?", "광명 안은 동선이 짧아 저녁 · 주말 일정도 비교적 맞추기 쉽습니다. 신청서에 편한 시간을 적어 주세요."),
    ]),
    ("제작 · 시공", [
        ("실측하고 며칠 뒤에 달 수 있나요?", "보통 일주일 안팎입니다. 원단 재고나 입주가 몰리는 시기에 따라 달라질 수 있어 상담 때 날짜를 정확히 말씀드려요."),
        ("설치하는 데 시간은 얼마나 걸리나요?", "일반 아파트 한 집 기준으로 몇 시간이면 끝나는 경우가 많습니다. 창 개수와 전동 제품 여부에 따라 달라져요."),
        ("쓰던 커튼과 블라인드는 떼어 주시나요?", "네, 설치하면서 기존 제품을 함께 떼어 드립니다. 쓰던 레일을 그대로 쓸 수 있는지도 그 자리에서 확인해요."),
        ("세입자라 벽에 구멍을 내기 어려워요.", "기존 레일이나 브라켓, 창틀에 거는 브라켓처럼 구멍 없이 다는 방법을 먼저 찾아봅니다. 창 구조마다 가능 여부가 달라 실측 때 확인해 드려요."),
    ]),
    ("제품", [
        ("커튼이 나을까요, 블라인드가 나을까요?", "분위기가 중요한 거실은 커튼, 깔끔하고 조작이 쉬워야 하는 방 · 주방은 블라인드를 많이 고르십니다. 한 집 안에서 섞어 쓰는 경우가 대부분이에요."),
        ("암막 커튼이면 완전히 깜깜해지나요?", "원단은 빛을 거의 막지만 커튼 가장자리로 새는 빛은 남을 수 있습니다. 레일 위치와 폭 · 길이를 맞춰 틈을 최대한 줄이고, 더 어둡게 원하면 암막 롤스크린을 함께 다는 방법도 있어요."),
        ("전동 커튼은 무엇이 필요한가요?", "커튼박스 가까이에 콘센트가 있어야 합니다. 인테리어 공사를 앞두고 있다면 공사 전에 상담해 주시면 선이 보이지 않게 준비할 수 있어요."),
        ("커튼은 집에서 빨 수 있나요?", "물세탁이 되는 원단과 드라이클리닝이 필요한 원단이 있습니다. 원단을 고를 때 관리 방법까지 함께 알려드려요."),
    ]),
    ("지역 · A/S", [
        ("어디까지 방문하나요?", "광명시 전 지역과 구로 · 금천 · 영등포 · 양천 · 강서 · 관악 · 시흥 · 안양 · 부천을 주로 다니고, 그 밖의 서울 · 경기 · 인천 지역도 일정을 맞춰 방문합니다."),
        ("매장에 직접 가 볼 수 있나요?", "광명커튼은 매장보다 방문 상담 위주로 운영합니다. 원단 샘플을 들고 댁으로 찾아가 실제 창에 대 보며 고르시도록 돕는 방식이에요."),
        ("달고 나서 문제가 생기면 어떻게 하나요?", "전화나 카카오톡으로 사진을 보내 주시면 확인하고 방문해 점검합니다. 광명 안은 가까워 빨리 들를 수 있어요. A/S 기간과 범위는 상담 때 자세히 안내합니다."),
        ("광명뉴타운 사전점검 날 실측이 되나요?", "됩니다. 사전점검 날 재 두면 입주일에 바로 달 수 있어서 가장 권하는 방법이에요. 단지에 따라 외부 업체 동행 신청이 필요할 수 있습니다."),
    ]),
]


def build_faq():
    groups = ""
    all_pairs = []
    for label, pairs in FAQ_GROUPS:
        all_pairs += pairs
        groups += f'            <h2 class="faq-group-title">{label}</h2>\n            <div class="faq-list">\n{faq_items(pairs)}            </div>\n'
    body = f'''    <section class="page-hero is-short" data-hero="faq">
        <div class="container">
            <h1>자주 묻는 질문</h1>
            <p class="lead">상담과 실측, 제작과 시공, 제품, 지역과 A/S까지 많이 받는 질문을 모았습니다.</p>
        </div>
    </section>

    <section class="section">
        <div class="container-narrow">
{groups}            <div class="note-box mt-48">
                <strong>궁금한 게 더 있다면</strong>
                전화나 카카오톡으로 편하게 물어봐 주세요. <a href="inquiry.html">무료 견적 신청</a>
            </div>
        </div>
    </section>
'''
    write("faq.html", page("faq.html", "자주 묻는 질문 | 커튼 · 블라인드 실측 비용 · 제작 기간 · A/S | 광명커튼",
                           "커튼 · 블라인드 방문 실측 비용, 제작 기간, 무타공 설치, 암막 커튼 빛샘, 전동 커튼 조건, 방문 지역과 A/S까지 광명커튼에 자주 묻는 질문을 정리했습니다.",
                           "커튼 실측 비용, 커튼 제작 기간, 무타공 커튼, 암막커튼 빛샘, 전동커튼 조건, 커튼 A/S, 광명 커튼",
                           body, crumbs=[("FAQ", "faq.html")], lds=[faq_ld(all_pairs)]))


def build_inquiry():
    regions = [
        "광명 철산동", "광명 하안동", "광명 소하동", "광명동 (광명뉴타운)", "광명 일직동 (광명역)",
        "광명 학온동 (노온사 · 가학 · 옥길)", "구로 · 금천 · 영등포", "양천 · 강서 · 관악",
        "시흥 · 안양 · 부천", "그 밖의 서울", "그 밖의 경기 · 인천",
    ]
    opts = "".join(f'                        <option value="{r}">{r}</option>\n' for r in regions)
    types = ["린넨 커튼", "쉬폰 커튼", "암막 커튼", "콤비 블라인드", "우드 블라인드", "허니콤 블라인드", "롤스크린", "전동 제품", "아직 모르겠어요"]
    checks = "".join(f'                        <label><input type="checkbox" name="type" value="{t}"><span>{t}</span></label>\n' for t in types)
    body = f'''    <section class="page-hero is-short" data-hero="inquiry">
        <div class="container">
            <h1>무료 방문 견적 신청</h1>
            <p class="lead">남겨 주신 내용을 보고 연락드려 방문 날짜를 잡아 드립니다.</p>
        </div>
    </section>

    <section class="section">
        <div class="container inquiry-layout">
            <aside class="inquiry-aside">
                <h2>창 사진을 보내 주시면<br>더 빨리 안내해 드려요</h2>
                <p>신청서를 남기신 뒤 카카오톡으로 창 사진을 보내 주시면, 방문 전에 대략적인 구성과 예산을 먼저 알려드립니다. 새 아파트 입주라면 단지명 · 평형 · 타입을 함께 적어 주세요.</p>
                <div class="channel-list">
                    <a href="tel:{PHONE}" class="channel"><div><strong>전화 상담</strong><span data-text="phone">{PHONE}</span></div><span class="go">→</span></a>
                    <a href="#" class="channel" data-link="kakao"><div><strong>카카오톡 상담</strong><span>창 사진 보내고 바로 상담</span></div><span class="go">→</span></a>
                </div>
            </aside>

            <!-- 폼 전송 주소와 메일 제목은 js/config.js 에서 관리 (formspreeId) -->
            <form class="inquiry-form" action="#" method="POST">
                <input type="hidden" name="_next" value="{SITE}/thanks.html">
                <input type="hidden" name="_subject" value="[광명커튼] 새 견적 문의가 도착했습니다">
                <input type="hidden" name="사이트" value="광명커튼">
                <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">

                <div class="form-group">
                    <label class="title" for="f-name">이름 <span class="required">*</span></label>
                    <input type="text" id="f-name" name="name" required placeholder="홍길동" autocomplete="name">
                </div>
                <div class="form-group">
                    <label class="title" for="f-phone">전화번호 <span class="required">*</span></label>
                    <input type="tel" id="f-phone" name="phone" required placeholder="010-0000-0000" autocomplete="tel">
                </div>
                <div class="form-group">
                    <label class="title" for="f-region">지역 <span class="required">*</span></label>
                    <select id="f-region" name="region" required>
                        <option value="">동네를 골라 주세요</option>
{opts}                    </select>
                </div>
                <div class="form-group">
                    <label class="title" for="f-address">상세 주소 (동 · 아파트명)</label>
                    <input type="text" id="f-address" name="address" placeholder="예: 철산동 ○○아파트 / 광명뉴타운 ○구역">
                </div>
                <div class="form-group">
                    <label class="title" for="f-space">시공 공간 <span class="required">*</span></label>
                    <select id="f-space" name="space" required>
                        <option value="">어느 공간인가요?</option>
                        <option value="거실">거실</option>
                        <option value="안방 · 침실">안방 · 침실</option>
                        <option value="아이방">아이방</option>
                        <option value="서재 · 공부방">서재 · 공부방</option>
                        <option value="주방">주방</option>
                        <option value="집 전체 (새 아파트 입주)">집 전체 (새 아파트 입주)</option>
                        <option value="집 전체 (교체)">집 전체 (교체)</option>
                        <option value="단독 · 전원주택">단독 · 전원주택</option>
                        <option value="사무실 · 매장 · 학원">사무실 · 매장 · 학원</option>
                    </select>
                </div>
                <div class="form-group">
                    <span class="title" style="display:block;font-size:15px;font-weight:600;color:var(--color-ink);margin-bottom:10px">관심 제품 (여러 개 선택 가능)</span>
                    <div class="check-grid">
{checks}                    </div>
                </div>
                <div class="form-group">
                    <label class="title" for="f-date">방문 희망 날짜</label>
                    <input type="date" id="f-date" name="visit_date">
                </div>
                <div class="form-group">
                    <label class="title" for="f-msg">더 알려 주실 내용</label>
                    <textarea id="f-msg" name="message" placeholder="입주 · 이사 날짜, 원하는 분위기, 창 방향, 걱정되는 점 등을 편하게 적어 주세요."></textarea>
                </div>
                <label class="agree"><input type="checkbox" required> <span>상담 연락과 방문 일정을 잡기 위해 이름 · 전화번호 · 주소를 받는 것에 동의합니다. 받은 정보는 견적 상담 외에는 쓰지 않고, 상담을 마치면 지웁니다.</span></label>
                <button type="submit" class="btn btn-primary">신청서 보내기</button>
            </form>
        </div>
    </section>
'''
    write("inquiry.html", page("inquiry.html", "무료 방문 견적 신청 | 광명 커튼 · 블라인드 광명커튼",
                               "커튼 · 블라인드 무료 방문 견적 신청. 광명커튼이 원단 샘플을 들고 광명 철산 · 하안 · 소하 · 광명뉴타운 · 광명역과 서울 · 경기를 방문해 실측하고 견적을 드립니다.",
                               "광명 커튼 견적, 광명 블라인드 견적, 커튼 무료 실측, 커튼 방문 견적, 철산 커튼 견적, 하안동 커튼 견적",
                               body, crumbs=[("견적문의", "inquiry.html")]))


def build_404():
    body = '''    <section class="page-hero" data-hero="thanks">
        <div class="container">
            <h1>찾으시는 페이지가 없어요</h1>
            <p class="lead">주소가 바뀌었거나 없어진 페이지입니다.<br>아래에서 원하시는 곳으로 이동해 보세요.</p>
            <div class="hero-buttons">
                <a href="index.html" class="btn btn-light">홈으로 <span class="arrow">→</span></a>
                <a href="areas.html" class="btn btn-outline-white">시공 지역</a>
                <a href="inquiry.html" class="btn btn-outline-white">무료 견적 신청</a>
            </div>
        </div>
    </section>
'''
    out = page("404.html", "페이지를 찾을 수 없습니다 | 광명커튼", "요청하신 페이지를 찾을 수 없습니다.", "광명커튼", body, noindex=True)
    # 어떤 깊이의 주소에서 보여도 CSS · 사진 · 링크가 깨지지 않게
    write("404.html", out.replace("<head>\n", '<head>\n    <base href="/">\n', 1))


def build_thanks():
    body = '''    <section class="page-hero" data-hero="thanks">
        <div class="container">
            <h1>신청서를 잘 받았습니다</h1>
            <p class="lead">적어 주신 번호로 곧 전화드릴게요.<br>그사이 커튼 고르는 법을 미리 읽어 보셔도 좋아요.</p>
            <div class="hero-buttons">
                <a href="blog.html" class="btn btn-light">매거진 보기 <span class="arrow">→</span></a>
                <a href="index.html" class="btn btn-outline-white">홈으로</a>
            </div>
        </div>
    </section>
'''
    write("thanks.html", page("thanks.html", "신청 완료 | 광명커튼", "신청서를 잘 받았습니다.", "광명커튼", body, noindex=True))


# ---------------------------------------------------------------
# includes.js (헤더 · 푸터 · 지역 링크)
# ---------------------------------------------------------------
def build_includes():
    completed = ",\n".join(f'  "{a["name"]}": "{area_file(a)}"' for a in AREAS)
    order = ",".join(f'"{a["name"]}"' for a in AREAS)
    tpl = open(os.path.join(os.path.dirname(__file__), "includes.template.js"), encoding="utf-8").read()
    js = (tpl.replace("/*__COMPLETED_AREAS__*/", completed)
             .replace("/*__ALL_AREAS__*/", order)
             .replace("__VER__", VER))
    write("js/includes.js", js)


# ---------------------------------------------------------------
# sitemap · rss · robots · htaccess · 네이버 수집 요청 목록
# ---------------------------------------------------------------
def build_meta_files():
    basics = ["index.html", "areas.html", "inquiry.html", "products.html", "blog.html", "faq.html", "about.html"]
    pri = {"index.html": "1.0", "inquiry.html": "0.9", "areas.html": "0.9", "products.html": "0.8",
           "blog.html": "0.7", "faq.html": "0.7", "about.html": "0.6", "gallery.html": "0.8"}
    if CASES:
        basics.insert(4, "gallery.html")
    urls = [(p, pri[p]) for p in basics]
    for a in AREAS:
        urls.append((area_file(a), "0.9" if a["group"] == "gwangmyeong" else "0.8"))
    for c in CASES:
        urls.append((f"case-{c['no']}.html", "0.6"))
    for p in POSTS:
        urls.append((p["slug"] + ".html", "0.6"))
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, pr in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        xml += f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{pr}</priority>\n  </url>\n"
    xml += "</urlset>\n"
    write("sitemap.xml", xml)

    # 네이버 서치어드바이저 '웹 페이지 수집' 요청용 (하루 요청 개수 제한이 있어 나눔)
    def u(p):
        return SITE + "/" + ("" if p == "index.html" else p)
    lines = [f"# {BRAND} 네이버 수집 요청 URL (총 {len(urls)}개)",
             "# 서치어드바이저 > 요청 > 웹 페이지 수집 에 한 줄씩 붙여넣기", "",
             "########## 1일차 ##########", "", "## 기본 페이지"]
    lines += [u(p) for p in basics]
    lines += ["", "## 광명 동네"] + [u(area_file(a)) for a in AREAS if a["group"] == "gwangmyeong"]
    lines += ["", "########## 2일차 ##########", "", "## 광명과 맞닿은 지역"]
    lines += [u(area_file(a)) for a in AREAS if a["group"] == "near"]
    lines += ["", "## 매거진"] + [u(p["slug"] + ".html") for p in POSTS]
    if CASES:
        lines += ["", "########## 3일차 ##########", "", "## 시공사례"] + [u(f"case-{c['no']}.html") for c in CASES]
    write("naver-index-urls.txt", "\n".join(lines) + "\n")

    items = ""
    for p in POSTS:
        items += f'''    <item>
      <title>{esc(p["title"])}</title>
      <link>{SITE}/{p["slug"]}.html</link>
      <guid>{SITE}/{p["slug"]}.html</guid>
      <description>{esc(p["desc"])}</description>
      <category>{esc(p["cat"])}</category>
      <pubDate>Sat, 24 Oct 2026 09:00:00 +0900</pubDate>
    </item>
'''
    write("rss.xml", f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{BRAND} 매거진</title>
    <link>{SITE}/</link>
    <description>광명커튼의 커튼 · 블라인드 가이드</description>
    <language>ko</language>
{items}  </channel>
</rss>
''')

    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thanks.html\nDisallow: /404.html\nDisallow: /_build/\n\nSitemap: {SITE}/sitemap.xml\n")

    write(".htaccess", f'''# ============================================
# 광명커튼 - 서버 설정 (Apache 웹호스팅용)
# ▸ http:// 또는 www. 로 들어와도 https://{DOMAIN} 로 이동
#   (검색엔진이 주소를 하나로만 인식하게 해서 노출 점수가 나뉘지 않게 함)
# ▸ 업로드 후 "리디렉션이 너무 많습니다" 오류가 나면
#   호스팅 관리 화면에서 이미 https 자동 이동을 켜 둔 경우입니다.
#   그때는 아래 RewriteCond %{{HTTPS}} off [OR] 줄을 지우세요.
# ============================================

RewriteEngine On
RewriteCond %{{HTTPS}} off [OR]
RewriteCond %{{HTTP_HOST}} ^www\\. [NC]
RewriteRule ^ https://{DOMAIN}%{{REQUEST_URI}} [L,R=301]

# 없는 주소로 들어오면 안내 페이지
ErrorDocument 404 /404.html

# 생성기 폴더는 외부에서 볼 수 없게
RewriteRule ^_build/ - [F,L]

<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript application/json image/svg+xml text/xml application/xml application/rss+xml
</IfModule>

<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpeg "access plus 1 day"
    ExpiresByType image/png "access plus 1 day"
    ExpiresByType text/css "access plus 1 hour"
    ExpiresByType application/javascript "access plus 1 hour"
    ExpiresByType text/html "access plus 0 seconds"
</IfModule>
''')


if __name__ == "__main__":
    build_index()
    build_gallery()
    build_products()
    build_areas()
    build_blog()
    build_about()
    build_faq()
    build_inquiry()
    build_thanks()
    build_404()
    build_includes()
    build_meta_files()
    print(f"{len(written)} files written")
