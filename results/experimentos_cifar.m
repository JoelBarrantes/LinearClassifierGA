

x25_5_a = graphs('cifar_25_5_a_r',3, 10);
x25_5_l = graphs('cifar_25_5_l_r',3, 10);
x25_15_a = graphs('cifar_25_15_a_r',3, 10);
x25_15_l = graphs('cifar_25_15_l_r',3, 10);
x50_5_a = graphs('cifar_50_5_a_r',3, 10);
x50_5_l = graphs('cifar_50_5_l_r',3, 10);
x50_15_a = graphs('cifar_50_15_a_r',3, 10);
x50_15_l = graphs('cifar_50_15_l_r',3, 10);

x_axis = x25_5_a(:,1);



figure;
plot(x_axis, x50_5_a(:,5),'DisplayName','a(x)');
hold on;
plot(x_axis, x50_5_l(:,5),'DisplayName','$l(x)$');
hold on;

lgd = legend('show');
set(lgd,'Interpreter','latex')
title('Pérdida promedio de la función de fitness por generación')
xlabel('Generación')
ylabel('Hinge Loss')

figure;
plot(x_axis, x50_5_a(:,4),'DisplayName','$a(x)$');
hold on;
plot(x_axis, x50_5_l(:,4),'DisplayName','$l(x)$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Exactitud promedio de la función de fitness por generación')
xlabel('Generación')
ylabel('Exactitud')

%{
figure;
plot(x_axis, x50_5_a(:,3),'DisplayName','50-5-a');
hold on;
plot(x_axis, x50_15_a(:,3),'DisplayName','50-15-a');
hold on;
plot(x_axis, x50_5_l(:,3),'DisplayName','50-5-l');
hold on;
plot(x_axis, x50_15_l(:,3),'DisplayName','50-15-l');
hold on;

legend('show')
%}


figure;
plot(x_axis, x25_5_a(:,4),'DisplayName','$5\%$');
hold on;
plot(x_axis, x25_15_a(:,4),'DisplayName','$15\%$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Exactitud promedio de probabilidad de mutación por generación')
xlabel('Generación')
ylabel('Exactitud')

figure;
plot(x_axis, x50_5_a(:,4),'DisplayName','$5\%$');
hold on;
plot(x_axis, x50_15_a(:,4),'DisplayName','$15\%$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Exactitud promedio de probabilidad de mutación por generación')
xlabel('Generación')
ylabel('Exactitud')


