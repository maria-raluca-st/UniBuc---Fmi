public class Test1 {
    String str = "a";

    void A(){
        try{
            str+= "b";
            B();
        } catch(Exception e) {str+= "c";}
    }
    void B() throws Exception{
       try{
           str +="d";
           C();
       } catch(Exception e){throw new Exception();}
       finally{ str+= "e"; }
       str += "f";
    }

    void C() throws Exception { throw new Exception();}
}
