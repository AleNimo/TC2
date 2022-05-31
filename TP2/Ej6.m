

T = tf( 105 ,[1 10 45 105 105]);

W = logspace(-3,6,1000);

figure()
pzmap(T)
figure()
[mag, phase] = bode(T,W);
figure()
[h,w] = freqs(105,[1 10 45 105 105],1000);
grpdel = diff(unwrap(angle(h)))./diff(w);

clf
semilogx(w(2:end),grpdel)
xlabel('Frequency (rad/s)')
ylabel('Group delay (s)')
