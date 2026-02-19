# Part 1-1: AI 기초와 데이터 이해 (생산기술자용)

> **v12 Enhanced**: Jupyter Notebook + 단계별 가이드 + 한글 완벽 지원

---

## 🎯 학습 목표

이 실습을 통해 다음을 배울 수 있습니다:

- ✅ KAMP 한국 공공 제조 데이터 활용
- ✅ 데이터 탐색 및 시각화
- ✅ PyCaret을 사용한 AutoML
- ✅ SHAP을 통한 AI 모델 해석
- ✅ 제조 현장 문제에 AI 적용

---

## 📚 실습 구성

| 순서 | 실습 | 파일 | 소요 시간 | 난이도 |
|:----:|------|------|:---------:|:------:|
| 1 | 데이터 탐색 | `01_kamp_data_exploration.ipynb` | 30분 | ⭐ |
| 2 | AutoML | `02_pycaret_automl.ipynb` | 45분 | ⭐⭐ |
| 3 | 모델 해석 | `03_shap_explainer.ipynb` | 30분 | ⭐⭐ |

**총 소요 시간**: 약 2시간

---

## 🚀 시작하기

### 1️⃣ 환경 설정

```bash
# 프로젝트 루트에서
cd practice-v12-enhanced

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

### 2️⃣ Jupyter Lab 실행

```bash
# Part 1-1 폴더로 이동
cd part1-1

# Jupyter Lab 시작
jupyter lab
```

### 3️⃣ 실습 순서대로 진행

```
notebooks/
  ├─ 01_kamp_data_exploration.ipynb  ← 여기서 시작!
  ├─ 02_pycaret_automl.ipynb
  └─ 03_shap_explainer.ipynb
```

---

## 📂 폴더 구조

```
part1-1/
├── README.md                          # 이 문서
├── notebooks/                         # Jupyter 실습
│   ├── 01_kamp_data_exploration.ipynb # 데이터 탐색
│   ├── 02_pycaret_automl.ipynb        # AutoML
│   └── 03_shap_explainer.ipynb        # 모델 해석
├── scripts/                           # Python 스크립트
│   ├── kamp_data_loader.py
│   ├── pycaret_trainer.py
│   └── shap_analyzer.py
├── data/                              # 샘플 데이터
│   ├── sample_kamp_cnc.csv            # CNC 가공 데이터
│   └── sample_kamp_vibration.csv      # 진동 데이터
├── outputs/                           # 결과 저장
│   └── .gitkeep
└── docs/                              # 참고 문서
    └── getting_started.md
```

---

## 📊 사용 데이터

### KAMP CNC 가공 데이터

| 항목 | 내용 |
|------|------|
| **파일** | `sample_kamp_cnc.csv` |
| **크기** | 240KB (약 1,000행) |
| **출처** | [KAMP](https://mdata.kamp-ai.kr/) |
| **설명** | CNC 가공 공정 센서 데이터 |

**주요 변수**:
- 온도, 진동, 회전수, 이송속도
- 절삭력, 공구 마모
- 품질 등급 (양품/불량)

### KAMP 진동 데이터

| 항목 | 내용 |
|------|------|
| **파일** | `sample_kamp_vibration.csv` |
| **크기** | 1.5MB (약 10,000행) |
| **출처** | [KAMP](https://mdata.kamp-ai.kr/) |
| **설명** | 회전 설비 진동 센서 데이터 |

---

## 🔧 실습 상세 내용

### 실습 1: 데이터 탐색 (30분)

**학습 내용**:
- KAMP 데이터 로드 (한글 인코딩 처리)
- 데이터 구조 및 통계량 파악
- 시각화를 통한 패턴 발견
- 데이터 품질 평가

**주요 코드**:
```python
# 한글 인코딩 자동 처리
df = pd.read_csv('data.csv', encoding='utf-8-sig')

# 인터랙티브 시각화
import plotly.express as px
fig = px.scatter_matrix(df)
fig.show()
```

### 실습 2: PyCaret AutoML (45분)

**학습 내용**:
- PyCaret 기본 사용법
- 자동 전처리 및 피처 엔지니어링
- 18+ 모델 자동 비교
- 하이퍼파라미터 튜닝

**주요 코드**:
```python
from pycaret.classification import *

