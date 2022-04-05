public class GenreMaker {
    private Genre classical;
    private Genre rock;
    private Genre jazz;
 
    public GenreMaker() {
       classical = new Classical();
       rock = new Rock();
       jazz = new Jazz();
    }
 
    public void singClassical(){
       classical.sing();
    }
    public void singRock(){
       rock.sing();
    }
    public void singJazz(){
       jazz.sing();
    }
 }