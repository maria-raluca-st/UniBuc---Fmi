public class FactoryPatternDemo {

    public static void main(String[] args) {
       GenreFactory genreFactory = new GenreFactory();
 
       //get an object of Classical and call its sing method.
       Genre genre1 = genreFactory.getGenre("Classical");
 
       //call draw method of Circle
       genre1.sing();
 
       //get an object of Rock and call its sing method.
       Genre genre2 = genreFactory.getGenre("Rock");
 
       //call draw method of Rectangle
       genre2.sing();
 
       //get an object of Jazz and call its sing method.
       Genre genre3 = genreFactory.getGenre("Jazz");
 
       //call sing method of Jazz
       genre3.sing();
    }
 }