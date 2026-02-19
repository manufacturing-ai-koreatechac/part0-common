# 🚀 빠른 시작 가이드

Part 1-1 실습을 시작하기 위한 단계별 가이드입니다.

---

## ⏱️ 5분 안에 시작하기

### 1. 터미널 열기

**Mac**: `Cmd + Space` → "Terminal" 입력
**Windows**: `Win + R` → "cmd" 입력

### 2. 프로젝트 폴더로 이동

```bash
cd /Users/hongmartin/dev/korea_tech_ech_ppt_part_1-1/practice-v12-enhanced
```

### 3. 가상환경 생성 (처음 한 번만)

```bash
python -m venv venv
```

### 4. 가상환경 활성화

**Mac/Linux**:
```bash
source venv/bin/activate
```

**Windows**:
```bash
venv\Scripts\activate
```

### 5. 패키지 설치 (처음 한 번만)

```bash
pip install -r requirements.txt
```

⏳ **설치 시간**: 약 3-5분

### 6. Jupyter Lab 실행

```bash
cd part1-1
jupyter lab
```

🎉 **완료!** 브라우저가 자동으로 열립니다.

---

## 📚 실습 순서

1. `notebooks/01_kamp_data_exploration.ipynb` 열기
2. `Shift + Enter`로 셀을 하나씩 실행
3. 완료 후 `02_pycaret_automl.ipynb`로 이동
4. 마지막으로 `03_shap_explainer.ipynb` 실습

---

## 🆘 문제 발생 시

### Python이 없어요
```bash
# Mac
brew install python3

# Windows
# python.org에서 다운로드
```

### pip install이 실패해요
```bash
# pip 업그레이드
pip install --upgrade pip

# 다시 시도
pip install -r requirements.txt
```

### Jupyter Lab이 안 열려요
```bash
# 직접 브라우저에서 열기
jupyter lab --no-browser
# 출력된 URL을 복사하여 브라우저에 붙여넣기
```

### 한글이 깨져요
```python
# 노트북 첫 셀에 추가
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'  # Mac
# plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
```

---

## 💡 유용한 명령어

### 가상환경 종료
```bash
deactivate
```

### Jupyter Lab 종료
`Ctrl + C` (터미널에서) → `y` → `Enter`

### 패키지 재설치
```bash
pip install -r requirements.txt --force-reinstall
```

---

## 📖 더 알아보기

- [Jupyter Lab 가이드](https://jupyterlab.readthedocs.io/)
- [Python 가상환경](https://docs.python.org/3/tutorial/venv.html)
- [Part 1-1 README](../README.md)

---

*제조AI 교육 v12 Enhanced | 2025.02*
