# format input:
# dimensiune_pop = dimensiunea populatiei
# a b = capetele domeniului de definitie
# a b c = coeficientii polinomului de grad 2
# p = nr zecimale precizie cu care se discretiseaza intervalul
# p_recombinare = probabilitatea de recombinare
# p_mutatie = probabilitatea de mutatie
# nr_etape = nr de etape ale algoritmului

import random
import math
import copy


#------------------------------------Functii---------------------------------------------------


# return 1 bit random
def random_bit():
    x = random.random()
    if x < 0.5:
        return 1
    else:
        return 0

# return cromosom de lungime data
def generate_chromosome(length):
    return [random_bit() for y in range(length)]

# return prima populatie- random
def generate_random_population():
    tmp = [ generate_chromosome(lungime_cromozom) for x in range(dimensiune_pop)]
    return tmp

# definirea functia de fitness
def fct(x):
    return coef_functie[0]*x*x + coef_functie[1]*x + coef_functie[2]


# cromozom = x in baza 2 - > baza 10
# (translatie liniara)
def get_x(cromozom):
    x = 0
    for bit in cromozom:
        x = (x << 1) | bit

    return (dom_definitie[1]-dom_definitie[0])/(pow(2,lungime_cromozom))*x+dom_definitie[0]

# fitness level populatie
def get_all_values(populatie):
    return [fct(get_x(ch)) for ch in populatie]

# media performantei
def get_medie_values(pop):
    s = 0
    for individ in pop :
        s += fct(get_x(individ))
    return s / len(pop) 

# print chromosome (baza 2)
def p_cromozom(lst):
    return "".join(map(str,lst))

# print population
def print_population(populatie):
    if iteratie == 1:
        # pt prima populatie se afiseaza sub forma :
        # i:reprezentare cromozom , x = valoarea coresp cromozomului în dom de def al funct. 
        # f = valoarea coresp cromozomului (f(Xi))
        for i in range(1,len(populatie)+1):
            x = get_x(populatie[i-1])
            fl.write(str(i) + ": ")
            fl.write(p_cromozom(populatie[i-1]) + ", x=")
            fl.write('{: f}, '.format(x))
            fl.write("f=" + str(fct(x)))
        
            fl.write('\n')
        fl.write('\n\n')
    return

# probabilitatile de selectie pt fiec cromozom
def get_prob_selectie(populatie):

    valori_cromozomi = get_all_values(populatie)
    F = sum(valori_cromozomi)
    tmp = []
    for f_x in valori_cromozomi:
        # probabilitate = nr cazuri favorabile / nr cazuri posibile
        tmp.append(f_x/F)

    if iteratie == 1:
        fl.write("Probabilitati selectie:\n")
        for i in range(1,dimensiune_pop+1):
            fl.write("Cromozom " + format(i,'3') +' probabilitate: ' + str(tmp[i-1]) + '\n')
        fl.write("\n\n")
    return tmp
    
# prob selectie cumulate = > intervalele de selectie
# qi = p1+p2+...+pi
def get_intervale_selectie(prob_selectie):
    tmp = []
    s = 0
    for p in prob_selectie:
        tmp.append(s) 
        s+= p 
    tmp.append(1.0)

    if iteratie == 1:
        fl.write("Intervale probabilitati selectie:\n")
        for t in tmp:
            fl.write(str(t) + ' ')
        fl.write("\n\n")
    return tmp

#cautarea binara
def cautare_interval(list, x, left, right):
    if x<=list[left]:
        return left
    elif x>=list[right]:
        return right + 1
    elif left < right:
        mid = int((left+right)/2)
        if list[mid]<=x and list[mid+1]>x:
            return mid+1
        elif list[mid]<=x and list[mid+1]<=x:
            return cautare_interval(list, x, mid+2, right)
        else:
            return cautare_interval(list, x, left, mid-1)

#procesul de selectie
def metoda_ruletei():
    pop = []
    for i in range(0,dimensiune_pop):
        # aleg nr random intre [0,1] si gasesc intervalul in care se incadreaza si adaug cromozomul asociat intervalului in populatia noua
        u = random.random()
        j = cautare_interval(intervale_prob_selectie, u , 0, len(intervale_prob_selectie)-1)

        if iteratie == 1:
             fl.write("u = " + str(u) + " selectam cromozomul " + str(j)+"\n")
        pop.append(copy.deepcopy(populatie[j-1]))               
    return pop


def get_crossover_candidates(populatie,p_recombinare):
    # aleg nr random intre [0,1] pt fiecare dintre cromozomi si daca nr < probabilitate_recombinare
    #  atunci il adaug in lista de cromozomi ce vor fi recombinati
    tmp = []
    for i in range(1,dimensiune_pop+1):
        sansa = random.random()
        msg = ""
        msg +=(str(i) + ": ")
        msg+=(p_cromozom(populatie[i-1]) + ", u=")
        msg+=(str(sansa))
        if sansa < p_recombinare:
            tmp.append(i-1)
            msg+=" < " + str(p_recombinare) + " participa"
        if iteratie == 1:
            fl.write(msg + '\n')
    return tmp