# 자동 전처리 + 모델 비교
setup(data=df, target='품질등급')
best_model = compare_models()

# 튜닝 및 저장
tuned_model = tune_model(best_model)
save_model(tuned_model, 'my_model')
```

### 실습 3: SHAP 모델 해석 (30분)

**학습 내용**:
- SHAP 값 계산
- 피처 중요도 분석
- 개별 예측 설명
- 불량 원인 분석

**주요 코드**:
```python
import shap

# SHAP 분석
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# 시각화
shap.summary_plot(shap_values, X_test)
shap.waterfall_plot(explainer(X_test.iloc[[0]])[0])
```

---

## 💡 학습 팁

### Jupyter Notebook 사용법

**셀 실행**:
- `Shift + Enter`: 셀 실행 후 다음 셀로 이동
- `Ctrl + Enter`: 셀 실행만 (이동 안함)

**셀 추가/삭제**:
- `A`: 위에 셀 추가
- `B`: 아래에 셀 추가
- `DD`: 셀 삭제

**마크다운 <-> 코드**:
- `M`: 마크다운 셀로 변경
- `Y`: 코드 셀로 변경

### 한글 폰트 설정

```python
import matplotlib.pyplot as plt

# Mac
plt.rcParams['font.family'] = 'AppleGothic'

# Windows
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
```

### 자주 발생하는 오류

**1. 한글 깨짐**
```python
# 해결: 인코딩 명시
df = pd.read_csv('data.csv', encoding='utf-8-sig')
```

**2. PyCaret 느림**
```python
# 해결: n_jobs 증가
setup(data=df, target='target', n_jobs=-1)
```

**3. Plotly 차트 안 보임**
```bash
# 해결: ipywidgets 설치
pip install ipywidgets
jupyter labextension install jupyterlab-plotly
```

---

## 🎓 학습 체크리스트

### 실습 1 완료 후
- [ ] KAMP 데이터를 성공적으로 로드했다
- [ ] 데이터의 기본 통계량을 이해했다
- [ ] 히스토그램과 상관관계 히트맵을 그렸다
- [ ] 데이터 품질을 평가했다

### 실습 2 완료 후
- [ ] PyCaret setup을 실행했다
- [ ] 여러 모델을 자동으로 비교했다
- [ ] 최적 모델을 튜닝했다
- [ ] 모델을 저장했다

### 실습 3 완료 후
- [ ] SHAP 값을 계산했다
- [ ] Summary Plot을 해석했다
- [ ] Waterfall Plot으로 개별 예측을 설명했다
- [ ] 불량의 주요 원인을 파악했다

---

## 📚 참고 자료

### 데이터 소스
- [KAMP 데이터 포털](https://mdata.kamp-ai.kr/)
- [AI Hub](https://www.aihub.or.kr/)
- [공공데이터포털](https://www.data.go.kr/)

### 라이브러리 문서
- [PyCaret 공식 문서](https://pycaret.org/)
- [SHAP 문서](https://shap.readthedocs.io/)
- [Plotly 튜토리얼](https://plotly.com/python/)

### 추가 학습
- [Pandas 10분 튜토리얼](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Jupyter Notebook 가이드](https://jupyter.org/documentation)

---

## 🆘 문제 해결

### Q: Jupyter Lab이 실행되지 않아요
```bash
# 해결
pip install --upgrade jupyterlab
jupyter lab --version  # 버전 확인
```

### Q: 한글이 깨져요
```python
# 노트북 첫 셀에 추가
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'  # Mac
# plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
plt.rcParams['axes.unicode_minus'] = False
```

### Q: 데이터 파일이 없어요
```bash
# practice-v11에서 복사
cp ../../practice-v11/sample_kamp_*.csv data/
```

---

## 🎉 다음 단계

Part 1-1 실습을 완료했다면:

1. **Part 1-2**: AI Hub 비전 데이터 분석
2. **Part 2-1**: 예지보전 (진동 데이터 분석)
3. **Part 2-2**: 생산최적화 (ViT, YOLOv8)
4. **Part 3-1**: 에이전틱 AI (한국어 LLM, RAG)

---

*제조AI 교육 v12 Enhanced | Part 1-1 | 2025.02*
