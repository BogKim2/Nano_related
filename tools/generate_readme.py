# -*- coding: utf-8 -*-
"""ASCII-only source: rebuilds README.md as UTF-8 (avoids editor mangling Hangul)."""
from pathlib import Path

def main() -> None:
    p: list[str] = []
    a = p.append
    root = Path(__file__).resolve().parents[1]
    readme = root / "README.md"

    a("# Nano_related\n\n")
    a("**Languages:** Korean (\uD55C\uAD6D\uC5B4) first \u00B7 English below.\n\n")
    a("---\n\n")
    a("## Korean (\uD55C\uAD6D\uC5B4)\n\n")

    a(
        "NANO \uB300\uD559\uC6D0(\uB098\uB178\uACFC\uD559 "
        "\uC804\uACF5 \uBC0F \uAD00\uB828 "
        "\uACFC\uC815) \uD559\uC2B5\u00B7\uC5F0\uAD6C \uCC38\uACE0 "
        "\uC790\uB8CC\uB97C \uBAA8\uC544\uB450\uB294 "
        "\uC800\uC7A5\uC18C\uC785\uB2C8\uB2E4. "
        "\uBC18\uB3C4\uCCB4 \uACF5\uC815 \uC774\uD574, "
        "\uC5D0\uCE6D \uC7A5\uBE44\uC6A9 "
        "\uC815\uC804 \uCD08\uD074(ESC) \uB4F1 "
        "\uC8FC\uC81C\uBCC4\uB85C \uCC28\uC2DC\uBCC4 "
        "\uB514\uB809\uD130\uB9AC\uB85C \uC815\uB9AC\uD569\uB2C8\uB2E4.\n\n"
    )

    a("### \uB514\uB809\uD130\uB9AC \uAD6C\uC870\n\n")
    a("```\n")
    a(".\n")
    a("+-- README.md\n")
    a("`-- day1/          # 1\uCC28 \uC218\uC9D1\u00B7\uC815\uB9AC \uC790\uB8CC\n")
    a("    +-- (\uBC18\uB3C4\uCCB4 \uAC1C\uB860\u00B7\uACF5\uC815 \uBE44\uAD50 \uBB38\uC11C \uBC0F \uD15C\uD50C\uB9BF)\n")
    a("    +-- (ESC \uB17C\uBB38\u00B7\uC694\uC57D \uC790\uB8CC)\n")
    a("    +-- ...\n")
    a("```\n\n")

    a("### day1 \uD3EC\uD568 \uC790\uB8CC\n\n")
    a("| \uD30C\uC77C | \uC124\uBA85 |\n")
    a("|------|------|\n")
    r1 = "`cd00003986-introduction-to-semiconductor-technology-stmicroelectronics.pdf`"
    a(f"| {r1} | ST \uB9C8\uC774\uD06C\uB85C\uC77C\uB809\uD2B8\uB85C\uB2C9\uC2A4 \uBC18\uB3C4\uCCB4 \uAE30\uC220 \uC785\uBB38 \uC790\uB8CC |\n")
    r2 = "`Thermal_and_Electrical_Analysis_of_the_Electrostatic_Chuck_for_the_Etch_Equipment.pdf`"
    a(f"| {r2} | ")
    a("\uC5D0\uCE6D \uC7A5\uBE44\uC6A9 \uC815\uC804 \uCC99(Electrostatic Chuck) ")
    a("\uC5F4\u00B7\uC804\uAE30 \uD2B9\uC131 \uBD84\uC11D \uB17C\uBB38 |\n")
    a("| `ESC_paper_summary.docx` | ESC \uB17C\uBB38 \uC694\uC57D |\n")
    a("| `ESC_pros_cons_apple.pptx` | ESC \uC7A5\uB2E8\uC810 \uC815\uB9AC \uBC1C\uD45C \uC790\uB8CC |\n")
    a("| `CVD_PVD_ALD_comparison.xlsx` | CVD / PVD / ALD \uACF5\uC815 \uBE44\uAD50 |\n")
    a("| `semiconductor_intro_bilingual.docx` | ")
    a("\uBC18\uB3C4\uCCB4 \uC18C\uAC1C(\uC774\uC911\uC5B8\uC5B4) |\n")
    a("| `semiconductor_lab_notebook_template.docx` | \uC2E4\uD5D8 \uB178\uD2B8 \uD15C\uD50C\uB9BF |\n")
    a("| `business_meeting_emails.docx` | ")
    a("\uBE44\uC988\uB2C8\uC2A4 \uBBF8\uD305 \uC774\uBA54\uC77C \uC608\uC2DC |\n")
    a("| `Claude_\uACC4\uC57D\uD559\uACFC_\uBC18\uB3C4\uCCB4_\uC138\uBBF8\uB098.pdf` | ")
    a("Claude \uACC4\uC57D\uD559\uACFC \uBC18\uB3C4\uCCB4 \uC138\uBBF8\uB098 \uAD00\uB828 \uC790\uB8CC |\n\n")

    a("> \uB85C\uCEEC OS \uC778\uCF54\uB529\uC5D0 \uB530\uB77C \uD30C\uC77C\uBA85\uC774 ")
    a("\uB2E4\uB974\uAC8C \uBCF4\uC77C \uC218 \uC788\uC2B5\uB2C8\uB2E4. ")
    a("\uCD5C\uC2E0 \uBAA9\uB85D\uC740 \uC774 \uC800\uC7A5\uC18C\uC758 \uD30C\uC77C ")
    a("\uD2B8\uB9AC\uB97C \uD655\uC778\uD558\uC138\uC694.\n\n")

    a("### day2 (\uC608\uC815)\n\n")
    a("\uCD94\uAC00 \uD559\uC2B5\u00B7\uC2E4\uD5D8\u00B7\uACFC\uC81C ")
    a("\uC790\uB8CC\uB294 `day2` \uD3F4\uB354\uB97C \uB9CC\uB4E4\uC5B4 ")
    a("\uAC19\uC740 \uBC29\uC2DD\uC73C\uB85C \uC815\uB9AC\uD560 \uC608\uC815\uC785\uB2C8\uB2E4. ")
    a("\uB514\uB809\uD1A0\uB9AC\uAC00 \uCD94\uAC00\uB418\uBA74 \uC774 README\uB3C4 ")
    a("\uD568\uAED8 \uAC31\uC2E0\uD569\uB2C8\uB2E4.\n\n")

    a("### \uC0AC\uC6A9 \uBC29\uBC95\n\n")
    a("1. \uC800\uC7A5\uC18C \uD074\uB860:\n\n")
    a("   ```bash\n")
    a("   git clone https://github.com/BogKim2/Nano_related.git\n")
    a("   ```\n\n")
    a("2. `day1`(\uC774\uD6C4 `day2` \uD3EC\uD568) \uD3F4\uB354\uC5D0\uC11C PDF \uBC0F ")
    a("\uBB38\uC11C\uB97C \uC774\uC6A9\uD569\uB2C8\uB2E4.\n\n")
    a("3. \uB300\uC6A9\uB7C9 \uBC14\uC774\uB108\uB9AC\uAC00 \uB9CE\uC544\uC9C0\uBA74 ")
    a("[Git LFS](https://git-lfs.com/) \uC0AC\uC6A9\uC744 \uAC80\uD1A0\uD569\uB2C8\uB2E4.\n\n")

    a("### \uC800\uC791\uAD8C\n\n")
    a("\uAC01 \uD30C\uC77C\uC740 \uD574\uB2F9 \uC800\uC791\u00B7\uC774\uC6A9 ")
    a("\uC870\uAC74\uC744 \uB530\uB985\uB2C8\uB2E4. ")
    a("\uC678\uBD80 \uC7AC\uBC30\uD3EC \uB610\uB294 2\uCC28 \uC774\uC6A9 \uC2DC ")
    a("\uC6D0\uBB38\u00B7\uCD9C\uCC98\uB97C \uD655\uC778\uD558\uC138\uC694.\n\n")

    a("### \uBB38\uC758\u00B7\uAE30\uC5EC\n\n")
    a("\uAC1C\uC778 \uD559\uC2B5\uC6A9 \uC815\uB9AC \uC800\uC7A5\uC18C\uC785\uB2C8\uB2E4. ")
    a("\uC218\uC815 \uC81C\uC548\uC740 Issue \uB610\uB294 Pull Request\uB85C ")
    a("\uC54C\uB824 \uC8FC\uC138\uC694.\n\n")

    a("*\uCD08\uAE30 \uC791\uC131: 2026\uB144 4\uC6D4*\n\n")

    a("---\n\n")
    a("## English\n\n")

    a(
        "Study and reference materials for the **NANO graduate program** "
        "(nano-related science and coursework). Topics include semiconductor "
        "processes and the electrostatic chuck (ESC) for etch tools, organized "
        "under dated/session folders (`day1`, and **`day2` planned**).\n\n"
    )

    a("### Repository layout\n\n")
    a("```\n")
    a(".\n")
    a("+-- README.md\n")
    a("`-- day1/          # First batch \u2014 collected & organized\n")
    a("    +-- (Introduction, process comparison, templates)\n")
    a("    +-- (ESC papers and summaries)\n")
    a("    +-- ...\n")
    a("```\n\n")

    a("### Contents of `day1`\n\n")
    a("| File | Description |\n")
    a("|------|-------------|\n")
    a(
        "| `cd00003986-introduction-to-semiconductor-technology-stmicroelectronics.pdf` | "
        "ST Microelectronics \u2014 introduction to semiconductor technology |\n"
    )
    a(
        "| `Thermal_and_Electrical_Analysis_of_the_Electrostatic_Chuck_for_the_Etch_Equipment.pdf` | "
        "Thermal & electrical analysis of ESC for etch equipment |\n"
    )
    a("| `ESC_paper_summary.docx` | Summary of the ESC paper |\n")
    a("| `ESC_pros_cons_apple.pptx` | Pros/cons presentation on ESC |\n")
    a("| `CVD_PVD_ALD_comparison.xlsx` | CVD / PVD / ALD comparison |\n")
    a("| `semiconductor_intro_bilingual.docx` | Bilingual semiconductor introduction |\n")
    a("| `semiconductor_lab_notebook_template.docx` | Lab notebook template |\n")
    a("| `business_meeting_emails.docx` | Sample business-meeting emails |\n")
    a(
        "| `Claude_\uACC4\uC57D\uD559\uACFC_\uBC18\uB3C4\uCCB4_\uC138\uBBF8\uB098.pdf` | "
        "Contract-track semiconductor seminar (Claude-related); "
        "UTF-8 filename as shown |\n\n"
    )

    a(
        "> On some systems, file names may display differently. "
        "The **GitHub repository file tree** is the source of truth.\n\n"
    )

    a("### `day2` (planned)\n\n")
    a(
        "Additional readings, lab notes, and assignments will be placed in a "
        "**`day2`** directory using the same convention. "
        "This README will be updated when `day2` is added.\n\n"
    )

    a("### Usage\n\n")
    a("1. Clone:\n\n")
    a("   ```bash\n")
    a("   git clone https://github.com/BogKim2/Nano_related.git\n")
    a("   ```\n\n")
    a("2. Open materials under `day1` (and later `day2`).\n\n")
    a("3. Consider [Git LFS](https://git-lfs.com/) if binary assets grow large.\n\n")

    a("### Copyright\n\n")
    a(
        "Each document follows its original license and terms. "
        "Verify the source before redistributing or reusing content.\n\n"
    )

    a("### Contact & contributions\n\n")
    a("Personal study repository. Suggestions welcome via Issues or Pull Requests.\n\n")

    a("*First revision: April 2026*\n")
    a("\n<!-- Regenerate UTF-8: python tools/generate_readme.py -->\n")

    text = "".join(p)
    readme.write_text(text, encoding="utf-8", newline="\n")

    raw = readme.read_bytes()
    if b"\xed\x95\x9c" not in raw:
        raise SystemExit("verify failed: expected Hangul UTF-8 in output")
    print("Wrote", readme, "UTF-8 bytes:", len(raw))


if __name__ == "__main__":
    main()
