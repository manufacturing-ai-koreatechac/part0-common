# Part0: 공통기반 (4세션, 8시간)

> **[v1.6.15]** KOREATECH 제조AI 실무 교육과정 — 공통 필수과정

## 학습 목표

- ML 핵심 개념: 지도·비지도·강화학습 이해
- Jupyter + Pandas + Matplotlib 실습환경 구축
- KAMP 공공 제조 데이터 탐색 및 EDA
- PyCaret AutoML로 모델 선택·튜닝·평가
- 딥러닝 아키텍처 이해 (CNN·LSTM·Transformer 개요)

## 세션 구성

| 세션 | 내용 | 소요 시간 |
|:----:|------|:---------:|
| S1 | ML 개론 — 제조AI 전체 그림 | 2h |
| S2 | 도구·EDA — 데이터 이해 실습 | 2h |
| S3 | AutoML·평가 — PyCaret 실습 | 2h |
| S4 | 아키텍처 — CNN·LSTM·Transformer | 2h |

**총 소요 시간**: 8시간

## 노트북 구성

| 파일 | 내용 | 세션 |
|------|------|:----:|
| 01_kamp_data_exploration.ipynb | KAMP 데이터 탐색·EDA | S1~S2 |
| 02_pycaret_automl.ipynb | AutoML 모델 선택·평가 | S3 |
| 03_architecture_overview.ipynb | CNN·LSTM·Transformer 개요 | S4 |

> **v1.6.15 변경**: SHAP Explainer는 기초 범위 초과로 제거됨. Track A/B 심화에서 다룸.

## 데이터셋

- KAMP id=1~5: 스마트제조 공공 데이터
- sample_kamp_cnc.csv — CNC 공정 데이터 샘플
- sample_kamp_vibration.csv — 설비 진동 데이터 샘플

## 시작하기

pip install pycaret pandas matplotlib seaborn jupyter

## 다음 단계

- 설비지능화 → Track A-1: https://github.com/manufacturing-ai-koreatechac/track-a1-vibration-fft
- 품질검사AI → Track B-1: https://github.com/manufacturing-ai-koreatechac/track-b1-cnn-transfer

---
KOREATECH 제조AI 실무 교육과정 v1.6.15 | 2026-03-04
