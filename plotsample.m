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

figure(2)
plot(Pressure,"Cuff")

R_sgf = sgolayfilt(double(R{:,:}),3,501);
G_sgf = sgolayfilt(double(G{:,:}),3,501);
B_sgf = sgolayfilt(double(B{:,:}),3,501);

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

