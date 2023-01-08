public class test {
    public static void main(String[] args) {
        //A a = new B();
        //System.out.println(a.f(1) + a.g(3));
        // A ob = new B();
        // System.out.println(++ob.x);   

        int a[] = {1,2,3,4,5} , b = 6;
        Tablou.met(a,b);
        int s = b;
        for(int i = 0; i< a.length ;i++)
        {
            s = s+ a[i];
        }
        System.out.println(s);
    
    }
}

