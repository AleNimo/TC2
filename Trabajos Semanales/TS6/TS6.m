
wz = 1/3;
wp = 1;

T = tf( [1 0 wz^2] ,[1 wp wp^2]) * tf([1 0], [1 wp])

W = logspace(-3,3,100000);

figure()
pzmap(T)
figure()
bode(T,W);