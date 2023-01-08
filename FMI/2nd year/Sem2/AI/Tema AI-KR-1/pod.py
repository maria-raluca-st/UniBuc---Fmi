import sys
import os
import time
from heapq import heapify, heappop, heappush
from copy import deepcopy
from math import inf


globalMaxNoduri = 0
maxNoduri = 0

# 1.Forma in care se apeleaza programul + 10.
if len(sys.argv) != 5:
    print('Usage: python pod.py folder_intrare folder_iesire nrsol timeout')
    print('Ex: python pod.py input output 2 100')

# ------------------------------CLASELE-------------------------------

# informatii despre un nod din arborele de parcurgere (nu din graful initial)


class NodParcurgere:

    def __init__(self,info, board, distance = 0, predecessor=None, id = 0 , heuristic_value = 0):
        self.board = board
        self.info = info
        self.distance = distance
        self.heuristic_value = heuristic_value
        self.id = id

        # Precompute the node's value
        self.value = self.distance + self.heuristic_value

        # Save the predecessor for retracing the path at the end
        self.predecessor = predecessor

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.board)

    def __lt__(self, other):
        if self.value == other.value:
            return self.distance > other.distance
        return self.value < other.value

    def obtineDrum(self):
        l = [self.info]
        nod = self
        while nod.predecessor is not None:
            l.insert(0, nod.predecessor.info)
            nod = nod.parinte
        return l

    def afisDrum(self, f):  # scrie si nodul
        l = self.obtineDrum()
        for nod in l:
            f.write(f"Nodul cu id: {nod.id}\n")
            f.write(str(nod))
        f.write(f"Cost: {self.distance}\n")
        f.write(f"Lungime: {len(l)}\n")

    def contineInDrum(self, infoNodNou):
        # return infoNodNou in self.obtineDrum()
        nodDrum = self
        while nodDrum is not None:
            if(infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.predecessor

        return False



class Graph:  # graful problemei

     # 2.citirea din fisier + memorarea starii
     def __init__(self, nume_fisier):
        '''
        :param nume_fisier: calea catre fisierul de input
        Citeste input-ul si seteaza board + k
        '''

        with open(nume_fisier, 'r') as fin:
           fline = fin.readline()
           # k = int(fline.strip())
           self.ok = True
           i = 0
           self.k = 1         # k = latura submatricii care se roteste in dreapta , care e pe prima linie a fisierului de intrare
           okk = 0  # okk-pt a verfica daca citim k
           # nr de placi(@) din matrice pt verif daca se poate ajunge in starea finala
           ct_placi = 0
           while fline[i].isdigit():
               self.k = self.k * 10 + int(fline[i])
               i = i+1
               okk = 1
               # am nevoie de bool ca sa verific daca se citeste k de la tastatura
               if(okk == 0):
                 print(f"Date de intrare invalide in fisierul {nume_fisier}.")
                 self.ok = False
                 exit()

           self.board = []
           line = fin.readline()
           while line:
            row = list(line.strip())
            nr_coloane = len(row)
            if row[0] != 'a' or row[len(row)-1] != 'b':
                print(f"Date de intrare invalide in fisierul {nume_fisier}.")
                self.ok = False
                exit()
            for i in range(1, len(row)-1):
                if row[i] != '#' and row[i] != '@':
                    print(
                        f"Date de intrare invalide in fisierul {nume_fisier}.")
                    self.ok = False
                    exit()
                if row[i] == '@':
                    ct_placi += 1
            self.board.append(row)
            self.start = self.board  # stare initiala 
            line = fin.readline()
            # 10.verificare ca din starea initiala se poate ajunge in stare finala
            # conditia este ca nr de placi sa fie cel putin nr_coloane-2 , in cazul in care putem forma un drum de la un mal la celalalt
            if ct_placi < nr_coloane - 2:
                 print(
                     f"Nu se poate ajunge in starea finala in fisierul {nume_fisier}")
                 self.ok = False
                 exit()
        # return {board,k}

     def get_zones(board):
    
      rows = len(board)

      if rows == 0:
        return []

      columns = len(board[0])

      visited = [[False for _ in range(columns)] for _ in range(rows)]

      def visit(i, j):
         zone = [(i, j)]

         if ((i > 0) and (not visited[i - 1][j]) and (board[i][j] == board[i - 1][j]) and board[i][j] != 'a' and board[i][j] != 'b'):
            # zonele nu includ malurile
            visited[i - 1][j] = True
            zone += visit(i - 1, j)

         if ((i < rows - 1) and (not visited[i + 1][j]) and (board[i][j] == board[i + 1][j]) and board[i][j] != 'a' and board[i][j] != 'b'):
            # zonele nu includ malurile
            visited[i + 1][j] = True
            zone += visit(i + 1, j)

         if ((j > 0) and (not visited[i][j - 1]) and (board[i][j] == board[i][j - 1])):
            visited[i][j - 1] = True
            zone += visit(i, j - 1)

         if ((j < columns - 1) and (not visited[i][j + 1]) and (board[i][j] == board[i][j + 1])):
            visited[i][j + 1] = True
            zone += visit(i, j + 1)
        
         return zone


      zones = []

      for column in range(columns):
        for row in range(rows):
            if visited[row][column]:
                continue

            visited[row][column] = True
            zone = visit(row, column)
            zone_color = board[row][column]

            if zone_color == 'a' or zone_color == 'b':
                # nu luam in considerare malurile
                continue

            zones.append((zone_color, zone))

      return zones

     def log_count(zona):
      "Counts how many logs the zone has. -- pt zona/submatrice"
      count = 0
      for line in zona:
        for cell in line:
            if cell == '@':
                count += 1

      return count

     #5.Testatrea ajungerii in stare scop : 
     # Daca pe matricea obtinuta avem o zona de placi care incepe 
     # pe prima coloana si se termina pe ultima , atunci suntem in stare scop
     def testeaza_scop(self, nodCurent):
        '''
        :param nodCurent:
        :return: Bool, true daca e stare scop, false altfel
        '''
        #return nodCurent.info in self.scopuri
        ok = 0
        zones = get_zones(nodCurent.board)
        for zone in zones:
            if zone[1] == '@':   # zone[1] = zone_color
                ok1 = 0          # pentru fiecare zona de placi resetam ok1 si ok2
                ok2 = 0
                for pair in zone[2]:  #zone[2] = zone 
                    if pair[1] == 1:
                        ok1 = 1
                    if pair[2] == len(self.board[0]) - 2:
                        ok1 = 1
        if ok1 == 1 and ok2 == 1:
            ok = 1
        return ok == 1 

     def calculeaza_h(self, infoNod, tip_euristica="euristica_banala"):
        
        #euristica banala - returneaza 1 daca nu e stare finala , 0 altfel
        if tip_euristica == "euristica_banala":
            if testeaza_scop(self,infoNod) == 0:
                return 1
            return 0
        elif tip_euristica == "euristica1":  
            # In cel mai bun caz se roteste submatricea o singura data
            cost = 0
            # daca nu e stare finala se adauga 1 la cost
            if testeaza_scop(self,infoNod) == 0:
                cost += 1 
            return cost
        elif tip_euristica == "euristica2": 
            return 0
        elif tip_euristica == "inadmisibila":
            return 0 

     def genereazaSuccesori(self, nodCurent):
        listaSuccesori = []
        return listaSuccesori

     def addNode(self, nodParcurgere):
        """
        Adauga nodParcurgere in graf pentru a putea tine minte ID-ul
           :param nodParcurgere: NodParcurgere
           :return nothing
       """
        try:
            indice = self.noduri[nodParcurgere]
            nodParcurgere.id = indice
        except KeyError:
            indice = len(self.noduri) - 1
            nodParcurgere.id = indice
            self.noduri[nodParcurgere] = indice

    

     

# ------------------------------FUNCTIILE-----------------------------------

def a_star_optimizat(f, gr, tipEuristica="euristica_banala", nrSolutiiCautate=1, timeOut=1000000000):
    """

   :param f : File pt output
   :param gr: Graful prblemei
   :param tipEuristica: eursitica folosita

    """
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
    heapify(c)
    # coada c este numita Open (noduri neexpandate inca) in algoritmul dat la curs
    # closed e cu nodurile expandate
    closed = []
    t1 = time.time()
    t2 = time.time()
    max_noduri = 0
    noduri_generate = 0
    milis = round(1000 * (t2 - t1))
    while len(c) > 0 and milis < timeOut:
        nodCurent = heappop(c)
        gr.addNode(nodCurent)
        closed.append(nodCurent)
        if gr.testeaza_scop(nodCurent):
            timpGasire = time.time()
            f.write("Solutie: \n")
            nodCurent.afisDrum(f)
            f.write(f"Timp pt a gasi solutia: {round(1000 * (timpGasire - t1))} ms\n")
            f.write(f"Nr maxim noduri in memorie: {max_noduri}\n")
            f.write(f"Nr de noduri generate: {noduri_generate}\n")
            f.write("----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tipEuristica)
        noduri_generate += len(lSuccesori)
        max_noduri = max(max_noduri, len(c) + len(lSuccesori) + len(closed))
        t2 = time.time()
        milis = round(1000 * (t2 - t1))
        if milis > timeOut:
            f.write('TIMED OUT\n')
            return
        for s in lSuccesori:
            gasitC = False
            for nodC in c:
                if s.info == nodC.info:
                    gasitC = True
                    if s.f >= nodC.f:
                        lSuccesori[:] = [x for x in lSuccesori if  x != s]  #remove s
                    else:  # s.f<nodC.f
                        c[:] = [x for x in c if x != nodC]  #remove nodCS
            if not gasitC:
                for nodC in closed:
                    if s.info == nodC.info:
                        if s.f >= nodC.f:
                            lSuccesori[:] = [x for x in lSuccesori if x != s]
                        else:  # s.f<nodC.f
                            closed[:] = [x for x in closed if x != nodC]
            heapify(c)
        for s in lSuccesori:
            heappush(c, s)
    milis = round(1000 * (time.time() - t1))
    if milis > timeOut:
        f.write('TIMED OUT\n')
        return


def a_star(f, gr, tipEuristica="euristica_banala", nrSolutiiCautate=1, timeOut=10000000000):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
    heapify(c)
    t1 = time.time()
    t2 = time.time()
    max_noduri = 0
    noduri_generate = 0
    milis = round(1000 * (t2 - t1))
    while len(c) > 0 and milis < timeOut:
        nodCurent = heappop(c)
        gr.addNode(nodCurent)
        if gr.testeaza_scop(nodCurent):
            timpGasire = time.time()
            f.write("Solutie: \n")
            nodCurent.afisDrum(f)
            f.write(f"Timp pt a gasi solutia: {round(1000 * (timpGasire - t1))} ms\n")
            f.write(f"Nr maxim noduri in memorie: {max_noduri}\n")
            f.write(f"Nr de noduri generate: {noduri_generate}\n")
            f.write("----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tipEuristica)
        noduri_generate += len(lSuccesori)
        t2 = time.time()
        milis = round(1000 * (t2 - t1))
        for s in lSuccesori:
            heappush(c, s)
        max_noduri = max(max_noduri, len(c))
    milis = round(1000 * (time.time() - t1))
    if milis > timeOut:
        f.write('TIMED OUT\n')
        return

def ida_star(f, gr, tipEuristica="euristica_banala", nrSolutiiCautate=1, timeOut=100000):
    def construieste_drum(gr, startTime, noduri_generate, nodCurent, limita, nrSolutiiCautate, tipEuristica="euristica_banala"):
        global maxNoduri, globalMaxNoduri
        milis = round(1000 * (time.time() - startTime))

        if milis > timeOut:
            f.write("TIMED OUT")
            return nrSolutiiCautate, float('inf'), noduri_generate

        if nodCurent.f > limita:
            return nrSolutiiCautate, nodCurent.f, noduri_generate

        if gr.testeaza_scop(nodCurent) and nodCurent.f == limita:
            f.write("Solutie: \n")
            nodCurent.afisDrum(f)
            f.write(f"Timp pt a gasi solutia: {round(1000 * (time.time() - startTime))} ms\n")
            f.write(f"Nr maxim noduri in memorie: {globalMaxNoduri}\n")
            f.write(f"Nr de noduri generate: {noduri_generate}\n")
            f.write("----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return 0, "gata", 0
        lSuccesori = gr.genereazaSuccesori(nodCurent, tipEuristica)
        noduri_generate += len(lSuccesori)
        maxNoduri += len(lSuccesori)
        globalMaxNoduri = max(maxNoduri, globalMaxNoduri)
        minim = 2e9
        for s in lSuccesori:
            maxNoduri -= 1
            gr.addNode(s)
            milis = round(1000 * (time.time() - startTime))
            if milis > timeOut:
                return nrSolutiiCautate, float('inf'), noduri_generate
            nrSolutiiCautate, rez, noduri_generate = construieste_drum(gr, t1, noduri_generate,s, limita, nrSolutiiCautate, tipEuristica)
            if rez == "gata":
                return 0, "gata", noduri_generate
            minim = min(minim, rez)
        return nrSolutiiCautate, minim, noduri_generate

    global maxNoduri
    t1 = time.time()
    noduri_generate = 0
    nodStart = NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))
    limita = nodStart.f
    while round(1000 * (time.time() - t1)) < timeOut:
        nrSolutiiCautate, rez, noduri_generate = construieste_drum(gr, t1, noduri_generate, nodStart, limita,nrSolutiiCautate, tipEuristica)
        if rez == "gata":
            break
        if rez == float('inf'):
            f.write("Nu exista solutii!\n")
            break
        limita = rez



def breadth_first(f,gr, nrSolutiiCautate=1, timeout = 10000000000):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0)]
    heapify(c)
    t1 = time.time()
    t2 = time.time()
    max_noduri = 0
    noduri_generate = 0
    milis = round(1000 * (t2 - t1))
    while len(c) > 0 and milis < timeOut:
        nodCurent = heappop(c)
        
        if gr.testeaza_scop(nodCurent):
           if gr.testeaza_scop(nodCurent):
            timpGasire = time.time()
            f.write("Solutie: \n")
            nodCurent.afisDrum(f)
            f.write(f"Timp pt a gasi solutia: {round(1000 * (timpGasire - t1))} ms\n")
            f.write(f"Nr maxim noduri in memorie: {max_noduri}\n")
            f.write(f"Nr de noduri generate: {noduri_generate}\n")
            f.write("----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
    
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        noduri_generate += len(lSuccesori)
        t2 = time.time()
        milis = round(1000 * (t2 - t1))
        for s in lSuccesori:
            heappush(c, s)
        max_noduri = max(max_noduri, len(c))
    milis = round(1000 * (time.time() - t1))
    if milis > timeOut:
        f.write('TIMED OUT\n')
        return
    


def depth_first(f,gr, nrSolutiiCautate=1, timeOut=10000000000):
    return

def df(f,nodCurent, nrSolutiiCautate=1, timeOut=10000000000):
    return

def dfi(f,nodCurent, adancime, nrSolutiiCautate=1,timeOut=10000000000):
    return 

def depth_first_iterativ(f,gr, nrSolutiiCautate =1,timeOut=10000000000):
    return


# -------------------------------------------------------------------------



functii1 = [a_star, a_star_optimizat, ida_star]
functii2 = [breadth_first,depth_first,depth_first_iterativ]
euristici = ["euristica_banala", "euristica1", "euristica2", "inadmisibil"]


#-----1----

# Daca nu exista folderul de output,trb creat
if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])


