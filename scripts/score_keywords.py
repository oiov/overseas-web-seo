#!/usr/bin/env python3
"""Score candidate keywords with kdroi, KGR and Trends-based volume estimates.

CSV columns (only `keyword` is required; leave unknown cells empty):
  keyword, volume (monthly), kd, cpc, intitle, trends_ratio
"""

import argparse
import csv
import sys


def parse_number(value):
    if value is None:
        return None
    text = value.strip().replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def format_number(value, digits=0):
    if value is None:
        return "-"
    if digits == 0:
        return f"{value:,.0f}"
    return f"{value:,.{digits}f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path")
    parser.add_argument(
        "--benchmark-daily",
        type=float,
        default=None,
        help="Calibrated daily searches of the Trends benchmark keyword (e.g. GPTs). Enables volume estimates from trends_ratio.",
    )
    parser.add_argument("--sort", choices=["kdroi", "kgr", "volume"], default="kdroi")
    args = parser.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))

    if not rows or "keyword" not in rows[0]:
        sys.exit("CSV must have a header row with at least a `keyword` column.")

    results = []
    for row in rows:
        volume = parse_number(row.get("volume"))
        estimated = False
        trends_ratio = parse_number(row.get("trends_ratio"))
        if volume is None and trends_ratio is not None and args.benchmark_daily:
            volume = trends_ratio * args.benchmark_daily * 30
            estimated = True

        kd = parse_number(row.get("kd"))
        cpc = parse_number(row.get("cpc"))
        intitle = parse_number(row.get("intitle"))

        kdroi = None
        if volume is not None and cpc is not None and kd is not None:
            kdroi = volume * cpc / max(kd, 1)

        kgr = None
        if volume and intitle is not None:
            kgr = intitle / volume

        results.append(
            {
                "keyword": row["keyword"].strip(),
                "volume": volume,
                "estimated": estimated,
                "kd": kd,
                "cpc": cpc,
                "kdroi": kdroi,
                "kgr": kgr,
            }
        )

    if args.sort == "kgr":
        results.sort(key=lambda item: (item["kgr"] is None, item["kgr"] or 0))
    else:
        results.sort(key=lambda item: (item[args.sort] is None, -(item[args.sort] or 0)))

    print("| Keyword | Monthly volume | KD | CPC | kdroi | KGR | KGR < 0.25 |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for item in results:
        volume_text = format_number(item["volume"])
        if item["estimated"]:
            volume_text += " (est.)"
        kgr_flag = "-" if item["kgr"] is None else ("yes" if item["kgr"] < 0.25 else "no")
        print(
            f"| {item['keyword']} | {volume_text} | {format_number(item['kd'])} | "
            f"{format_number(item['cpc'], 2)} | {format_number(item['kdroi'], 1)} | "
            f"{format_number(item['kgr'], 4)} | {kgr_flag} |"
        )

    if any(item["estimated"] for item in results):
        print(
            f"\n(est.) = trends_ratio x {args.benchmark_daily:,.0f}/day x 30; order-of-magnitude only. "
            "Original KGR rule targets keywords under 250 monthly searches."
        )


if __name__ == "__main__":
    main()
