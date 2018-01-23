const real per_check_s_base = 0.0000001;
inline real ldabs (real x) { return (x<0) ? -x : x; }

iter calculate_pixel (real x, real y) {
  real zx = 0;
  real zy = 0;
  real zx2 = 0;
  real zy2 = 0;
  real zzx = 0;
  real zzy = 0;
  real zzx2 = 0;
  real zzy2 = 0;
  real dst;
  iter i = 0;
  int mod16 = 0;

  while (zx2+zy2 <= bail_radius_squared && i < maxiter) {
    if (mod16 == 16) {
      mod16 = 0;
      zzy = 2*zzx*zzy + y;
      zzx = zzx2 - zzy2 + x;
      zzx2 = zzx*zzx;
      zzy2 = zzy*zzy;
    }
    ++mod16;
    zy = 2*zx*zy + y;
    zx = zx2 - zy2 + x;
    zx2 = zx*zx;
    zy2 = zy*zy;
    ++i;
    dst = ldabs(zx - zzx) + ldabs(zy - zzy);
    if (dst < per_check_sens) i = maxiter;
  }
  return i;
}


