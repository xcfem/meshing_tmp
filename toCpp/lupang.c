/* lupang.f -- translated by f2c (version 20160102).
   You must link the resulting object file with libf2c:
	on Microsoft Windows system, link with libf2c.lib;
	on Linux or Unix systems, link with .../path/to/libf2c.a -lm
	or, if you install libf2c.a in a standard place, with -lf2c -lm
	-- in that order, at the end of the command line, as in
		cc *.o -lf2c -lm
	Source for libf2c is in /netlib/f2c/libf2c.zip, e.g.,

		http://www.netlib.org/f2c/libf2c.zip
*/

#ifdef __cplusplus
extern "C" {
#endif
#include "f2c.h"

/*    Copyright(C) 1999-2020 National Technology & Engineering Solutions */
/*    of Sandia, LLC (NTESS).  Under the terms of Contract DE-NA0003525 with */
/*    NTESS, the U.S. Government retains certain rights in this software. */

/*    See packages/seacas/LICENSE for details */
/* Subroutine */ int lupang_(integer *mxnd, integer *mln, real *xn, real *yn, 
	real *zn, integer *lxk, integer *kxl, integer *nxl, integer *lxn, 
	integer *nloop, real *angle, integer *lnodes, integer *nstart, 
	integer *lll, real *xmin, real *xmax, real *ymin, real *ymax, real *
	zmin, real *zmax, char *dev1, integer *kreg, logical *err, ftnlen 
	dev1_len)
{
    /* System generated locals */
    integer lnodes_dim1, lnodes_offset;

    /* Local variables */
    static integer n0, n1, n2, kount;
    extern /* Subroutine */ int mesage_(char *, ftnlen), getang_(integer *, 
	    integer *, real *, real *, integer *, integer *, integer *, 
	    integer *, integer *, integer *, integer *, integer *, real *, 
	    logical *);

/* *********************************************************************** */
/*  SUROUTINE LUPANG = CALCULATES THE NEW ANGLES FOR ALL NODES IN A LOOP */
/* *********************************************************************** */
    /* Parameter adjustments */
    --angle;
    lxn -= 5;
    nxl -= 3;
    kxl -= 3;
    lxk -= 5;
    --zn;
    --yn;
    --xn;
    lnodes_dim1 = *mln;
    lnodes_offset = 1 + lnodes_dim1;
    lnodes -= lnodes_offset;

    /* Function Body */
    *err = FALSE_;
/*  LOOP AROUND THE INTERIOR PERIMETER CALCULATING THE NEW */
/*  ANGLES */
    n1 = *nstart;
    kount = 0;
L100:
    n0 = lnodes[n1 * lnodes_dim1 + 2];
    n2 = lnodes[n1 * lnodes_dim1 + 3];
    getang_(mxnd, mln, &xn[1], &yn[1], &lnodes[lnodes_offset], &lxk[5], &kxl[
	    3], &nxl[3], &lxn[5], &n0, &n1, &n2, &angle[n1], err);
    if (*err) {
	mesage_(" ** ERROR IN LUPANG ** ", (ftnlen)23);
	goto L110;
    }
    n1 = n2;
    if (n1 == *nstart) {
	goto L110;
    }
    ++kount;
    if (kount > *nloop) {
	mesage_(" ** ERROR IN LUPANG ** ", (ftnlen)23);
	*err = TRUE_;
	goto L110;
    }
    goto L100;
L110:
    return 0;
} /* lupang_ */

#ifdef __cplusplus
	}
#endif
