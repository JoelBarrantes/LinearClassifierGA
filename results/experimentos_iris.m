

x25= graphs('iris_25_5_l_r',5, 10);
x50 = graphs('iris_50_5_l_r',5, 10);
x100= graphs('iris_100_5_l_r',5, 10);

x25_50= graphs('iris_25_5_l_re',3, 50);
x100_50= graphs('iris_100_5_l_re',3, 50);

x100_b = graphs('iris_100_5_l_ree',5, 10);


%Mejor loss promedio
x_axis = x25(:,1);
figure;
plot(x_axis, x25(:,5),'DisplayName','25 individuos');
hold on;
plot(x_axis, x50(:,5),'DisplayName','50 individuos');
hold on;
plot(x_axis, x100(:,5),'DisplayName','100 individuos');
hold on;

legend('show');
title('Pérdida promedio del mejor individuo por generación')
xlabel('Generación')
ylabel('Hinge Loss')

%Mejor exactitud promedio
figure;
plot(x_axis, x25(:,4),'DisplayName','25 individuos');
hold on;
plot(x_axis, x50(:,4),'DisplayName','50 individuos');
hold on;
plot(x_axis, x100(:,4),'DisplayName','100 individuos');
hold on;

legend('show', 'Location','southeast');
title('Exactitud promedio del mejor individuo por generación')
xlabel('Generación')
ylabel('Exactitud')

%Loss promedio, crossover a vs b
figure;
plot(x_axis, x100(:,3),'DisplayName','$a(x,y)$');
hold on;
plot(x_axis, x100_b(:,3),'DisplayName','$b(x,y)$');
hold on;

lgd = legend('show');
set(lgd,'Interpreter','latex')
title('Pérdida Promedio del Crossover por Generación')
xlabel('Generación')
ylabel('Hinge Loss')

%Mejor loss promedio, 50 generaciones
x_axis = x25_50(:,1);
figure;
plot(x_axis, x25_50(:,5),'DisplayName','25 individuos');
hold on;
plot(x_axis, x100_50(:,5),'DisplayName','100 individuos');
hold on;

legend('show');
title('Pérdida promedio del mejor individuo por generación')
xlabel('Generación')
ylabel('Hinge Loss')

%Mejor exactitud promedio, 50 generaciones
figure;
plot(x_axis, x25_50(:,4),'DisplayName','25 individuos');
hold on;
plot(x_axis, x100_50(:,4),'DisplayName','100 individuos');
hold on;

legend('show', 'Location','southeast');
title('Exactitud promedio del mejor individuo por generación')
xlabel('Generación')
ylabel('Exactitud')


