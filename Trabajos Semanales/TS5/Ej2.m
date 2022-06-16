

a=0.5;
b=1;
d=1;
R=1/sqrt(2);
L=1;
C=1;

T = tf( [1 0 16] ,[1 sqrt(2) 1]);

W = logspace(-2,2,1000);

figure()
pzmap(T)
figure()
bode(T,W);
