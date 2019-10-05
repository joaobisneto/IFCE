import java.util.ArrayList;
import java.util.Scanner;

public class Main{


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ArrayList<Usuario> usuarios = new ArrayList<>();

        int m = scanner.nextInt();
        CaixaPostal caixaPostalA = new CaixaPostal(m);
        CaixaPostal caixaPostalB = new CaixaPostal(m);

        Usuario usuario = new Usuario(1, 1);
        Pombo pombo = new Pombo(1, 1, 1, 1);

        usuario.iniciarUsuarios(5, usuarios);
        usuario.criarUsuario();
        pombo.criarPombo();



    }
}
