/* jumplp.f -- translated by f2c (version 20160102).
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
integer jumplp_(integer *mxnd, integer *mln, integer *lnodes, integer *inow, 
	integer *ijump)
{
    /* System generated locals */
    integer lnodes_dim1, lnodes_offset, ret_val, i__1;

    /* Local variables */
    static integer i__;

/* *********************************************************************** */
/*  FUNCTION JUMPLP = JUMPS IJUMP STEPS FORWARD AROUND THE CLOSED LOOP */
/* *********************************************************************** */
    /* Parameter adjustments */
    lnodes_dim1 = *mln;
    lnodes_offset = 1 + lnodes_dim1;
    lnodes -= lnodes_offset;

    /* Function Body */
    ret_val = *inow;
    i__1 = *ijump;
    for (i__ = 1; i__ <= i__1; ++i__) {
	ret_val = lnodes[ret_val * lnodes_dim1 + 3];
/* L100: */
    }
    return ret_val;
} /* jumplp_ */

#ifdef __cplusplus
	}
#endif
