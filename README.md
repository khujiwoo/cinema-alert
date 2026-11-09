# 치이카와 영화관 빈자리 감시 (설정 중)

2026-11-11, 2026-11-14 CGV 왕십리와 롯데시네마 청량리 첫 회차 대상.

**중요:** 현재 버전은 GitHub Actions 실행 및 예매 페이지 로딩용 뼈대입니다. 영화관별 실제 첫 회차 식별 및 잔여 좌석 파서는 검증되지 않아 **빈자리 알림은 아직 발송하지 않습니다.** 작동한다고 오해하지 마세요.

설정: Repository Settings → Secrets and variables → Actions에서 Secrets에 `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`를 등록하고 Variables에 해당 날짜/극장별 직접 예매 URL 네 개를 등록합니다. 토큰은 코드나 공개 파일에 입력하지 마세요. 이후 첫 회차 및 잔여 좌석을 판별하는 검증된 로직이 추가되어야 알림이 작동합니다.

업로드: ZIP 압축을 풀고 `monitor.py`, `requirements.txt`, `README.md`, `.github/workflows/seat-monitor.yml`을 **폴더 구조를 유지해** 저장소에 업로드하세요. GitHub 웹 업로드가 숨김 폴더를 누락하면 `.github/workflows/seat-monitor.yml`은 GitHub의 Create new file에서 경로를 직접 입력해야 합니다.
