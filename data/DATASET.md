# Part 1-1 데이터셋 설명

## 개요
AI 기반 제조 품질 예측을 위한 CNC 가공 및 설비 진동 데이터.

## 포함 샘플 파일

| 파일 | 크기 | 행 수 | 설명 |
|------|------|-------|------|
| `sample_kamp_cnc.csv` | ~200KB | 1,000 | CNC 가공 품질 데이터 (합성) |
| `sample_kamp_vibration.csv` | ~1.5MB | 10,000 | 설비 진동 센서 데이터 (합성) |

## sample_kamp_cnc.csv 컬럼

| 컬럼 | 타입 | 설명 |
|------|------|------|
| 가공일시 | datetime | 가공 시작 시각 |
| 설비ID | str | CNC 장비 식별자 (CNC-001~003) |
| 작업자ID | str | 작업자 식별자 |
| 공구번호 | int | 사용 공구 번호 |
| 스핀들속도_RPM | float | 주축 회전수 |
| 이송속도_mm_min | float | 가공 이송 속도 |
| 절삭깊이_mm | float | 절삭 깊이 |
| 가공시간_sec | float | 총 가공 시간 |
| 진동_X/Y/Z_mm_s | float | 3축 진동 값 |
| 온도_C | float | 장비 온도 |
| 전류_A | float | 소비 전류 |
| 표면조도_Ra | float | 가공 표면 조도 |
| 치수오차_mm | float | 가공 치수 오차 |
| 품질판정 | str | OK / NG |

## sample_kamp_vibration.csv 컬럼

| 컬럼 | 타입 | 설명 |
|------|------|------|
| 측정시간 | datetime | 센서 측정 시각 |
| 설비ID | str | 설비 식별자 (MOTOR, PUMP, FAN 등) |
| 센서위치 | str | Housing, DE_Bearing, NDE_Bearing |
| RMS_velocity_mm_s | float | 진동 속도 RMS |
| Peak_acceleration_g | float | 최대 가속도 |
| Kurtosis | float | 첨도 (베어링 손상 지표) |
| Crest_factor | float | 파고율 |
| 온도_C | float | 베어링/하우징 온도 |
| RPM | float | 회전수 |
| 상태 | str | 정상 / 주의 / 경고 / 위험 |

## KAMP 원본 데이터셋 (전체)

**출처**: [KAMP (Korea AI Manufacturing Platform)](https://www.kamp-ai.kr/)

### CNC 가공 데이터
- **데이터셋명**: CNC 공구마모 예측 데이터
- **전체 규모**: ~50만 행, ~200MB
- **수집 주기**: 1초 / 1분 단위
- **포함 항목**: 가공 조건, 센서 데이터, 공구 마모량, 품질 검사 결과

### 진동 센서 데이터
- **데이터셋명**: 설비 진동 데이터 (PHM 2012 기반 확장)
- **전체 규모**: ~100만 행, ~500MB
- **수집 주기**: 1초 / 10ms 단위 (고속 진동)
- **포함 항목**: 3축 가속도, 속도, 온도, 베어링 상태 레이블

### 다운로드 방법
1. https://www.kamp-ai.kr/ 접속
2. 회원가입 및 데이터 이용 신청
3. CNC / 진동 데이터셋 선택 후 다운로드
4. 다운로드 파일을 `../../dataset/part1-1/` 경로에 배치

> 노트북은 KAMP 실데이터가 없으면 자동으로 이 샘플 파일을 사용합니다 (dual-path 로딩).
