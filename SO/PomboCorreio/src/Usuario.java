import java.util.Scanner;
import java.util.ArrayList;

public class Usuario extends Thread{

    private int id;     //identificação;
    private int te;     //tempoEscrita;
    ArrayList<Usuario> usuarios = new ArrayList<>();

    public Usuario(int identificacao, int tempoEscrita) {
        this.id = identificacao;
        this.te = tempoEscrita;
    }

    public void iniciarUsuarios(int qtdUsuarios, ArrayList<Usuario> usuarios){

        for(int i=0; i<qtdUsuarios; i++) {
            usuarios.add(criarUsuario());
        }

        System.out.println("Foram inseridos "+ qtdUsuarios +" usuários inicialmente.");
    }

    public Usuario criarUsuario(){

        int identificacao;
        int tempoEscrita;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Insira o ID do usuário: ");
        identificacao = scanner.nextInt();
        System.out.print("\n");

        System.out.print("Insira o tempo de escrita do usuário: ");
        tempoEscrita = scanner.nextInt();
        System.out.print("\n");
        Usuario usuario = new Usuario(identificacao, tempoEscrita);

        return usuario;
    }

    public void eliminarUsuario(int identificacao){
        for(int i=0; i<usuarios.size(); i++){
            if((usuarios.get(i)).id == identificacao) {
                usuarios.remove(i);
            }
        }
        System.out.println("Usuário #" + identificacao + "foi eliminado.");
    }

    @Override
    public void run() {
        System.out.println("Usuario #" + id + " escreveu uma carta.");
    }
}