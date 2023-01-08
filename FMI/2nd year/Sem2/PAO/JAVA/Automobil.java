public class Automobil {
    String marca;
    String model;
    int capacitate;
    int pret;
    public Automobil(String m , String mo , int c , int pr){
          marca = m ;
          model = mo;
          capacitate = c;
          pret = pr;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString();
    }

    //@Override
    public boolean equals(Automobil a) {
        // TODO Auto-generated method stub
        return super.equals(a);
    }
  
    @Override
    public int hashCode() {
        // TODO Auto-generated method stub
        return super.hashCode();
    }

public int getCapacitate() {
    return capacitate;
}
public String getMarca() {
    return marca;
}
public String getModel() {
    return model;
}
public int getPret() {
    return pret;
}
public void setCapacitate(int capacitate) {
    this.capacitate = capacitate;
}
public void setMarca(String marca) {
    this.marca = marca;
}
public void setModel(String model) {
    this.model = model;
}
public void setPret(int pret) {
    this.pret = pret;
}

}
