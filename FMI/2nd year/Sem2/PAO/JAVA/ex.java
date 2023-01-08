public class ex{
     public static void main(String args[]){
         try{
             C.met_2();
         }
         catch(Exception e){
            System.out.print("C");
         }
         finally{
            System.out.print("D");
         }
         System.out.print("E");
     }
}