
m = load('10_426_1542277946.mat');
m = cell2mat( struct2cell( m ));

p = m(:,1:1024);
k1 = p(1,:);
k2 = p(2,:);
k3 = p(3,:);
k4 = p(4,:);


k1 = reshape(k1,32,32)';
k2 = reshape(k2,32,32)';
k3 = reshape(k3,32,32)';
k4 = reshape(k4,32,32)';

k1 = k1 - min(k1(:));
k1 = k1 ./ max(k1(:)); % *

k2 = k2 - min(k2(:));
k2 = k2 ./ max(k2(:)); % *

k3 = k3 - min(k3(:));
k3 = k3 ./ max(k3(:)); % *

k4 = k4 - min(k4(:));
k4 = k4 ./ max(k4(:)); % *

figure;
imshow(k1);
figure;
imshow(k2);
figure;
imshow(k3);
figure;
imshow(k4);