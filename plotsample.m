clear
clc

R = readtable("R_data.csv");
G = readtable("G_data.csv");
B = readtable("B_data.csv");
Pressure = readtable("Cuff_data.csv");

figure(1)
plot(R,"R0")
hold on
plot(R,"R1")
plot(R,"R2")
plot(G,"G0")
plot(G,"G1")
plot(G,"G2")
plot(B,"B0")
plot(B,"B1")
plot(B,"B2")
xlabel("Samples");
ylabel("Voltage (V)");

figure(2)
plot(Pressure,"Cuff")
xlabel("Samples");
ylabel("Pressure (mmHg)");
title("Pressurization Curve");

x = double(R{:,:});

R_sgf = sgolayfilt(double(R{:,:}),3,13);
G_sgf = sgolayfilt(double(G{:,:}),3,13);
B_sgf = sgolayfilt(double(B{:,:}),3,13);

figure(3)
plot(R_sgf(:,1))
hold on
plot(R_sgf(:,2))
plot(R_sgf(:,3))
plot(G_sgf(:,1))
plot(G_sgf(:,2))
plot(G_sgf(:,3))
plot(B_sgf(:,1))
plot(B_sgf(:,2))
plot(B_sgf(:,3))
xlabel("Samples");
ylabel("Voltage (V)");
