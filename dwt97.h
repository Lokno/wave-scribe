#ifndef DWT97_H
#define DWT97_H

#ifdef __cplusplus
extern "C" {
#endif

void fwt97(double* x, int n);

void iwt97(double* x,int n);

void dwtcleanup();

#ifdef __cplusplus
}
#endif

#endif