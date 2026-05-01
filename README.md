# Nano_related

**Languages:** Korean (한국어) first · English below.

---

## Korean (한국어)

NANO 대학원(나노과학 전공 및 관련 과정) 학습·연구 참고 자료를 모아두는 저장소입니다. 반도체 공정 이해, 에칭 장비용 정전 초크(ESC) 등 주제별로 차시별 디렉터리로 정리합니다.

### 디렉터리 구조

```
.
+-- README.md
+-- .gitignore
+-- tools/           # (선택) 유틸 스크립트
+-- day1/            # 1차 수집·정리 자료
|   +-- (반도체 개론·공정 비교 문서 및 템플릿)
|   +-- (ESC 논문·요약 자료)
|   +-- ...
`-- day2/            # 2차 — 견적서·플롯·논문 처리 등 워크스페이스
    +-- 1quotation/      견적서 생성 스크립트(JS/Python) 및 샘플 출력
    +-- 2plot/           matplotlib 예제 및 PDF 출력
    +-- 3quotation_re/   견적서 재작업 산출물
    +-- 4paper/          논문 PDF, 텍스트 추출·DOCX 생성 스크립트
    +-- .claude/          Claude Code 에이전트·스킬(로컬 설정 포함 가능)
    +-- (루트: Claude.md, DESIGN-apple.md, Install.docx, todo.txt 등)
```

**`day3/`** 폴더는 로컬 전용으로 두고 싶은 작업물을 위해 **Git에서 제외**되어 있습니다 (`.gitignore`). 원격 저장소에는 올라가지 않습니다.

### day1 포함 자료

| 파일 | 설명 |
|------|------|
| `cd00003986-introduction-to-semiconductor-technology-stmicroelectronics.pdf` | ST 마이크로일렉트로닉스 반도체 기술 입문 자료 |
| `Thermal_and_Electrical_Analysis_of_the_Electrostatic_Chuck_for_the_Etch_Equipment.pdf` | 에칭 장비용 정전 척(Electrostatic Chuck) 열·전기 특성 분석 논문 |
| `ESC_paper_summary.docx` | ESC 논문 요약 |
| `ESC_pros_cons_apple.pptx` | ESC 장단점 정리 발표 자료 |
| `CVD_PVD_ALD_comparison.xlsx` | CVD / PVD / ALD 공정 비교 |
| `semiconductor_intro_bilingual.docx` | 반도체 소개(이중언어) |
| `semiconductor_lab_notebook_template.docx` | 실험 노트 템플릿 |
| `business_meeting_emails.docx` | 비즈니스 미팅 이메일 예시 |
| `Claude_계약학과_반도체_세미나.pdf` | Claude 계약학과 반도체 세미나 관련 자료 |

> 로컬 OS 인코딩에 따라 파일명이 다르게 보일 수 있습니다. 최신 목록은 이 저장소의 파일 트리를 확인하세요.

### day2 요약

| 영역 | 내용 |
|------|------|
| `1quotation/` | `make_docx.js`, `make_xlsx.py` 등 견적서 자동화 및 `.xlsx`/`.docx` 샘플 |
| `2plot/` | `plot_random.py`, `histogram.pdf` |
| `3quotation_re/` | 견적서 재생성 관련 문서 |
| `4paper/` | `data/` 원본 PDF, `output/`에서 텍스트 추출·`make_00x.py`로 DOCX 생성 |
| 기타 | `Claude.md`, `DESIGN-apple.md`, 계약학과 2회차 PDF, 설치 안내 등 |

### 사용 방법

1. 저장소 클론:

   ```bash
   git clone https://github.com/BogKim2/Nano_related.git
   ```

2. `day1`, `day2` 폴더에서 PDF·문서·스크립트를 이용합니다.

3. 대용량 바이너리가 많아지면 [Git LFS](https://git-lfs.com/) 사용을 검토합니다.

### 저작권

각 파일은 해당 저작·이용 조건을 따릅니다. 외부 재배포 또는 2차 이용 시 원문·출처를 확인하세요.

### 문의·기여

개인 학습용 정리 저장소입니다. 수정 제안은 Issue 또는 Pull Request로 알려 주세요.

*초기 작성: 2026년 4월 · README 갱신: 2026년 5월*

---

## English

Study and reference materials for the **NANO graduate program** (nano-related science and coursework). Topics include semiconductor processes and the electrostatic chuck (ESC) for etch tools, organized under dated/session folders (`day1`, `day2`).

### Repository layout

```
.
+-- README.md
+-- .gitignore
+-- tools/
+-- day1/          # First batch — collected & organized
|   +-- (Introduction, process comparison, templates)
|   +-- (ESC papers and summaries)
|   +-- ...
`-- day2/          # Second batch — quotations, plotting, paper tooling
    +-- 1quotation/    Scripts (JS/Python) + sample spreadsheets/documents
    +-- 2plot/         matplotlib script + PDF export
    +-- 3quotation_re/ Regenerated quotation outputs
    +-- 4paper/        Source PDFs, extraction text, DOCX builders
    +-- .claude/       Claude Code agents/skills (may include local settings)
    +-- (root notes: Claude.md, DESIGN-apple.md, Install.docx, todo.txt, …)
```

The **`day3/`** directory is **ignored by Git** (see `.gitignore`) and is kept for **local-only** work; it is **not** pushed to GitHub.

### Contents of `day1`

| File | Description |
|------|-------------|
| `cd00003986-introduction-to-semiconductor-technology-stmicroelectronics.pdf` | ST Microelectronics — introduction to semiconductor technology |
| `Thermal_and_Electrical_Analysis_of_the_Electrostatic_Chuck_for_the_Etch_Equipment.pdf` | Thermal & electrical analysis of ESC for etch equipment |
| `ESC_paper_summary.docx` | Summary of the ESC paper |
| `ESC_pros_cons_apple.pptx` | Pros/cons presentation on ESC |
| `CVD_PVD_ALD_comparison.xlsx` | CVD / PVD / ALD comparison |
| `semiconductor_intro_bilingual.docx` | Bilingual semiconductor introduction |
| `semiconductor_lab_notebook_template.docx` | Lab notebook template |
| `business_meeting_emails.docx` | Sample business-meeting emails |
| `Claude_계약학과_반도체_세미나.pdf` | Contract-track semiconductor seminar (Claude-related); UTF-8 filename as shown |

> On some systems, file names may display differently. The **GitHub repository file tree** is the source of truth.

### `day2` overview

| Area | Contents |
|------|----------|
| `1quotation/` | Quotation automation (`make_docx.js`, `make_xlsx.py`, variants) and sample `.xlsx`/`.docx` |
| `2plot/` | `plot_random.py`, `histogram.pdf` |
| `3quotation_re/` | Revised quotation documents |
| `4paper/` | PDFs under `data/`, scripts under `output/` (`make_00x.py`) producing DOCX |
| Misc | `Claude.md`, `DESIGN-apple.md`, contract-course PDFs, install notes |

### Usage

1. Clone:

   ```bash
   git clone https://github.com/BogKim2/Nano_related.git
   ```

2. Open materials under `day1` and `day2`.

3. Consider [Git LFS](https://git-lfs.com/) if binary assets grow large.

### Copyright

Each document follows its original license and terms. Verify the source before redistributing or reusing content.

### Contact & contributions

Personal study repository. Suggestions welcome via Issues or Pull Requests.

*First revision: April 2026 · README update: May 2026*

<!-- Regenerate UTF-8: python tools/generate_readme.py -->
