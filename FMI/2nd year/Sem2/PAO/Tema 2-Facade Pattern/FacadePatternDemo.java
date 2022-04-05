public class FacadePatternDemo {
    public static void main(String[] args) {
       GenreMaker genreMaker = new GenreMaker();
 
       genreMaker.singClassical();
       genreMaker.singRock();
       genreMaker.singJazz();		
    }
 }