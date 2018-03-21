


x50_5_a = graphs('cifar_50_5_a_r',3, 10);
x50_5_l = graphs('cifar_50_5_l_r',3, 10);
x50_15_a = graphs('cifar_50_15_a_r',3, 10);
x50_15_l = graphs('cifar_50_15_l_r',3, 10);

x_axis = x50_5_a(:,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
plot(x_axis, x50_15_a(:,5),'DisplayName','Fitness $e(x)$');
hold on;
plot(x_axis, x50_15_l(:,5),'DisplayName','Fitness $p(x)$');
hold on;

lgd = legend('show');
set(lgd,'Interpreter','latex')
title('Pérdida promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Hinge Loss')

figure;
plot(x_axis, x50_15_a(:,4),'DisplayName','Fitness $e(x)$');
hold on;
plot(x_axis, x50_15_l(:,4),'DisplayName','Fitness $p(x)$');
hold on;

lgd = legend('show');
set(lgd,'Interpreter','latex')
title('Exactitud promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Exactitud')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
figure;
plot(x_axis, x50_5_a(:,5),'DisplayName','Fitness $e(x)$');
hold on;
plot(x_axis, x50_5_l(:,5),'DisplayName','Fitness $p(x)$');
hold on;

lgd = legend('show');
set(lgd,'Interpreter','latex')
title('Pérdida promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Hinge Loss')

figure;
plot(x_axis, x50_5_a(:,4),'DisplayName','Fitness $e(x)$');
hold on;
plot(x_axis, x50_5_l(:,4),'DisplayName','Fitness $p(x)$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Exactitud promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Exactitud')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
plot(x_axis, x50_5_a(:,5),'DisplayName','Mut. $5\%$');
hold on;
plot(x_axis, x50_15_a(:,5),'DisplayName','Mut. $15\%$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Pérdida promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Pérdida')

figure;
plot(x_axis, x50_5_a(:,4),'DisplayName','Mut. $5\%$');
hold on;
plot(x_axis, x50_15_a(:,4),'DisplayName','Mut. $15\%$');
hold on;

lgd = legend('show', 'Location','southeast');
set(lgd,'Interpreter','latex')
title('Exactitud promedio por generación del mejor individuo')
xlabel('Generación')
ylabel('Exactitud')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

