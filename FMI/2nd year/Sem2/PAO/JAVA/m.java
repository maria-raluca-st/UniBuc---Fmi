import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class m {
    static List<Automobil> automobilList = new ArrayList<>();

    public static void main(String[] args) {
        automobilList.add(new Automobil("Skoda", "Fabia", 1000, 5500));
        automobilList.add(new Automobil("Nissan", "Qashqai", 20000, 2000));
        automobilList.add(new Automobil("Nissan", "Qashqai2", 25000, 2000));
        automobilList.add(new Automobil("Skoda", "Octavia", 2000, 1200));

        System.out.println("EX II - I");

        automobilList.stream()
                .filter(p->p.getPret()>=5000)
                .sorted(Comparator.comparing(Automobil::getPret).reversed())
                .forEach(System.out::println);

        System.out.println("EX II - II");

        automobilList.stream()
           .map(Automobil::getMarca)
           .collect(Collectors.toSet())
           .forEach(System.out::println);

        System.out.println("EX II - III");

        List<Automobil> ex3 = automobilList
                .stream()
                .filter(c -> c.getCapacitate() >= 2000 && c.getCapacitate() <= 3000).collect(Collectors.toList());


        for(Automobil a:ex3)
        {
            System.out.println(a.toString());
        }

        System.out.println("EX II - IV");

        //print obiect dupa marca
        //System.out.println(automobilList.stream().collect(Collectors.groupingBy(Automobil::getMarca)));
        
        //print model dupa marca
        automobilList.stream()
        .collect(Collectors.groupingBy(Automobil::getMarca))
        .entrySet()
        .forEach(x-> {
            System.out.println("Marca: " + x.getKey());
            x.getValue().forEach(m-> System.out.println(m.getModel()));
        });

    }

}