#recombinare
def crossover(candidates):
    fl.write('\n')
    rezultat_1 = []
    rezultat_2 = []
    while len(candidates) >= 2 :
        # iau 2 cromozomi din cei alesi la etapa anterioara
        sample = random.sample(candidates,2)
        candidates.remove(sample[0])
        candidates.remove(sample[1])

        # se alege punct de rupere generat aleator
        pct_rupere = random.randrange(0,lungime_cromozom)
        if iteratie == 1:
            #evidentiam perechile de cromozomi care participa la recombinare
            fl.write("Recombinare dintre cromozomul {0} cu cromozomul {1}:\n".format(sample[0]+1,sample[1]+1))
            fl.write("{0} {1} punct {2}\n".format(p_cromozom(new_pop[sample[0]]),p_cromozom(new_pop[sample[1]]),pct_rupere))

        # combin bucatile
        rezultat_1 = new_pop[sample[0]][:pct_rupere] + new_pop[sample[1]][pct_rupere:]
        rezultat_2 = new_pop[sample[1]][:pct_rupere] + new_pop[sample[0]][pct_rupere:]

        if iteratie == 1:
            #cromozomii rezltati in urma combinarii
            fl.write("Rezultat: {0} {1}\n\n".format(p_cromozom(rezultat_1),p_cromozom(rezultat_2)))
        new_pop[sample[0]] = rezultat_1
        new_pop[sample[1]] = rezultat_2        
    return


def mutate():
    if iteratie == 1:
        fl.write("\nProbabilitatea de mutatie pentru fiecare gena {0}:\nAu fost modificati cromozomii:\n".format(p_mutatie))
    for i in range(dimensiune_pop-1):
        #se alege un nr random
        u = random.random()
        #daca e mai mic decat prob de mutatie
        if u < p_mutatie:
            if iteratie == 1:
                fl.write(str(i+1) + ' ')
            # se ia un bit random si se modifica
            poz = random.randrange(0,lungime_cromozom-1)
            new_pop[i][poz] = abs(new_pop[i][poz]-1)
    if iteratie == 1:
        fl.write('\n')
    return

# index de la fittest chromosome(max fucntie de fitness)
def get_fittest(populatie):
    ind = 0
    maxx = fct(get_x(populatie[0]))
    for i in range(len(populatie)):
        f_x = fct(get_x(populatie[i]))
        if f_x > maxx:
            ind = i 
            maxx = f_x
    return ind

# index de la least fit chromosome
def get_least_fit(populatie):
    ind = 0
    minn = fct(get_x(populatie[0]))
    for i in range(len(populatie)):
        f_x = fct(get_x(populatie[i]))
        if minn > f_x:
            ind = i 
            minn = f_x

    return ind

# inlocuim least fit cu fittest ca sa se asiguram ca trece in generatia urmatoare
#(individul cu indicele de fitness cel mai mare trece automat in generatia urmatoare)
def criteriu_elitist() :
    ind_fittest_old_pop = get_fittest(populatie)
    ind_least_fit_new_pop = get_least_fit(new_pop)

    new_pop[ind_least_fit_new_pop] = copy.copy(populatie[ind_fittest_old_pop])
    return


# ----------------------------- END FUNCTII ------------------------------------------------

# citire date intrare

#print("Computing, please wait...")

fl = open("output.txt","w")
with open("input.txt") as f:
    lines = f.read().splitlines()

dimensiune_pop = int(lines[0])
dom_definitie = [int(x) for x in lines[1].split()]
coef_functie = [int(x) for x in lines[2].split()]
precizie = int(lines[3])
p_recombinare = float(lines[4])
p_mutatie = float(lines[5])
nr_etape = int(lines[6])
iteratie = 1

# calculez lungimea cromozomului
# discretizare interval in (b-a) * 10^precizie_subintervale

lungime_cromozom = math.floor(math.log((dom_definitie[1] - dom_definitie[0])*(math.pow(10,precizie)), 2))


#  1. generare aleator indivizi

populatie = generate_random_population()
if iteratie == 1:
    fl.write("Populatia initiala:\n")
    print_population(populatie)

while iteratie <= nr_etape :
    # 2. calc probabilitati de selectie pt fiecare cromozom
    prob_selectie = get_prob_selectie(populatie)

    # 3. get intervale prob_selectie
    intervale_prob_selectie = get_intervale_selectie(prob_selectie)

    # 4. metoda ruletei
    new_pop = metoda_ruletei()

    if iteratie == 1:
        fl.write("\nDupa selectie:\n")
        print_population(new_pop)

    # 5. selectie pt incrucisare
    index_cr_incrucisare = get_crossover_candidates(new_pop,p_recombinare)

    # 6. Incrucisare
    crossover(index_cr_incrucisare)

    # 7. Populatie dupa recombinare
    if iteratie == 1:
        fl.write("\nDupa recombinare:\n")
        print_population(new_pop)

    # 8. Mutatie
    mutate()
    if iteratie == 1:
        fl.write("Dupa mutatie: \n")
        print_population(new_pop)

    # 9. Criteriul elitist
    criteriu_elitist()

    if iteratie == 1:
        fl.write("Dupa aplicarea criteriului elitist: \n")
        print_population(new_pop)

    # 10. evolutia maximului

    # se aplica pe populatia noua functia care returneaza fittest 
    # fittest in baza 10 + fct_fitness(fittest)
    if iteratie == 1:
        fl.write("Evolutia maximului: \n")

    fl.write(str(fct(get_x(new_pop[get_fittest(new_pop)]))) + ' ' + str(get_medie_values(new_pop)))
    
    # 11. preg pt urmatoarea iteratie
    iteratie += 1
    populatie = copy.deepcopy(new_pop)

    ## Done! 
print("Finished!")