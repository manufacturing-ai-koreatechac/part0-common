"""
viz_utils.py — 제조 AI 교육 공통 시각화 유틸리티
================================================
모든 트랙(Part0, A-1, A-2, B-1, B-2, X1)에서 공통으로 사용하는
표준화된 시각화 함수 모음.

사용법:
    import sys; sys.path.append('../../part0-common')
    from utils.viz_utils import setup_korean_font, plot_manufacturing_result

색상 정책: Okabe-Ito 색맹 친화 팔레트 기본 적용
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import platform


# ============================================================
# 색상 팔레트 (Okabe-Ito 색맹 친화)
# ============================================================
COLORS = {
    'normal':   '#0072B2',  # 파랑   — 정상/정답
    'fault':    '#D55E00',  # 주황   — 결함/오답/경보
    'warning':  '#E69F00',  # 노랑   — 경고/임계값
    'positive': '#009E73',  # 초록   — 합격/양호
    'negative': '#CC79A7',  # 분홍   — 불합격
    'neutral':  '#56B4E9',  # 하늘   — 중립/스펙트럼
    'gray':     '#999999',  # 회색   — 배경/보조
    'black':    '#333333',  # 진회색 — 텍스트
}

# 순서 있는 팔레트 리스트
PALETTE = list(COLORS.values())


# ============================================================
# 한글 폰트 자동 설정
# ============================================================
def setup_korean_font(dpi: int = 100, figsize: tuple = (12, 5)) -> dict:
    """
    OS/환경별 한글 폰트 자동 설정 및 공통 rcParams 적용.

    Args:
        dpi:     figure DPI (기본 100)
        figsize: 기본 figure 크기

    Returns:
        COLORS dict (색맹 친화 팔레트)

    Example:
        from utils.viz_utils import setup_korean_font, COLORS
        COLORS = setup_korean_font()
    """
    system = platform.system()

    # Google Colab 감지
    in_colab = False
    try:
        import google.colab
        in_colab = True
    except ImportError:
        pass

    if in_colab:
        import subprocess
        subprocess.run(['apt-get', 'install', '-y', 'fonts-nanum'], capture_output=True)
        fm._load_fontmanager(try_read_cache=False)
        plt.rcParams['font.family'] = 'NanumGothic'
        print("✅ 한글 폰트: NanumGothic (Colab)")

    elif system == 'Darwin':
        candidates = ['AppleGothic', 'Apple SD Gothic Neo', 'Noto Sans KR']
        for font in candidates:
            if any(f.name == font for f in fm.fontManager.ttflist):
                plt.rcParams['font.family'] = font
                print(f"✅ 한글 폰트: {font} (macOS)")
                break

    elif system == 'Linux':
        nanum = [f for f in fm.fontManager.ttflist if 'Nanum' in f.name]
        if nanum:
            plt.rcParams['font.family'] = 'NanumGothic'
            print("✅ 한글 폰트: NanumGothic (Linux)")
        else:
            print("⚠️ NanumGothic 미설치. 다음 명령으로 설치하세요:")
            print("   sudo apt-get install -y fonts-nanum && fc-cache -fv")
            plt.rcParams['font.family'] = 'DejaVu Sans'

    elif system == 'Windows':
        for font in ['Malgun Gothic', '맑은 고딕', 'NanumGothic']:
            if any(f.name == font for f in fm.fontManager.ttflist):
                plt.rcParams['font.family'] = font
                print(f"✅ 한글 폰트: {font} (Windows)")
                break

    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.dpi']         = dpi
    plt.rcParams['figure.figsize']     = list(figsize)
    plt.rcParams['axes.spines.top']    = False
    plt.rcParams['axes.spines.right']  = False

    return COLORS


# ============================================================
# 표준 시각화 함수
# ============================================================
def plot_manufacturing_result(
    data_dict: dict,
    plot_type: str = 'bar',
    title: str = '결과',
    xlabel: str = '',
    ylabel: str = '',
    figsize: tuple = (12, 5),
    colors: list = None,
    threshold_lines: list = None,
    anomaly_indices: list = None,
    show_values: bool = True,
    save_path: str = None,
) -> tuple:
    """
    제조 AI 교육 표준 시각화 함수

    Args:
        data_dict:        {'레이블': 값} 또는 {'x': [...], 'y': [...]}
        plot_type:        'bar' | 'line' | 'scatter' | 'confusion'
        threshold_lines:  [{'y': float, 'label': str, 'color': str}]
        anomaly_indices:  이상치로 강조할 인덱스 리스트 (scatter용)
        show_values:      bar 차트에서 값 레이블 표시 여부
        save_path:        저장 경로 (None이면 저장 안 함)

    Returns:
        (fig, ax) 튜플

    Examples:
        # F1-Score 바 차트
        plot_manufacturing_result(
            {'정상': 0.98, '스크래치': 0.91, '오염': 0.87},
            plot_type='bar', title='클래스별 F1-Score', ylabel='F1',
            threshold_lines=[{'y': 0.90, 'label': '합격 기준', 'color': '#D55E00'}]
        )

        # 시계열 라인 차트
        plot_manufacturing_result(
            {'x': range(100), '정상': rms_vals, '이상': anomaly_score},
            plot_type='line', title='RMS 트렌드', xlabel='시간 (s)', ylabel='RMS'
        )

        # 혼동 행렬
        plot_manufacturing_result(
            {'matrix': cm, 'class_names': ['정상', '불량']},
            plot_type='confusion', title='혼동 행렬'
        )
    """
    if colors is None:
        colors = PALETTE

    fig, ax = plt.subplots(figsize=figsize)

    # ── bar ──────────────────────────────────────
    if plot_type == 'bar':
        labels = list(data_dict.keys())
        values = list(data_dict.values())
        bar_colors = [colors[i % len(colors)] for i in range(len(labels))]
        bars = ax.bar(labels, values, color=bar_colors, alpha=0.85,
                      edgecolor='white', linewidth=1.5)

        if show_values:
            for bar, val in zip(bars, values):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + max(values) * 0.01,
                    f'{val:.3f}' if isinstance(val, float) else str(val),
                    ha='center', va='bottom', fontsize=9, fontweight='bold'
                )
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=30, ha='right')
        ax.set_ylim(0, max(values) * 1.18)

    # ── line ──────────────────────────────────────
    elif plot_type == 'line':
        x_vals = data_dict.get('x', None)
        c_idx = 0
        for key, y_vals in data_dict.items():
            if key == 'x':
                continue
            xs = x_vals if x_vals is not None else range(len(y_vals))
            ax.plot(xs, y_vals, color=colors[c_idx % len(colors)],
                    linewidth=2, label=key, marker='o', markersize=3, alpha=0.85)
            c_idx += 1
        ax.legend(framealpha=0.9)

    # ── scatter ───────────────────────────────────
    elif plot_type == 'scatter':
        x, y = data_dict['x'], data_dict['y']
        c = [colors[1] if (anomaly_indices and i in anomaly_indices) else colors[0]
             for i in range(len(x))]
        ax.scatter(x, y, c=c, alpha=0.7, s=35)
        if anomaly_indices:
            ax.scatter(
                [x[i] for i in anomaly_indices],
                [y[i] for i in anomaly_indices],
                c=COLORS['fault'], s=90, marker='x', linewidth=2.5,
                label=f'이상치 ({len(anomaly_indices)}개)', zorder=5
            )
            ax.legend()

    # ── confusion matrix ──────────────────────────
    elif plot_type == 'confusion':
        try:
            import seaborn as sns
        except ImportError:
            print("⚠️ seaborn 미설치. pip install seaborn")
            return fig, ax

        matrix = np.array(data_dict['matrix'])
        class_names = data_dict.get(
            'class_names', [str(i) for i in range(len(matrix))]
        )
        # 행 정규화
        row_sum = matrix.sum(axis=1, keepdims=True) + 1e-8
        matrix_norm = matrix.astype('float') / row_sum
        # 셀 주석: "수치\n(비율%)"
        annot = np.array([
            [f'{matrix[i,j]}\n({matrix_norm[i,j]:.0%})'
             for j in range(matrix.shape[1])]
            for i in range(matrix.shape[0])
        ])
        sns.heatmap(
            matrix_norm, annot=annot, fmt='', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names,
            ax=ax, cbar_kws={'label': '비율 (행 정규화)'},
            linewidths=0.5, linecolor='white'
        )
        ax.set_xlabel('예측 클래스', fontsize=11)
        ax.set_ylabel('실제 클래스', fontsize=11)

    # ── 기준선 ────────────────────────────────────
    if threshold_lines:
        for tl in threshold_lines:
            ax.axhline(
                y=tl['y'], color=tl.get('color', COLORS['fault']),
                linestyle='--', linewidth=2, alpha=0.85,
                label=tl.get('label', f"기준: {tl['y']}")
            )
        ax.legend(loc='lower right', framealpha=0.9)

    ax.set_title(title, fontsize=13, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11)
    ax.grid(alpha=0.3, axis='y' if plot_type == 'bar' else 'both')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✅ 저장: {save_path}")

    plt.show()
    return fig, ax


# ============================================================
# 제조 AI 특화 시각화
# ============================================================
def plot_anomaly_timeline(
    timestamps, scores, threshold: float,
    title: str = '이상 탐지 타임라인',
    xlabel: str = '시간', ylabel: str = '이상 점수',
    figsize: tuple = (14, 5),
) -> tuple:
    """
    시계열 이상 점수 + 임계값 + 이상 구간 강조 플롯

    Args:
        timestamps: 시간 축 값 배열
        scores:     이상 점수 배열
        threshold:  이상 판단 임계값

    Example:
        plot_anomaly_timeline(
            timestamps=df['time'], scores=recon_errors,
            threshold=0.05, title='AutoEncoder 재구성 오차'
        )
    """
    fig, ax = plt.subplots(figsize=figsize)

    # 정상/이상 구분 색상
    is_anomaly = np.array(scores) > threshold
    ax.fill_between(timestamps, scores, threshold,
                    where=is_anomaly,
                    alpha=0.35, color=COLORS['fault'], label='이상 구간')
    ax.plot(timestamps, scores, linewidth=1.2,
            color=COLORS['neutral'], label='이상 점수', zorder=3)
    ax.axhline(y=threshold, color=COLORS['warning'], linestyle='--',
               linewidth=2, label=f'임계값: {threshold:.4f}')

    n_anomaly = is_anomaly.sum()
    ax.set_title(f'{title}\n(이상 탐지: {n_anomaly}건 / 전체 {len(scores)}건)',
                 fontsize=13, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.legend(framealpha=0.9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    return fig, ax


def plot_rul_prediction(
    actual_rul, predicted_rul,
    maintenance_threshold: int = 30,
    title: str = 'RUL 예측 vs 실제',
    figsize: tuple = (12, 5),
) -> tuple:
    """
    RUL(잔여 수명) 예측값 vs 실제값 비교 플롯

    Args:
        actual_rul:           실제 RUL 배열
        predicted_rul:        예측 RUL 배열
        maintenance_threshold: 정비 권고 기준 (기본 30 사이클)

    Example:
        plot_rul_prediction(y_test, y_pred, maintenance_threshold=30)
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # 왼쪽: 예측 vs 실제 산점도
    ax1 = axes[0]
    max_val = max(max(actual_rul), max(predicted_rul)) * 1.05
    ax1.scatter(actual_rul, predicted_rul,
                alpha=0.5, s=25, color=COLORS['neutral'])
    ax1.plot([0, max_val], [0, max_val],
             color=COLORS['fault'], linestyle='--', linewidth=2,
             label='이상적 예측 (y=x)')
    ax1.axhline(y=maintenance_threshold, color=COLORS['warning'],
                linestyle=':', linewidth=1.5,
                label=f'정비 기준: {maintenance_threshold}')
    ax1.axvline(x=maintenance_threshold, color=COLORS['warning'],
                linestyle=':', linewidth=1.5)
    ax1.set_title('예측 vs 실제 RUL', fontsize=11, fontweight='bold')
    ax1.set_xlabel('실제 RUL (사이클)', fontsize=10)
    ax1.set_ylabel('예측 RUL (사이클)', fontsize=10)
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.3)

    # 오른쪽: 오차 분포 히스토그램
    ax2 = axes[1]
    errors = np.array(predicted_rul) - np.array(actual_rul)
    ax2.hist(errors, bins=30, color=COLORS['neutral'],
             edgecolor='white', alpha=0.85)
    ax2.axvline(x=0, color=COLORS['fault'], linestyle='--',
                linewidth=2, label='오차=0 (완벽한 예측)')
    ax2.axvline(x=errors.mean(), color=COLORS['warning'],
                linestyle='--', linewidth=1.5,
                label=f'평균 오차: {errors.mean():.1f}')
    ax2.set_title('예측 오차 분포', fontsize=11, fontweight='bold')
    ax2.set_xlabel('예측 오차 (예측 - 실제)', fontsize=10)
    ax2.set_ylabel('빈도', fontsize=10)
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3)

    mae  = np.mean(np.abs(errors))
    rmse = np.sqrt(np.mean(errors**2))
    plt.suptitle(f'{title}  |  MAE: {mae:.1f}  RMSE: {rmse:.1f}',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()
    return fig, axes
