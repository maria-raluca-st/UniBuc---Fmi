//class C { 
//    public static int a=1; 

//}


class C{
    public static void met_1() throws Exception{
       try{
           throw new Exception();
       }
       finally{
           System.out.print("A");
       }
    }
    public static void met_2() throws Exception{
        try{
            met_1();
        }
        catch(Exception ex){
            System.out.print("B");
        }
     }
}
