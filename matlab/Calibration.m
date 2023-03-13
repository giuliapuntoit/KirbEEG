clear;
close all;

%% Read the recorded file and plot impedances

% Select file to read
read_Intan_RHD2000_file;

% Plot the impedances of all the channels, find the working channels
figure;
for i = 1:2
    plot(i-1,amplifier_channels(i).electrode_impedance_magnitude/1000,'o')
    hold on
end
set(gca,'XTick',0:1:2)

%% Choose channel(s) to process and apply filter(s)

% Select channel number(s) with useful signal
% [channel#]+1 because of matlab indexing
mapping = [0 1] + 1;

% Load and apply filters (Create your own filters and apply here)
load BandpassProj.mat
useful_Amp_Data = amplifier_data(mapping,:);
dataFiltered = zeros(length(mapping),size(useful_Amp_Data,2));
for i = 1:length(mapping)
    dataFiltered(i,:) = filtfilt(SOS,G,useful_Amp_Data(i,:));
end
%% Instantaneous Power
% p1 = [];
% p2 = [];
% power = [p1; p2];
figure(2);
% size(dataFiltered)

for j = 1:length(mapping)
    power(j, :) = (abs(hilbert(dataFiltered(j,:))).^2);
    subplot(2,1,j);
    hold on;
    plot( t_amplifier, power(j,:));
    yline(24);
    ylim([0 200]);
    xlabel('Time (s)');
    ylabel('Instantaneous Power (\muV^2)');
    hold off;
end

%print the means
idx30 = find(t_amplifier==30);
idx60 = find (t_amplifier==60);
idx90 = find (t_amplifier==90);

meanp1_30_60 = mean(power(1, (idx30:idx60)))
meanp1_60_90 = mean(power(1, (idx60:idx90)))
meanp1_30_90 = mean(power(1, (idx30:idx90)))


meanp2_30_60 = mean(power(2, (idx30:idx60)))
meanp2_60_90 = mean(power(2, (idx60:idx90)))
meanp2_30_90 = mean(power(2, (idx30:idx90)))

% Define control threshold

player1_threshold_up = meanp1_30_60;
player1_threshold_down = meanp1_60_90;
player2_threshold_up = meanp2_30_60;
player2_threshold_down = meanp2_60_90;

save("players_threshold","player1_threshold_up","player1_threshold_down", "player2_threshold_up","player2_threshold_down");


