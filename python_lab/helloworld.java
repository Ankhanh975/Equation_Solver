interface Vinfast{
    void showModel();
}
class VF9 implements Vinfast{
    public void showModel(){
        System.out.println("VF9");
    }
}
class VF8 extends VF9{
    public void showModel(){
        System.out.println("VF8");
    }
}

public class helloworld {
    public static void main(String[] args) {
        Vinfast vf = new VF8();
        vf.showModel();
    }
}