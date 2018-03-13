function output = graphs(experimento,k, d)
    output = zeros(d+1,5);
    best_acc = zeros(k,1);
    best_loss = zeros(k,1);
    for i = 1:k
        matFileName = sprintf(strcat(experimento,'%d.txt'), i);
        m = load(matFileName);
        best_acc(i) = m(11,4);
        best_loss(i) = m(11,5);
        output = output + m;

    end 

    prom = output/k;
    prom(11,1) = prom(11,1)+1;
    output = prom;
end 


