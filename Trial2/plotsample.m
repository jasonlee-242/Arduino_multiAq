clear
clc

R = readtable("R_data.csv");
R = table2array(R);
G = readtable("G_data.csv");
G = table2array(G);
B = readtable("B_data.csv");
B = table2array(B);
P = readtable("Cuff_data.csv");
P = table2array(P);

t = 32;
sr1 = length(R)/t;
sr2 = length(P)/t;

intr = 3;

x1 = 1:intr:length(R);
x2 = 1:length(P);

R_arr = [R(1:intr:end,1),R(1:intr:end,2),R(1:intr:end,3)];
G_arr = [G(1:intr:end,1),G(1:intr:end,2),G(1:intr:end,3)];
B_arr = [B(1:intr:end,1),B(1:intr:end,2),B(1:intr:end,3)];

figure(1)
subplot(3,1,1)
set(gcf,'color','w');
p1 = plot(x1'./sr1,R_arr(:,1),'Color','r'); hold on
p1_2 = plot(x1'./sr1,G_arr(:,1),'Color','g');
p1_3 = plot(x1'./sr1,B_arr(:,1),'Color','b');
p1.LineWidth = 2;
p1_2.LineWidth = 2;
p1_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Top Sensors vs. Time (s)');

subplot(3,1,2)
set(gcf,'color','w');
p2 = plot(x1'./sr1,R_arr(:,2),'Color','r'); hold on
p2_2 = plot(x1'./sr1,G_arr(:,2),'Color','g');
p2_3 = plot(x1'./sr1,B_arr(:,2),'Color','b');
p2.LineWidth = 2;
p2_2.LineWidth = 2;
p2_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Middle Sensors vs. Time (s)');

subplot(3,1,3)
set(gcf,'color','w');
p3 = plot(x1'./sr1,R_arr(:,3),'Color','r'); hold on
p3_2 = plot(x1'./sr1,G_arr(:,3),'Color','g');
p3_3 = plot(x1'./sr1,B_arr(:,3),'Color','b');
p3.LineWidth = 2;
p3_2.LineWidth = 2;
p3_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Bottom Sensors vs. Time (s)');

figure(2)
plot(x2/sr2,P(:,1));
set(gcf,'color','w');
set(gca,'fontsize',24);
xlabel("Time (s)");
ylabel("Pressure (mmHg)");
title("Pressurization Curve");

R_sgf = sgolayfilt(R,3,13);
G_sgf = sgolayfilt(G,3,13);
B_sgf = sgolayfilt(B,3,13);

R_arr = [R_sgf(1:intr:end,1),R_sgf(1:intr:end,2),R_sgf(1:intr:end,3)];
G_arr = [G_sgf(1:intr:end,1),G_sgf(1:intr:end,2),G_sgf(1:intr:end,3)];
B_arr = [B_sgf(1:intr:end,1),B_sgf(1:intr:end,2),B_sgf(1:intr:end,3)];

figure(3)
subplot(3,1,1)
set(gcf,'color','w');
p1 = plot(x1'./sr1,R_arr(:,1),'Color','r'); hold on
p1_2 = plot(x1'./sr1,G_arr(:,1),'Color','g');
p1_3 = plot(x1'./sr1,B_arr(:,1),'Color','b');
p1.LineWidth = 2;
p1_2.LineWidth = 2;
p1_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Top Sensors vs. Time (s)');

subplot(3,1,2)
set(gcf,'color','w');
p2 = plot(x1'./sr1,R_arr(:,2),'Color','r'); hold on
p2_2 = plot(x1'./sr1,G_arr(:,2),'Color','g');
p2_3 = plot(x1'./sr1,B_arr(:,2),'Color','b');
p2.LineWidth = 2;
p2_2.LineWidth = 2;
p2_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Middle Sensors vs. Time (s)');

subplot(3,1,3)
set(gcf,'color','w');
p3 = plot(x1'./sr1,R_arr(:,3),'Color','r'); hold on
p3_2 = plot(x1'./sr1,G_arr(:,3),'Color','g');
p3_3 = plot(x1'./sr1,B_arr(:,3),'Color','b');
p3.LineWidth = 2;
p3_2.LineWidth = 2;
p3_3.LineWidth = 3;
ylim([-.001 0.1])
set(gca,'fontsize',24);
xlabel('Time (s)');
ylabel('Voltage (V)')
title('Bottom Sensors vs. Time (s)');