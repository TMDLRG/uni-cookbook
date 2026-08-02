# -*- coding: utf-8 -*-
"""Falsifier for PL-08's geometry, run BEFORE the plate is drawn.

Every number PL-08 draws is either (a) printed in the corpus, or (b) computed here
from constants printed in the corpus. This script checks that (b) reproduces the
corpus's own printed values. A failure here means the plate must not be drawn.

Constants, all from encyclopedia/wing-NATURA/NA-05 + NATURE-LEDGER:
  b1 = 0.5371  (NA05-08, temperature-corrected fit, M0 = 1 g)
  b2 = 0.0294  (NA05-07, temperature-corrected fit)
  local slope = b1 + 2*b2*log10(M/1g)      (NA05-09)
"""
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

b1, b2 = 0.5371, 0.0294
slope = lambda x: b1 + 2 * b2 * x
mass_at = lambda s: (s - b1) / (2 * b2)          # returns log10 M (g)
f = lambda x: b1 * x + b2 * x * x                 # log10 B, minus the unprinted b0

ok = True
def check(label, got, want, tol, unit=""):
    global ok
    good = abs(got - want) <= tol
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] {label:<44} computed {got:>12.4f}{unit}  corpus {want}{unit}")

print("NA05-09 / NA05-10 / NA05-11 / NA05-12 — the local-slope table (temp fit)")
check("slope at 3.6 g (corpus 0.57)",      slope(math.log10(3.6)),      0.57,   0.005)
check("slope at 460 kg (corpus 0.87)",     slope(math.log10(460e3)),    0.87,   0.005)
check("M at slope 2/3 (corpus ~160 g)",    10**mass_at(2/3),            160.0,  2.0, " g")
check("M at slope 3/4 (corpus ~4.2 kg)",   10**mass_at(0.75)/1000,      4.2,    0.05, " kg")
check("M at slope 1.0 (corpus ~7.4e7 g)",  10**mass_at(1.0)/1e7,        7.4,    0.1, "e7 g")

print("\nNA05-10 / NA05-11 — the SAME crossings under the no-temperature fit (b1=0.5400, b2=0.0322)")
b1n, b2n = 0.5400, 0.0322
mass_at_n = lambda s: (s - b1n) / (2 * b2n)
check("M at slope 2/3, no-T (corpus ~93 g)",   10**mass_at_n(2/3),          93.0, 1.0, " g")
check("M at slope 3/4, no-T (corpus ~1.8 kg)", 10**mass_at_n(0.75)/1000,    1.8,  0.05, " kg")

print("\nNA-05 §'How to use a ratio' — the shrew extrapolation (3/4 line vs the quadratic)")
x34, x_shrew = math.log10(4200), math.log10(3)
d_line = 0.75 * (x_shrew - x34)
d_quad = f(x_shrew) - f(x34)
check("3/4 line, dlog10B (corpus -2.360)", d_line, -2.360, 0.002)
check("quadratic, dlog10B (corpus -2.069)", d_quad, -2.069, 0.002)
check("discrepancy in log10 (corpus 0.291)", d_quad - d_line, 0.291, 0.002)
check("underprediction factor (corpus 1.95x)", 10**(d_quad - d_line), 1.95, 0.01, "x")

print("\nNA-05 quadratic intermediates the chapter prints verbatim (0.263 - 2.332)")
check("f(log10 3 g)   (corpus 0.263)", f(x_shrew), 0.263, 0.001)
check("f(log10 4.2 kg) (corpus 2.332)", f(x34),    2.332, 0.001)

print("\nCN11-40 / CN11-41 / CN11-42 — Froude gait, v = sqrt(Fr*g*L), g = 9.81 m/s^2")
v = lambda Fr, L: math.sqrt(Fr * 9.81 * L)
check("v at Fr=0.5, L=0.9 m (corpus ~2.1 m/s)", v(0.5, 0.9), 2.1, 0.02, " m/s")
check("v at Fr=0.5, L=0.8 m (corpus 2.0)",      v(0.5, 0.8), 2.0, 0.02, " m/s")
check("v at Fr=0.5, L=1.0 m (corpus 2.2)",      v(0.5, 1.0), 2.2, 0.02, " m/s")
check("v at Fr=1,   L=0.9 m (corpus ~3.0 m/s)", v(1.0, 0.9), 3.0, 0.03, " m/s")

print("\nCN-08 recorded convention trap — Fr=v^2/(gL) vs Fr=v/sqrt(gL) differ by a square")
check("sqrt(0.5) (corpus 'Fr 0.5 is Fr ~0.71')", math.sqrt(0.5), 0.71, 0.005)

print("\nNA06-05 — De Witt et al. 2014 lunar transition band, 1.39 +/- 0.45")
print(f"  band = [{1.39-0.45:.2f}, {1.39+0.45:.2f}] — lower bound {1.39-0.45:.2f} vs Earth prediction 0.50")
print(f"  [{'PASS' if 1.39-0.45 > 0.5 else 'FAIL'}] the lunar band's LOWER bound lies above the Earth prediction (the failure is real, not overlap)")
ok &= (1.39 - 0.45) > 0.5

print("\nNA05-06 — White & Seymour 2005 '+/-' bars against the two thresholds")
for name, pt, e, verdict in [("BMR 0.686+/-0.014", .686, .014, "excludes 3/4, ~excludes 2/3"),
                             ("SMR 0.675+/-0.013", .675, .013, "includes 2/3, excludes 3/4"),
                             ("RMRt 0.712+/-0.013", .712, .013, "excludes BOTH")]:
    lo, hi = pt - e, pt + e
    inc23 = lo <= 2/3 <= hi
    inc34 = lo <= 0.75 <= hi
    print(f"  {name:<20} [{lo:.3f},{hi:.3f}]  2/3 {'IN' if inc23 else 'out'} · 3/4 {'IN' if inc34 else 'out'}   corpus: {verdict}")

print("\nNA05-03 / NA05-04 — Savage CIs against the two thresholds")
for name, lo, hi, verdict in [("binned   [0.711,0.762]", .711, .762, "includes 3/4, excludes 2/3"),
                              ("unbinned [0.699,0.724]", .699, .724, "excludes 2/3 AND 3/4")]:
    print(f"  {name:<24} 2/3 {'IN' if lo<=2/3<=hi else 'out'} · 3/4 {'IN' if lo<=0.75<=hi else 'out'}   corpus: {verdict}")

print("\n" + ("ALL CHECKS PASS — the plate's geometry reproduces the corpus." if ok
              else "A CHECK FAILED — do not draw the plate."))
sys.exit(0 if ok else 1)
