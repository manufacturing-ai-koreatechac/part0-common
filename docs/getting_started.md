# 빠른 시작 가이드 — 제조 AI 교육 v1.6.15

각 트랙 실습을 시작하기 위한 단계별 가이드입니다.

---

## 전제 조건

- Python 3.9 이상 (3.10 권장)
- Git
- 인터넷 연결 (패키지 설치 및 허깅페이스 모델 다운로드)

---

## 1단계: 저장소 클론

수강 중인 트랙의 저장소를 클론합니다.

```bash
# 예시: Track A-1 (진동 FFT 고장 진단)
git clone https://github.com/<org>/track-a1-vibration-fft.git
cd track-a1-vibration-fft
```

트랙별 저장소 이름:

| 트랙 | 저장소 |
|------|--------|
| Part 0 (공통) | `part0-common` |
| Track A-1 | `track-a1-vibration-fft` |
| Track A-2 | `track-a2-autoencoder-rul` |
| Track B-1 | `track-b1-cnn-transfer` |
| Track B-2 | `track-b2-vit-yolov8` |
| X1 (RAG·Agent) | `x1-rag-agent`, `x1-s3-rag-streamlit` 등 |

---

## 2단계: 가상환경 생성 및 활성화

```bash
# 가상환경 생성 (처음 한 번만)
python -m venv venv

# 활성화 — Mac/Linux
source venv/bin/activate

# 활성화 — Windows
venv\Scripts\activate
```

---

## 3단계: 패키지 설치

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **설치 시간**: 약 3~10분 (트랙별로 다름)

Part 0 공통 유틸리티도 설치합니다:

```bash
# 저장소 루트에서 실행하거나, notebooks 내 셀에 추가
pip install -e ../part0-common   # 로컬 클론한 경우
```

---

## 4단계: Jupyter Lab 실행

```bash
jupyter lab
```

브라우저가 자동으로 열립니다. 안 열리면 터미널에 출력된 URL을 복사해 붙여넣으세요.

---

## 5단계: 노트북 실행 순서

각 트랙의 `notebooks/` 폴더에서 번호 순서대로 실행합니다.

**Track A-1 예시**:
1. `01_data_exploration.ipynb` — 데이터 탐색
2. `02_fft_frequency_analysis.ipynb` — FFT 분석 + BPFI/BPFO 마커
3. `03_fault_classification.ipynb` — 고장 분류 모델

`Shift + Enter`로 셀을 하나씩 실행하거나, `Kernel > Restart & Run All`로 전체 실행합니다.

---

## 문제 해결

### Python이 없어요

```bash
# Mac (Homebrew 사용)
brew install python@3.10

# Windows
# https://www.python.org/downloads/ 에서 다운로드
```

### pip install 실패

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 한글 폰트 깨짐

노트북 첫 셀에서 `setup_korean_font()`를 호출하면 OS를 자동 감지합니다:

```python
import sys; sys.path.append('../../part0-common')
from utils.viz_utils import setup_korean_font, COLORS
COLORS = setup_korean_font()
```

직접 설정하려면:

```python
import matplotlib.pyplot as plt
# Mac
plt.rcParams['font.family'] = 'Apple SD Gothic Neo'
# Windows
# plt.rcParams['font.family'] = 'Malgun Gothic'
# Linux/Colab: NanumGothic (apt-get install -y fonts-nanum)
plt.rcParams['axes.unicode_minus'] = False
```

### Jupyter Lab 포트 충돌

```bash
jupyter lab --port=8889
```

### 모듈을 찾을 수 없음 (`ModuleNotFoundError`)

```bash
# 가상환경이 활성화됐는지 확인
which python   # Mac/Linux → venv/bin/python 이어야 함
where python   # Windows  → venv\Scripts\python.exe 이어야 함

# 패키지 재설치
pip install -r requirements.txt --force-reinstall
```

---

## 유용한 단축키

| 단축키 | 동작 |
|--------|------|
| `Shift + Enter` | 셀 실행 후 다음 셀 이동 |
| `Ctrl + Enter` | 셀 실행 (이동 없음) |
| `A` (명령 모드) | 위에 새 셀 추가 |
| `B` (명령 모드) | 아래에 새 셀 추가 |
| `D D` (명령 모드) | 셀 삭제 |
| `Esc` | 편집 모드 → 명령 모드 |

---

## 참고 자료

- [Jupyter Lab 공식 문서](https://jupyterlab.readthedocs.io/)
- [Python 가상환경 가이드](https://docs.python.org/ko/3/tutorial/venv.html)
- [KAMP 데이터 포털](https://www.kamp-ai.kr/)

---

*제조 AI 교육 v1.6.15 | 2026*