nrSol = int(sys.argv[3])
timeOut = int(sys.argv[4])

# Pentru fiecare fisier de input:

for numeFisier in os.listdir(sys.argv[1]):
    g = Graph(sys.argv[1] + '/' + numeFisier)  # graful 
    if g.ok:                                   # Daca sunt ok toate datele de intrare
        for functie in functii1:               # Pt fiecare functie
            for euristica in euristici:        # Pt fiecare euristica
                print(f"Apelez {functie.__name__} cu {euristica} pentru {numeFisier}")
                numeFisierOutputLocal = "output_" + "_" + functie.__name__ + "_" + euristica + "_" + numeFisier[ :-4] + ".txt"  
                stream = open(sys.argv[2] + "/" + numeFisierOutputLocal, "w")
                functie(stream, g, euristica, nrSol, timeOut)
                # închid fișierul
                stream.close()

        for functie in functii2:                # Pt fiecare functie
                print(f"Apelez {functie.__name__} pentru {numeFisier}")
                numeFisierOutputLocal = "output_" + "_" + functie.__name__ + "_" + numeFisier[ :-4] + ".txt"  
                stream = open(sys.argv[2] + "/" + numeFisierOutputLocal, "w")
                functie(stream, g, nrSol, timeOut)
                # închid fișierul
                stream.close()
        


