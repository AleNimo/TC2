ep2 = (10^0.1 - 1);

s = tf('s');

s11_2 = ep2*(64*s^8 + 128*s^6 + 80*s^4 + 16*s^2 + 1) / (1+ ep2*(64*s^8 + 128*s^6 + 80*s^4 + 16*s^2 + 1));

polos = pole(s11_2);

s11 = (s^4+s^2+1/8) / ((s-polos(1))*(s-polos(2))*(s-polos(5))*(s-polos(6)));

s11 = tf(s11.Numerator{1,1}, real(s11.Denominator{1,1})) %(Se deben eliminar componentes imaginarias espurias en los coeficientes)

z1 = (1+s11)/(1-s11)

z1 = minreal(z1) %(La función minreal cancela polos y ceros en la misma posición del plano S)

%#ok<*NOPTS> %